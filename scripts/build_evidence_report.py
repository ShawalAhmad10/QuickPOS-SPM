from pathlib import Path
from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    Image,
    Indenter,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "docs" / "evidence" / "website"
OUTPUT = ROOT / "output" / "pdf" / "QuickPOS_Evidence_Report.pdf"

NAVY = colors.HexColor("#0F172A")
TEAL = colors.HexColor("#0891B2")
BLUE = colors.HexColor("#0369A1")
GREEN = colors.HexColor("#15803D")
AMBER = colors.HexColor("#B45309")
RED = colors.HexColor("#B91C1C")
SLATE = colors.HexColor("#475569")
LIGHT = colors.HexColor("#F1F5F9")
LINE = colors.HexColor("#CBD5E1")
WHITE = colors.white

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverKicker", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=10, leading=14, textColor=TEAL, alignment=TA_CENTER, spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=27, leading=31, textColor=NAVY, alignment=TA_CENTER, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="CoverSub", parent=styles["Normal"], fontName="Helvetica",
    fontSize=11, leading=16, textColor=SLATE, alignment=TA_CENTER, spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="Section", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=18, leading=22, textColor=NAVY, spaceBefore=3, spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="Task", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=12.5, leading=16, textColor=TEAL, spaceBefore=6, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="Subhead", parent=styles["Heading3"], fontName="Helvetica-Bold",
    fontSize=10.5, leading=14, textColor=BLUE, spaceBefore=5, spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="BodyQ", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=9.2, leading=13.2, textColor=NAVY, spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="SmallQ", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=7.7, leading=10.2, textColor=NAVY,
))
styles.add(ParagraphStyle(
    name="TinyQ", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=6.8, leading=8.8, textColor=NAVY,
))
styles.add(ParagraphStyle(
    name="CaptionQ", parent=styles["BodyText"], fontName="Helvetica-Oblique",
    fontSize=7.5, leading=10, textColor=SLATE, alignment=TA_CENTER, spaceBefore=3,
))
styles.add(ParagraphStyle(
    name="TableHeaderQ", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=7.5, leading=9.5, textColor=WHITE,
))
styles.add(ParagraphStyle(
    name="Callout", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=8.5, leading=12, textColor=NAVY, backColor=LIGHT,
    borderColor=LINE, borderWidth=0.5, borderPadding=7, spaceBefore=4, spaceAfter=6,
))


def p(text, style="BodyQ"):
    return Paragraph(text, styles[style])


def link(url, label=None):
    return f'<link href="{url}" color="#0369A1">{label or url}</link>'


def status_color(status):
    if status == "PASS":
        return GREEN
    if status == "PARTIAL":
        return AMBER
    if status == "BLOCKED":
        return RED
    return SLATE


def styled_table(rows, widths, header=True, tiny=False):
    style_name = "TinyQ" if tiny else "SmallQ"
    data = []
    for row_index, row in enumerate(rows):
        data.append([
            p(str(value), "TableHeaderQ" if header and row_index == 0 else style_name)
            for value in row
        ])
    commands = [
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1 if header else 0), (-1, -1), [WHITE, LIGHT]),
    ]
    if header:
        commands += [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ]
    return Table(data, colWidths=widths, repeatRows=1 if header else 0,
                 style=TableStyle(commands))


def evidence_image(filename, caption, max_width=165 * mm, max_height=175 * mm):
    path = EVIDENCE / filename
    if not path.exists():
        return [p(f"Evidence image not found: {filename}", "Callout")]
    with PILImage.open(path) as image:
        width_px, height_px = image.size
    scale = min(max_width / width_px, max_height / height_px)
    rendered = Image(str(path), width=width_px * scale, height=height_px * scale)
    return [rendered, p(caption, "CaptionQ")]


def page_header_footer(canvas, doc):
    canvas.saveState()
    width, height = A4
    if doc.page > 1:
        canvas.setFillColor(NAVY)
        canvas.rect(0, height - 12 * mm, width, 12 * mm, fill=1, stroke=0)
        canvas.setFillColor(WHITE)
        canvas.setFont("Helvetica-Bold", 8)
        canvas.drawString(18 * mm, height - 7.5 * mm, "QuickPOS - CS4002 Evidence Report")
        canvas.setFont("Helvetica", 7.5)
        canvas.drawRightString(width - 18 * mm, height - 7.5 * mm, "Verified integration candidate")
    canvas.setStrokeColor(LINE)
    canvas.line(18 * mm, 15 * mm, width - 18 * mm, 15 * mm)
    canvas.setFont("Helvetica", 7.2)
    canvas.setFillColor(SLATE)
    canvas.drawString(18 * mm, 10 * mm, "Shawal Ahmad | 22F-3303 | BCS-9C | 23 November 2026")
    page_text = f"Page {doc.page}"
    canvas.drawString(width - 18 * mm - stringWidth(page_text, "Helvetica", 7.2), 10 * mm, page_text)
    canvas.restoreState()


def task(title, status, body):
    color = status_color(status).hexval()
    return [
        p(f'{title} - <font color="{color}">{status}</font>', "Task"),
        p(body),
    ]


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT), pagesize=A4,
        rightMargin=18 * mm, leftMargin=18 * mm,
        topMargin=20 * mm, bottomMargin=20 * mm,
        title="QuickPOS Semester Project - Evidence Report",
        author="Shawal Ahmad",
        subject="FAST-NUCES CS4002 Tasks 1-16 evidence report",
    )
    story = []

    # Cover
    story += [
        Spacer(1, 14 * mm),
        p("FAST NATIONAL UNIVERSITY OF COMPUTER AND EMERGING SCIENCES", "CoverKicker"),
        p("Faisalabad Campus", "CoverSub"),
        Spacer(1, 9 * mm),
        p("QUICKPOS", "CoverTitle"),
        p("Semester Project - Evidence Report", "CoverTitle"),
        Spacer(1, 5 * mm),
        p("Fundamentals of Software Project Management", "CoverSub"),
        p("CS4002 | Fall 2026", "CoverSub"),
        Spacer(1, 8 * mm),
        styled_table([
            ["Submitted By", "Shawal Ahmad"],
            ["Roll Number", "22F-3303"],
            ["Class / Section", "BCS-9C"],
            ["Group Description", "Approved Solo Project (student-reported; documentary proof not included)"],
            ["GitHub Work Identity 1", "Shawal Ahmad - ShawalAhmad10"],
            ["GitHub Work Identity 2", "Shawal Ahmad - ShawalAhmad97"],
            ["Identity Disclosure", "Both GitHub accounts belong to the same enrolled student."],
            ["Submitted To", "Miss Maham Saleem"],
            ["Preparation Date", "23 November 2026"],
        ], [47 * mm, 118 * mm], header=False),
        Spacer(1, 8 * mm),
        p("Integration candidate status", "Subhead"),
        p("The source represented in this report combines the genuine changes from PRs #2, #3, #4 and #1 on the feature/project-documentation branch. It is verified and green, but it is not final merged main because qualifying PR review evidence is not present.", "Callout"),
        PageBreak(),
    ]

    # Executive summary and overview
    story += [
        p("Executive Summary", "Section"),
        p("QuickPOS is a responsive PHP marketing landing page for a fictional point-of-sale product. The project combines a six-section website, server-side contact validation, a Jira Scrum backlog, Jira-keyed GitHub development, automated PHP tests and a GitHub Actions workflow."),
        p("The current candidate preserves the accepted website and integrates the real QPOS-23 Jira linkage documentation, QPOS-19 validation-test hardening, QPOS-24 repository-wide PHP linting and refreshed academic evidence. Local verification passes 17 PHP lint checks and 13 automated validation tests. All four open PRs have passing CI. No independent review or merge is claimed."),
        p("Project Overview and Objectives", "Section"),
        styled_table([
            ["Objective", "Verified implementation"],
            ["Product", "Professional QuickPOS landing page with Header, Hero, Features, Pricing, Contact and Footer."],
            ["Backend behavior", "PHP POST validation, field-specific errors and one-time thank-you flow; no database or email delivery."],
            ["Project management", "QPOS Scrum project with 32 issues, 13 Done overall and two correctly dated sprints."],
            ["Traceability", "QPOS keys appear in real branches, commits and PRs; QPOS-23 shows linked development activity."],
            ["Quality", "Repository-wide PHP lint, 13 executable validation cases and controlled failed-to-fixed CI evidence."],
            ["Delivery", "Verified integration-candidate ZIP, evidence report, viva notes and explicit remaining gaps."],
        ], [45 * mm, 120 * mm]),
        p("Technology Stack and Architecture", "Section"),
        styled_table([
            ["Layer", "Technology / responsibility"],
            ["Presentation", "Semantic HTML5, custom CSS3, minimal vanilla JavaScript and responsive layouts."],
            ["Server", "PHP 8.3 entry points and reusable validation/helper modules."],
            ["Application structure", "public/ web root, src/ reusable code and views, tests/ dependency-free runner."],
            ["Security", "Output encoding, normalized input, CSP/clickjacking/MIME/referrer headers and hardened short-lived sessions."],
            ["Automation", "GitHub Actions on Ubuntu with PHP setup, all-tracked-file lint and automated tests."],
            ["Management", "Jira QPOS board 35; GitHub for Atlassian development linkage."],
        ], [45 * mm, 120 * mm]),
        PageBreak(),
    ]

    # Part A
    story += [
        p("Part A - QuickPOS Website Development", "Section"),
        *task("Task 1 - Product Design and Responsive UI", "PASS",
              "The accepted custom interface uses a consistent visual system and original POS dashboard mockup. QA found no unintended horizontal overflow at approximately 375px, 768px and 1280px, with additional checks at 320px and 1440px."),
        *evidence_image("01-desktop-full-1280.png", "Figure A1. Complete desktop page at 1280px.", 150 * mm, 160 * mm),
        PageBreak(),
        p("Part A - Responsive Detail", "Section"),
        *evidence_image("03b-pricing-375.png", "Figure A2. Readable mobile pricing layout at 375px.", 70 * mm, 178 * mm),
        Spacer(1, 4 * mm),
        p("The representative mobile capture keeps plan hierarchy, pricing and controls readable without horizontal scrolling. The mobile navigation evidence is shown on the following page."),
        PageBreak(),
        *task("Task 2 - Required Landing-Page Sections", "PASS",
              "Header/Navigation, Hero, Features, Pricing, Contact and Footer are implemented. Navigation and CTA targets were checked; the mobile menu supports Escape and focus return."),
        *evidence_image("03-pricing-1280.png", "Figure A3. Distinct Basic, Pro and Enterprise plans.", 165 * mm, 112 * mm),
        Spacer(1, 4 * mm),
        *evidence_image("07-mobile-menu-open-375.png", "Figure A4. Accessible mobile navigation and Hero detail.", 72 * mm, 92 * mm),
        PageBreak(),
        Spacer(1, 12 * mm),
        p("Part A - PHP Contact Validation", "Section"),
        *task("Task 3 - PHP Contact Form and Server-Side Validation", "PASS",
              "The form uses POST and validates required name, email and message values plus email format. Invalid requests return understandable field errors; valid requests redirect with HTTP 303 to a one-time confirmation. No database, real email, authentication or permanent submission storage is used."),
        *evidence_image("05-validation-errors-1280.png", "Figure A5. Server-side validation errors with retained safe values.", 165 * mm, 103 * mm),
        Spacer(1, 5 * mm),
        *evidence_image("06-thank-you-1280.png", "Figure A6. Honest one-time confirmation after valid input.", 165 * mm, 86 * mm),
        PageBreak(),
    ]

    # Part B
    story += [
        p("Part B - Jira Agile Project Management", "Section"),
        p("The following evidence is derived from the authorized Jira connector on 23 November 2026. It is presented as labeled data, not as an invented interface screenshot.", "Callout"),
        *task("Task 4 - Jira Setup, Epics and Backlog", "PASS",
              "The real QuickPOS - SPM Jira project (key QPOS) contains 32 issues assigned to Shawal Ahmad. The hierarchy includes the six required functional Epics plus Testing and CI."),
        styled_table([
            ["Issue type", "Count", "Evidence"],
            ["Epic", "7", "Navigation/Header, Hero, Features, Pricing, Contact, Footer, Testing and CI"],
            ["Story", "15", "User-facing and quality stories with priority, assignee and estimates"],
            ["Task", "5", "Repository, Jira integration, PHP lint, evidence and package work"],
            ["Subtask", "5", "Implementation and verification work below parent items"],
            ["Total", "32", "QPOS-1 through QPOS-32"],
        ], [35 * mm, 20 * mm, 110 * mm]),
        p("Screenshot-only gap: Jira backlog, Epic and two detailed-story UI screenshots were not captured in this milestone; connector-derived data and live URLs are included instead.", "Callout"),
        *task("Task 5 - Two Sprints: Planning and Development", "PARTIAL",
              "Exactly two one-week sprints exist with the assignment dates and clear goals. Sprint 1 is active with 6 Done and 3 In Progress; Sprint 2 is future. Neither sprint is prematurely reported complete."),
        styled_table([
            ["Sprint", "ID / state", "Dates", "Current evidence"],
            ["QPOS Sprint 1", "69 / active", "23-29 Nov 2026", "9 issues: 6 Done, 3 In Progress"],
            ["QPOS Sprint 2", "70 / future", "30 Nov-6 Dec 2026", "Planned with testing, CI and evidence goal"],
        ], [38 * mm, 30 * mm, 35 * mm, 62 * mm]),
        *task("Task 6 - Risk/Bug Tracking, Progress and Retrospectives", "PARTIAL",
              "The board truthfully shows 13 issues Done overall. QPOS-14 through QPOS-18 contain genuine pre-sprint implementation and QA comments but remain To Do for real Sprint 2 reverification. No fabricated bug is added. Sprint reports, closure evidence and retrospectives remain future because both sprint end dates have not occurred."),
        PageBreak(),
    ]

    # Part C
    story += [
        p("Part C - GitHub Collaboration and Jira Integration", "Section"),
        *task("Task 7 - Repository, README and Jira Integration", "PASS",
              f"The public repository is {link('https://github.com/ShawalAhmad10/QuickPOS-SPM')}. QPOS-23 displays linked GitHub development activity. The README contains purpose, identity, technology, local run, test and CI information. The final main branch is still the stable baseline."),
        *task("Task 8 - Jira-Linked Branches and Meaningful Commits", "PASS",
              "Real Jira keys are used in the QPOS-23, QPOS-19 and QPOS-24 development branches, commits and PRs. The already-complete website was published as one truthful initial baseline rather than divided into fabricated historical work."),
        styled_table([
            ["PR", "Jira / purpose", "Verified head", "Verified CI evidence"],
            ["#2", "QPOS-23 Jira development integration", "8024ec2", "45109153077 - PASS"],
            ["#3", "QPOS-19 validation test hardening", "9d17c8c", "45112783653 - PASS"],
            ["#4", "QPOS-24 repository-wide PHP lint", "881232b", "45112936298 - PASS"],
            ["#1", "Combined integration baseline", "cf54093", "45116680054 - PASS"],
        ], [14 * mm, 72 * mm, 25 * mm, 54 * mm]),
        *task("Task 9 - Pull Requests and Code Review", "BLOCKED",
              "Four meaningful PRs are open, mergeable and green. AI-assisted technical findings are visibly labeled and do not count as independent human approvals. GitHub reports no qualifying reviews; therefore no PR is merged. Prepared order: #2, #3, #4, then #1."),
        *task("Task 10 - Balanced Participation and GitHub Activity", "PARTIAL",
              "This is an Approved Solo Project according to the student; documentary approval is not included in the repository. ShawalAhmad10 and ShawalAhmad97 are two work identities of the same enrolled student, Shawal Ahmad (22F-3303), not separate contributors. The student remains responsible for explaining all work in the viva."),
        p("Screenshot-only gap: GitHub branch/PR UI screenshots were not captured. The report provides public PR URLs, immutable head SHAs and GitHub CLI/API check results.", "Callout"),
        PageBreak(),
    ]

    # Part D
    story += [
        p("Part D - GitHub Actions and Automated Testing", "Section"),
        *task("Task 11 - CI Workflow File and Triggers", "PASS",
              "The workflow at .github/workflows/ci.yml uses a GitHub-hosted Ubuntu runner and PHP 8.3. It runs on pushes to feature/**, bugfix/** and main, and on pull requests targeting main."),
        *task("Task 12 - Automated PHP Syntax Checks", "PASS",
              "CI uses git ls-files to discover every tracked .php file, fails if none are found and propagates any php -l failure. The verified candidate contains 17 tracked PHP files and all lint cleanly."),
        *task("Task 13 - Automated Contact-Form Tests", "PASS",
              "The dependency-free suite contains 13 cases, including the four mandatory scenarios, whitespace/missing/non-string handling, exact length boundaries and normalization behavior. PHP warnings/notices and failed assertions produce nonzero exit status."),
        *task("Task 14 - CI Failure, Fix and Passing Evidence", "PASS",
              f"The controlled negative exercise failed truthfully at {link('https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110283311', 'run 45110283311')} with 13/14 tests. The corrective commit removed only the sentinel and {link('https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110435088', 'run 45110435088')} passed. Stable main remained green."),
        styled_table([
            ["Verification", "Observed result", "Evidence"],
            ["Candidate PHP lint", "PASS - 17/17", "Local repository-wide run"],
            ["Candidate automated tests", "PASS - 13/13", "php tests/run.php"],
            ["Stable main CI", "PASS", "Actions run 45043988754"],
            ["Controlled negative CI", "FAIL as intended", "Actions run 45110283311"],
            ["Corrected CI", "PASS", "Actions run 45110435088"],
            ["PR #1 integration baseline CI", "PASS", "Actions run 45116680054"],
        ], [45 * mm, 42 * mm, 78 * mm]),
        p("Screenshot-only gap: Actions UI captures were not generated. The public run links and GitHub API results are the authoritative evidence in this candidate report.", "Callout"),
        PageBreak(),
    ]

    # Part E
    story += [
        Spacer(1, 12 * mm),
        Indenter(left=10 * mm),
        p("Part E - Submission and Viva Readiness", "Section"),
        *task("Task 15 - Submission Package and Evidence Report", "PARTIAL",
              "The package contains the verified integration-candidate source, README, tests, workflow, evidence PDF, final audit and viva notes. The ZIP is not represented as merged main. Final LMS submission and evaluator access confirmation remain external activities."),
        *task("Task 16 - Live Viva and Evaluation", "PARTIAL",
              "Viva notes cover the product, PHP validation, architecture, Jira, PR traceability, tests, CI failure/fix evidence, identity disclosure and remaining gaps. The live evaluation has not yet occurred."),
        p("Submission Candidate Contents", "Subhead"),
        styled_table([
            ["Artifact", "Purpose / state"],
            ["QuickPOS_Source.zip", "Verified integration candidate, not merged main"],
            ["QuickPOS_Evidence_Report.pdf", "Tasks 1-16 report with genuine website evidence and API-derived tables"],
        ], [50 * mm, 105 * mm]),
        p("Academic and identity statement", "Subhead"),
        p("Submitted by Shawal Ahmad, roll number 22F-3303, BCS-9C, to Miss Maham Saleem. The group description is Approved Solo Project based on the student's report. No documentary approval attachment, second enrolled student, independent reviewer, PR merge, sprint closure, grade or LMS receipt is fabricated."),
        Indenter(left=-10 * mm),
        PageBreak(),
    ]

    # Traceability matrix
    story += [p("Requirements Traceability Matrix - Tasks 1-16", "Section")]
    matrix = [
        ["#", "Requirement", "Status", "Evidence / exact outstanding action"],
        ["1", "Responsive product UI", "PASS", "Desktop and mobile evidence; multi-width QA complete."],
        ["2", "Six required sections", "PASS", "All sections and CTA/navigation behavior verified."],
        ["3", "PHP validation", "PASS", "Real invalid/valid flows and 13 automated cases."],
        ["4", "Jira backlog", "PASS", "32 issues with required hierarchy; capture final Jira UI screenshots."],
        ["5", "Two sprints", "PARTIAL", "Sprint 1 active; Sprint 2 future; close only on real dates."],
        ["6", "Bugs/progress/retros", "PARTIAL", "Complete reports and two retrospectives after sprint closures."],
        ["7", "Repo/README/integration", "PASS", "Public repo and QPOS-23 development link verified."],
        ["8", "Branches/commits", "PASS", "QPOS-keyed development evidence present."],
        ["9", "PRs/reviews", "BLOCKED", "Obtain qualifying review evidence and merge four PRs."],
        ["10", "Participation", "PARTIAL", "Solo status reported; documentary proof/review arrangement not included."],
        ["11", "CI workflow", "PASS", "Required triggers, Ubuntu and PHP setup verified."],
        ["12", "PHP lint", "PASS", "17/17 tracked PHP files pass."],
        ["13", "Automated tests", "PASS", "13/13 cases pass and failure propagates."],
        ["14", "Failed-to-fixed CI", "PASS", "Runs 45110283311 and 45110435088."],
        ["15", "ZIP/report", "PARTIAL", "Candidate generated; final merged source and LMS receipt remain."],
        ["16", "Live viva", "NOT VERIFIED", "Attend and complete the live evaluation."],
    ]
    data = []
    for row_index, row in enumerate(matrix):
        cells = []
        for col_index, value in enumerate(row):
            if row_index == 0:
                cells.append(p(value, "TableHeaderQ"))
            elif col_index == 2:
                color = status_color(value).hexval()
                cells.append(p(f'<font color="{color}"><b>{value}</b></font>', "TinyQ"))
            else:
                cells.append(p(value, "TinyQ"))
        data.append(cells)
    story.append(Table(
        data, colWidths=[9 * mm, 48 * mm, 24 * mm, 84 * mm], repeatRows=1,
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("GRID", (0, 0), (-1, -1), 0.35, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT]),
            ("LEFTPADDING", (0, 0), (-1, -1), 3),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ])
    ))
    story += [PageBreak(), p("Evidence and References", "Section")]
    references = [
        ["Evidence", "Verified reference"],
        ["GitHub repository", link("https://github.com/ShawalAhmad10/QuickPOS-SPM")],
        ["Jira project", link("https://shawalahmad97.atlassian.net/jira/software/projects/QPOS")],
        ["PR #1", link("https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/1")],
        ["PR #2", link("https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/2")],
        ["PR #3", link("https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/3")],
        ["PR #4", link("https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/4")],
        ["Stable main CI", link("https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754")],
        ["Controlled failed CI", link("https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110283311")],
        ["Corrected passing CI", link("https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110435088")],
        ["Integration baseline CI", link("https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45116680054")],
        ["Website evidence", "docs/evidence/website/01 through 07"],
        ["Official requirements", "CS4002 QuickPOS Semester Project brief, 7 pages"],
    ]
    story.append(styled_table(references, [50 * mm, 115 * mm]))
    story += [
        p("Accurate Remaining Gaps", "Section"),
        p("1. Capture readable Jira backlog, Epic, detailed-story and sprint-board UI screenshots.", "BodyQ"),
        p("2. Capture readable GitHub PR/branch and Actions UI screenshots if required by the evaluator.", "BodyQ"),
        p("3. Obtain and retain the actual qualifying PR review arrangement and visible review evidence.", "BodyQ"),
        p("4. Merge PRs #2, #3, #4 and #1 only when authorized; then verify final main CI and Jira linkage.", "BodyQ"),
        p("5. Complete Sprint 1 and Sprint 2 on their real dates, then add sprint reports and retrospectives.", "BodyQ"),
        p("6. Retain documentary solo-project approval if available; this report records only the student's statement.", "BodyQ"),
        p("7. Submit the final merged-main ZIP/report through the designated channel and retain the receipt.", "BodyQ"),
        p("8. Complete the live viva.", "BodyQ"),
        Spacer(1, 5 * mm),
        p("Final integrity statement", "Task"),
        p("This report does not claim a second enrolled student, independent approval, merged PRs, completed future sprints, a final grade or an LMS submission receipt. API-derived Jira and GitHub facts are labeled as data rather than interface screenshots. Missing screenshot-only evidence is explicitly reported instead of fabricated."),
    ]

    doc.build(story, onFirstPage=page_header_footer, onLaterPages=page_header_footer)
    print(OUTPUT)


if __name__ == "__main__":
    build()
