# vadapayasam.github.io — Project Context for Tina

Public HTML publishing repo. Owns: agent-publish, MSP research artifacts, daily/weekly sketches.

## Layout
- `warehouse/sketch/` — primary artifact dir (numerous review sketches)
- `daily/` — daily research drops
- `weekly/` — weekly summarizations  
- `landing/` — landing pages
- `assets/` — shared CSS/JS/images
- Root: index.html, agent-publish-twitter-thread.html, mspclaw-*.html

## Workflow
1. Research markdown lives in `~/.hermes/raw/` (cron output drops here)
2. Tina converts → HTML via research-to-web-publishing skill
3. File lands in `warehouse/sketch/<name>.html`
4. `git commit` + push — site auto-deploys (gh-pages)

## Rules
- Default output target: `vadapayasam.github.io/warehouse/sketch/`
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
