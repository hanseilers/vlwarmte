/* eslint-disable */
/* Section 04 — Prijsindicatie transparency */

function PrijsCurrent() {
  return (
    <div style={{ padding: 22, background: "#0e1825", minHeight: 320 }}>
      <div style={{ fontSize: "1.2rem", fontWeight: 800, color: "white", marginBottom: 8 }}>
        Vraag een vrijblijvende prijsindicatie aan
      </div>
      <p style={{ color: "#97a3b6", fontSize: "0.85rem", margin: "0 0 16px" }}>
        Kies wat je wilt: informatie, een offerte, of dat we je terugbellen.
      </p>
      <div style={{ padding: 14, border: "1px dashed rgba(180,35,24,0.5)", borderRadius: 8, color: "#ee8c7e", fontSize: "0.82rem", marginBottom: 10 }}>
        Geen prijsrange genoemd. Geen indicatie van wat een traject ongeveer kost. Bezoeker moet eerst een formulier invullen om een richtprijs te zien.
      </div>
      <div style={{ display: "flex", gap: 8, marginTop: 12 }}>
        <span style={{ fontSize: "0.78rem", color: "#7a8699" }}>FAQ: "Wat kost vloerverwarming gemiddeld?" → "Vraag een prijsindicatie aan."</span>
      </div>
    </div>
  );
}

function PrijsProposed() {
  const [type, setType] = React.useState("nieuwbouw");
  const [m2, setM2] = React.useState(120);
  // simple range estimator
  const ranges = {
    nieuwbouw: [38, 58],
    renovatie: [48, 72],
  };
  const [lo, hi] = ranges[type];
  const totalLo = (lo * m2).toLocaleString("nl-NL");
  const totalHi = (hi * m2).toLocaleString("nl-NL");
  return (
    <div style={{
      padding: 20, minHeight: 320,
      background: "linear-gradient(180deg, #0f1724 0%, #0a1220 100%)", position: "relative",
    }}>
      <div style={{ fontSize: "0.66rem", letterSpacing: "0.16em", textTransform: "uppercase", color: "var(--ink-muted)", marginBottom: 10 }}>
        Indicatie · vrijblijvend
      </div>
      <div style={{ fontSize: "1.1rem", fontWeight: 800, color: "white", letterSpacing: "-0.02em", marginBottom: 14 }}>
        Wat kost mijn vloerverwarming ongeveer?
      </div>
      <div style={{ display: "flex", gap: 6, marginBottom: 12 }}>
        {[["nieuwbouw", "Nieuwbouw"], ["renovatie", "Renovatie"]].map(([k, l]) => (
          <button key={k} onClick={() => setType(k)} style={{
            border: 0, padding: "7px 14px", borderRadius: 999,
            background: type === k ? "linear-gradient(135deg, var(--brand), var(--brand-dark))" : "rgba(255,255,255,0.04)",
            color: type === k ? "white" : "var(--ink-dim)",
            fontWeight: 700, fontSize: "0.78rem", cursor: "pointer",
            border: type === k ? "0" : "1px solid var(--line-strong)",
          }}>
            {l}
          </button>
        ))}
      </div>
      <div style={{ marginBottom: 10 }}>
        <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
          <span style={{ fontSize: "0.78rem", color: "var(--ink-muted)" }}>Oppervlakte</span>
          <span style={{ fontSize: "0.84rem", color: "white", fontWeight: 700, fontFamily: "var(--font-mono)" }}>{m2} m²</span>
        </div>
        <input type="range" min="40" max="300" value={m2} onChange={(e) => setM2(+e.target.value)}
          style={{ width: "100%", accentColor: "var(--brand)" }} />
      </div>
      <div style={{
        marginTop: 10, padding: 14,
        border: "1px solid var(--line-warm)",
        borderRadius: 12,
        background: "rgba(224,85,47,0.06)",
      }}>
        <div style={{ fontSize: "0.7rem", color: "var(--ink-muted)", letterSpacing: "0.12em", textTransform: "uppercase", marginBottom: 4 }}>
          Richtprijs · totaal
        </div>
        <div style={{ fontSize: "1.45rem", fontWeight: 800, color: "white", letterSpacing: "-0.02em", fontFamily: "var(--font-sans)" }}>
          € {totalLo} – € {totalHi}
        </div>
        <div style={{ fontSize: "0.74rem", color: "var(--ink-muted)", marginTop: 4 }}>
          € {lo}–{hi} per m² incl. materiaal · excl. btw · gemiddelde nieuwbouwsituatie
        </div>
      </div>
      <div style={{ marginTop: 12, fontSize: "0.74rem", color: "var(--ink-muted)" }}>
        Wil je een nauwkeurige offerte? <span style={{ color: "var(--brand)", fontWeight: 700, borderBottom: "1px solid var(--brand)" }}>Vraag aan →</span>
      </div>
    </div>
  );
}

function SectionPrijs() {
  return (
    <Section id="prijs" alt>
      <SectionHead
        num="04"
        kicker="Prijsindicatie"
        title="Geef de prijs voor het formulier — niet erna"
        lead="De huidige FAQ verstopt 'wat kost vloerverwarming gemiddeld?' achter een formulier. Voor een specialist met heldere prijsstructuur is dat een gemiste kans. Een eenvoudige range‑calculator bouwt vertrouwen, scheidt serieuze leads, en staat de offerte‑aanvraag niet in de weg."
      />

      <Finding
        problem={{
          title: "FAQ ontwijkt de belangrijkste vraag",
          body: [
            "'Wat kost vloerverwarming gemiddeld?' wordt beantwoord met 'vraag een vrijblijvende prijsindicatie aan'. Voor de bezoeker is dat een non-antwoord.",
            "Concurrenten geven wél direct een richtprijs per m² of een online configurator. Vlwarmte oogt daardoor onbedoeld minder transparant.",
          ],
        }}
        fix={{
          title: "Live calculator met range, vóór het formulier",
          body: [
            "Twee toggles (nieuwbouw/renovatie), één slider voor m². Direct zichtbaar: range per m² en totaal.",
            "Range, geen prijspunt — beschermt je tegen 'lokvogel'-perceptie en weerspiegelt de realiteit.",
            "Onder het resultaat: subtiele CTA naar het formulier voor een nauwkeurige offerte.",
          ],
        }}
      />

      <div className="mock-row">
        <MockFrame tag="current" url="vlwarmte.nl/prijsindicatie"><PrijsCurrent /></MockFrame>
        <MockFrame tag="proposed" url="vlwarmte.nl/prijsindicatie">
          <PrijsProposed />
          <Pin n="1" x={26} y={28} lx={50} ly={2} lw={200}
            label="Twee toggles voor de twee fundamenteel verschillende trajecten." />
          <Pin n="2" x={50} y={50} lx={54} ly={36} lw={200}
            label="Slider — geeft realtime feedback. Tabular-nums voor het getal voorkomt sprongen." />
          <Pin n="3" x={50} y={75} lx={2} ly={64} lw={210}
            label="Range, niet één bedrag. Subtekst legt uit: 'incl. materiaal, excl. btw'." />
        </MockFrame>
      </div>

      <Finding
        problem={{
          title: "Geen referentievoorbeelden bij het bedrag",
          body: "Een range zonder context laat de bezoeker raden waar ze in de range vallen. Zijn ze 'goedkoop' geval (nieuwbouw, vlak) of 'duur' (renovatie, gestapeld)?",
        }}
        fix={{
          title: "Drie referentie-trajecten naast de calculator",
          body: [
            "'Tussenwoning · 95 m² · €4.500–€5.800' — '2-onder-1-kap · 140 m² · €6.500–€8.500' — 'Vrijstaand · 200 m² · €9.500–€12.500'.",
            "Klikbaar: stelt de calculator in op die situatie.",
            "Gebruik echte projecten (geanonimiseerd) — versterkt geloofwaardigheid.",
          ],
        }}
      />

      <Specs title="Calculator specs" items={[
        { k: "Range nieuwbouw", v: "€38–58 / m² (incl. materiaal, excl. btw, excl. afwerkvloer)" },
        { k: "Range renovatie", v: "€48–72 / m² (infrezen of nieuwe ondervloer)" },
        { k: "Range opslag/regio", v: "Optioneel +5% Friesland-noord (rij-afstand) — alleen als prijsbeleid" },
        { k: "Slider min/max", v: "40 m² — 300 m². Step 5. Default 120 (gemiddelde)." },
        { k: "Number formatting", v: "Intl.NumberFormat('nl-NL') — punt als duizendtal-scheider" },
        { k: "Tabular-nums", v: "Op het bedrag: font-variant-numeric: tabular-nums (geen sprongen)" },
        { k: "Disclaimer", v: "Korte regel: 'incl. materiaal · excl. btw · indicatief' — niet meer" },
        { k: "CTA na resultaat", v: "Tekst-link, geen tweede primaire knop. Sticky CTA bovenaan blijft de hoofdactie." },
      ]} />

      <Note>
        <strong>Kanttekening:</strong> bespreek de ranges intern met VLWarmte vóór livegang. Als het prijsbeleid afwijkt van bovenstaande, pas de constanten aan in <code style={{ fontFamily: "var(--font-mono)", color: "var(--accent-glow)" }}>data.js</code> — niet inline in de component.
      </Note>
    </Section>
  );
}

window.SectionPrijs = SectionPrijs;
