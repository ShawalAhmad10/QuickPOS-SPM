<section class="section" id="pricing" aria-labelledby="pricing-title">
  <div class="container">
    <div class="section-head">
      <p class="kicker">Pricing</p>
      <h2 id="pricing-title">Simple, transparent pricing.</h2>
      <p class="section-lead">Pick the plan that fits your shop today and change it as you grow. <strong>Prices are illustrative</strong> &mdash; QuickPOS is a fictional product and nothing here can be purchased.</p>
    </div>

    <ul class="plan-grid">
      <?php foreach (plans() as $key => $p): ?>
        <li class="plan<?= $p['featured'] ? ' is-featured' : '' ?>">
          <?php if ($p['featured']): ?><span class="plan-chip">Recommended</span><?php endif; ?>
          <h3><?= e($p['name']) ?></h3>
          <p class="plan-blurb"><?= e($p['blurb']) ?></p>
          <p class="plan-price">
            <span class="amount"><?= e($p['price']) ?></span>
            <?php if ($p['period'] !== ''): ?><span class="period"><?= e($p['period']) ?></span><?php endif; ?>
          </p>
          <p class="plan-flag">Illustrative price</p>
          <ul class="plan-features">
            <?php foreach ($p['features'] as $feature): ?>
              <li><?= icon('check') ?><span><?= e($feature) ?></span></li>
            <?php endforeach; ?>
          </ul>
          <a class="btn <?= $p['featured'] ? 'btn-primary' : 'btn-secondary' ?> btn-block"
             href="index.php?plan=<?= e($key) ?>#contact"
             aria-label="<?= e($p['cta']) ?>: go to the contact form for the <?= e($p['name']) ?> plan"><?= e($p['cta']) ?></a>
        </li>
      <?php endforeach; ?>
    </ul>
  </div>
</section>
