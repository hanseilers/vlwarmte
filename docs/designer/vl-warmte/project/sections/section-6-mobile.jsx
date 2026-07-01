/* eslint-disable */
/* Section 06 — Mobile-first */

function MobileCurrent() {
  return (
    <div style={{
      width: 220, margin: "20px auto",
      border: "1px solid var(--line-strong)",
      borderRadius: 22, overflow: "hidden",
      background: "#0e1825",
      boxShadow: "0 16px 40px rgba(0,0,0,0.45)",
    }}>
      <div style={{ padding: "10px 14px", borderBottom: "1px solid rgba(255,255,255,0.08)", display: "flex", justifyContent: "space-between", alignItems: "center", fontSize: "0.78rem", color: "white", fontWeight: 800 }}>
        <span><span style={{ color: "var(--brand)" }}>VL</span>Warmte</span>
        <span style={{ color: "#cdd6e3", fontSize: "1.1rem" }}>☰</span>
      </div>
      <div style={{ padding: 14 }}>
        <div style={{ fontSize: "0.96rem", fontWeight: 800, color: "white", lineHeight: 1.15, marginBottom: 8 }}>
          Van ondervloer tot afgewerkte vloerverwarming
        </div>
        <p style={{ fontSize: "0.7rem", color: "#97a3b6", margin: "0 0 12px" }}>
          VLWarmte realiseert het complete traject — ondervloer, schuimbeton, leidingen en dekvloer.
        </p>
        <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
          <span style={{ background: "linear-gradient(135deg,var(--brand),var(--brand-dark))", color: "white", padding: "8px 12px", borderRadius: 999, fontSize: "0.74rem", fontWeight: 700, textAlign: "center" }}>
            Vrijblijvende prijsindicatie
          </span>
          <span style={{ border: "1px solid rgba(255,255,255,0.18)", color: "#cfd9e8", padding: "8px 12px", borderRadius: 999, fontSize: "0.74rem", fontWeight: 600, textAlign: "center" }}>
            Bekijk werkwijze
          </span>
        </div>
        <div style={{ marginTop: 14, fontSize: "0.66rem", color: "#7a8699", textAlign: "center" }}>
          ↓ scroll: 4 reassurance items, 4 stappen, 6 diensten…
        </div>
      </div>
    </div>
  );
}

function MobileProposed() {
  return (
    <div style={{
      width: 220, margin: "20px auto", position: "relative",
      border: "1px solid var(--line-strong)",
      borderRadius: 22, overflow: "hidden",
      background: "linear-gradient(180deg, #0f1724 0%, #0a1220 100%)",
      boxShadow: "0 16px 40px rgba(0,0,0,0.45)",
    }}>
      <div style={{
        padding: "10px 14px",
        borderBottom: "1px solid rgba(255,255,255,0.08)",
        display: "flex", justifyContent: "space-between", alignItems: "center",
        fontSize: "0.78rem", color: "white", fontWeight: 800,
        background: "rgba(9,15,24,0.86)",
      }}>
        <span><span style={{ color: "var(--brand)" }}>VL</span>Warmte</span>
        <span style={{ display: "inline-flex", flexDirection: "column", gap: 3 }}>
          <span style={{ width: 16, height: 2, background: "var(--ink)" }} />
          <span style={{ width: 16, height: 2, background: "var(--ink)" }} />
        </span>
      </div>
      <div style={{ padding: 14, paddingBottom: 60 }}>
        <div style={{ fontSize: "0.6rem", letterSpacing: "0.16em", textTransform: "uppercase", color: "var(--ink-muted)", marginBottom: 8 }}>
          Vloerverwarming
        </div>
        <div style={{ fontSize: "1.1rem", fontWeight: 800, color: "white", letterSpacing: "-0.025em", lineHeight: 1.05, marginBottom: 8 }}>
          Slim gelegd.<br /><span style={{ background: "linear-gradient(120deg, var(--brand), var(--vl-orange-300))", WebkitBackgroundClip: "text", backgroundClip: "text", WebkitTextFillColor: "transparent" }}>Gelijkmatig warm.</span>
        </div>
        <p style={{ fontSize: "0.7rem", color: "var(--ink-dim)", margin: "0 0 12px", lineHeight: 1.5 }}>
          Eén specialist voor het hele traject — eigen team, geen onderaanneming.
        </p>
        <div style={{ display: "flex", alignItems: "center", gap: 6, fontSize: "0.66rem", color: "var(--ink)", marginBottom: 10 }}>
          <span style={{ color: "var(--brand)" }}>★★★★★</span>
          <strong style={{ color: "white" }}>4.9</strong>
          <span style={{ color: "var(--ink-muted)" }}>· 38 reviews</span>
        </div>
        <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
          <span style={{ border: "1px solid var(--line-cool)", color: "white", padding: "8px 12px", borderRadius: 999, fontSize: "0.72rem", fontWeight: 600, textAlign: "center", background: "rgba(255,255,255,0.04)" }}>
            Hoe wij werken
          </span>
        </div>
      </div>
      {/* Sticky CTA */}
      <div style={{
        position: "absolute", bottom: 0, left: 0, right: 0,
        padding: 10,
        background: "linear-gradient(180deg, rgba(11,18,28,0) 0%, rgba(11,18,28,0.95) 60%)",
      }}>
        <div style={{
          background: "linear-gradient(135deg, var(--brand), var(--brand-dark))",
          color: "white",
          padding: "10px 12px",
          borderRadius: 999,
          textAlign: "center",
          fontSize: "0.78rem",
          fontWeight: 700,
          boxShadow: "0 8px 20px rgba(188,63,31,0.4)",
        }}>
          Prijsindicatie · 30 sec →
        </div>
      </div>
    </div>
  );
}

function SectionMobile() {
  return (
    <Section id="mobile" alt>
      <SectionHead
        num="06"
        kicker="Mobile-first"
        title="De helft van het verkeer staat bij een bouwplaats"
        lead="Vloerverwarming‑zoekers staan vaak letterlijk op locatie als ze de site openen — bouwval, kruipruimte, verbouwing. Ze hebben één hand vrij. De huidige site is responsive, maar niet specifiek voor mobiel ontworpen."
      />

      <Finding
        problem={{
          title: "Hoofd-CTA verdwijnt zodra je scrollt",
          body: "De primaire knop staat alleen in de hero. Op mobiel betekent dat: scroll → CTA weg → gebruiker moet helemaal terug naar boven of helemaal naar onderen.",
        }}
        fix={{
          title: "Sticky bottom-CTA met tijdsindicatie",
          body: [
            "Vaste balk onder in beeld: 'Prijsindicatie · 30 sec →' — gradient-vulling, één regel.",
            "Verdwijnt alleen wanneer het lead-formulier zelf in beeld is (IntersectionObserver).",
            "Tap-target ≥ 48px hoog, padding 10px ruim, brede touch-zone.",
          ],
        }}
      />

      <div className="mock-row">
        <MockFrame tag="current" url="vlwarmte.nl (mobiel)" h="380px"><MobileCurrent /></MockFrame>
        <MockFrame tag="proposed" url="vlwarmte.nl (mobiel)" h="380px">
          <MobileProposed />
          <Pin n="1" x={50} y={28} lx={70} ly={6} lw={170}
            label="Eyebrow + tweelijns hero — past op kleine viewports zonder af te kappen." />
          <Pin n="2" x={50} y={56} lx={4} ly={42} lw={180}
            label="Trust-strip blijft compact: 1 regel met sterren + score." />
          <Pin n="3" x={50} y={92} lx={70} ly={84} lw={170}
            label="Sticky CTA met tijdsindicatie — verdwijnt alleen bij het formulier zelf." />
        </MockFrame>
      </div>

      <Finding
        problem={{
          title: "Diensten‑grid wordt op mobiel een eindeloze lijst",
          body: "6 kaarten worden op mobiel 6 verticale blokken — geen samenvatting, geen scan-modus. De gebruiker scrollt door zonder te weten wat hij eigenlijk leest.",
        }}
        fix={{
          title: "Op mobiel: horizontale snap-scroll voor diensten",
          body: [
            "Scroll-snap container met 6 kaarten naast elkaar (90% viewport-breedte per kaart).",
            "Kleine dot-paginatie eronder — geeft visueel feedback over hoeveel diensten er zijn.",
            "Op desktop: gewoon het 3-koloms grid uit het UI kit.",
          ],
        }}
      />

      <Specs title="Mobile-first specs" items={[
        { k: "Tap target min", v: "48×48px (Apple/Google guideline). CTA pill 44px hoogte minimum." },
        { k: "Sticky CTA hoogte", v: "60px incl. padding. z-index 50, onder de header (z-30)." },
        { k: "Sticky CTA hide", v: "IntersectionObserver op #lead-form section. Wanneer in view → CTA fade-out." },
        { k: "Scroll-snap diensten", v: "scroll-snap-type: x mandatory, 90vw per card, padding-inline 5vw" },
        { k: "Mobile breakpoint", v: "< 720px voor sticky CTA, < 920px voor het kolommenraster" },
        { k: "Hamburger drawer", v: "Volledig scherm, niet uitschuif. Backdrop-filter blur op de inhoud erachter." },
        { k: "Form keyboard", v: "type='tel' / type='email' — opent juist toetsenbord. Inputmode op getallen." },
        { k: "Reduced motion", v: "@media (prefers-reduced-motion) — alle animaties van de glow uit (al gedekt door token)." },
      ]} />

      <Note>
        <strong>Performance:</strong> de breathing‑glow gebruikt vier radial gradients met een keyframe.
        Op laagvermogen mobielen levert dat zichtbare jank op. Optie: vervang het door één SVG‑filter <code style={{ fontFamily: "var(--font-mono)", color: "var(--accent-glow)" }}>feGaussianBlur</code> + opacity‑animation, of zet hem uit onder 720px (geen visueel verlies, het effect is al subtiel op kleine schermen).
      </Note>
    </Section>
  );
}

window.SectionMobile = SectionMobile;
