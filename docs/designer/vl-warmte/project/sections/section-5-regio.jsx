/* eslint-disable */
/* Section 05 — Regionale SEO / stadspagina-template */

function RegioCurrent() {
  return (
    <div style={{ padding: 22, background: "#0e1825", minHeight: 320 }}>
      <div style={{ fontSize: "0.78rem", color: "#7a8699", marginBottom: 8 }}>vlwarmte.nl (homepage)</div>
      <div style={{ fontSize: "0.9rem", color: "#cdd6e3", lineHeight: 1.55, marginBottom: 12 }}>
        "Werkzaam in <strong style={{ color: "white" }}>Groningen, Friesland en Drenthe</strong>" —
        deze regel staat 4× op de homepage. Verder geen lokale paginas, geen kaart, geen lokale projecten gefilterd, geen NAP‑gegevens schema.
      </div>
      <div style={{ padding: 12, border: "1px dashed rgba(180,35,24,0.5)", borderRadius: 8, fontSize: "0.78rem", color: "#ee8c7e" }}>
        Geen URL voor 'vloerverwarming Drachten', 'vloerverwarming Assen' etc. Lokale zoekers vinden alleen de homepage — als ze hem al vinden.
      </div>
    </div>
  );
}

function StadspaginaProposed() {
  return (
    <div style={{
      minHeight: 320,
      background: "linear-gradient(180deg, #0f1724 0%, #0a1220 100%)",
      position: "relative", overflow: "hidden",
    }}>
      <div style={{
        padding: "16px 22px",
        borderBottom: "1px solid var(--line)",
        fontSize: "0.74rem", color: "var(--ink-muted)",
        fontFamily: "var(--font-mono)",
      }}>
        vlwarmte.nl / regio / <span style={{ color: "var(--brand)" }}>zuidlaren</span>
      </div>
      <div style={{ padding: "20px 22px" }}>
        <div style={{ fontSize: "0.66rem", letterSpacing: "0.16em", textTransform: "uppercase", color: "var(--ink-muted)", marginBottom: 8 }}>
          Regio · Drenthe
        </div>
        <div style={{ fontSize: "1.4rem", fontWeight: 800, color: "white", letterSpacing: "-0.025em", lineHeight: 1.1, marginBottom: 10 }}>
          Vloerverwarming in <span style={{ background: "linear-gradient(120deg, var(--brand), var(--vl-orange-300))", WebkitBackgroundClip: "text", backgroundClip: "text", WebkitTextFillColor: "transparent" }}>Zuidlaren</span>
        </div>
        <p style={{ color: "var(--ink-dim)", fontSize: "0.85rem", lineHeight: 1.55, margin: "0 0 14px", maxWidth: "44ch" }}>
          Onze thuisbasis. Korte aanrijtijden, ervaring met de typische bouwvormen in het gebied (boerderijwoningen, vrijstaand op zandgrond), en regelmatig terugkerend onderhoud.
        </p>
        <div style={{ display: "flex", gap: 10, marginBottom: 14 }}>
          <span style={{ background: "linear-gradient(135deg, var(--brand), var(--brand-dark))", color: "white", padding: "8px 14px", borderRadius: 999, fontSize: "0.78rem", fontWeight: 700 }}>
            Prijsindicatie voor Zuidlaren →
          </span>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 8, marginBottom: 12 }}>
          {[["28", "trajecten"], ["10 km", "rijafstand"], ["1–3 dgn", "intake"]].map(([n, l]) => (
            <div key={l} style={{
              padding: "8px 10px", border: "1px solid var(--line)", borderRadius: 8,
              background: "rgba(255,255,255,0.02)",
            }}>
              <div style={{ fontSize: "0.96rem", fontWeight: 800, color: "white", letterSpacing: "-0.02em", fontVariantNumeric: "tabular-nums" }}>{n}</div>
              <div style={{ fontSize: "0.7rem", color: "var(--ink-muted)" }}>{l}</div>
            </div>
          ))}
        </div>
        <div style={{ fontSize: "0.74rem", color: "var(--ink-muted)" }}>
          Ook in de buurt: <span style={{ color: "var(--ink)" }}>Vries</span> · <span style={{ color: "var(--ink)" }}>Eelde</span> · <span style={{ color: "var(--ink)" }}>Tynaarlo</span> · <span style={{ color: "var(--ink)" }}>Annen</span>
        </div>
      </div>
    </div>
  );
}

function SectionRegio() {
  return (
    <Section id="regio">
      <SectionHead
        num="05"
        kicker="Regionale SEO"
        title="Vijf stadspagina's, één template, structureel zoekverkeer"
        lead="Lokale zoekopdrachten zijn een van de hoogste-intentie verkeersbronnen voor een vakman. De huidige site geeft Google geen aanleiding om VLWarmte te koppelen aan 'vloerverwarming + stad'. Een lichte set stadspagina's lost dat op — mits ze géén copy‑paste boilerplate worden."
      />

      <Finding
        problem={{
          title: "Regio is alleen tekst, geen structuur",
          body: "De drie provincies en vijf steden bestaan in de prose, maar niet als URL, schema, of pagina. Google heeft geen anker.",
        }}
        fix={{
          title: "Eén /regio hub + 5 stadspagina's met dezelfde template",
          body: [
            "Top: Zuidlaren, Groningen, Assen, Leeuwarden, Drachten — gekozen op zoekvolume × eigen historisch werkgebied.",
            "Eén hub op /regio met kaart en lijst; 5 detailpagina's met identieke structuur maar lokale invulling (aantallen, projecten, omliggende dorpen).",
            "Per stad: minimaal 250 woorden uniek — niet meer boilerplate dan 30%.",
          ],
        }}
      />

      <div className="mock-row">
        <MockFrame tag="current" url="vlwarmte.nl"><RegioCurrent /></MockFrame>
        <MockFrame tag="proposed" url="vlwarmte.nl/regio/zuidlaren">
          <StadspaginaProposed />
          <Pin n="1" x={50} y={20} lx={3} ly={2} lw={210}
            label="Eigen URL per stad — primaire SEO-winst. Kebab-case, alleen plaatsnaam." />
          <Pin n="2" x={26} y={42} lx={56} ly={32} lw={200}
            label="Plaatsnaam in H1, gradient op het stadnaamwoord — herkenbaar en gepersonaliseerd." />
          <Pin n="3" x={50} y={75} lx={56} ly={64} lw={210}
            label="3 lokale stats — concreet bewijs dat dit géén landingspagina-leeg-blok is." />
          <Pin n="4" x={50} y={92} lx={3} ly={84} lw={210}
            label="Omliggende dorpen — vangt long-tail ('vloerverwarming Vries') zonder N+1 paginas." />
        </MockFrame>
      </div>

      <Specs title="Stadspagina-template" note="elk veld vullen vanuit data.js" items={[
        { k: "<title>", v: "Vloerverwarming {stad} — VLWarmte" },
        { k: "<meta description>", v: "Specialist in vloerverwarming in {stad}. {n_trajecten} trajecten, eigen team, doorgaans binnen 1 werkdag een prijsindicatie. Lees meer." },
        { k: "h1", v: "Vloerverwarming in {stad}" },
        { k: "Lead (uniek per stad)", v: "1 alinea over typische woningvormen, lokale ervaring, aanrijtijd" },
        { k: "Stats-grid", v: "{n} trajecten · {km} rijafstand · {intake_tijd}" },
        { k: "Projects-filter", v: "Auto-filter Projecten op deze stad — toon 3 thumbnails als ze er zijn" },
        { k: "Omliggende plaatsen", v: "Array van 4–6 plaatsnamen — geen aparte URL, alleen tekstvermelding" },
        { k: "JSON-LD", v: "LocalBusiness schema met areaServed = stad + omliggende plaatsen" },
        { k: "FAQ-stadsspecifiek", v: "1–2 vragen die specifiek lokaal zijn (kruipruimtes in oude stadsdelen, etc.)" },
        { k: "CTA", v: "'Prijsindicatie voor {stad} →' — pre-fills regio-veld op formulier" },
      ]} />

      <Finding
        problem={{
          title: "Geen LocalBusiness‑schema",
          body: "Zonder JSON‑LD weet Google niet dat dit een lokaal bedrijf is met service‑gebied en NAP‑gegevens. Geen 'Local pack' kans.",
        }}
        fix={{
          title: "JSON‑LD op homepage + per stadspagina",
          body: [
            "Homepage: één LocalBusiness met areaServed = ['Groningen', 'Friesland', 'Drenthe'].",
            "Stadspagina: extra Service-schema met provider = LocalBusiness en areaServed = die stad.",
            "Vergeet de NAP-consistentie niet (Google Business Profile, KvK, footer — exact dezelfde notatie).",
          ],
        }}
      />
    </Section>
  );
}

window.SectionRegio = SectionRegio;
