# vadapayasam.github.io — Project Context for Tina

Public HTML publishing repo. Owns: agent-publish, MSP research artifacts, daily/weekly sketches.

## Layout
- `sketch/` — primary artifact dir (numerous review sketches)
- `daily/` — daily tweet logs and research drops
- `weekly/` — weekly summarizations
- `landing/` — landing pages
- `assets/` — shared CSS/JS/images
- Root: index.html, agent-publish-twitter-thread.html, mspclaw-*.html

## Workflow
1. Research markdown lives in `~/.hermes/raw/` (cron output drops here)
2. Tina converts → HTML via research-to-web-publishing skill
3. File lands in `sketch/<name>.html` or `daily/<name>.html`
4. Use `tm deploy-html /path/to/file.html --dir sketch|daily` — commits and pushes
5. Site auto-deploys via GitHub Pages

## Deploy Commands
- Sketches: `tm deploy-html /path/to/file.html --dir sketch`
- Daily tweets: `tm deploy-html /path/to/file.html --dir daily`
- Default dir is `sketch` (hardcoded in script)

## Rules
- Default output target: `vadapayasam.github.io/warehouse/sketch/`
- Daily tweets ALWAYS go to `daily/` dir, never `sketch/`
- `thisisprabha.github.io` ONLY when Prabha explicitly says so
- ALWAYS load `prabha-taste` skill before writing HTML
- No em dashes in public-facing copy. Tasteful profanity OK.
- Style: clean, simple, warm flat 2D/2.5D

## Stack
- Static HTML, CSS only, GitHub Pages
- No build step. Plain files.
- Local server for preview: `python3 -m http.server 8000` (optional)

## Skills to load
- `prabha-taste` — design guardrails
- `research-to-web-publishing` — markdown → HTML pipeline
- `html-design-systems` — token reference
