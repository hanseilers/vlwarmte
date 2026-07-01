---
name: vlwarmte-ux-review
description: >-
  Run an adversarial UX review for VLWarmte pages with focus on affluent,
  well-educated homeowners in Noord-Nederland. Produces prioritized, actionable
  findings tied to lead quality and conversion.
---

# VLWarmte Adversarial UX Review

Use this skill when reviewing page quality, lead flow friction, or trust/perception gaps for `vlwarmte.nl`.

## Audience lens (always apply)

- Geography: Groningen, Friesland, Drenthe (with Zuidlaren as anchor).
- Segment: homeowners, affluent, well-educated.
- Decision style: compare quality, reliability, planning certainty, and craftsmanship proof before contact.

## Primary review goals

1. Increase qualified lead submissions.
2. Improve trust at first glance (within first viewport and first scroll).
3. Reduce friction in high-intent flows (`prijsindicatie` and `contact`).

## Review method

1. Read target page HTML and key CSS/JS affecting the experience.
2. Validate live copy and CTA sequence using the public URL.
3. Score each section on:
   - Clarity of value proposition
   - Trust/proof density
   - Friction to next action
   - Relevance to affluent homeowners
4. Produce findings with severity:
   - `High`: likely to reduce leads or trust materially
   - `Medium`: likely to reduce efficiency or perceived quality
   - `Low`: polish or minor consistency

## Adversarial checklist

- Is premium trust visible above the fold (proof, certainty, references, response SLA)?
- Is messaging specific enough for Noord-Nederland projects?
- Does copy feel consultative and expert, not generic or salesy?
- Are next steps explicit (what happens after submit, by when)?
- Is form effort proportional to user confidence at that point?
- Is there visual evidence of real craftsmanship (not stock-like)?
- Is pricing language confident but honest (indicatie vs offerte)?
- Are mobile tap targets and CTA order resilient on small screens?

## Output format

Return:

1. Prioritized issue list (`High` -> `Low`) with page path.
2. Why it matters for this audience.
3. Concrete fix recommendation.
4. A 1-week implementation shortlist (max 5 tasks).

Keep recommendations implementation-ready for PM and developer handoff.
