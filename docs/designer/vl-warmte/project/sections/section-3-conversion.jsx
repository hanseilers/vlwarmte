/* eslint-disable */
/* Section 03 — Conversie & vertrouwen */

function HeroNoTrust() {
  return (
    <div style={{ padding: 22, background: "#0e1825", minHeight: 320, position: "relative" }}>
      <div style={{ fontSize: "0.66rem", letterSpacing: "0.16em", textTransform: "uppercase", color: "#7a8699", marginBottom: 10 }}>
        Vloerverwarming
      </div>
      <div style={{ fontSize: "1.5rem", fontWeight: 800, color: "white", lineHeight: 1.1, marginBottom: 10 }}>
        Van ondervloer tot afgewerkte vloerverwarming
      </div>
      <p style={{ color: "#97a3b6", fontSize: "0.85rem", margin: "0 0 16px", maxWidth: "36ch" }}>
        VLWarmte realiseert het complete traject — ondervloer, schuimbeton, leidingen en dekvloer.
      </p>
      <div style={{ display: "flex", gap: 8 }}>
        <span style={{ background: "linear-gradient(135deg,var(--brand),var(--brand-dark))", color: "white", padding: "8px 14px", borderRadius: 999, fontSize: "0.78rem", fontWeight: 700 }}>
          Vrijblijvende prijsindicatie
        </span>
        <span style={{ border: "1px solid rgba(255,255,255,0.18)", color: "#cfd9e8", padding: "8px 14px", borderRadius: 999, fontSize: "0.78rem", fontWeight: 600 }}>
          Bekijk werkwijze
        </span>
      </div>
      <div style={{ marginTop: 50, padding: 12, border: "1px dashed rgba(180,35,24,0.5)", borderRadius: 8, fontSize: "0.78rem", color: "#ee8c7e" }}>
        Geen reviews · geen logo's · geen aantallen projecten zichtbaar
      </div>
    </div>
  );
}

function HeroWithTrust() {
  return (
    <div className="snap-new" style={{ minHeight: 320 }}>
      <div className="body" style={{ padding: 22 }}>
        <div className="eyebrow">Vloerverwarming</div>
        <h1 style={{ fontSize: "1.5rem" }}>
          Slim gelegd.<br /><em>Gelijkmatig warm.</em>
        </h1>
        <p className="lead" style={{ fontSize: "0.85rem", marginBottom: 14 }}>
          Eén specialist voor het hele traject. Eigen team, geen onderaanneming.
        </p>
        <div className="ctas">
          <span className="btn p">Vrijblijvende prijsindicatie →</span>
          <span className="btn s">Hoe wij werken</span>
        </div>
        <div style={{
          marginTop: 18, padding: "10px 14px", borderRadius: 12,
          border: "1px solid var(--line)", background: "rgba(255,255,255,0.025)",
          display: "flex", alignItems: "center", justifyContent: "space-between", gap: 12,
        }}>
          <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
            <div style={{ display: "flex", color: "var(--brand)", fontSize: "0.85rem", letterSpacing: 1 }}>★★★★★</div>
            <div style={{ fontSize: "0.74rem", color: "var(--ink)" }}>
              <strong style={{ color: "white" }}>4.9</strong>
              <span style={{ color: "var(--ink-muted)" }}> · 38 reviews · Google</span>
            </div>
          </div>
          <div style={{ fontSize: "0.74rem", color: "var(--ink-muted)" }}>
            <strong style={{ color: "white" }}>140+</strong> trajecten
          </div>
        </div>
        <div style={{ marginTop: 10, display: "flex", gap: 8, flexWrap: "wrap" }}>
          {["Bouwgarant", "VCA*", "10 jr garantie", "KvK 00000000"].map((t) => (
            <span key={t} style={{
              fontSize: "0.7rem", color: "var(--ink-dim)",
              padding: "3px 9px", borderRadius: 999,
              border: "1px dashed var(--line-strong)",
            }}>{t}</span>
          ))}
        </div>
      </div>
    </div>
  );
}

function FormCurrent() {
  return (
    <div style={{ padding: 22, background: "#0e1825", minHeight: 320 }}>
      <div style={{ display: "inline-flex", padding: 3, gap: 4, border: "1px solid rgba(255,255,255,0.18)", borderRadius: 999, marginBottom: 16 }}>
        <span style={{ padding: "6px 12px", borderRadius: 999, background: "linear-gradient(135deg,var(--brand),var(--brand-dark))", color: "white", fontSize: "0.74rem", fontWeight: 700 }}>Informatie</span>
        <span style={{ padding: "6px 12px", borderRadius: 999, color: "#9aabbe", fontSize: "0.74rem", fontWeight: 600 }}>Offerte</span>
        <span style={{ padding: "6px 12px", borderRadius: 999, color: "#9aabbe", fontSize: "0.74rem", fontWeight: 600 }}>Bel mij</span>
      </div>
      {[["Naam", "Voor- en achternaam"], ["E-mail", "naam@voorbeeld.nl"], ["Telefoon", "06 …"]].map(([l, p]) => (
        <div key={l} style={{ marginBottom: 10 }}>
          <div style={{ fontSize: "0.74rem", color: "white", fontWeight: 600, marginBottom: 4 }}>{l}</div>
          <div style={{ height: 32, background: "#0c1523", border: "1px solid rgba(255,255,255,0.18)", borderRadius: 8, padding: "8px 10px", color: "#5c6878", fontSize: "0.74rem" }}>{p}</div>
        </div>
      ))}
      <div style={{ height: 60, background: "#0c1523", border: "1px solid rgba(255,255,255,0.18)", borderRadius: 8, marginBottom: 12 }} />
      <span style={{ background: "linear-gradient(135deg,var(--brand),var(--brand-dark))", color: "white", padding: "9px 16px", borderRadius: 999, fontSize: "0.78rem", fontWeight: 700 }}>
        Verzenden
      </span>
    </div>
  );
}

function FormProposed() {
  return (
    <div style={{ padding: 22, background: "linear-gradient(180deg, #0f1724 0%, #0a1220 100%)", minHeight: 320, position: "relative" }}>
      <div style={{ fontSize: "0.74rem", color: "var(--ink-muted)", marginBottom: 8 }}>Stap 1 van 3 · 30 sec</div>
      <div style={{ height: 4, background: "rgba(255,255,255,0.06)", borderRadius: 999, marginBottom: 16, overflow: "hidden" }}>
        <div style={{ width: "33%", height: "100%", background: "linear-gradient(90deg, var(--brand), var(--vl-orange-300))" }} />
      </div>
      <div style={{ fontSize: "1.05rem", fontWeight: 700, color: "white", marginBottom: 16 }}>
        Wat speelt er bij jou?
      </div>
      {[
        ["Nieuwbouw", "Volledig traject", true],
        ["Renovatie", "Infrezen of nieuwe ondervloer", false],
        ["Alleen advies", "Ik weet het nog niet zeker", false],
      ].map(([t, s, on]) => (
        <div key={t} style={{
          padding: "12px 14px", marginBottom: 8,
          border: `1px solid ${on ? "rgba(224,85,47,0.5)" : "var(--line-strong)"}`,
          background: on ? "rgba(224,85,47,0.08)" : "rgba(255,255,255,0.02)",
          borderRadius: 12,
          display: "flex", justifyContent: "space-between", alignItems: "center",
        }}>
          <div>
            <div style={{ fontSize: "0.86rem", fontWeight: 700, color: "white" }}>{t}</div>
            <div style={{ fontSize: "0.74rem", color: "var(--ink-muted)" }}>{s}</div>
          </div>
          <div style={{
            width: 18, height: 18, borderRadius: 999,
            border: `2px solid ${on ? "var(--brand)" : "var(--line-strong)"}`,
            background: on ? "var(--brand)" : "transparent",
          }} />
        </div>
      ))}
      <div style={{ marginTop: 14, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <span style={{ fontSize: "0.74rem", color: "var(--ink-muted)" }}>← Terug</span>
        <span style={{ background: "linear-gradient(135deg,var(--brand),var(--brand-dark))", color: "white", padding: "9px 16px", borderRadius: 999, fontSize: "0.78rem", fontWeight: 700 }}>
          Volgende →
        </span>
      </div>
    </div>
  );
}

function SectionConversion() {
  return (
    <Section id="conversion">
      <SectionHead
        num="03"
        kicker="Conversie & vertrouwen"
        title="Vertrouwen tonen waar de keuze valt"
        lead="Een vakman‑specialist heeft maar weinig sociale bewijslast nodig — maar wel op het juiste moment. Op de hero, op de prijspagina, en in het lead‑formulier zelf."
      />

      <Finding
        problem={{
          title: "Hero mist vertrouwens-anchors",
          body: "Bezoeker landt, leest claim, en moet kiezen tussen 'prijsindicatie' en 'werkwijze' zonder enige aanwijzing dat dit een serieuze partij is. Geen reviews, geen aantallen, geen certificeringen.",
        }}
        fix={{
          title: "Trust-strip direct onder de CTA's",
          body: [
            "Google-rating + aantal reviews + aantal trajecten — als één compacte horizontale balk.",
            "Onder die balk: vier keurmerk-pills (Bouwgarant, VCA*, 10 jr garantie, KvK).",
            "Verleng de garantie‑claim niet — '10 jaar garantie' is sterk juist omdat hij nuchter is.",
          ],
        }}
      />

      <div className="mock-row">
        <MockFrame tag="current" url="vlwarmte.nl"><HeroNoTrust /></MockFrame>
        <MockFrame tag="proposed" url="vlwarmte.nl">
          <HeroWithTrust />
          <Pin n="1" x={50} y={62} lx={62} ly={50} lw={210}
            label="Trust-strip: ster-rating + aantal trajecten in één regel. Compact, niet pochend." />
          <Pin n="2" x={50} y={86} lx={2} ly={82} lw={170}
            label="Keurmerken als gestreepte pills — leesbaar maar visueel ondergeschikt aan de hero." />
        </MockFrame>
      </div>

      <Finding
        problem={{
          title: "Lead‑formulier is een muur van velden",
          body: "Drie modes (info/offerte/bel mij), 4 verplichte velden, één textarea — alles tegelijk zichtbaar. De bezoeker met '5 minuten' tijd haakt af.",
        }}
        fix={{
          title: "Conversational form: 3 stappen, één vraag per scherm",
          body: [
            "Stap 1 (15 sec): wat speelt er — nieuwbouw / renovatie / advies. Visuele kaarten, geen radio.",
            "Stap 2 (15 sec): contactgegevens. Slechts naam + 1 contactmethode (telefoon óf e‑mail).",
            "Stap 3 (15 sec): toelichting (optioneel) en consent.",
            "Boven elke stap: voortgangsbalk + 'X van 3 · 30 sec' — verlaagt de drempel.",
          ],
        }}
      />

      <div className="mock-row">
        <MockFrame tag="current" url="vlwarmte.nl/prijsindicatie"><FormCurrent /></MockFrame>
        <MockFrame tag="proposed" url="vlwarmte.nl/prijsindicatie">
          <FormProposed />
          <Pin n="1" x={48} y={11} lx={56} ly={2} lw={200}
            label="Voortgang + tijdschatting — verlaagt drempel ('30 sec, niet 5 min')." />
          <Pin n="2" x={50} y={53} lx={64} ly={42} lw={180}
            label="Visuele keuze-kaarten in plaats van radiobuttons. Eén klik = één antwoord." />
        </MockFrame>
      </div>

      <Note>
        <strong>CTA-copy:</strong> vervang 'Verzenden' door iets concreters als <em>'Stuur mijn aanvraag'</em> of <em>'Bel mij doordeweeks ochtend'</em> (afhankelijk van mode). Generieke CTA's converteren slechter dan beschrijvende.
      </Note>

      <Specs title="Conversie-componenten" items={[
        { k: "<TrustStrip>", v: "Hero-onder. Sterren + aantal + jaren ervaring + 'eigen team' tag." },
        { k: "<KeurmerkPills>", v: "4 dashed pills, --line-strong border. Onder TrustStrip." },
        { k: "<MultiStepLead>", v: "3 steps, useState({step, mode, naam, contact, toelichting})" },
        { k: "Sticky mobile CTA", v: "Onderaan viewport, gradient brand, opent multi-step modal" },
        { k: "Form a11y", v: "aria-current='step', fieldset per stap, autofocus eerste invoer" },
        { k: "Consent", v: "Korte regel + link naar privacyverklaring; geen verplicht checkboxje" },
      ]} />
    </Section>
  );
}

window.SectionConversion = SectionConversion;
