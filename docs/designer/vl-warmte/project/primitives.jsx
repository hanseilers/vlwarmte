/* eslint-disable */
/* Shared primitives for the VLWarmte design recommendations doc.
   All shared components are exported to window so each Babel script
   shares the same scope. */

const { useState, useEffect, useRef } = React;

/* ---------- Pin / annotation ---------- */

function Pin({ n, x, y, label, lx, ly, lw }) {
  // Pin is positioned by x/y (% of the mock body).
  // Label is positioned by lx/ly. A dashed line connects them.
  // lw = max-width override on the label box.
  const labelStyle = { left: `${lx}%`, top: `${ly}%` };
  if (lw) labelStyle.maxWidth = lw;
  return (
    <div className="pin">
      <span className="pin-dot" style={{ left: `calc(${x}% - 11px)`, top: `calc(${y}% - 11px)` }}>{n}</span>
      <span className="pin-label" style={labelStyle}>{label}</span>
    </div>
  );
}

/* ---------- Browser-frame mock ---------- */

function MockFrame({ tag, url, children, h }) {
  const tagClass = tag === "current" ? "tag current" : tag === "proposed" ? "tag proposed" : "tag";
  const tagText = tag === "current" ? "Huidig" : tag === "proposed" ? "Voorstel" : tag;
  return (
    <div className="mock-frame">
      <div className="mock-bar">
        <span className="traffic"><span /><span /><span /></span>
        <span className="url">{url || "vlwarmte.nl"}</span>
        <span className={tagClass}>{tagText}</span>
      </div>
      <div className="mock-body" style={h ? { minHeight: h } : null}>
        {children}
      </div>
    </div>
  );
}

/* ---------- Section header ---------- */

function SectionHead({ num, kicker, title, lead }) {
  return (
    <div className="section-head">
      <div className="section-num">
        <span className="big">{num}</span>
        <span className="label-tag">{kicker}</span>
      </div>
      <div>
        <h2 className="section-title">{title}</h2>
        <p className="section-lead">{lead}</p>
      </div>
    </div>
  );
}

/* ---------- Finding row (problem -> recommendation) ---------- */

function Finding({ problem, fix, problemTitle = "Bevinding", fixTitle = "Aanbeveling" }) {
  return (
    <div className="finding">
      <div className="finding-pane problem">
        <div className="label">{problemTitle}</div>
        <h3>{problem.title}</h3>
        {Array.isArray(problem.body)
          ? problem.body.map((p, i) => <p key={i}>{p}</p>)
          : <p>{problem.body}</p>}
      </div>
      <div className="finding-pane fix">
        <div className="label">{fixTitle}</div>
        <h3>{fix.title}</h3>
        {Array.isArray(fix.body)
          ? fix.body.map((p, i) => <p key={i}>{p}</p>)
          : <p>{fix.body}</p>}
      </div>
    </div>
  );
}

/* ---------- Specs / token list ---------- */

function Specs({ title = "Specs", note, items }) {
  return (
    <div className="specs">
      <div className="specs-head">
        <span>{title}</span>
        {note && <span style={{ color: "var(--ink-muted)", textTransform: "none", letterSpacing: 0 }}>{note}</span>}
      </div>
      <div className="specs-list">
        {items.map((it, i) => (
          <div key={i}>
            <div className="k">{it.k}</div>
            <div className="v">{it.v}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

/* ---------- Note box ---------- */

function Note({ children }) {
  return <div className="note-box">{children}</div>;
}

/* ---------- Pill row ---------- */

function Pills({ items }) {
  return (
    <div className="pill-row">
      {items.map((it, i) => (
        <span key={i} className="pill"><span className="dot" />{it}</span>
      ))}
    </div>
  );
}

/* ---------- "Current site" snapshot — a chunky, less-refined version ---------- */

function SnapshotCurrent({ children }) {
  return <div className="snap-cur">{children}</div>;
}

/* ---------- Section root wrapper ---------- */

function Section({ id, alt, children }) {
  return (
    <section id={id} className={"section" + (alt ? " alt" : "")}>
      <div className="container">{children}</div>
    </section>
  );
}

Object.assign(window, {
  Pin, MockFrame, SectionHead, Finding, Specs, Note, Pills,
  SnapshotCurrent, Section,
});
