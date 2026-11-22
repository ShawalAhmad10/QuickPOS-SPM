<section class="section section-surface" id="features" aria-labelledby="features-title">
  <div class="container">
    <div class="section-head">
      <p class="kicker">Features</p>
      <h2 id="features-title">Run the whole shop from one screen.</h2>
      <p class="section-lead">Four tools that work together, so the numbers at the till always match the numbers in your reports.</p>
    </div>

    <ul class="feature-grid">
      <?php foreach (features() as $f): ?>
        <li class="feature-card">
          <span class="feature-icon"><?= icon($f['icon']) ?></span>
          <h3><?= e($f['title']) ?></h3>
          <p><?= e($f['text']) ?></p>
          <span class="feature-meta"><?= icon('check') ?> <?= e($f['meta']) ?></span>
        </li>
      <?php endforeach; ?>
    </ul>
  </div>
</section>
