## Learned User Preferences

- Before recommending a local dev URL, validate it: `curl` the URL from the same machine, expect `200`, `text/html`, body starting with `<!doctype` (or project `<title>`), and **not** a “Directory listing” page; if the port is already taken by another process, use another port and document it. A directory listing almost always means the server was started from the wrong working directory or the wrong process owns the port.
- Prefer clarifying questions one at a time and include how many questions remain.
- Prefer multiple-choice clarifying questions when possible.
- Require explicit permission before creating new `.md` files.
- Dislikes using worktrees in general; only use them when they clearly help and can be justified briefly.
- For VLWarmte warranty copy, describe pipe (buis) warranty as a straight “10 jaar garantie”; avoid “fabrieksgarantie” and avoid hedging with supplier/type conditions unless the user explicitly asks for that nuance.
- For the contact/offerte form, prefer a vertical field pattern (label, optional hint, then input). Avoid side-by-side label+input rows that use large spaces or spacers to align inputs, which hurt scanability and label–field association.
- For FAQ or accordion blocks, do not set the question title smaller or visually weaker than the answer body; the title should be at least as prominent for clear hierarchy.

## Learned Workspace Facts

- Workspace at `/Users/hanseilers/vlwarmte` is used for the VLWarmte website redesign workstream.
- Design specs and implementation plans are maintained under `docs/superpowers/`.
- Current VLWarmte redesign direction favors a modern/tighter, potentially darker look with stronger imagery.
- VLWarmte's preferred logo direction is an SVG "Slakkenhuis Flow" underfloor-heating laying pattern using the site's CTA accent color, without a surrounding border.
- Mobile responsiveness is a priority for the VLWarmte site, especially keeping the header and navigation compact and visible on small screens.
- The offerte form collects crawl-space depth in mm in field `vloerdiepte`, with user-facing copy centered on “Diepte kruipruimte” and a short hint tying the measure to build-up and chape/beton planning (not a generic “floor thickness only” label).
- VLWarmte mobile header: do not put `backdrop-filter` on the same element that contains a `position: fixed` nav drawer; Chromium can treat it as a containing block and clip the drawer—apply frosted blur on a `::before` (e.g. with `pointer-events: none`) instead.
- VLWarmte mobile menu open state: a full-bleed `::after` dimmer on the header must sit *below* the inner wrapper and drawer in the stacking order (e.g. raise `.site-header-inner`’s `z-index` when open); otherwise the dimmer paints over the menu links.
