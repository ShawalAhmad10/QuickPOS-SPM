<?php
declare(strict_types=1);

/** Escape a value for safe HTML output. */
function e(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

/** Render a view from src/views with the given variables in scope. */
function render(string $view, array $vars = []): void
{
    $file = QP_ROOT . '/views/' . $view . '.php';
    if (!is_file($file)) {
        throw new RuntimeException('View not found: ' . $view);
    }
    extract($vars, EXTR_SKIP);
    require $file;
}

/**
 * Inline line icons (24x24 grid, uniform 1.75 stroke).
 * Paths are static, trusted strings defined here.
 */
function icon(string $name, string $class = 'icon'): string
{
    static $paths = [
        'inventory' => '<path d="M3.5 7.5 12 3l8.5 4.5v9L12 21l-8.5-4.5z"/><path d="M3.5 7.5 12 12l8.5-4.5M12 12v9"/>',
        'analytics' => '<path d="M4 20V4"/><path d="M4 20h16"/><path d="m8 15 3.5-4 3 2.5L19 7.5"/>',
        'customers' => '<circle cx="9" cy="8" r="3.25"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M16 5.2a3.25 3.25 0 0 1 0 5.6M18 14.4c1.8.8 3 2.6 3 5.6"/>',
        'integrations' => '<rect x="3.5" y="3.5" width="7" height="7" rx="1.75"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.75"/><path d="M14 7h2.5A3.5 3.5 0 0 1 20 10.5V11M10 17H7.5A3.5 3.5 0 0 1 4 13.5V13"/>',
        'arrow' => '<path d="M5 12h14M13 6l6 6-6 6"/>',
        'sales' => '<path d="M4 12.5 9 7l4 4 7-7"/><path d="M15 4h5v5"/>',
        'orders' => '<path d="M6 3.5h12v17l-3-2-3 2-3-2-3 2z"/><path d="M9 8.5h6M9 12h6"/>',
        'grid' => '<rect x="4" y="4" width="6.5" height="6.5" rx="1.5"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="1.5"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="1.5"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="1.5"/>',
        'people' => '<circle cx="12" cy="8" r="3.5"/><path d="M5 20c0-3.9 3.1-7 7-7s7 3.1 7 7"/>',
        'cog' => '<circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/>',
        'check' => '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    ];
    $body = $paths[$name] ?? '';
    return '<svg class="' . e($class) . '" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        . 'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
        . $body . '</svg>';
}

/**
 * Navigation links, shared by the desktop and mobile menus.
 * $base is '' on the home page and 'index.php' on pages that are not the home page.
 */
function nav_links(string $base = ''): array
{
    return [
        ['label' => 'Features', 'href' => $base . '#features'],
        ['label' => 'Pricing', 'href' => $base . '#pricing'],
        ['label' => 'Contact', 'href' => $base . '#contact'],
    ];
}

/** Illustrative pricing plans (fictional; no billing exists). */
function plans(): array
{
    return [
        'basic' => [
            'name' => 'Basic',
            'price' => '$19',
            'period' => '/month',
            'blurb' => 'For small shops getting started with one till.',
            'featured' => false,
            'cta' => 'Choose Basic',
            'features' => [
                '1 register',
                'Up to 500 products',
                'Daily sales summary',
                'Email support',
            ],
        ],
        'pro' => [
            'name' => 'Pro',
            'price' => '$49',
            'period' => '/month',
            'blurb' => 'For growing teams that need stock and customer insight.',
            'featured' => true,
            'cta' => 'Choose Pro',
            'features' => [
                'Up to 5 registers',
                'Unlimited products',
                'Low-stock alerts and reordering',
                'Customer insights',
                'Accounting and payment integrations',
                'Priority support',
            ],
        ],
        'enterprise' => [
            'name' => 'Enterprise',
            'price' => 'Custom',
            'period' => '',
            'blurb' => 'For larger operations with several locations.',
            'featured' => false,
            'cta' => 'Talk to us',
            'features' => [
                'Unlimited registers and locations',
                'Custom integrations',
                'Role-based staff permissions',
                'Dedicated account manager',
                'Service-level agreement',
            ],
        ],
    ];
}

/** Return a valid plan key from untrusted input, or '' if none matches. */
function normalize_plan(mixed $raw): string
{
    return is_string($raw) && array_key_exists($raw, plans()) ? $raw : '';
}

/** The four approved POS feature cards. */
function features(): array
{
    return [
        [
            'icon' => 'inventory',
            'title' => 'Inventory Management',
            'text' => 'Know what is on the shelf at every moment, with low-stock alerts before an item sells out.',
            'meta' => 'Live stock levels',
        ],
        [
            'icon' => 'analytics',
            'title' => 'Sales Analytics',
            'text' => 'See daily revenue, best sellers and busy hours in clear reports you can read at a glance.',
            'meta' => 'Daily and weekly trends',
        ],
        [
            'icon' => 'customers',
            'title' => 'Customer Insights',
            'text' => 'Understand who your regulars are and what they buy, so every visit feels personal.',
            'meta' => 'Purchase history at the till',
        ],
        [
            'icon' => 'integrations',
            'title' => 'Seamless Integrations',
            'text' => 'Connect accounting, payments and online storefront tools without re-keying a single sale.',
            'meta' => 'One workspace, fewer tabs',
        ],
    ];
}

/** Baseline response headers for every web page. No-op for CLI and once output has started. */
function send_security_headers(): void
{
    if (PHP_SAPI === 'cli' || headers_sent()) {
        return;
    }
    header('X-Content-Type-Options: nosniff');
    header('X-Frame-Options: DENY');
    header('Referrer-Policy: strict-origin-when-cross-origin');
    // Local scripts/styles only, plus Google Fonts; inline style attributes are used by the mockup bars.
    header("Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; "
        . "style-src-attr 'unsafe-inline'; font-src https://fonts.gstatic.com; img-src 'self' data:; "
        . "form-action 'self'; frame-ancestors 'none'; base-uri 'self'");
}

/** Start the short-lived confirmation session with hardened cookie settings. */
function start_confirmation_session(): void
{
    if (session_status() === PHP_SESSION_ACTIVE) {
        return;
    }
    session_set_cookie_params([
        'lifetime' => 0,
        'path' => '/',
        'httponly' => true,
        'samesite' => 'Lax',
        'secure' => !empty($_SERVER['HTTPS']),
    ]);
    session_start();
}
