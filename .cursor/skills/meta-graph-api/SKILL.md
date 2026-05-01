---
name: meta-graph-api
description: >-
  Guides correct use of Meta (Facebook) Graph API, Business Manager system users,
  Page publishing, tokens, versioning, errors, and rate limits when building or
  reviewing scripts and integrations. Use when the user mentions Facebook Page API,
  Graph API, Meta Business Suite, system user tokens, page feed posting, Instagram
  Graph API basics, Marketing API boundaries, or secrets/meta-facebook.env.
---

# Meta Graph API — agent coding guide

Use this skill when writing, reviewing, or debugging **server-side** integrations with Meta (Facebook) **Graph API**, **Page** endpoints, **Business Manager / system users**, or when distinguishing Graph API from **Marketing API** / **Instagram Platform**.

**Canonical docs (prefer these over blog posts):**

- Graph API overview: https://developers.facebook.com/docs/graph-api  
- Versioning: https://developers.facebook.com/docs/graph-api/guides/versioning/  
- Page `/feed` reference: https://developers.facebook.com/docs/graph-api/reference/page/feed/  
- Error handling: https://developers.facebook.com/docs/graph-api/guides/error-handling/  
- Graph API rate limits: https://developers.facebook.com/docs/graph-api/overview/rate-limiting/  
- System user permissions (Business Management APIs): https://developers.facebook.com/docs/business-management-apis/system-users/guides/permissions/  
- Marketing API rate limits (separate from Graph platform limits): https://developers.facebook.com/docs/marketing-api/overview/rate-limiting/  
- Business Help — system users: https://www.facebook.com/business/help/503306463479099  

---

## 1. Three different “Facebook APIs” (do not conflate)

| Surface | Base URL / scope | Typical use |
|--------|-------------------|-------------|
| **Graph API** | `https://graph.facebook.com/{version}/...` | Pages, users, photos, many insights, **Page feed** |
| **Marketing API** | Same host, **Ads** object model | Campaigns, ad sets, ads, insights at ad-account level — **different** rate-limit and permission story |
| **Instagram Platform** | Graph endpoints on Instagram objects | Professional IG accounts, publishing where permitted |

**Rule:** If the task is “post on **Facebook Page**” or “read **Page** insights”, start from **Graph API Page reference**, not Marketing API docs.

---

## 2. API versioning (mandatory habit)

- **Always** send an explicit version in the path: `https://graph.facebook.com/v25.0/{node-id}...` (replace `v25.0` with the version pinned in the app; Meta documents a **current** Graph version — verify on the [versioning](https://developers.facebook.com/docs/graph-api/guides/versioning/) page).
- **Unversioned** calls use the app’s default version from the App Dashboard (**Settings → Advanced**); avoid unversioned calls in code so behavior stays predictable in CI and production.
- **Changelog:** Breaking and deprecation notices are per version — before upgrading `vN`, read the [Graph API changelog](https://developers.facebook.com/docs/graph-api/changelog/) for that version.

---

## 3. Authentication model (what the token is)

- Every successful request includes **`access_token=...`** (query or POST body, depending on client; many examples use query — prefer **POST body** or JSON for new code to avoid token leakage in logs/proxy URLs where possible).
- A **system user** is a **Business Manager identity**, not a substitute for a token. You still use a **token string** issued for that system user + **app** + scopes (e.g. **Generate token** in Business Suite).
- **Naming:** A token used for `GET/POST /{page-id}/...` is often called a “Page access token” in docs; this repo uses **`META_GRAPH_ACCESS_TOKEN`** in `secrets/meta-facebook.env` for that string.
- **Page ID:** Numeric string `{page-id}` for Page-scoped calls (this repo: **`META_PAGE_ID`**).

**Never:** commit tokens, paste tokens into `AGENTS.md`, issue templates, or user-facing markdown. Use gitignored `secrets/*.env` / `secrets/*.json` only.

---

## 4. Page feed — read vs publish

**Reference:** [Page feed](https://developers.facebook.com/docs/graph-api/reference/page/feed/)

- **Read** `GET /{page-id}/feed` — requires appropriate Page token and permissions; response shape and fields depend on `fields` parameter.
- **Publish** `POST /{page-id}/feed` — typically requires:
  - A **Page access token** from someone who can perform **`CREATE_CONTENT`** on the Page (Meta wording in docs), and  
  - App permission such as **`pages_manage_posts`** (exact names are versioned — confirm in the reference for your API version).
- **Payload:** Usually at least **`message`** OR **`link`** (not necessarily both — follow reference). Optional **`published`**, **`scheduled_publish_time`** where supported.
- **Voice:** Published posts appear **as the Page** when using a Page token.

---

## 5. System user ↔ Page **tasks** (API vocabulary)

From Business Management APIs — [Assign System User Pages Tasks](https://developers.facebook.com/docs/business-management-apis/system-users/guides/permissions/):

- Page task types include: **`MANAGE`**, **`CREATE_CONTENT`**, **`MODERATE`**, **`ADVERTISE`**, **`ANALYZE`**.
- **Minimal for posting:** ensure **`CREATE_CONTENT`** (and app scopes aligned with publishing).
- **Broader admin:** `MANAGE` is more powerful — use **least privilege**.

Assigning via API uses `POST /{PAGE_ID}/assigned_users` with `user`, `tasks`, and an admin token — UI assignment in Business Suite is often easier for small teams.

---

## 6. Permissions, App Review, and “Standard vs Advanced”

- **Development mode:** Only testers/roles on the app can authorize; good for local tests.
- **Production / non-test users:** Many permissions require **App Review** and sometimes **business verification**.
- **Feature vs permission:** Some behaviors need a **feature** (e.g. Page Public Content Access) — check the exact endpoint doc, not assumptions.

When the user hits “permission denied” or `(#200)`, verify: token type, app mode, granted scopes, Page role/tasks, and whether the endpoint requires Advanced Access.

---

## 7. Errors — when to retry vs fix

**Reference:** [Handle Errors](https://developers.facebook.com/docs/graph-api/guides/error-handling/)

| Code (examples) | Typical meaning | Agent guidance |
|-----------------|-----------------|----------------|
| **190** | Invalid/expired token | Refresh token; do not blind-retry |
| **200** / **10** family | Permission / capability | Fix scopes or App Review; do not retry blindly |
| **4**, **17**, **32**, **613**, **800xx** | Throttling / rate | Back off; see rate limit section |
| **2**, **5xx** | Transient / server | Limited retry with backoff |
| **368** | Policy / blocked | Do not spam retry |
| **506** | Duplicate consecutive post | Change content |

Parse JSON body: `{ "error": { "message", "type", "code", "error_subcode", "fbtrace_id" } }`. Log **`fbtrace_id`** for support; never log full **`access_token`**.

---

## 8. Rate limiting

**Graph (platform):** https://developers.facebook.com/docs/graph-api/overview/rate-limiting/

- Throttle codes include **4** (app), **17** (user; watch subcodes), **32** (user/app for Pages API context per doc), **613** (custom).
- **Best practice:** When limited, **stop** increasing call volume; spread traffic; use **`fields`** to reduce payload; monitor **`X-App-Usage`** (and related headers Meta documents for the endpoint).
- **Marketing API** has **separate** BUC limits — do not assume Graph throttle explains Ads errors ([Marketing API rate limiting](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting/)).

---

## 9. Security & operational checklist (for code the agent writes)

1. **Secrets:** Load from env file or OS secret store; never hardcode.  
2. **Logging:** Redact tokens from logs, URLs, and exception messages.  
3. **HTTP:** Prefer **POST body** for `access_token` on mutations if the stack allows, to reduce query-string leakage.  
4. **Least privilege:** Request minimum scopes; minimal Page tasks for system users.  
5. **Version pin:** One `META_GRAPH_API_VERSION` (or constant) per deployment; document upgrade path.  
6. **Idempotency:** For “post once” workflows, consider dedupe keys client-side — Meta may return duplicate-content errors (**506** family per error doc).  
7. **User consent:** OAuth Login flows belong in **controlled** browser/server flows — do not trick users into pasting tokens into chat.

---

## 10. VLWarmte repo convention

- Optional local file: **`secrets/meta-facebook.env`** (gitignored via `secrets/*.env`).  
- Variables: **`META_GRAPH_ACCESS_TOKEN`**, **`META_PAGE_ID`**, optional **`META_APP_ID`**, **`META_GRAPH_API_VERSION`**.  
- Template: **`secrets/meta-facebook.env.example`**.  
- Playbooks that may use this: **`.claude/commands/marketing-research-agent.md`**, **`social-media-agent.md`** — follow “no tokens in committed output”.

---

## 11. Quick verification (read-only)

Safe check without publishing:

```bash
# After: set -a && . ./secrets/meta-facebook.env && set +a
curl -sS "https://graph.facebook.com/${META_GRAPH_API_VERSION}/${META_PAGE_ID}?fields=id,name&access_token=${META_GRAPH_ACCESS_TOKEN}"
```

Expect JSON with `id` and `name`. Do not add this line to docs with a real token.

---

## 12. When the agent should stop and ask the human

- Changing **Business Manager** ownership, **deleting** assets, or **App Review** submissions.  
- The user must paste a **new secret** or complete **2FA** / **Login** in browser.  
- Legal/compliance copy for ads or **special ad categories**.

---

**Maintenance:** Re-read Meta’s **changelog** when bumping `vN`; this skill is a **distillation**, not a replacement for the official reference pages linked above.
