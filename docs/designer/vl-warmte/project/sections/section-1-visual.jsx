/* eslint-disable */
/* Section 01 — Visuele verfijning (typografie, hiërarchie, ruimte) */

function HeroCurrent() {
  return (
    <SnapshotCurrent>
      <div className="header">
        <div className="logo"><span className="vl">VL</span>Warmte</div>
        <div className="nav">
          <span>Home</span><span>Diensten</span><span>Werkwijze</span>
          <span>Projecten</span><span>Contact</span>
        </div>
      </div>
      <div className="body">
        <h1>Van ondervloer tot afgewerkte vloerverwarming</h1>
        <p className="lead">VLWarmte realiseert het complete traject — ondervloer, schuimbeton, leidingen en dekvloer. Eén aanspreekpunt van intake tot oplevering.</p>
        <div className="ctas">
          <span className="btn p">Vrijblijvende prijsindicatie</span>
          <span className="btn s">Bekijk werkwijze</span>
        </div>
        <div style={{ marginTop: 22, display: "flex", gap: 14, flexWrap: "wrap", fontSize: "0.78rem", color: "#8a97ad" }}>
          <span>✓ Eigen team</span>
          <span>✓ 10 jaar garantie</span>
          <span>✓ Heldere planning</span>
          <span>✓ Groningen · Friesland · Drenthe</span>
        </div>
      </div>
    </SnapshotCurrent>
  );
}

function HeroProposed() {
  return (
    <div className="snap-new">
      <div className="header">
        <div className="left">
          <span className="mark" />
          <span className="logo"><span className="vl">VL</span>Warmte</span>
        </div>
        <div className="nav">
          <span>Diensten</span><span>Werkwijze</span><span>Projecten</span>
          <span>Regio</span><span className="pill">Prijsindicatie</span>
        </div>
      </div>
      <div className="body">
        <div className="eyebrow">Vloerverwarming · van ondervloer tot oplevering</div>
        <h1>Slim gelegd.<br /><em>Gelijkmatig warm.</em></h1>
        <p className="lead">Eén specialist voor het hele traject — van ondervloer en schuimbeton tot leidingwerk en dekvloer. We werken met een eigen team in Groningen, Friesland en Drenthe.</p>
        <div className="ctas">
          <span className="btn p">Vrijblijvende prijsindicatie →</span>
          <span className="btn s">Hoe wij werken</span>
        </div>
      </div>
    </div>
  );
}

function SectionVisual() {
  return (
    <Section id="visual">
      <SectionHead
        num="01"
        kicker="Visuele verfijning"
        title="Een rustiger hiërarchie en meer ademruimte"
        lead="De huidige hero werkt — maar hij vraagt om meer ruimte, een duidelijker leeshiërarchie en typografie die past bij het specialistische karakter van het merk. Kleine ingrepen, groot effect."
      />

      <Finding
        problem={{
          title: "Hero is dichtbevolkt en zonder duidelijke focuspunt",
          body: [
            "H1, lead, twee CTA's en vier reassurance‑items concurreren visueel om aandacht. Niets ‘rust’ — het oog stuitert.",
            "Het belangrijkste verkoopargument (‘één aanspreekpunt’) verzuipt in de lopende lead.",
          ],
        }}
        fix={{
          title: "Eén heldere boodschap, ondersteund door visuele rust",
          body: [
            "Een tagline‑hero: korte krachtige claim met retorische pauze (regel 1: feit, regel 2: belofte).",
            "Reassurance verplaats je naar een aparte trust‑strip onder de hero — niet in de hero zelf.",
            "Eyebrow met streep ankert de pagina; gradient‑accent op één woord houdt de hero levendig zonder druk.",
          ],
        }}
      />

      <div className="mock-row">
        <MockFrame tag="current" url="vlwarmte.nl">
          <HeroCurrent />
        </MockFrame>
        <MockFrame tag="proposed" url="vlwarmte.nl">
          <HeroProposed />
          <Pin n="1" x={50} y={26} lx={4} ly={4} lw={210}
            label="Eyebrow met dunne streep — ankert de pagina, leest als 'van wat is dit een hero'." />
          <Pin n="2" x={42} y={48} lx={62} ly={36} lw={210}
            label="H1 in twee regels: claim + belofte. Gradient-fill alleen op woord 2 — verleidt zonder te schreeuwen." />
          <Pin n="3" x={28} y={87} lx={55} ly={82} lw={210}
            label="Twee CTA's, primair eerst. Reassurance verplaatst zich naar een aparte strip eronder." />
        </MockFrame>
      </div>

      <Specs title="Type & spacing tokens" items={[
        { k: "--fs-display", v: "clamp(2.6rem, 1.4rem + 4vw, 4.25rem) — gebruik op hero, niet op H1 reguliere secties" },
        { k: "--tracking-tight", v: "-0.03em — alle headings; voorkomt 'losse' kop-typografie" },
        { k: "--lh-tight", v: "1.1 — display; H1 in hero op 1.05 voor extra impact" },
        { k: "--space-16 / --space-20", v: "Hero padding: 5rem boven, 4rem onder. Niet kleiner — ademruimte is het punt." },
        { k: "Eyebrow streep", v: "16px breed, 1px hoog, --brand. Verticaal gecentreerd op de eyebrow x-height." },
        { k: "Gradient text", v: "linear-gradient(120deg, --vl-orange-500, --vl-orange-300) — alleen op één woord per pagina" },
      ]} />

      <Finding
        problem={{
          title: "Body‑tekst is te grijs én te grof",
          body: "Lead op #97a3b6 mist contrast op kleinere schermen; fontgrootte 1rem is te klein voor de moderne brede vloeitekst. Geen onderscheid tussen lead en gewone tekst.",
        }}
        fix={{
          title: "Twee tinten ink, twee groottes",
          body: [
            "Lead: 1.06rem op --ink-muted (#9aabbe). Body: 1rem op --ink (#e8eef7).",
            "max-width: 62ch op alle vloeitekst — dwingt rust af en houdt regellengte leesbaar.",
            "text-wrap: pretty op headings — voorkomt eenzame woorden op de laatste regel.",
          ],
        }}
      />

      <Note>
        <strong>Kleine WCAG-winst:</strong> de huidige muted-grijs (#97a3b6) op het pagina‑background haalt geen 4.5:1 in alle contexten.
        Token <code style={{ fontFamily: "var(--font-mono)", color: "var(--accent-glow)" }}>--ink-muted</code> staat al op #9aabbe — gebruik hem ook werkelijk voor body‑lead, niet voor body‑tekst.
      </Note>
    </Section>
  );
}

window.SectionVisual = SectionVisual;
