document.addEventListener("DOMContentLoaded", () => {
  initMobileNav();
  initFaq();
  initLeadForm();
  setYear();
});

function initMobileNav() {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector("[data-nav-toggle]");
  const nav = document.querySelector(".site-nav");
  if (!header || !toggle || !nav) return;

  function closeNav() {
    header.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
  }

  function openNav() {
    header.classList.add("is-open");
    toggle.setAttribute("aria-expanded", "true");
  }

  toggle.addEventListener("click", () => {
    if (header.classList.contains("is-open")) {
      closeNav();
    } else {
      openNav();
    }
  });

  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => closeNav());
  });

  document.addEventListener("click", (event) => {
    if (!header.classList.contains("is-open")) return;
    const target = event.target;
    if (target instanceof Node && !nav.contains(target) && !toggle.contains(target)) {
      closeNav();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeNav();
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 1080) closeNav();
  });
}

function initFaq() {
  const faqButtons = document.querySelectorAll("[data-faq-toggle]");
  faqButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const item = button.closest(".faq-item");
      if (!item) return;
      item.classList.toggle("is-open");
    });
  });
}

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
  return h === "lead-form";
}

function scrollLeadFormAnchorIntoView() {
  const el = document.getElementById("aanvraag");
  if (!el) return;
  const reduced = window.matchMedia?.("(prefers-reduced-motion: reduce)")?.matches;
  requestAnimationFrame(() => {
    el.scrollIntoView({ block: "start", behavior: reduced ? "auto" : "smooth" });
  });
}

function initLeadForm() {
  const form = document.querySelector("#lead-form");
  if (!form) return;

  let mode = "info";
  const modeButtons = document.querySelectorAll("[data-lead-mode]");
  const status = document.querySelector("#lead-status");

  const soortField = form.querySelector("#soort_aanvraag");

  function setSoortAanvraag() {
    if (!soortField) return;
    if (mode === "info") soortField.value = "Informatie";
    else if (mode === "offerte") soortField.value = "Offerte";
    else if (mode === "bel") soortField.value = "Terugbelverzoek";
  }

  function applyMode(nextMode) {
    mode = nextMode;
    modeButtons.forEach((button) => {
      button.classList.toggle("is-active", button.dataset.leadMode === mode);
    });
    setSoortAanvraag();

    form.querySelectorAll("[data-only='offerte']").forEach((fieldWrap) => {
      const hidden = mode !== "offerte";
      fieldWrap.classList.toggle("hidden", hidden);
      const input = fieldWrap.querySelector("input, select, textarea");
      if (input) input.required = !hidden;
    });

    form.querySelectorAll("[data-only='bel']").forEach((fieldWrap) => {
      const hidden = mode !== "bel";
      fieldWrap.classList.toggle("hidden", hidden);
      const input = fieldWrap.querySelector("input, select, textarea");
      if (input) input.required = !hidden;
    });
  }

  modeButtons.forEach((button) => {
    button.addEventListener("click", () => applyMode(button.dataset.leadMode));
  });

  form.addEventListener("submit", (event) => {
    const result = validateLeadForm(form, mode);
    if (!status) return;

    if (!result.ok) {
      event.preventDefault();
      status.className = "status error";
      status.textContent = result.message;
      return;
    }

    status.className = "status success";
    status.textContent = "Bedankt! We nemen binnen 1 werkdag contact met je op. Je wordt doorgestuurd...";
    // GA4: contact_submit event met soort_aanvraag (informatie/offerte/terugbelverzoek)
    if (typeof gtag === "function") {
      const soort = mode === "info" ? "informatie" : mode === "offerte" ? "offerte" : "terugbelverzoek";
      gtag("event", "contact_submit", { soort_aanvraag: soort });
    }
    // Let the form submit to Formspree
  });

  const fromUrl = readLeadModeFromUrl();
  applyMode(fromUrl || "info");
  if (leadFormDeepLinkNeedsJsScroll()) scrollLeadFormAnchorIntoView();
}

function validateLeadForm(form, mode) {
  const requiredFields = ["name", "phone", "email"];
  if (mode === "offerte") requiredFields.push("m2", "vloerdiepte", "ondergrond", "projecttype");
  if (mode === "bel") requiredFields.push("terugbel_moment");

  for (const fieldName of requiredFields) {
    const input = form.elements[fieldName];
    if (!input || !String(input.value).trim()) {
      return {
        ok: false,
        message: "Vul alle verplichte velden in voordat je verzendt."
      };
    }
  }

  const emailInput = form.elements.email;
  if (emailInput && !String(emailInput.value).includes("@")) {
    return { ok: false, message: "Vul een geldig e-mailadres in." };
  }

  return { ok: true };
}

function setYear() {
  const yearNode = document.querySelector("#year");
  if (yearNode) yearNode.textContent = String(new Date().getFullYear());
}
