## Learned User Preferences

- Before recommending a local dev URL, validate it: `curl` the URL from the same machine, expect `200`, `text/html`, body starting with `<!doctype` (or project `<title>`), and **not** a “Directory listing” page; if the port is already taken by another process, use another port and document it. A directory listing almost always means the server was started from the wrong working directory or the wrong process owns the port.
- Prefer clarifying questions one at a time and include how many questions remain.
- Prefer multiple-choice clarifying questions when possible.
- Require explicit permission before creating new `.md` files.
- Dislikes using worktrees in general; only use them when they clearly help and can be justified briefly.
- For VLWarmte warranty copy, describe pipe (buis) warranty as a straight “10 jaar garantie”; avoid “fabrieksgarantie” and avoid hedging with supplier/type conditions unless the user explicitly asks for that nuance.
- For the contact/offerte form, prefer a vertical field pattern (label, optional hint, then input). Avoid side-by-side label+input rows that use large spaces or spacers to align inputs, which hurt scanability and label–field association.

## Learned Workspace Facts

- Workspace at `/Users/hanseilers/vlwarmte` is used for the VLWarmte website redesign workstream.
- Design specs and implementation plans are maintained under `docs/superpowers/`.
- Current VLWarmte redesign direction favors a modern/tighter, potentially darker look with stronger imagery.
- VLWarmte's preferred logo direction is an SVG "Slakkenhuis Flow" underfloor-heating laying pattern using the site's CTA accent color, without a surrounding border.
- Mobile responsiveness is a priority for the VLWarmte site, especially keeping the header and navigation compact and visible on small screens.
- The offerte form collects crawl-space depth in mm in field `vloerdiepte`, with user-facing copy centered on “Diepte kruipruimte” and a short hint tying the measure to build-up and chape/beton planning (not a generic “floor thickness only” label).
