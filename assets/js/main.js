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
    // Let the form submit to Formspree
  });

  applyMode("info");
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
