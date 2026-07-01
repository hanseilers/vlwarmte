/* eslint-disable */

const COVER = {
  title: "Aanbevelingen voor een betere VLWarmte‑website",
  lead: "Een interne audit voor het ontwerp‑ en ontwikkelteam. Per onderdeel: bevinding, aanbeveling, geannoteerd voorstel en concrete specs op token‑niveau. Bedoeld om in één keer door te lezen en daarna stuk voor stuk te oppakken.",
  meta: [
    { k: "Voor", v: "Ontwerp + dev team" },
    { k: "Onderwerp", v: "vlwarmte.nl — marketingsite" },
    { k: "Datum", v: "9 mei 2026" },
    { k: "Status", v: "Concept — v1" },
  ],
};

const TOC = [
  { id: "visual", num: "01", label: "Visuele verfijning" },
  { id: "ia", num: "02", label: "Informatie-architectuur" },
  { id: "conversion", num: "03", label: "Conversie & vertrouwen" },
  { id: "prijs", num: "04", label: "Prijsindicatie" },
  { id: "regio", num: "05", label: "Regionale SEO" },
  { id: "mobile", num: "06", label: "Mobile-first" },
  { id: "roadmap", num: "07", label: "Roadmap" },
];

function DocHeader() {
  return (
    <header className="doc-header">
      <div className="container">
        <div className="doc-header-inner">
          <a href="#top" className="doc-brand">
            <span className="doc-brand-mark">
              <img src="assets/logo-mark-krul.svg" alt="" />
            </span>
            <span className="doc-brand-text">
              <span className="doc-brand-wordmark">
                <span className="vl">VL</span>Warmte
              </span>
              <span className="doc-brand-tagline">Design recommendations</span>
            </span>
          </a>
          <div className="doc-title-meta">
            <span className="label">Interne audit · v1</span>
            <span className="meta">9 mei 2026 · 7 hoofdstukken</span>
          </div>
        </div>
        <nav className="doc-toc" aria-label="Inhoudsopgave">
          {TOC.map((t) => (
            <a key={t.id} href={"#" + t.id}>
              <span className="num">{t.num}</span>
              <span>{t.label}</span>
            </a>
          ))}
        </nav>
      </div>
    </header>
  );
}

function Cover() {
  return (
    <section className="cover" id="top">
      <div className="container">
        <span className="cover-eyebrow">
          <span className="dot" />
          Interne audit · ontwerp + dev
        </span>
        <h1 className="cover-title">
          Aanbevelingen voor een <em>betere</em> VLWarmte‑website
        </h1>
        <p className="cover-lead">{COVER.lead}</p>
        <div className="cover-meta">
          {COVER.meta.map((m, i) => (
            <div key={i}>
              <div className="k">{m.k}</div>
              <div className="v">{m.v}</div>
            </div>
          ))}
        </div>
        <Pills items={[
          "Visuele verfijning",
          "Informatie-architectuur",
          "Conversie & vertrouwen",
          "Prijsindicatie",
          "Regionale SEO",
          "Mobile-first",
          "Roadmap",
        ]} />
      </div>
    </section>
  );
}

function DocFooter() {
  return (
    <footer style={{
      padding: "60px 0 80px",
      borderTop: "1px solid var(--line)",
      background: "linear-gradient(180deg, transparent 0%, rgba(8,14,22,0.6) 100%)",
    }}>
      <div className="container" style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", flexWrap: "wrap", gap: 12 }}>
        <div style={{ color: "var(--ink-muted)", fontSize: "0.85rem" }}>
          Document gegenereerd voor intern gebruik · VLWarmte design system v1
        </div>
        <div style={{ color: "var(--ink-muted)", fontSize: "0.85rem", fontFamily: "var(--font-mono)" }}>
          7 hoofdstukken · 24 aanbevelingen · concept
        </div>
      </div>
    </footer>
  );
}

function App() {
  return (
    <>
      <DocHeader />
      <Cover />
      <SectionVisual />
      <SectionIA />
      <SectionConversion />
      <SectionPrijs />
      <SectionRegio />
      <SectionMobile />
      <SectionRoadmap />
      <DocFooter />
    </>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
