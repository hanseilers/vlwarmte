# Sprint — week van 9 juni 2026 (cyclus 15)

**PM beslissing genomen op:** 2026-06-07 16:15
**Doel deze sprint:** Koude instappers laten converteren — prijsindicatie wizard ATF op mobile, projecten-pagina engagement, organische laagopbouw + Heerenveen message-match zonder nieuwe stad-pagina.
**Meetdoel:** in 4 weken (juni-fetch ~22 juni) — (a) `prijsindicatie.html` entry-bounce <45% bij ≥10 entry-sess; (b) `projecten.html` bounce <50% bij ≥10 sess; (c) Paid Search ≥1 conv. na GA4↔Ads + RSA-sync (PO/Admin); (d) GSC-fetch beschikbaar na token refresh.

---

## Goedgekeurde taken voor Developer Agent

### Taak 1: `prijsindicatie.html` — mobile ATF wizard zichtbaar `[GOEDGEKEURD]`
**Bron:** Analytics Agent (#3) + Marketing Research Agent (#3)
**Prioriteit:** Hoog (CTA/conversie)
**Actie:**
- Op viewports ≤768px: wizard-stap 0 (productkeuze) zichtbaar maken **zonder scroll** na compacte hero.
- Verkort hero-padding/lead indien nodig; geen extra CTA-knoppen; wizard-logica ongewijzigd.
- Desktop-layout niet verslechteren.
**Succescriterium:** Op 375×667 staat productkeuze in viewport na hero; entry-bounce richting <45% bij ≥10 entry-sess in juni-fetch.

### Taak 2: `projecten.html` — hero-lead verkorten `[GOEDGEKEURD]`
**Bron:** Analytics Agent (#8)
**Prioriteit:** Midden (engagement)
**Actie:**
- Verkort de hero `.lead` tot max. ~2 korte zinnen; behoud trust-strip/regio-vermelding.
- Verwijder of verplaats lange interne link-lijst uit hero-lead naar body (één korte zin met link naar werkwijze mag blijven).
- Geen extra CTA-knoppen toevoegen.
**Succescriterium:** Hero-lead ≤~280 tekens; bounce <50% en gem. duur >30 s bij ≥10 sess (juni-fetch).

### Taak 3: `systemen-producten.html` — `#laagopbouw` SEO-sectie versterken `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (content gap laagopbouw/droge vloerverwarming)
**Prioriteit:** Midden (SEO)
**Actie:**
- Onder `#laagopbouw`: voeg één H2 toe met zoekterm "droge vloerverwarming" of "laagopbouw vloerverwarming" (natuurlijk in zin).
- Voeg 1 korte alinea (3–4 zinnen) over wanneer laagopbouw zinvol is in renovatie/kruipruimte; noem Drenthe/Groningen/Friesland.
- Eén interne link naar `prijsindicatie.html` in die sectie; geen nieuwe pagina.
**Succescriterium:** H2 + body bevat laagopbouw/droge vloerverwarming + regio; sectie blijft semantisch HTML.

### Taak 4: `vloerverwarming-drachten.html` — Heerenveen message-match `[GOEDGEKEURD]`
**Bron:** Marketing Research Agent (#5) — Ads-keyword `vloerverwarming heerenveen` zonder dedicated pagina
**Prioriteit:** Midden (SEO + paid landing)
**Actie:**
- Voeg onder bestaande hero één H2: bv. "Vloerverwarming Heerenveen en Zuidwest-Friesland" met 2–3 zinnen dat VLWarmte vanuit Zuidlaren ook Heerenveen bedient (zelfde traject als Drachten-pagina).
- Geen nieuwe stad-pagina; geen extra CTA-band boven de fold.
**Succescriterium:** Pagina bevat expliciet "Heerenveen" in H2 + body; Ads kan op deze URL landen tot GSC anders adviseert.

### Taak 5: `werkwijze.html` — mid-page offerte-CTA `[GOEDGEKEURD]`
**Bron:** Analytics Agent — werkwijze entry 0% bounce, 4 conv. op 2 sess; lange pagina zonder mid-CTA
**Prioriteit:** Midden (CTA/conversie)
**Actie:**
- Na het blok met de stappen (halverwege pagina, vóór FAQ/slot): voeg één bestaande `cta-band`-structuur toe met primary link `contact.html?modus=offerte#aanvraag` ("Vraag offerte aan") en secundair `prijsindicatie.html`.
- Geen wijziging hero-CTA's; max. één extra band.
**Succescriterium:** Mid-page CTA zichtbaar zonder scroll op desktop; smoke-tests PASS.

---

## Uitgestelde voorstellen `[WACHT]`

- **GA4 ↔ Google Ads koppeling + auto-tagging + live RSA sync** — PO/Admin; campagne `23834672782`. Blokkeert Paid Search-interpretatie.
- **GSC refresh token** — `invalid_grant`; PO via `scripts/gsc_get_refresh_token.py`.
- **Assen LCP/hero-image** — layout-fix 6 dagen live; 90d nog 0,7 s / 0 scrollers — afwachten juni-fetch ~22 juni.
- **Paid Search negatives `--apply`** — na attributiefix; JSON klaar.
- **Heerenveen dedicated pagina** — max. 1 city/sprint; Drachten-H2 eerst meten via GSC.
- **Homepage hero-CTA wijzigen** — cyclus 14 afgewezen; eerst Ads-koppeling.
- **`extra_rsa --apply`** — na schone attributie + PO-akkoord.
- **Budgetverhoging Ads >€2/dag** — Paid Search nog 0 conv. in GA4-kanaal.

---

## Afgewezen voorstellen `[AFGEWEZEN]`

- **Nieuwe pagina `vloerverwarming-heerenveen.html`** — discipline 1 city/sprint; Taak 4 dekt Ads-landing tijdelijk.
- **Standalone `vloerverwarming-drenthe.html`** — thin-content-risico (cyclus 14).
- **Prijsindicatie wizard herbouwen** — wizard bestaat en presteert; alleen ATF-tweak.
- **Facebook deep links naar `modus=informatie`** — social kalender cyclus 15; geen HTML-werk.

---

## Social Media
**Status:** Weekplanning in `docs/website-manager/social/weekly_calendar.md` (week van 9 juni 2026, cyclus 15)
**Actie vereist:** Handmatige publicatie door VLWarmte team — één intentie per post (prijsindicatie of offerte-deeplink, geen informatie-tab)

---

## Context voor volgende sprint

- GSC beschikbaar? → prijsindicatie CTR, Heerenveen-rang op Drachten-URL, Drenthe-hub op `/`.
- GA4↔Ads gekoppeld + RSA op offerte-deeplink? → Paid Search conv. >0?
- Prijsindicatie entry-bounce na mobile ATF?
- Assen na layout-fix (cyclus 14): bounce/duur/scrollers?
- Juni-fetch ~22 juni is ijkpunt voor cyclus 13–15 meetdoelen.

---

## Developer Rapport — 2026-06-07 18:45
- Geïmplementeerde taken:
  1. **prijsindicatie.html** — compacte hero + `page-hero--wizard-entry` mobile CSS (≤768px) zodat wizard-stap 0 (productkeuze) ATF zichtbaar is; verkorte lead; wizard-logica ongewijzigd.
  2. **projecten.html** — hero-lead verkort tot 139 tekens; regio-/Drachten-/werkwijze-links verplaatst naar body `.small` onder sectiekop.
  3. **systemen-producten.html** — H2 “Wanneer is laagopbouw vloerverwarming zinvol?” + alinea (renovatie/kruipruimte, Drenthe/Groningen/Friesland) met link naar `prijsindicatie.html` onder `#laagopbouw`.
  4. **vloerverwarming-drachten.html** — H2 “Vloerverwarming Heerenveen en Zuidwest-Friesland” direct onder hero (geen extra CTA-band).
  5. **werkwijze.html** — mid-page `cta-band` na stappenblok: primary offerte-deeplink + secundair prijsindicatie.
- Overgeslagen taken: geen (alle 5 `[GOEDGEKEURD]` taken uitgevoerd).
- Deployment: **Nog niet live** — PM voert commit + `git push origin main` uit; daarna: [PM vult run-id / succes in]
- Live URL: https://www.vlwarmte.nl
- Smoke-tests: `navigation-links.sh` PASS · `form-behavior.sh` PASS
- Lokale verificatie: `curl` HTTP 200 + `<!doctype html>` op alle 5 gewijzigde pagina's (poort 8765).
- Aandachtspunten voor volgende sprint: mobile ATF prijsindicatie visueel controleren op fysiek device (375×667); Heerenveen Ads-landing meten via GSC zodra token refresh klaar is.
