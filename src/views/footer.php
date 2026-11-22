<?php
$base = $base ?? '';
$year = date('Y');
?>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand brand-light" href="<?= e($base) ?>#top" aria-label="QuickPOS, back to top">
          <svg class="brand-mark" viewBox="0 0 32 32" aria-hidden="true" focusable="false">
            <rect width="32" height="32" rx="8" fill="#FFFFFF"/>
            <path d="M9 9h6v6H9zM17 9h6v6h-6zM9 17h6v6H9z" fill="none" stroke="#0891B2" stroke-width="2" stroke-linejoin="round"/>
            <rect x="17" y="17" width="6" height="6" rx="1" fill="#0891B2"/>
          </svg>
          <span class="brand-name">Quick<span>POS</span></span>
        </a>
        <p>One workspace for sales, stock and customers. A fictional product concept built for a course project.</p>
      </div>

      <nav aria-label="Site">
        <h2 class="footer-title">Site</h2>
        <ul>
          <?php foreach (nav_links($base) as $link): ?>
            <li><a href="<?= e($link['href']) ?>"><?= e($link['label']) ?></a></li>
          <?php endforeach; ?>
        </ul>
      </nav>

      <nav aria-label="Product">
        <h2 class="footer-title">Product</h2>
        <ul>
          <li><a href="<?= e($base) ?>#features">Inventory</a></li>
          <li><a href="<?= e($base) ?>#features">Analytics</a></li>
          <li><a href="<?= e($base) ?>#features">Customers</a></li>
          <li><a href="<?= e($base) ?>#features">Integrations</a></li>
        </ul>
      </nav>

      <div class="footer-social">
        <h2 class="footer-title">Follow</h2>
        <ul class="social-list">
          <li><span>LinkedIn</span></li>
          <li><span>X</span></li>
          <li><span>Instagram</span></li>
        </ul>
        <p class="footer-small">Social profiles are placeholders &mdash; QuickPOS has none yet.</p>
      </div>
    </div>

    <p class="footer-legal">&copy; <?= e($year) ?> QuickPOS. Fictional product for a course project. Prices and figures are illustrative.</p>
  </div>
</footer>
