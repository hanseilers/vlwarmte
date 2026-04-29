/**
 * Load gtag after window "load" so first paint / LCP are less contended.
 * Events later in the session still call window.gtag once the script arrives.
 */
(function () {
  var MEASUREMENT_ID = "G-0BB9M7HYSF";

  function inject() {
    var s = document.createElement("script");
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + MEASUREMENT_ID;
    s.async = true;
    document.head.appendChild(s);
    s.onload = function () {
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      window.gtag = gtag;
      gtag("js", new Date());
      gtag("config", MEASUREMENT_ID);
    };
  }

  if (document.readyState === "complete") {
    inject();
  } else {
    window.addEventListener("load", inject, { once: true });
  }
})();
