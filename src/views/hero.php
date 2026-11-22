<section class="hero" aria-labelledby="hero-title">
  <div class="container hero-grid">
    <div class="hero-copy">
      <p class="kicker">Smarter retail operations</p>
      <h1 id="hero-title">Everything your business needs, at one point of sale.</h1>
      <p class="lead">Track sales, stay ahead of inventory, and understand customers&mdash;all from one streamlined workspace.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#contact">Get Started</a>
        <a class="btn btn-secondary" href="#features">Explore Features <?= icon('arrow') ?></a>
      </div>
      <ul class="hero-points" aria-label="Highlights">
        <li><?= icon('check') ?> Sales, stock and customers in one view</li>
        <li><?= icon('check') ?> Built for shops, caf&eacute;s and small teams</li>
      </ul>
    </div>
    <div class="hero-visual">
      <?php render('dashboard-mockup'); ?>
    </div>
  </div>
</section>
