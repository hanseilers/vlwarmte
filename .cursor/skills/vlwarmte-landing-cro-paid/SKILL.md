---
name: vlwarmte-landing-cro-paid
description: >-
  CRO review and optimization workflow for paid traffic landing pages on
  vlwarmte.nl. Focuses on message match, trust sequencing, and lead-form
  completion quality.
---

# VLWarmte Paid Landing CRO

Use this skill for Google Ads and social landing analysis, especially for:

- `contact.html?modus=offerte#aanvraag`
- `prijsindicatie.html`
- campaign-specific city/service pages

## Mission

Turn paid clicks into qualified aanvragen with minimal friction and maximal trust.

## Workflow

1. Confirm campaign intent and keyword/ad-group theme.
2. Check landing message match:
   - Headline aligns with ad promise
   - CTA aligns with click intent
   - Region fit is explicit (Noord-Nederland / Zuidlaren anchor)
3. Audit first-screen conversion readiness:
   - Primary action visible
   - Trust cue visible
   - No conflicting action overload
4. Audit form friction:
   - Required fields justified
   - Error handling clear
   - Mobile completion realistic
5. Validate measurement:
   - Key events fire for submit and critical wizard steps
   - URL/deeplink behavior preserves intent (`modus`, `#aanvraag`)

## Adversarial failure modes

- Ad promises speed, page opens with generic company intro.
- Paid clicks land on high-friction form before trust is established.
- Multiple equal CTAs create decision paralysis.
- "Indicatie" flow does not clearly route to next paid action.
- Tracking captures sessions but not lead intent milestones.

## Recommendation template

For each landing page:

1. `Issue` (what is broken/misaligned)
2. `Impact` (lead volume, lead quality, CPC efficiency)
3. `Fix` (specific copy/layout/flow change)
4. `Metric` (what to watch in GA4/Ads after rollout)

## Success targets (default)

- Lower bounce on paid landings
- Higher lead submit rate from paid sessions
- Higher share of offerte-mode starts and completions
- Reduced `Unassigned` noise in traffic attribution
