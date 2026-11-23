from __future__ import annotations

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
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "QuickPOS_Evidence_Report.pdf"
EVIDENCE = ROOT / "docs" / "evidence" / "website"

NAVY = colors.HexColor("#0F172A")
CYAN = colors.HexColor("#0891B2")
LIGHT = colors.HexColor("#F1F5F9")
MUTED = colors.HexColor("#475569")
GREEN = colors.HexColor("#166534")
AMBER = colors.HexColor("#92400E")
RED = colors.HexColor("#991B1B")


def link(url: str, label: str | None = None) -> str:
    safe_label = label or url
    return f'<link href="{url}" color="#087F9A">{safe_label}</link>'


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="CoverTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=28,
        leading=33,
        textColor=NAVY,
        alignment=TA_LEFT,
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        name="CoverSub",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=18,
        textColor=MUTED,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="Part",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=NAVY,
        spaceBefore=8,
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        name="Task",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=17,
        textColor=CYAN,
        spaceBefore=10,
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyQ",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.2,
        leading=13.2,
        textColor=NAVY,
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="SmallQ",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=7.8,
        leading=10.2,
        textColor=NAVY,
    )
)
styles.add(
    ParagraphStyle(
        name="TableHeaderQ",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=7.8,
        leading=10.2,
        textColor=colors.white,
    )
)
styles.add(
    ParagraphStyle(
        name="CaptionQ",
        parent=styles["BodyText"],
        fontName="Helvetica-Oblique",
        fontSize=8,
        leading=10,
        textColor=MUTED,
        alignment=TA_CENTER,
        spaceBefore=4,
        spaceAfter=8,
    )
)


def p(text: str, style: str = "BodyQ") -> Paragraph:
    return Paragraph(text, styles[style])


def status_color(status: str):
    if status == "PASS":
        return GREEN
    if status == "PARTIAL":
        return AMBER
    return RED


def evidence_image(filename: str, caption: str, max_height: float = 205 * mm):
    path = EVIDENCE / filename
    with PILImage.open(path) as img:
        width_px, height_px = img.size
    max_width = 170 * mm
    scale = min(max_width / width_px, max_height / height_px)
    rendered = Image(str(path), width=width_px * scale, height=height_px * scale)
    return [rendered, p(caption, "CaptionQ")]


def on_page(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(colors.HexColor("#CBD5E1"))
    canvas.line(20 * mm, 15 * mm, width - 20 * mm, 15 * mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(20 * mm, 10 * mm, "QuickPOS evidence report - verified through 23 November 2026")
    page_text = f"Page {doc.page}"
    canvas.drawString(width - 20 * mm - stringWidth(page_text, "Helvetica", 7.5), 10 * mm, page_text)
    canvas.restoreState()


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=22 * mm,
        title="QuickPOS Evidence Report",
        author="Shawal Ahmad",
        subject="CS4002 QuickPOS Parts A-E and Tasks 1-16",
    )

    story = []
    story.extend(
        [
            Spacer(1, 25 * mm),
            p("FAST-NUCES | CS4002 | Fall 2026", "CoverSub"),
            p("QuickPOS", "CoverTitle"),
            p("Evidence report", "CoverTitle"),
            Spacer(1, 8 * mm),
            Table(
                [
                    [p("Student", "SmallQ"), p("Shawal Ahmad", "SmallQ")],
                    [p("Roll number", "SmallQ"), p("Not supplied", "SmallQ")],
                    [p("Approved Group ID", "SmallQ"), p("Not supplied", "SmallQ")],
                    [p("Prepared", "SmallQ"), p("23 November 2026 (PKT)", "SmallQ")],
                    [p("Repository", "SmallQ"), p(link("https://github.com/ShawalAhmad10/QuickPOS-SPM"), "SmallQ")],
                    [p("Jira", "SmallQ"), p(link("https://shawalahmad97.atlassian.net/jira/software/projects/QPOS", "QPOS project"), "SmallQ")],
                    [p("Baseline commit", "SmallQ"), p("fe10bd36b1eb77907a222d8f74d9c28b7aad38f5", "SmallQ")],
                    [p("Passing CI", "SmallQ"), p(link("https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754", "Actions run 45043988754"), "SmallQ")],
                ],
                colWidths=[40 * mm, 125 * mm],
                style=TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (0, -1), LIGHT),
                        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
                        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#CBD5E1")),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 6),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                        ("TOPPADDING", (0, 0), (-1, -1), 6),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                    ]
                ),
            ),
            Spacer(1, 10 * mm),
            p(
                "Current pre-submission evidence. It records verified results and explicit gaps; it is not a grade, proof of future sprint completion, proof of instructor approval, or an LMS receipt.",
                "CoverSub",
            ),
            PageBreak(),
        ]
    )

    story.append(p("Executive evidence status", "Part"))
    status_rows = [
        ("1", "UI and responsive design", "PASS", "Real desktop/mobile captures and multi-width browser QA"),
        ("2", "Six required sections", "PASS", "Screenshots 01-07 and link/menu audit"),
        ("3", "PHP validation", "PASS", "HTTP flow, screenshots and 13 tests"),
        ("4", "Jira backlog", "PASS", "QPOS has 32 issues: 7 Epics, 15 Stories, 5 Tasks, 5 Subtasks"),
        ("5", "Two sprints", "PARTIAL", "Sprint 1 active; Sprint 2 planned; closures remain"),
        ("6", "Bugs/reports/retros", "PARTIAL", "Genuine work only; reports and retros remain"),
        ("7", "Repository/integration", "PASS", "Public repo and QPOS-23 Development PR link"),
        ("8", "Branches/commits", "PASS", "QPOS-19, QPOS-23 and QPOS-24 development evidence"),
        ("9", "PRs/reviews", "BLOCKED", "Four open green PRs; no qualifying approval or merge"),
        ("10", "Participation", "BLOCKED", "Solo exception not confirmed"),
        ("11", "CI workflow", "PASS", "Remote run 45043988754 succeeded"),
        ("12", "PHP lint", "PASS", "17/17 tracked files on open PR"),
        ("13", "Automated tests", "PASS", "13/13 hardened cases on open PR"),
        ("14", "CI fail/fix", "PASS", "Failed run 45110283311; fixed run 45110435088"),
        ("15", "Submission package", "PARTIAL", "Refreshed artifacts; identifiers/submission remain"),
        ("16", "Live viva", "PARTIAL", "Preparation only"),
    ]
    table_data = [[p("Task", "TableHeaderQ"), p("Requirement", "TableHeaderQ"), p("Status", "TableHeaderQ"), p("Evidence / gap", "TableHeaderQ")]]
    for number, requirement, status, evidence in status_rows:
        table_data.append([p(number, "SmallQ"), p(requirement, "SmallQ"), p(f'<font color="{status_color(status).hexval()}"><b>{status}</b></font>', "SmallQ"), p(evidence, "SmallQ")])
    story.append(
        Table(
            table_data,
            colWidths=[12 * mm, 48 * mm, 28 * mm, 77 * mm],
            repeatRows=1,
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#CBD5E1")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]
            ),
        )
    )
    story.extend([Spacer(1, 6 * mm), p("Contributor disclosure", "Task")])
    story.append(p("Shawal Ahmad is the only identified student contributor. ShawalAhmad10 is the primary GitHub account. ShawalAhmad97 is controlled by the same person and is not a second student or independent reviewer. AI tools assisted development and documentation; the student remains responsible for correctness, understanding and the live viva."))
    story.append(PageBreak())

    story.extend([p("Part A - QuickPOS website development", "Part"), p("Task 1 - Product design and responsive UI - PASS", "Task")])
    story.append(p("The custom PHP landing page has a consistent design system, an original HTML/CSS/SVG POS dashboard and accessible responsive layouts. Browser QA found no horizontal overflow at 320, 375, 768, 1280 or 1440 pixels."))
    story.extend(evidence_image("01-desktop-full-1280.png", "Figure A1. Complete desktop page at 1280px.", 185 * mm))
    story.append(PageBreak())
    story.extend(evidence_image("02-mobile-full-375.png", "Figure A2. Complete mobile page at 375px.", 215 * mm))
    story.append(PageBreak())
    story.extend([p("Task 2 - Six required sections - PASS", "Task"), p("Header/Navigation, Hero, Features, Pricing, Contact and Footer are implemented. Navigation and CTAs have meaningful destinations; the mobile menu supports Escape and focus return.")])
    story.extend(evidence_image("03-pricing-1280.png", "Figure A3. Illustrative Basic, Pro and Enterprise pricing.", 150 * mm))
    story.extend(evidence_image("07-mobile-menu-open-375.png", "Figure A4. Accessible mobile menu open at 375px.", 125 * mm))
    story.append(PageBreak())
    story.extend([p("Task 3 - PHP contact form and validation - PASS", "Task"), p("Invalid input returns HTTP 422 with field-specific errors and safely retained values. Valid input redirects with HTTP 303 to a one-time confirmation. The form does not email or permanently save submissions.")])
    story.extend(evidence_image("05-validation-errors-1280.png", "Figure A5. Server-side validation errors with the selected plan retained.", 120 * mm))
    story.extend(evidence_image("06-thank-you-1280.png", "Figure A6. Honest one-time confirmation after valid input.", 110 * mm))
    story.append(PageBreak())

    story.extend([p("Part B - Jira Scrum", "Part")])
    story.extend([p("Task 4 - Jira backlog - VERIFIED SETUP", "Task"), p(f"The real QPOS Scrum project at {link('https://shawalahmad97.atlassian.net/jira/software/projects/QPOS', 'Jira QPOS')} contains 32 issues (QPOS-1 through QPOS-32): seven Epics, fifteen Stories, five Tasks and five Subtasks. Final submission still needs readable backlog, Epic and two detailed-story screenshots.")])
    story.extend([p("Task 5 - Two sprints - IN PROGRESS", "Task"), p("Sprint 1 is active for 23-29 November 2026. Sprint 2 is planned for 30 November-6 December 2026. Neither sprint is falsely reported closed; both real summaries remain future evidence.")])
    story.extend([p("Task 6 - Bugs, progress and retrospectives - PARTIAL", "Task"), p("Only genuine Jira and engineering activity is recorded. Sprint reports and both retrospectives must be completed from actual events after their real closure dates.")])

    story.extend([p("Part C - GitHub collaboration and Jira integration", "Part")])
    story.extend([p("Task 7 - Repository, README and integration - VERIFIED", "Task"), p(f"The public repository is live at {link('https://github.com/ShawalAhmad10/QuickPOS-SPM')}. Jira QPOS-23's Development field exposes one open GitHub pull request, verifying real integration.")])
    story.extend([p("Task 8 - Branches and meaningful commits - VERIFIED", "Task"), p("PR 2 uses QPOS-23, PR 3 uses QPOS-19 and PR 4 uses QPOS-24. The already-complete source remains one truthful baseline rather than fabricated historical commits.")])
    story.extend([p("Task 9 - Pull requests and code review - BLOCKED", "Task"), p(f"Four genuine pull requests are open: {link('https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/1', 'PR 1')}, {link('https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/2', 'PR 2')}, {link('https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/3', 'PR 3')} and {link('https://github.com/ShawalAhmad10/QuickPOS-SPM/pull/4', 'PR 4')}. All latest verified checks pass. AI-assisted technical comments are preserved but are not independent approvals. No PR is merged.")])
    story.extend([p("Task 10 - Balanced participation - BLOCKED", "Task"), p("Only Shawal Ahmad is identified. The secondary account is the same person and cannot satisfy independent contribution or review requirements.")])
    story.append(PageBreak())

    story.extend([Spacer(1, 8 * mm), p("Part D - Tests and GitHub Actions CI", "Part")])
    story.extend([p("Task 11 - Workflow and triggers - PASS", "Task"), p(f"The workflow uses Ubuntu and PHP 8.3 and runs on main, feature branches, bugfix branches and pull requests targeting main. Passing evidence: {link('https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45043988754', 'Actions run 45043988754')}.")])
    story.extend([p("Task 12 - Automated PHP syntax checks - PASS ON OPEN PR", "Task"), p("The workflow discovers every tracked PHP path with git ls-files and fails if none exist or any lint fails. All 17 tracked PHP files pass.")])
    story.extend([p("Task 13 - Automated contact-form tests - PASS ON OPEN PR", "Task"), p("The 13-case dependency-free suite treats warnings/notices as failures and proves exact maximum-length fixtures. Result: 13/13.")])
    story.extend([p("Task 14 - CI failure, fix and passing evidence - VERIFIED", "Task"), p(f"The explicitly labeled controlled exercise failed truthfully at {link('https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110283311', 'run 45110283311')} with 13/14 tests and nonzero exit. The corrective commit removed only the sentinel; {link('https://github.com/ShawalAhmad10/QuickPOS-SPM/actions/runs/45110435088', 'run 45110435088')} passed. Main stayed green.")])
    ci_table = Table(
        [
            [p("Check", "TableHeaderQ"), p("Result", "TableHeaderQ")],
            [p("Local PHP lint", "SmallQ"), p("PASS - 17 files", "SmallQ")],
            [p("Local tests", "SmallQ"), p("PASS - 13/13", "SmallQ")],
            [p("GitHub Actions main", "SmallQ"), p("PASS - run 45043988754", "SmallQ")],
            [p("Controlled CI exercise", "SmallQ"), p("FAIL 45110283311 -> PASS 45110435088", "SmallQ")],
            [p("Secret/key scan", "SmallQ"), p("PASS - no findings", "SmallQ")],
        ],
        colWidths=[80 * mm, 80 * mm],
        style=TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CBD5E1")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        ),
    )
    story.extend([Spacer(1, 6 * mm), ci_table, PageBreak()])

    story.extend([p("Part E - Submission and live evaluation", "Part")])
    story.extend([p("Task 15 - Submission package and evidence report - PARTIAL", "Task"), p("The source ZIP, this PDF and viva notes are refreshed from current evidence. Group ID, roll number, final review/merge/sprint evidence and the LMS receipt remain absent.")])
    story.extend([p("Task 16 - Live viva - PARTIAL", "Task"), p("Viva preparation covers the website, validation, security, tests, CI and governance disclosures. The actual live evaluation has not occurred.")])
    story.extend([p("Explicit evidence gaps", "Task")])
    gaps = [
        "Approved Group ID and roll number.",
        "Readable final Jira backlog, Epic and two-story screenshots.",
        "Real Sprint 1 and Sprint 2 closures, reports and retrospectives.",
        "Instructor-approved solo-group and qualifying-review arrangements.",
        "Four legitimate reviews and authorized merges, then final main CI/Jira verification.",
        "Final submission receipt and live-viva result.",
    ]
    for item in gaps:
        story.append(p(f"- {item}"))
    story.extend([Spacer(1, 5 * mm), p("Integrity note", "Task"), p("No Group ID, roll number, sprint closure, second student, reviewer approval, merge, grade or submission receipt has been invented. The controlled failed CI run is labeled accurately and linked. This report stays incomplete wherever authoritative evidence does not yet exist.")])

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(OUTPUT)


if __name__ == "__main__":
    build()
