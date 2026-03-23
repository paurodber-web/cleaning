
(function () {
  var STORAGE_KEY = 'mah_cookie_consent_v1';

  function getConsent() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null'); }
    catch (e) { return null; }
  }

  function setConsent(consent) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(consent));
  }

  function updateGtm(consent) {
    if (!window.dataLayer) { window.dataLayer = []; }
    window.dataLayer.push({
      event: 'cookie_consent_update',
      consent: consent
    });

    if (typeof gtag === 'function') {
      gtag('consent', 'update', {
        analytics_storage: consent.analytics ? 'granted' : 'denied',
        ad_storage: consent.marketing ? 'granted' : 'denied',
        ad_user_data: consent.marketing ? 'granted' : 'denied',
        ad_personalization: consent.marketing ? 'granted' : 'denied'
      });
    }
  }

  function ensureDefaultConsent() {
    if (typeof gtag === 'function') {
      gtag('consent', 'default', {
        analytics_storage: 'denied',
        ad_storage: 'denied',
        ad_user_data: 'denied',
        ad_personalization: 'denied'
      });
    }
  }

  function buildBanner() {
    var banner = document.createElement('div');
    banner.className = 'cs_cookie_banner';
    banner.innerHTML = [
      '<h3>Cookie preferences</h3>',
      '<p>We use cookies to improve your experience. Choose which cookies you want to allow.</p>',
      '<div class="cs_cookie_options">',
      '  <div class="cs_cookie_option"><label><input type="checkbox" checked disabled> Essential</label><span>Always on</span></div>',
      '  <div class="cs_cookie_option"><label><input type="checkbox" id="cs_cookie_analytics"> Analytics</label><span>Helps us improve</span></div>',
      '  <div class="cs_cookie_option"><label><input type="checkbox" id="cs_cookie_marketing"> Marketing</label><span>Personalized ads</span></div>',
      '</div>',
      '<div class="cs_cookie_actions">',
      '  <button class="cs_btn cs_btn_outline" id="cs_cookie_reject">Reject non-essential</button>',
      '  <button class="cs_btn cs_btn_primary" id="cs_cookie_accept">Accept all</button>',
      '  <button class="cs_btn" id="cs_cookie_save" style="grid-column: 1 / -1;">Save preferences</button>',
      '</div>'
    ].join('');

    return banner;
  }

  function init() {
    ensureDefaultConsent();

    var existing = getConsent();
    if (existing) {
      updateGtm(existing);
      return;
    }

    setTimeout(function() {
      var banner = buildBanner();
      document.body.appendChild(banner);

      var analytics = banner.querySelector('#cs_cookie_analytics');
      var marketing = banner.querySelector('#cs_cookie_marketing');

      banner.querySelector('#cs_cookie_accept').addEventListener('click', function () {
        var consent = { analytics: true, marketing: true };
        setConsent(consent);
        updateGtm(consent);
        banner.remove();
      });

      banner.querySelector('#cs_cookie_reject').addEventListener('click', function () {
        var consent = { analytics: false, marketing: false };
        setConsent(consent);
        updateGtm(consent);
        banner.remove();
      });

      banner.querySelector('#cs_cookie_save').addEventListener('click', function () {
        var consent = { analytics: !!analytics.checked, marketing: !!marketing.checked };
        setConsent(consent);
        updateGtm(consent);
        banner.remove();
      });
    }, 2000);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
