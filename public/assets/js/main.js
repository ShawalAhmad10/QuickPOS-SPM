(function () {
  'use strict';

  // After a failed form submit, move focus to the error summary for screen readers.
  var summary = document.getElementById('form-summary');
  // Deferred so it runs after the browser's own #contact fragment scroll/focus reset.
  if (summary) {
    window.addEventListener('load', function () {
      setTimeout(function () { summary.focus(); }, 50);
    });
  }

  var toggle = document.querySelector('.menu-toggle');
  var menu = document.getElementById('mobile-menu');
  if (!toggle || !menu) return;

  function setOpen(open, returnFocus) {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    menu.hidden = !open;
    document.documentElement.classList.toggle('menu-open', open);
    if (!open && returnFocus) toggle.focus();
  }

  toggle.addEventListener('click', function () {
    setOpen(toggle.getAttribute('aria-expanded') !== 'true');
  });

  // Close on Escape (returning focus to the button) and after choosing a link.
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false, true);
    }
  });
  menu.addEventListener('click', function (e) {
    if (e.target.closest('a')) setOpen(false);
  });

  // Close if the viewport grows to the desktop layout.
  var mq = window.matchMedia('(min-width: 861px)');
  var onChange = function (e) { if (e.matches) setOpen(false); };
  if (mq.addEventListener) mq.addEventListener('change', onChange);
  else if (mq.addListener) mq.addListener(onChange);
})();
