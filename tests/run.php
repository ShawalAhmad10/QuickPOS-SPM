<?php
declare(strict_types=1);

require_once __DIR__ . '/../src/ContactValidator.php';
require_once __DIR__ . '/../src/helpers.php';

/**
 * Minimal dependency-free test runner for the QuickPOS validation contract.
 */
final class TestFailure extends RuntimeException
{
}

// Test infrastructure warnings must fail CI instead of being printed and ignored.
set_error_handler(
    static function (int $severity, string $message, string $file, int $line): bool {
        if ((error_reporting() & $severity) === 0) {
            return false;
        }

        throw new ErrorException($message, 0, $severity, $file, $line);
    }
);

function assertTrue(bool $condition, string $message): void
{
    if (!$condition) {
        throw new TestFailure($message);
    }
}

function assertFalse(bool $condition, string $message): void
{
    assertTrue(!$condition, $message);
}

function assertSameValue(mixed $expected, mixed $actual, string $message): void
{
    if ($expected !== $actual) {
        throw new TestFailure(
            $message . ' Expected ' . var_export($expected, true)
            . ', got ' . var_export($actual, true) . '.'
        );
    }
}

/** @param array{errors: array<string, string>} $result */
function assertFieldError(array $result, string $field): void
{
    assertTrue(isset($result['errors'][$field]), "Expected an error for {$field}.");
}

/** @param array{errors: array<string, string>} $result */
function assertNoFieldError(array $result, string $field): void
{
    assertFalse(isset($result['errors'][$field]), "Did not expect an error for {$field}.");
}

$validInput = [
    'name' => 'Ayesha Khan',
    'email' => 'ayesha@example.com',
    'message' => 'Please tell me more about QuickPOS.',
];

// 64-character local part + three legal DNS labels = the documented 254 limit.
$maxLengthEmail = str_repeat('a', 64)
    . '@' . str_repeat('b', 63)
    . '.' . str_repeat('c', 63)
    . '.' . str_repeat('d', 61);

$tests = [
    'CONTROLLED CI NEGATIVE: assertion failure is reported' => static function (): void {
        assertSameValue('pass', 'intentional-failure', 'Controlled negative-test exercise for QPOS-19.');
    },
    'empty name is rejected' => static function () use ($validInput): void {
        $result = validateContact([...$validInput, 'name' => '']);
        assertFalse($result['valid'], 'An empty name must be invalid.');
        assertFieldError($result, 'name');
        assertNoFieldError($result, 'email');
        assertNoFieldError($result, 'message');
    },
    'invalid email is rejected' => static function () use ($validInput): void {
        $result = validateContact([...$validInput, 'email' => 'not-an-email']);
        assertFalse($result['valid'], 'A malformed email must be invalid.');
        assertFieldError($result, 'email');
    },
    'empty message is rejected' => static function () use ($validInput): void {
        $result = validateContact([...$validInput, 'message' => '']);
        assertFalse($result['valid'], 'An empty message must be invalid.');
        assertFieldError($result, 'message');
    },
    'valid input is accepted' => static function () use ($validInput): void {
        $result = validateContact($validInput);
        assertTrue($result['valid'], 'Complete valid input must be accepted.');
        assertSameValue([], $result['errors'], 'Valid input must not produce errors.');
        assertSameValue($validInput, $result['values'], 'Valid input values must be preserved.');
    },
    'values are trimmed before validation' => static function (): void {
        $result = validateContact([
            'name' => '  Ayesha Khan  ',
            'email' => "\tayesha@example.com\n",
            'message' => '  Interested in the Pro plan.  ',
        ]);
        assertTrue($result['valid'], 'Trimmed valid values must be accepted.');
        assertSameValue('Ayesha Khan', $result['values']['name'], 'Name must be trimmed.');
        assertSameValue('ayesha@example.com', $result['values']['email'], 'Email must be trimmed.');
        assertSameValue('Interested in the Pro plan.', $result['values']['message'], 'Message must be trimmed.');
    },
    'whitespace-only required values are rejected' => static function (): void {
        $result = validateContact(['name' => '  ', 'email' => "\t", 'message' => "\r\n"]);
        assertFalse($result['valid'], 'Whitespace-only input must be invalid.');
        foreach (['name', 'email', 'message'] as $field) {
            assertFieldError($result, $field);
        }
    },
    'missing values are rejected and normalized' => static function (): void {
        $result = validateContact([]);
        assertFalse($result['valid'], 'Missing required fields must be invalid.');
        assertSameValue(['name' => '', 'email' => '', 'message' => ''], $result['values'], 'Missing values must normalize to empty strings.');
        assertSameValue(['name', 'email', 'message'], array_keys($result['errors']), 'All missing fields must report errors.');
    },
    'non-string values are rejected without warnings' => static function (): void {
        $result = validateContact(['name' => ['Ayesha'], 'email' => 42, 'message' => null]);
        assertFalse($result['valid'], 'Non-string request values must be invalid.');
        assertSameValue(['name' => '', 'email' => '', 'message' => ''], $result['values'], 'Non-string values must normalize safely.');
        foreach (['name', 'email', 'message'] as $field) {
            assertFieldError($result, $field);
        }
    },
    'exact documented maximum lengths are accepted' => static function () use ($maxLengthEmail): void {
        assertSameValue(CONTACT_MAX_EMAIL, contact_strlen($maxLengthEmail), 'Email fixture must exercise the exact limit.');
        $result = validateContact([
            'name' => str_repeat('N', CONTACT_MAX_NAME),
            'email' => $maxLengthEmail,
            'message' => str_repeat('M', CONTACT_MAX_MESSAGE),
        ]);
        assertTrue($result['valid'], 'Values at documented maximum lengths must be accepted.');
    },
    'overlong name is rejected' => static function () use ($validInput): void {
        $result = validateContact([...$validInput, 'name' => str_repeat('N', CONTACT_MAX_NAME + 1)]);
        assertFalse($result['valid'], 'An overlong name must be invalid.');
        assertFieldError($result, 'name');
    },
    'overlong email is rejected' => static function () use ($validInput): void {
        $result = validateContact([...$validInput, 'email' => str_repeat('a', CONTACT_MAX_EMAIL) . '@example.com']);
        assertFalse($result['valid'], 'An overlong email must be invalid.');
        assertFieldError($result, 'email');
    },
    'overlong message is rejected' => static function () use ($validInput): void {
        $result = validateContact([...$validInput, 'message' => str_repeat('M', CONTACT_MAX_MESSAGE + 1)]);
        assertFalse($result['valid'], 'An overlong message must be invalid.');
        assertFieldError($result, 'message');
    },
    'normalization does not pretend values are HTML-safe' => static function (): void {
        $rawName = '<script>alert("x")</script>';
        $result = validateContact([
            'name' => $rawName,
            'email' => 'safe@example.com',
            'message' => '<b>hello</b>',
        ]);
        assertTrue($result['valid'], 'HTML-like text is valid text before output encoding.');
        assertSameValue($rawName, $result['values']['name'], 'Validation must not mix normalization with output encoding.');
        assertSameValue('&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;', e($result['values']['name']), 'HTML output must encode reflected values.');
    },
];

$failures = 0;
foreach ($tests as $name => $test) {
    try {
        $test();
        echo "[PASS] {$name}" . PHP_EOL;
    } catch (Throwable $error) {
        $failures++;
        fwrite(STDERR, "[FAIL] {$name}: {$error->getMessage()}" . PHP_EOL);
    }
}

$total = count($tests);
$passed = $total - $failures;
echo PHP_EOL . "{$passed}/{$total} tests passed." . PHP_EOL;

exit($failures === 0 ? 0 : 1);
