<?php
declare(strict_types=1);

require_once __DIR__ . '/../src/bootstrap.php';

// Confirmation is only shown right after a valid POST to contact.php.
// Visiting this URL directly (or refreshing) cannot produce a false success.
start_confirmation_session();
$thanks = $_SESSION['qp_thanks'] ?? null;
unset($_SESSION['qp_thanks']);

if (!is_array($thanks)) {
    header('Location: index.php#contact', true, 303);
    exit;
}

$name = is_string($thanks['name'] ?? null) ? $thanks['name'] : '';
$plan = normalize_plan($thanks['plan'] ?? null);

$base = 'index.php';
render('layout-top', ['title' => 'Thanks — QuickPOS']);
render('header', ['base' => $base]);
?>
<main id="main">
  <section class="section thanks" aria-labelledby="thanks-title">
    <div class="container thanks-inner">
      <span class="thanks-icon"><?= icon('check') ?></span>
      <h1 id="thanks-title">Thanks, <?= e($name) ?>.</h1>
      <p class="lead">Your message passed validation<?= $plan !== '' ? ' and your interest in the ' . e(plans()[$plan]['name']) . ' plan was noted' : '' ?>.</p>
      <p class="demo-note">QuickPOS is a fictional demo. This submission was checked on the server, and your name and selected plan were kept only briefly in the PHP session for this one-time confirmation. <strong>It was not emailed, saved permanently or sent to anyone</strong>, and no one will reply.</p>
      <a class="btn btn-primary" href="index.php">Back to home</a>
    </div>
  </section>
</main>
<?php
render('footer', ['base' => $base]);
render('layout-bottom');
