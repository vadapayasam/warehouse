# Daily Tweet Generator Re-Plan
## 2026-07-07 · Why the Output Was Bad, How to Fix It

---

## 1. The Problem (with receipts)

The 2026-07-07 06:00 cron produced:

- **T1-T3**: Generic thread about "agentic debt," stateless infrastructure, and observability tax.
- **T4**: Contrarian take on context windows.
- **T5**: Deterministic execution advice.

**What's wrong:**

| Issue | Example |
|-------|---------|
| Zero personal stories | "VentureBeat Pulse Research (132 enterprise respondents)" — could be any tech account |
| Zero exact numbers from your projects | "132 respondents" is a web stat, not "400 lines removed" or "12-item checklist" |
| Zero real failures | All abstract, no "I shipped a bug and fixed it" |
| No project names | No CloakBrowser, LeaveHack, Hermes, iOS — just "enterprise AI" |
| Safe abstraction voice | "The complexity cliff" instead of "Two hours to trace. One line to fix" |

The fixed version (now live) uses **real builds, real numbers, real shame**:

- CloakBrowser v0.3.28 path traversal — 2 hours to trace, 1 line to fix
- LeaveHack crumple animation — 2 weeks wasted, 400 lines removed
- GitHub Pages stale CDN bug — 3 days of broken redirects
- 131 HTML artifacts, 30 skills, 4 iOS apps, $0 cloud cost

**This is the difference between a research digest and a build log.**

---

## 2. Root Cause

The cron prompt (minimax-m2.7) was pulling from **web research feeds** (SearXNG, news APIs) and synthesizing industry trends. It had no access to:

1. Your git commit logs
2. Your project directories and recent changes
3. Your actual bug fixes, ship notes, or PR descriptions
4. Your Hermes skill/cron/script counts
5. Your iOS build status

So it did what any model does when starved of personal context: **it defaulted to safe, generic industry commentary.**

---

## 3. The Fix: Data Sources (ranked)

### Priority 1: Git + Project Files (the gold)

Run these **before** generating tweets every morning:

```bash
# Recent commits across all repos
for repo in ~/Projects/CloakBrowser ~/Projects/leavehack-v2 ~/Projects/whatimpaying; do
  echo "=== $(basename $repo) ==="
  cd $repo && git log --oneline -5 --since="3 days ago" 2>/dev/null || echo "no recent"
done

# Recent Swift files (iOS work)
find ~/Projects -name "*.swift" -mtime -3 2>/dev/null | head -10

# Hermes stats (zero cost)
ls ~/.hermes/skills/ | wc -l
ls ~/.hermes/cron/ | wc -l
ls ~/.hermes/scripts/ 2>/dev/null | wc -l

# Sketch artifact count
cd ~/Projects/vadapayasam.github.io && find . -name '*.html' -not -path '*/.git/*' | wc -l
```

### Priority 2: Vault Raw Files (research context)

```bash
ls -lt ~/.hermes/raw/ ~/Documents/hermes-vault/raw/ 2>/dev/null | head -10
```

These give you **topics you have actually researched**, not random news.

### Priority 3: Web Research (sparingly)

Only use if P1 and P2 produce fewer than 3 story candidates. And when you do, **anchor it to your work**:

> BAD: "47% of enterprises cite integration friction"  
> GOOD: "After hitting the same integration wall in CloakBrowser's Lambda handler, this VentureBeat stat feels personal"

---

## 4. Content Rules (non-negotiable)

### Every tweet must have ONE of:

1. **A specific project name** (CloakBrowser, LeaveHack, Hermes, iOS app)
2. **An exact number** (400 lines, 12-item checklist, 131 files, v0.3.28)
3. **A real failure** (bug shipped, stale CDN, broken animation)
4. **A tool or stack detail** (MLX, GitHub Pages, SwiftUI, minimax-m2.7)

### Category rotation (force variety):

| Slot | Category | Example |
|------|----------|---------|
| Thread (2 parts) | `failures` or `workflow` | Bug story + fix story |
| Hot Take | `tips` or `interesting` | Lesson from a mistake |
| Deep Cut | `workflow` or `hermes` | Infrastructure/tooling insight |
| Wind-down | `apps` or `hermes` | Stack snapshot or ship note |

**Never** do 3+ tweets in the same category. The old output had 3 `interesting` tags. Boring.

### Voice checklist:

- [ ] First person when telling a story ("I spent two weeks," "I found a bug")
- [ ] Exact numbers, not round abstractions ("400 lines" not "a lot of code")
- [ ] Specific tools named ("MLX" not "local models")
- [ ] No em-dashes (replace with periods or commas)
- [ ] No AI slop words (elevate, seamless, unleash, transformative, etc.)
- [ ] Dry, slightly bitter about wasted hours
- [ ] Builder-in-the-weeds, not thought-leader-on-stage

---

## 5. Prompt Template (for cron)

```
You are generating today's tweet batch for a builder's public build log.
The account owner is Prabha, a Lead Product Designer who also builds iOS apps,
open-source tools, and runs a local AI automation stack.

FIRST: Read the following data sources to find real stories from the last 3 days:
1. Git commits from ~/Projects/CloakBrowser, ~/Projects/leavehack-v2, ~/Projects/whatimpaying
2. Recent .swift files modified in ~/Projects
3. Hermes skill/cron counts
4. HTML artifact count in ~/Projects/vadapayasam.github.io
5. Files in ~/.hermes/raw/ and ~/Documents/hermes-vault/raw/

Use ONLY stories, numbers, and failures from these sources.
Do NOT make up projects, versions, or numbers.
Do NOT write generic industry commentary.

Generate 4-5 tweets:
- Slot 1 (9 AM): 2-part thread. Category: failures or workflow. Must be a real bug/fix story.
- Slot 2 (12 PM): Hot take. Category: tips or interesting. Lesson from a recent mistake.
- Slot 3 (4 PM): Deep cut. Category: workflow or hermes. Infrastructure/tooling insight.
- Slot 4 (7 PM): Wind-down. Category: apps or hermes. Stack snapshot with exact numbers.

Each tweet:
- 0-220 words
- Contains at least one project name, exact number, or real failure
- First person for personal stories
- Dry builder voice, no em-dashes, no AI slop words
- Category tag from: hermes, workflow, tips, apps, interesting, failures

After generating, verify:
1. Count tweets. Must be 4-5.
2. Check char counts with t.strip().
3. Check for em-dashes.
4. Check for banned starts (here is, this is a, in summary, etc.).
5. Check for AI slop words.
6. Ensure at least 2 different categories are used.
```

---

## 6. Verification Checklist (pre-commit)

```bash
python3 -c "
import re
with open('FILE') as f: c = f.read()
tweets = re.findall(r'<div class=\"tweet-text\">(.*?)</div>', c, re.DOTALL)
assert len(tweets) in [4,5], f'Tweet count: {len(tweets)}'
for i,t in enumerate(tweets,1):
    assert len(t.strip()) <= 220*6, f'T{i} too long'  # rough word-to-char
    assert not t.strip().lower().startswith(('here is','this is a','in summary')), f'T{i} banned start'
assert len(re.findall(r'—', c)) == 0, 'Em dashes found'
assert not any(w in c.lower() for w in ['delve','leverage','seamless','unleash','transformative']), 'AI slop'
print('All checks passed')
"
```

---

## 7. What Was Fixed Today

**File overwritten:** `daily/tweets-2026-07-07.html`

| Before | After |
|--------|-------|
| "VentureBeat Pulse Research (132 respondents)" | "Found a path traversal bug in CloakBrowser v0.3.28" |
| "47% cite integration/governance gap" | "12-item checklist before every tag now" |
| "The observability tax hits unevenly" | "Two weeks on a paper-crumple swipe for LeaveHack" |
| "Context window arms race" | "GitHub Pages served stale content for three days" |
| Generic stats, no projects | 4 project names, 6 exact numbers, 2 real failures |

**Live URL:** https://vadapayasam.github.io/warehouse/daily/tweets-2026-07-07.html

---

## 8. Next Steps

1. **Update the cron prompt** with the template above
2. **Add git-mining commands** to the cron's pre-generation step
3. **Enforce category rotation** (max 2 same tags per day)
4. **Run the new prompt manually tomorrow** and verify output quality
5. **Save this re-plan** as a skill reference for future cron debugging

This is the Way.
