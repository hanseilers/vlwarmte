#!/usr/bin/env python3
"""Browser regression: successful form sends queue GA events while gtag downloads.

Formspree responses are controlled fixtures here; Google tag itself is real.
Analytics collection requests are inspected and intercepted to avoid test traffic.
Real production submit/mail verification is a separate check.
"""
import asyncio
import json
import os
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(os.environ.get('E2E_EVIDENCE_DIR', '/tmp/vlwarmte-contact-analytics'))

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

async def main():
    OUT.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    report = {'fixtures': 'Formspree only; Google tag real, collection intercepted (204), not delivered', 'cases': []}
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(channel=os.environ.get('E2E_BROWSER_CHANNEL') or None)
            try:
                for mode, status, valid in [('informatie', 200, True), ('offerte', 200, True), ('bel', 200, True), ('informatie', 500, True), ('informatie', 200, False)]:
                    label = f'{mode}-{status}-{valid}'
                    ctx = await browser.new_context(viewport={'width': 390, 'height': 844}, record_video_dir=str(OUT / label))
                    gate = asyncio.Event()
                    hits = []
                    async def route_request(route):
                        url = route.request.url
                        if 'googletagmanager.com/gtag/js' in url:
                            await gate.wait()
                            await route.continue_()
                        elif 'google-analytics.com' in url or 'analytics.google.com' in url:
                            data = parse_qs(urlsplit(url).query)
                            body = route.request.post_data or ''
                            for line in body.splitlines() or ['']:
                                values = {**data, **parse_qs(line)}
                                hits.append({'event': values.get('en', [''])[0], 'measurement': values.get('tid', [''])[0], 'mode': values.get('ep.soort_aanvraag', [''])[0], 'endpoint': urlsplit(url).netloc+urlsplit(url).path, 'params': {k:v for k,v in values.items() if k in ['en','ep.soort_aanvraag','ep.form_id','ep.form_name','_eu','_ee','epn.form_submit_text','_c','_et']}})
                            await route.fulfill(status=204, body="")
                        elif 'formspree.io/f/' in url:
                            await route.fulfill(status=status, content_type='application/json', body='{"ok":true}' if status == 200 else '{"error":"test"}')
                        else:
                            await route.continue_()
                    await ctx.route('**/*', route_request)
                    page = await ctx.new_page()
                    await page.goto(f'http://127.0.0.1:{server.server_port}/contact.html?modus={mode}#aanvraag', wait_until='domcontentloaded')
                    if valid:
                        # Kort formulier: naam, telefoon of e-mail, vraag. De modus komt uit de deeplink.
                        contact = '0618817459' if mode == 'bel' else 'synthetic@example.invalid'
                        for field, value in [('name', 'VLWarmte synthetic test'), ('contact', contact), ('message', 'Synthetische test: 50 m², betonvloer.')]:
                            await page.locator('#' + field).fill(value)
                    await page.locator('#lead-form button[type=submit]').click()
                    success = status == 200 and valid
                    await page.locator('#lead-status.success' if success else '#lead-status.error').wait_for()
                    queued = await page.evaluate("Array.from(window.dataLayer || []).filter(x => x[0] === 'event' && x[1] === 'contact_submit').map(x => x[2])")
                    assert len(queued) == int(success), f'{label}: successful send lost before Google finished loading: {queued}'
                    if success:
                        expected = {'informatie':'informatie','offerte':'offerte','bel':'terugbelverzoek'}[mode]
                        assert queued == [{'soort_aanvraag': expected}], queued
                    await page.screenshot(path=str(OUT / (label + '.png')))
                    gate.set()
                    if success:
                        for _ in range(100):
                            if any(x['event'] == 'contact_submit' for x in hits):
                                break
                            await page.wait_for_timeout(100)
                        lead_hits = [x for x in hits if x['event'] == 'contact_submit' and x['endpoint'].endswith('/g/collect')]
                        assert len(lead_hits) == 1, hits
                        assert lead_hits[0]['measurement'] == 'G-0BB9M7HYSF', lead_hits
                        assert lead_hits[0]['mode'] == expected, lead_hits
                    else:
                        await page.wait_for_timeout(1500)
                        assert not any(x['event'] == 'contact_submit' for x in hits), hits
                    report['cases'].append({'mode': mode, 'status': status, 'valid': valid, 'queued_leads': len(queued), 'hits': hits, 'passed': True})
                    await ctx.close()
            finally:
                await browser.close()
    finally:
        server.shutdown()
        (OUT / 'report.json').write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    asyncio.run(main())
