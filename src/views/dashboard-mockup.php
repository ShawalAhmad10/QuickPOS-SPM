<?php
/**
 * Original, illustrative POS dashboard built from HTML/CSS/SVG.
 * All figures and product names are fictional sample data.
 */
$products = [
    ['name' => 'Single-origin beans 1kg', 'units' => 148, 'pct' => 92],
    ['name' => 'Oat milk, 1L', 'units' => 121, 'pct' => 76],
    ['name' => 'Ceramic pour-over set', 'units' => 74, 'pct' => 48],
    ['name' => 'Reusable cup, 350ml', 'units' => 52, 'pct' => 34],
];
$sales = [
    ['id' => '#4821', 'item' => '3 items', 'time' => '2:41 PM', 'amount' => '$42.60', 'tag' => 'Card'],
    ['id' => '#4820', 'item' => '1 item', 'time' => '2:38 PM', 'amount' => '$18.00', 'tag' => 'Cash'],
    ['id' => '#4819', 'item' => '5 items', 'time' => '2:30 PM', 'amount' => '$96.25', 'tag' => 'Card'],
];
?>
<figure class="mock" role="img" aria-label="Illustrative QuickPOS dashboard showing today's sales, orders, low-stock items, a revenue trend, top products and recent sales. Sample data only.">
  <div class="mock-window" aria-hidden="true">
    <div class="mock-bar">
      <span class="dot"></span><span class="dot"></span><span class="dot"></span>
      <span class="mock-url">app.quickpos.example</span>
    </div>

    <div class="mock-body">
      <div class="mock-rail">
        <span class="rail-logo"></span>
        <span class="rail-item is-active"><?= icon('grid') ?></span>
        <span class="rail-item"><?= icon('orders') ?></span>
        <span class="rail-item"><?= icon('inventory') ?></span>
        <span class="rail-item"><?= icon('people') ?></span>
        <span class="rail-item rail-bottom"><?= icon('cog') ?></span>
      </div>

      <div class="mock-main">
        <div class="mock-head">
          <div>
            <p class="mock-title">Today</p>
            <p class="mock-sub">Harbor Street Café</p>
          </div>
          <div class="mock-tabs">
            <span class="is-active">Sales</span><span>Orders</span><span>Inventory</span>
          </div>
        </div>

        <div class="mock-kpis">
          <div class="kpi">
            <span class="kpi-label">Revenue</span>
            <strong>$3,284</strong>
            <span class="kpi-delta up">+12.4%</span>
          </div>
          <div class="kpi">
            <span class="kpi-label">Orders</span>
            <strong>186</strong>
            <span class="kpi-delta up">+8.1%</span>
          </div>
          <div class="kpi">
            <span class="kpi-label">Low stock</span>
            <strong>7 items</strong>
            <span class="kpi-delta warn">Reorder</span>
          </div>
        </div>

        <div class="mock-panels">
          <div class="panel panel-chart">
            <div class="panel-head">
              <span>Revenue by hour</span>
              <span class="legend"><i></i>Today <i class="prev"></i>Last week</span>
            </div>
            <svg class="chart" viewBox="0 0 400 150" preserveAspectRatio="none" focusable="false">
              <g stroke="#E2E8F0" stroke-width="1">
                <line x1="0" y1="30" x2="400" y2="30"/>
                <line x1="0" y1="70" x2="400" y2="70"/>
                <line x1="0" y1="110" x2="400" y2="110"/>
              </g>
              <path d="M0 108 C40 100 60 92 100 96 S160 70 200 74 S270 52 310 56 S370 34 400 28 L400 150 L0 150 Z" fill="#0891B2" fill-opacity="0.10"/>
              <path d="M0 118 C40 112 70 108 110 106 S170 96 210 98 S280 84 320 80 S375 70 400 66" fill="none" stroke="#94A3B8" stroke-width="2" stroke-dasharray="4 5" stroke-linecap="round" vector-effect="non-scaling-stroke"/>
              <path d="M0 108 C40 100 60 92 100 96 S160 70 200 74 S270 52 310 56 S370 34 400 28" fill="none" stroke="#0891B2" stroke-width="2.5" stroke-linecap="round" vector-effect="non-scaling-stroke"/>
              <circle cx="310" cy="56" r="4.5" fill="#fff" stroke="#0891B2" stroke-width="2.5" vector-effect="non-scaling-stroke"/>
            </svg>
            <div class="chart-axis"><span>9am</span><span>11am</span><span>1pm</span><span>3pm</span><span>5pm</span></div>
          </div>

          <div class="panel panel-products">
            <div class="panel-head"><span>Top products</span><span class="muted">Units</span></div>
            <ul class="prod-list">
              <?php foreach ($products as $p): ?>
                <li>
                  <div class="prod-row"><span><?= e($p['name']) ?></span><b><?= (int) $p['units'] ?></b></div>
                  <div class="bar"><i style="width: <?= (int) $p['pct'] ?>%"></i></div>
                </li>
              <?php endforeach; ?>
            </ul>
          </div>

          <div class="panel panel-sales">
            <div class="panel-head"><span>Recent sales</span><span class="muted">Live</span></div>
            <ul class="sale-list">
              <?php foreach ($sales as $s): ?>
                <li>
                  <span class="sale-id"><?= e($s['id']) ?></span>
                  <span class="sale-meta"><?= e($s['item']) ?> &middot; <?= e($s['time']) ?></span>
                  <span class="chip"><?= e($s['tag']) ?></span>
                  <b><?= e($s['amount']) ?></b>
                </li>
              <?php endforeach; ?>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="mock-float" aria-hidden="true">
    <span class="float-icon"><?= icon('inventory') ?></span>
    <div>
      <b>Oat milk, 1L</b>
      <span>Only 6 left &middot; reorder suggested</span>
    </div>
  </div>
  <figcaption class="mock-note">Illustrative interface &middot; sample data</figcaption>
</figure>
