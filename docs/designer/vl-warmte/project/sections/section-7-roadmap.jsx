/* eslint-disable */
/* Section 07 — Roadmap & priorities */

const ROADMAP = [
  {
    phase: "Fase 1",
    weeks: "Week 1–2",
    title: "Quick wins",
    subtitle: "Hoge impact, kleine ingreep — direct doen",
    items: [
      { t: "Trust-strip onder hero", impact: "Hoog", effort: "S" },
      { t: "FAQ verplaatsen naar eigen pagina", impact: "Mid", effort: "S" },
      { t: "Sticky mobile CTA", impact: "Hoog", effort: "S" },
      { t: "Hero-typografie verfijnen (eyebrow, gradient)", impact: "Mid", effort: "S" },
      { t: "JSON-LD LocalBusiness op homepage", impact: "Hoog", effort: "S" },
    ],
  },
  {
    phase: "Fase 2",
    weeks: "Week 3–5",
    title: "Calculator & lead-form",
    subtitle: "De conversie-pijler — vraagt iets meer engineering",
    items: [
      { t: "Prijscalculator met range (sectie 04)", impact: "Hoog", effort: "M" },
      { t: "Multi-step lead form (sectie 03)", impact: "Hoog", effort: "M" },
      { t: "Referentie-trajecten in calculator", impact: "Mid", effort: "S" },
      { t: "FAQ-pagina met JSON-LD schema", impact: "Mid", effort: "S" },
    ],
  },
  {
    phase: "Fase 3",
    weeks: "Week 6–9",
    title: "IA & regio",
    subtitle: "Structurele SEO-investering — content-werk parallel aan dev",
    items: [
      { t: "Diensten splitsen (nieuwbouw / renovatie)", impact: "Mid", effort: "M" },
      { t: "Stadspagina-template + 5 invullingen", impact: "Hoog", effort: "L" },
      { t: "Projecten-detail-pagina's met regiofilter", impact: "Mid", effort: "M" },
      { t: "Schema per stadspagina + NAP-audit", impact: "Mid", effort: "S" },
    ],
  },
  {
    phase: "Fase 4",
    weeks: "Week 10+",
    title: "Polish & meten",
    subtitle: "Pas zinvol als 1–3 staan en data binnenstroomt",
    items: [
      { t: "A/B-test hero copy (claim-vs-belofte)", impact: "?", effort: "S" },
      { t: "Performance: glow vervangen door SVG-filter onder 720px", impact: "Mid", effort: "M" },
      { t: "Klantcase-pagina's met technische detail (3 stuks)", impact: "Mid", effort: "L" },
      { t: "Reviews-aggregator (Google → on-site)", impact: "Mid", effort: "M" },
    ],
  },
];

function PhaseBlock({ phase, weeks, title, subtitle, items, idx }) {
  return (
    <div style={{
      border: "1px solid var(--line)",
      borderRadius: "var(--radius-lg)",
      padding: "22px 24px",
      background: "linear-gradient(180deg, rgba(255,255,255,0.025) 0%, rgba(255,255,255,0) 100%)",
      position: "relative",
      overflow: "hidden",
    }}>
      <div style={{
        position: "absolute", top: 0, left: 0, right: 0, height: 3,
        background: idx === 0
          ? "linear-gradient(90deg, var(--brand) 0%, var(--vl-orange-300) 100%)"
          : "linear-gradient(90deg, rgba(224,85,47,0.4) 0%, rgba(95,163,224,0.4) 100%)",
        opacity: 0.6 + (3 - idx) * 0.1,
      }} />
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", flexWrap: "wrap", gap: 12, marginBottom: 6 }}>
        <div>
          <div style={{ fontSize: "0.7rem", letterSpacing: "0.18em", textTransform: "uppercase", color: "var(--brand)", fontFamily: "var(--font-mono)", marginBottom: 6 }}>
            {phase} · {weeks}
          </div>
          <div style={{ fontSize: "1.2rem", fontWeight: 800, color: "var(--ink-strong)", letterSpacing: "-0.02em" }}>{title}</div>
        </div>
      </div>
      <p style={{ color: "var(--ink-dim)", fontSize: "0.92rem", margin: "0 0 16px", maxWidth: "60ch" }}>{subtitle}</p>
      <div style={{ display: "grid", gap: 6 }}>
        {items.map((it, i) => (
          <div key={i} style={{
            display: "grid",
            gridTemplateColumns: "1fr auto auto",
            gap: 12, alignItems: "center",
            padding: "10px 12px",
            border: "1px solid var(--line)",
            borderRadius: 10,
            background: "rgba(255,255,255,0.02)",
            fontSize: "0.92rem",
          }}>
            <div style={{ color: "var(--ink)" }}>{it.t}</div>
            <span style={{
              fontFamily: "var(--font-mono)",
              fontSize: "0.7rem", padding: "2px 8px", borderRadius: 999,
              border: "1px solid var(--line-strong)",
              color: it.impact === "Hoog" ? "var(--brand)" : "var(--ink-muted)",
              letterSpacing: "0.04em",
            }}>
              impact · {it.impact}
            </span>
            <span style={{
              fontFamily: "var(--font-mono)",
              fontSize: "0.7rem", padding: "2px 8px", borderRadius: 999,
              background: "rgba(95,163,224,0.08)",
              color: "var(--accent-glow)",
              letterSpacing: "0.04em",
            }}>
              {it.effort}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

function SectionRoadmap() {
  return (
    <Section id="roadmap">
      <SectionHead
        num="07"
        kicker="Roadmap"
        title="Vier fases, ongeveer een kwartaal"
        lead="Volgorde is bewust: trust-elementen en sticky CTA eerst (kleinste ingreep, meeste impact), dan het conversie-hart, dan de structurele SEO-investering, dan polish en meten. Niets in fase 4 doen voordat 1–3 staan en de data spreekt."
      />

      <div style={{ display: "grid", gap: 16 }}>
        {ROADMAP.map((p, i) => (
          <PhaseBlock key={p.phase} {...p} idx={i} />
        ))}
      </div>

      <Note>
        <strong>Effort‑schaal:</strong> S = ½–1 dag · M = 2–5 dagen · L = 1–2 weken (incl. content). Aannames: één frontend‑dev, design‑oversight halftijds, copy door het VLWarmte‑team zelf voor regio‑pagina's.
      </Note>

      <div style={{
        marginTop: 40,
        padding: "28px 28px 24px",
        border: "1px solid var(--line-warm)",
        borderRadius: "var(--radius-lg)",
        background: "linear-gradient(140deg, rgba(224,85,47,0.06) 0%, rgba(95,163,224,0.04) 100%)",
        position: "relative", overflow: "hidden", isolation: "isolate",
      }}>
        <div style={{
          position: "absolute", inset: 0, zIndex: 0, pointerEvents: "none",
          background: "radial-gradient(ellipse 80% 60% at 90% 0%, rgba(224,85,47,0.18), transparent 60%)",
        }} />
        <div style={{ position: "relative" }}>
          <div style={{ fontSize: "0.7rem", letterSpacing: "0.18em", textTransform: "uppercase", color: "var(--brand)", fontFamily: "var(--font-mono)", marginBottom: 8 }}>
            Volgende stap
          </div>
          <div style={{ fontSize: "1.45rem", fontWeight: 800, color: "var(--ink-strong)", letterSpacing: "-0.025em", marginBottom: 8, maxWidth: "32ch" }}>
            Akkoord op fase 1 — dan kan ontwerp diezelfde week in productie.
          </div>
          <p style={{ color: "var(--ink-dim)", margin: 0, maxWidth: "60ch" }}>
            De vijf items in fase 1 raken geen IA en geen content — alleen UI‑componenten en wat schema‑markup. Dat maakt ze veilig om los te laten van het bredere herstructurerings‑plan en is daarmee een prima manier om de eerste resultaten te meten.
          </p>
        </div>
      </div>
    </Section>
  );
}

window.SectionRoadmap = SectionRoadmap;
