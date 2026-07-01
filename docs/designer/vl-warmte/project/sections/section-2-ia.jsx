/* eslint-disable */
/* Section 02 — Informatie-architectuur */

function SitemapCurrent() {
  return (
    <div style={{ padding: 24, background: "#0e1825", minHeight: 320 }}>
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 14, color: "#cdd6e3" }}>
        <div style={{ padding: "10px 20px", border: "1px solid rgba(255,255,255,0.18)", borderRadius: 8, fontWeight: 700, fontSize: "0.88rem" }}>
          Home
        </div>
        <div style={{ width: 1, height: 18, background: "rgba(255,255,255,0.18)" }} />
        <div style={{ display: "flex", gap: 8, flexWrap: "wrap", justifyContent: "center" }}>
          {["Diensten", "Werkwijze", "Projecten", "Prijsindicatie", "Contact"].map((s) => (
            <div key={s} style={{ padding: "8px 14px", border: "1px solid rgba(255,255,255,0.15)", borderRadius: 8, fontSize: "0.78rem", color: "#a8b3c4" }}>
              {s}
            </div>
          ))}
        </div>
        <div style={{ marginTop: 12, color: "#7a8699", fontSize: "0.78rem", textAlign: "center", maxWidth: 320 }}>
          Eén lange homepage, alle diensten plat naast elkaar, geen regio‑pagina's, FAQ alleen onder prijsindicatie.
        </div>
      </div>
    </div>
  );
}

function SitemapProposed() {
  const Node = ({ children, accent, style }) => (
    <div style={{
      padding: "8px 14px",
      borderRadius: 8,
      fontSize: "0.78rem",
      fontWeight: accent ? 700 : 500,
      color: accent ? "white" : "var(--ink-dim)",
      border: `1px solid ${accent ? "rgba(224,85,47,0.5)" : "var(--line-strong)"}`,
      background: accent ? "linear-gradient(135deg, var(--brand), var(--brand-dark))" : "rgba(255,255,255,0.02)",
      ...style,
    }}>
      {children}
    </div>
  );
  const SubLine = ({ children }) => (
    <div style={{ display: "flex", gap: 6, flexWrap: "wrap", justifyContent: "center" }}>{children}</div>
  );
  const Sub = ({ children }) => (
    <div style={{
      padding: "5px 10px", borderRadius: 6, fontSize: "0.7rem",
      color: "var(--ink-muted)", border: "1px dashed var(--line-strong)",
    }}>{children}</div>
  );
  return (
    <div style={{ padding: 22, minHeight: 320, position: "relative" }}>
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 12 }}>
        <Node accent>Home</Node>
        <div style={{ width: 1, height: 14, background: "var(--line-strong)" }} />
        <SubLine>
          <Node>Diensten</Node>
          <Node>Werkwijze</Node>
          <Node>Projecten</Node>
          <Node>Regio</Node>
          <Node>Over</Node>
          <Node>Contact</Node>
        </SubLine>
        <div style={{ width: 1, height: 12, background: "var(--line-strong)" }} />
        <SubLine>
          <Sub>Nieuwbouw</Sub>
          <Sub>Renovatie · infrezen</Sub>
          <Sub>Schuimbeton</Sub>
          <Sub>Dekvloer</Sub>
        </SubLine>
        <SubLine>
          <Sub>Zuidlaren</Sub>
          <Sub>Groningen</Sub>
          <Sub>Assen</Sub>
          <Sub>Leeuwarden</Sub>
          <Sub>Drachten</Sub>
        </SubLine>
        <SubLine>
          <Sub>Prijsindicatie (sticky CTA)</Sub>
          <Sub>FAQ (eigen pagina)</Sub>
        </SubLine>
      </div>
    </div>
  );
}

function SectionIA() {
  return (
    <Section id="ia" alt>
      <SectionHead
        num="02"
        kicker="Informatie-architectuur"
        title="Diensten splitsen, regio's een eigen plek geven"
        lead="De site is nu één lange homepage met alle diensten plat naast elkaar. Voor SEO én voor de bezoeker met een specifieke vraag (renovatie? infrezen? in Drachten?) ontbreekt diepgang. Een lichte herstructurering opent veel content‑ en SEO‑ruimte."
      />

      <Finding
        problem={{
          title: "Geen onderscheid tussen nieuwbouw en renovatie",
          body: "Beide trajecten zijn fundamenteel anders (sloop vs. infrezen, droogtijden, prijsstructuur), maar de site behandelt ze als één rijtje 'diensten'. Bezoekers met een renovatievraag haken af.",
        }}
        fix={{
          title: "Twee duidelijke instappaden in de hoofdnav",
          body: [
            "Splits Diensten in twee kindpagina's: 'Nieuwbouw' en 'Renovatie · infrezen' — elk met eigen werkwijze, prijsrange en projectvoorbeelden.",
            "Houd /diensten als overzicht (hub), maar zorg dat de homepage rechtstreeks doorlinkt naar het juiste subpad.",
          ],
        }}
      />

      <Finding
        problem={{
          title: "Regio's bestaan in copy, niet in URL",
          body: "Groningen, Friesland en Drenthe staan vier keer op de homepage genoemd, maar er bestaat geen /regio/zuidlaren of /vloerverwarming-assen. Lokale zoekopdrachten ('vloerverwarming Drachten') vinden geen specifieke landingspagina.",
        }}
        fix={{
          title: "Eigen regio‑hub met vijf stadspagina's",
          body: [
            "Top: Zuidlaren · Groningen · Assen · Leeuwarden · Drachten. (Zie sectie 05 voor het sjabloon.)",
            "Eén /regio overzicht met kaart + lijst, en N stadspagina's met dezelfde structuur maar lokale invulling.",
          ],
        }}
      />

      <div className="mock-row">
        <MockFrame tag="current" url="vlwarmte.nl/sitemap">
          <SitemapCurrent />
        </MockFrame>
        <MockFrame tag="proposed" url="vlwarmte.nl/sitemap">
          <SitemapProposed />
          <Pin n="1" x={50} y={28} lx={3} ly={4} lw={170}
            label="Voeg 'Regio' en 'Over' toe aan de hoofdnav. 6 items past nog ruim." />
          <Pin n="2" x={28} y={64} lx={1} ly={56} lw={180}
            label="Diensten splitst in nieuwbouw vs. renovatie — twee aparte trajecten met eigen prijsrange." />
          <Pin n="3" x={70} y={70} lx={68} ly={50} lw={190}
            label="5 stadspagina's. Eigen URL per stad voor lokale SEO en context." />
        </MockFrame>
      </div>

      <Finding
        problem={{
          title: "FAQ is verstopt onder prijsindicatie",
          body: "5 veelgestelde vragen leven nu onderaan het lead‑formulier. Daar mis je de SEO‑waarde (FAQ‑schema) én bezoekers die op een specifieke vraag binnenkomen via Google.",
        }}
        fix={{
          title: "FAQ als eigen pagina + uitgebreide vraagset",
          body: [
            "Verhuis FAQ naar /veelgestelde-vragen met categorieën (Prijs, Werkwijze, Garantie, Renovatie, Regio).",
            "Voeg FAQ‑schema (JSON‑LD) toe — geeft 'rich snippets' in Google.",
            "Behoud een korte 'top 3' op de homepage als teaser onder de werkwijze.",
          ],
        }}
      />

      <Specs title="URL-structuur (voorstel)" note="kebab-case, Nederlands, géén trailing slash" items={[
        { k: "/", v: "Homepage — hero, werkwijze, top 3 diensten, projecten‑teaser" },
        { k: "/diensten", v: "Hub-pagina met alle 6 diensten als grid" },
        { k: "/diensten/nieuwbouw", v: "Volledig traject, prijsrange/m², 4 stappen" },
        { k: "/diensten/renovatie-infrezen", v: "Specifiek voor bestaande vloeren" },
        { k: "/werkwijze", v: "Detail van de 4 fasen met foto's per stap" },
        { k: "/projecten", v: "Overzicht (filter op type/regio) + detail‑pagina's" },
        { k: "/regio", v: "Hub met kaart + lijst van 5 stadspagina's" },
        { k: "/regio/zuidlaren", v: "Stadspagina (zie sectie 05 voor template)" },
        { k: "/prijsindicatie", v: "Calculator + lead‑formulier (zie sectie 04)" },
        { k: "/veelgestelde-vragen", v: "FAQ met categorieën + JSON-LD schema" },
        { k: "/over", v: "Bedrijfsverhaal, eigen team, certificeringen" },
        { k: "/contact", v: "Bel/mail/route + lead‑formulier" },
      ]} />
    </Section>
  );
}

window.SectionIA = SectionIA;
