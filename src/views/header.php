<?php $base = $base ?? ''; ?>
<header class="site-header" id="top">
  <div class="container header-inner">
    <a class="brand" href="<?= e($base) ?>#top" aria-label="QuickPOS home">
      <svg class="brand-mark" viewBox="0 0 32 32" aria-hidden="true" focusable="false">
        <rect width="32" height="32" rx="8" fill="currentColor"/>
        <path d="M9 9h6v6H9zM17 9h6v6h-6zM9 17h6v6H9z" fill="none" stroke="#22D3EE" stroke-width="2" stroke-linejoin="round"/>
        <rect x="17" y="17" width="6" height="6" rx="1" fill="#22D3EE"/>
      </svg>
      <span class="brand-name">Quick<span>POS</span></span>
    </a>

    <nav class="nav-desktop" aria-label="Primary">
      <ul>
        <?php foreach (nav_links($base) as $link): ?>
          <li><a href="<?= e($link['href']) ?>"><?= e($link['label']) ?></a></li>
        <?php endforeach; ?>
      </ul>
    </nav>

    <a class="btn btn-dark header-cta" href="<?= e($base) ?>#contact">Sign Up</a>

    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu">
      <span class="menu-bars" aria-hidden="true"><i></i><i></i><i></i></span>
    </button>
  </div>

  <nav class="nav-mobile" id="mobile-menu" aria-label="Mobile" hidden>
    <div class="container">
      <ul>
        <?php foreach (nav_links($base) as $link): ?>
          <li><a href="<?= e($link['href']) ?>"><?= e($link['label']) ?></a></li>
        <?php endforeach; ?>
      </ul>
      <a class="btn btn-dark btn-block" href="<?= e($base) ?>#contact">Sign Up</a>
    </div>
  </nav>
</header>
