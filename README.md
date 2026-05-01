# VLWarmte Website

Statische website (HTML/CSS/JS) voor VLWarmte.

## Structuur

- `index.html` - homepage
- `diensten.html` - dienstenoverzicht
- `systemen-producten.html` - systemen en materialen
- `werkwijze.html` - proces in stappen
- `over-ons.html` - bedrijfsprofiel
- `projecten.html` - projectvoorbeelden
- `contact.html` - informatie/offerte formulier
- `disclaimer.html` en `privacy.html` - juridische basispagina's

## Lokaal bekijken

Open `index.html` direct in je browser of serve via een simpele static server.

**Home-link (`/`):** in de markup wijst “Home” en het logo naar `/` (canonieke homepage online). Via `file://` opent `/` niet je projectmap — gebruik dan “Terug” naar `index.html` of start een lokale static server (`python3 -m http.server`) zodat `/` wél naar de site wijst.

## Smoke checks

```bash
bash tests/smoke/navigation-links.sh
bash tests/smoke/form-behavior.sh
```
