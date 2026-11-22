<?php
declare(strict_types=1);

/**
 * QuickPOS bootstrap: shared helpers, validator and page composition.
 */

const QP_ROOT = __DIR__;

require_once __DIR__ . '/helpers.php';
require_once __DIR__ . '/ContactValidator.php';
require_once __DIR__ . '/page.php';

send_security_headers();
