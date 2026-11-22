<?php
declare(strict_types=1);

require_once __DIR__ . '/../src/bootstrap.php';

// Only POST submissions are handled. A direct visit (GET/HEAD/etc.) never shows
// success: it is sent back to the Contact section.
if (($_SERVER['REQUEST_METHOD'] ?? 'GET') !== 'POST') {
    header('Location: index.php#contact', true, 303);
    exit;
}

$result = validateContact($_POST);
$plan = normalize_plan($_POST['plan'] ?? null);

if (!$result['valid']) {
    http_response_code(422);
    render_home([
        'values' => $result['values'],
        'errors' => $result['errors'],
        'plan' => $plan,
    ]);
    exit;
}

// Demo only: nothing is emailed or stored. Keep just enough in the session for the
// confirmation page, then redirect (Post/Redirect/Get) so a refresh cannot resubmit.
start_confirmation_session();
$_SESSION['qp_thanks'] = [
    'name' => $result['values']['name'],
    'plan' => $plan,
];
// Explicit fragment stops the browser carrying the form action's #contact over.
header('Location: thank-you.php#main', true, 303);
exit;
