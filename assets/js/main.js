document.addEventListener("DOMContentLoaded", () => {
  initMobileNav();
  initLeadForm();
  initCallbackForms();
  initOutboundGa();
  initWaFloat();
  setYear();
});

const FORM_ERROR_MESSAGE = "Er ging iets mis. App of bel ons op 06 188 17 459, of mail info@vlwarmte.nl.";
const MAX_PHOTO_BYTES = 10 * 1024 * 1024;

/* De zwevende WhatsApp-knop verdwijnt zolang een grote WhatsApp-knop, het contactblok,
   het formulier of de wizard in beeld is (alles met data-wa-primary). */
function initWaFloat() {
  const float = document.querySelector(".wa-float");
  const primaries = document.querySelectorAll("[data-wa-primary]");
  if (!float || !primaries.length || typeof IntersectionObserver === "undefined") return;
  const visible = new Set();
  const apply = () => float.setAttribute("data-hide", visible.size ? "true" : "false");

  // Beginstand direct bepalen; de observer houdt het daarna bij tijdens het scrollen.
  primaries.forEach((el) => {
    const rect = el.getBoundingClientRect();
    if (rect.width > 0 && rect.bottom > 0 && rect.top < window.innerHeight) visible.add(el);
  });
  apply();

  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) visible.add(entry.target);
      else visible.delete(entry.target);
    }
    apply();
  });
  primaries.forEach((el) => observer.observe(el));
}

function initMobileNav() {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector("[data-nav-toggle]");
  const nav = document.querySelector(".site-nav");
  if (!header || !toggle || !nav) return;

  function setOpen(open) {
    header.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? "Sluit navigatie" : "Open navigatie");
  }

  toggle.addEventListener("click", () => setOpen(!header.classList.contains("is-open")));

  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => setOpen(false));
  });

  document.addEventListener("click", (event) => {
    if (!header.classList.contains("is-open")) return;
    const target = event.target;
    if (target instanceof Node && !nav.contains(target) && !toggle.contains(target)) setOpen(false);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && header.classList.contains("is-open")) {
      setOpen(false);
      toggle.focus();
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth >= 1130) setOpen(false);
  });
}

/* ---------- Contactformulier: deeplinks ---------- */

const LEAD_MODES = {
  info: {
    soort: "Informatie",
    event: "informatie",
    title: "Liever een formulier?",
    intro: "Drie velden is genoeg. De rest vragen we als we contact met je opnemen.",
    messageLabel: "Je vraag",
    messageHint: "Bijvoorbeeld: welke ruimte, ongeveer hoeveel m² en wanneer je wilt beginnen."
  },
  offerte: {
    soort: "Offerte",
    event: "offerte",
    title: "Offerte aanvragen",
    intro: "Vertel kort wat je plan is. De maten en de rest vragen we als we contact met je opnemen.",
    messageLabel: "Je plan",
    messageHint: "Bijvoorbeeld: welke ruimte, ongeveer hoeveel m², wat er nu ligt en wanneer je wilt beginnen."
  },
  bel: {
    soort: "Terugbelverzoek",
    event: "terugbelverzoek",
    title: "Laat je terugbellen",
    intro: "Laat je nummer achter. We bellen je op een moment dat jou uitkomt.",
    messageLabel: "Wanneer komt het uit?",
    messageHint: "Bijvoorbeeld: morgenochtend, of na 17.00 uur. Je mag je vraag er ook bij zetten."
  }
};

function normalizeLeadModeQueryValue(raw) {
  if (raw == null) return null;
  const v = String(raw).trim().toLowerCase();
  if (!v) return null;
  if (v === "info" || v === "informatie") return "info";
  if (v === "offerte") return "offerte";
  if (v === "bel" || v === "terugbel" || v === "terugbelverzoek") return "bel";
  return null;
}

function readLeadModeFromUrl() {
  try {
    const params = new URL(window.location.href).searchParams;
    return (
      normalizeLeadModeQueryValue(params.get("modus")) ||
      normalizeLeadModeQueryValue(params.get("tab"))
    );
  } catch {
    return null;
  }
}

function leadFormDeepLinkNeedsJsScroll() {
  if (readLeadModeFromUrl()) return true;
  const h = window.location.hash.replace(/^#/, "").toLowerCase();
  return h === "lead-form" || h === "formulier";
}

function scrollLeadFormAnchorIntoView() {
  const el = document.getElementById("aanvraag");
  if (!el) return;
  const reduced = window.matchMedia?.("(prefers-reduced-motion: reduce)")?.matches;
  requestAnimationFrame(() => {
    el.scrollIntoView({ block: "start", behavior: reduced ? "auto" : "smooth" });
  });
}

/* Oude deeplinks (?modus=info|offerte|bel) vallen terug op hetzelfde korte formulier:
   alleen de kop, de toelichting en het verborgen veld soort_aanvraag passen zich aan. */
function applyLeadMode(form, mode) {
  const config = LEAD_MODES[mode] || LEAD_MODES.info;
  const soortField = form.querySelector("#soort_aanvraag");
  if (soortField) soortField.value = config.soort;
  const targets = {
    "[data-lead-title]": config.title,
    "[data-lead-intro]": config.intro,
    "[data-lead-message-label]": config.messageLabel,
    "[data-lead-message-hint]": config.messageHint
  };
  for (const [selector, text] of Object.entries(targets)) {
    const node = document.querySelector(selector);
    if (node) node.textContent = text;
  }
  document.body.classList.toggle("lead-mode-info", mode === "info");
  document.body.classList.toggle("lead-mode-offerte", mode === "offerte");
  document.body.classList.toggle("lead-mode-bel", mode === "bel");
}

function looksLikeEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}

function looksLikePhone(value) {
  return value.replace(/\D/g, "").length >= 8;
}

function validateLeadForm(form) {
  for (const fieldName of ["name", "contact", "message"]) {
    const input = form.elements[fieldName];
    if (!input || !String(input.value).trim()) {
      return {
        ok: false,
        field: input,
        message: "Vul je naam, je telefoonnummer of e-mailadres en je vraag in."
      };
    }
  }

  const contactInput = form.elements.contact;
  const contact = String(contactInput.value).trim();
  if (!looksLikeEmail(contact) && !looksLikePhone(contact)) {
    return {
      ok: false,
      field: contactInput,
      message: "Vul een geldig telefoonnummer of e-mailadres in, zodat we je kunnen bereiken."
    };
  }

  const photos = form.elements.foto;
  if (photos && photos.files) {
    let total = 0;
    for (const file of photos.files) total += file.size;
    if (total > MAX_PHOTO_BYTES) {
      return {
        ok: false,
        field: photos,
        message: "De foto's zijn samen groter dan 10 MB. Stuur ze gerust via WhatsApp."
      };
    }
  }

  return { ok: true };
}

function postForm(action, data) {
  return fetch(action, { method: "POST", body: data, headers: { Accept: "application/json" } });
}

function initLeadForm() {
  const form = document.querySelector("#lead-form");
  if (!form) return;
  const status = document.querySelector("#lead-status");

  const mode = readLeadModeFromUrl() || "info";
  applyLeadMode(form, mode);
  if (leadFormDeepLinkNeedsJsScroll()) scrollLeadFormAnchorIntoView();

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (!status) return;

    const result = validateLeadForm(form);
    if (!result.ok) {
      status.className = "status error";
      status.textContent = result.message;
      if (result.field && typeof result.field.focus === "function") result.field.focus();
      return;
    }

    const btn = form.querySelector('button[type="submit"]');
    const origLabel = btn ? btn.textContent : null;
    if (btn) { btn.disabled = true; btn.textContent = "Versturen…"; }
    status.className = "status";
    status.textContent = "";

    const data = new FormData(form);
    const contact = String(data.get("contact") || "").trim();
    // Formspree gebruikt het veld "email" als antwoordadres; zet het alleen als het er een is.
    if (looksLikeEmail(contact)) data.set("email", contact);
    else data.set("phone", contact);
    const photos = form.elements.foto;
    const hasPhotos = Boolean(photos && photos.files && photos.files.length);
    if (!hasPhotos) data.delete("foto");

    try {
      let res = await postForm(form.action, data);
      let photoDropped = false;
      if (!res.ok && hasPhotos) {
        // Komt de bijlage niet door, dan gaat het bericht alsnog zonder foto weg.
        data.delete("foto");
        data.set("foto_niet_meegekomen", "ja");
        res = await postForm(form.action, data);
        photoDropped = res.ok;
      }
      if (!res.ok) throw new Error("form submit failed");

      status.className = "status success";
      status.textContent = photoDropped
        ? "Bedankt, je bericht is verstuurd. De foto kwam niet mee: stuur die gerust via WhatsApp."
        : "Bedankt! We nemen binnen één werkdag contact met je op.";
      form.reset();
      applyLeadMode(form, mode);
      if (btn) { btn.disabled = false; btn.textContent = origLabel; }
      if (typeof gtag === "function") {
        gtag("event", "contact_submit", { soort_aanvraag: (LEAD_MODES[mode] || LEAD_MODES.info).event });
      }
    } catch {
      status.className = "status error";
      status.textContent = FORM_ERROR_MESSAGE;
      if (btn) { btn.disabled = false; btn.textContent = origLabel; }
    }
  });
}

/* ---------- Terugbelformulier in het contactblok ---------- */

function initCallbackForms() {
  document.querySelectorAll(".js-callback-form").forEach((form) => {
    const status = form.querySelector("[data-status]");
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      if (!status) return;

      const phoneInput = form.elements.phone;
      if (!phoneInput || !looksLikePhone(String(phoneInput.value))) {
        status.className = "status error";
        status.textContent = "Vul je telefoonnummer in, dan bellen we je terug.";
        if (phoneInput) phoneInput.focus();
        return;
      }

      const btn = form.querySelector('button[type="submit"]');
      const origLabel = btn ? btn.textContent : null;
      if (btn) { btn.disabled = true; btn.textContent = "Versturen…"; }
      status.className = "status";
      status.textContent = "";

      const data = new FormData(form);
      data.set("pagina", window.location.pathname);

      try {
        const res = await postForm(form.action, data);
        if (!res.ok) throw new Error("callback submit failed");
        status.className = "status success";
        status.textContent = "Bedankt! We bellen je terug op het moment dat je koos.";
        form.reset();
        if (typeof gtag === "function") {
          gtag("event", "contact_submit", { soort_aanvraag: "terugbelverzoek" });
        }
      } catch {
        status.className = "status error";
        status.textContent = FORM_ERROR_MESSAGE;
      } finally {
        if (btn) { btn.disabled = false; btn.textContent = origLabel; }
      }
    });
  });
}

/* ---------- GA4: uitgaande klikken naar Facebook en WhatsApp ---------- */

function initOutboundGa() {
  document.addEventListener("click", (event) => {
    const a = event.target && event.target.closest && event.target.closest("a[href]");
    if (!a || !(a instanceof HTMLAnchorElement)) return;
    let url;
    try {
      url = new URL(a.href, window.location.href);
    } catch {
      return;
    }
    if (typeof gtag !== "function") return;
    if (url.hostname.includes("facebook.com")) {
      gtag("event", "facebook_outbound", {
        link_url: a.href,
        link_text: (a.textContent || "").trim().slice(0, 100)
      });
      return;
    }
    if (url.hostname === "wa.me" || url.hostname.includes("whatsapp.com")) {
      gtag("event", "whatsapp_outbound", {
        link_url: a.href,
        link_text: (a.getAttribute("aria-label") || a.textContent || "").trim().slice(0, 100)
      });
    }
  });
}

function setYear() {
  const yearNode = document.querySelector("#year");
  if (yearNode) yearNode.textContent = String(new Date().getFullYear());
}
