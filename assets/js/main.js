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
    if (window.innerWidth > 1360) closeNav();
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

  function applyMode(nextMode) {
    mode = nextMode;
    modeButtons.forEach((button) => {
      button.classList.toggle("is-active", button.dataset.leadMode === mode);
    });

    const offerteFields = form.querySelectorAll("[data-only='offerte']");
    offerteFields.forEach((fieldWrap) => {
      const hidden = mode !== "offerte";
      fieldWrap.classList.toggle("hidden", hidden);
      const input = fieldWrap.querySelector("input, select, textarea");
      if (input) input.required = !hidden;
    });
  }

  modeButtons.forEach((button) => {
    button.addEventListener("click", () => applyMode(button.dataset.leadMode));
  });

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const result = validateLeadForm(form, mode);
    if (!status) return;

    if (!result.ok) {
      status.className = "status error";
      status.textContent = result.message;
      return;
    }

    status.className = "status success";
    status.textContent = "Bedankt! We nemen binnen 1 werkdag contact met je op.";
    form.reset();
    applyMode("info");
  });

  applyMode("info");
}

function validateLeadForm(form, mode) {
  const requiredFields = ["name", "phone", "email"];
  if (mode === "offerte") requiredFields.push("m2", "ondergrond", "projecttype");

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
