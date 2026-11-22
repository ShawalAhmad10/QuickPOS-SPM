<?php
/** @var array{values: array<string,string>, errors: array<string,string>, plan: string} $contact */
$values = $contact['values'];
$errors = $contact['errors'];
$plan = $contact['plan'];
$planName = $plan !== '' ? plans()[$plan]['name'] : '';

/** aria/id wiring for one field. */
$attrs = static function (string $field) use ($errors): string {
    return isset($errors[$field])
        ? ' aria-invalid="true" aria-describedby="' . $field . '-error"'
        : '';
};
?>
<section class="section section-surface" id="contact" aria-labelledby="contact-title">
  <div class="container contact-grid">
    <div class="contact-intro">
      <p class="kicker">Contact</p>
      <h2 id="contact-title">Tell us about your shop.</h2>
      <p class="section-lead">Share a few details and what you would like to see. Every field is checked on the server before anything is accepted.</p>

      <?php if ($planName !== ''): ?>
        <p class="plan-selected">
          <span>Interested in</span> <strong><?= e($planName) ?></strong> plan
          <a href="index.php#pricing">Change</a>
        </p>
      <?php endif; ?>

      <p class="demo-note"><strong>Demo form:</strong> QuickPOS is fictional. Submissions are validated but never emailed or saved permanently. Your name and selected plan are kept briefly in the PHP session only to show the confirmation page.</p>
    </div>

    <form class="contact-form" method="post" action="contact.php#contact" novalidate>
      <?php if ($errors !== []): ?>
        <div class="form-summary" id="form-summary" role="alert" tabindex="-1">
          <strong>Please fix the following before sending:</strong>
          <ul>
            <?php foreach ($errors as $field => $message): ?>
              <li><a href="#<?= e($field) ?>"><?= e($message) ?></a></li>
            <?php endforeach; ?>
          </ul>
        </div>
      <?php endif; ?>

      <input type="hidden" name="plan" value="<?= e($plan) ?>">

      <div class="field<?= isset($errors['name']) ? ' has-error' : '' ?>">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" autocomplete="name" maxlength="<?= CONTACT_MAX_NAME ?>"
               value="<?= e($values['name']) ?>"<?= $attrs('name') ?>>
        <?php if (isset($errors['name'])): ?><p class="field-error" id="name-error"><?= e($errors['name']) ?></p><?php endif; ?>
      </div>

      <div class="field<?= isset($errors['email']) ? ' has-error' : '' ?>">
        <label for="email">Email</label>
        <input type="email" id="email" name="email" autocomplete="email" maxlength="<?= CONTACT_MAX_EMAIL ?>"
               value="<?= e($values['email']) ?>"<?= $attrs('email') ?>>
        <?php if (isset($errors['email'])): ?><p class="field-error" id="email-error"><?= e($errors['email']) ?></p><?php endif; ?>
      </div>

      <div class="field<?= isset($errors['message']) ? ' has-error' : '' ?>">
        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" maxlength="<?= CONTACT_MAX_MESSAGE ?>"<?= $attrs('message') ?>><?= e($values['message']) ?></textarea>
        <?php if (isset($errors['message'])): ?><p class="field-error" id="message-error"><?= e($errors['message']) ?></p><?php endif; ?>
      </div>

      <button class="btn btn-primary btn-block" type="submit">Send message</button>
    </form>
  </div>
</section>
