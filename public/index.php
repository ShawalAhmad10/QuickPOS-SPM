<?php
declare(strict_types=1);

require_once __DIR__ . '/../src/bootstrap.php';

// ?plan=basic|pro|enterprise (from the Pricing buttons) pre-selects the plan in Contact.
render_home(['plan' => normalize_plan($_GET['plan'] ?? null)]);
