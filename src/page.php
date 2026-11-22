<?php
declare(strict_types=1);

/**
 * Render the full one-page site. Shared by index.php (empty form) and
 * contact.php (form re-rendered with validation errors).
 *
 * @param array{values?: array<string,string>, errors?: array<string,string>, plan?: string} $contact
 */
function render_home(array $contact = []): void
{
    $contact += ['values' => ['name' => '', 'email' => '', 'message' => ''], 'errors' => [], 'plan' => ''];

    render('layout-top', ['title' => 'QuickPOS — Everything your business needs, at one point of sale']);
    render('header');
    echo '<main id="main">';
    render('hero');
    render('features');
    render('pricing');
    render('contact', ['contact' => $contact]);
    echo '</main>';
    render('footer');
    render('layout-bottom');
}
