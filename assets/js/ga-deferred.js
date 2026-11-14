/**
 * Queue events immediately; defer the Google download until window "load" so
 * first paint / LCP stay less contended. A completed form can precede that
 * download, so gtag must exist before it finishes, not only in script.onload.
 */
(function () {
  var MEASUREMENT_ID = "G-0BB9M7HYSF";

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () {
    window.dataLayer.push(arguments);
  };
  window.gtag("js", new Date());
  window.gtag("config", MEASUREMENT_ID);

  function inject() {
    var s = document.createElement("script");
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + MEASUREMENT_ID;
    s.async = true;
    document.head.appendChild(s);
  }

  if (document.readyState === "complete") {
    inject();
  } else {
    window.addEventListener("load", inject, { once: true });
  }
})();
