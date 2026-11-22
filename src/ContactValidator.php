<?php
declare(strict_types=1);

/**
 * Contact form validation (shared, framework-free, no side effects).
 *
 * Implements the contract in docs/ARCHITECTURE.md. Used by public/contact.php.
 */

const CONTACT_MAX_NAME = 120;
const CONTACT_MAX_EMAIL = 254;
const CONTACT_MAX_MESSAGE = 2000;

/**
 * Character count (not bytes). Uses mbstring when loaded; otherwise falls back to
 * PCRE in UTF-8 mode, so validation never fatals on a PHP build without mbstring.
 * Invalid UTF-8 is treated as unusable input and counted as over-length.
 */
function contact_strlen(string $value): int
{
    if (function_exists('mb_strlen')) {
        return mb_strlen($value, 'UTF-8');
    }
    $count = preg_match_all('/./su', $value);
    return $count === false ? PHP_INT_MAX : $count;
}

/**
 * @param array<string, mixed> $input Raw request data (e.g. $_POST).
 * @return array{valid: bool, errors: array<string, string>, values: array<string, string>}
 *         `values` are trimmed strings and are NOT HTML-safe; escape on output.
 */
function validateContact(array $input): array
{
    $values = [];
    foreach (['name', 'email', 'message'] as $field) {
        $raw = $input[$field] ?? '';
        $values[$field] = is_string($raw) ? trim($raw) : '';
    }

    $errors = [];

    if ($values['name'] === '') {
        $errors['name'] = 'Please enter your name.';
    } elseif (contact_strlen($values['name']) > CONTACT_MAX_NAME) {
        $errors['name'] = 'Name must be ' . CONTACT_MAX_NAME . ' characters or fewer.';
    }

    if ($values['email'] === '') {
        $errors['email'] = 'Please enter your email address.';
    } elseif (contact_strlen($values['email']) > CONTACT_MAX_EMAIL
        || filter_var($values['email'], FILTER_VALIDATE_EMAIL) === false) {
        $errors['email'] = 'Please enter a valid email address.';
    }

    if ($values['message'] === '') {
        $errors['message'] = 'Please enter a message.';
    } elseif (contact_strlen($values['message']) > CONTACT_MAX_MESSAGE) {
        $errors['message'] = 'Message must be ' . CONTACT_MAX_MESSAGE . ' characters or fewer.';
    }

    return [
        'valid' => $errors === [],
        'errors' => $errors,
        'values' => $values,
    ];
}
