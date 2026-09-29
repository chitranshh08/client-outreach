---
name: niche-research
description: Find and score KDP niches from live Amazon data. Use when the owner asks "find a niche", "what should the next book be", "research <topic>", "is <topic> a good KDP niche", or before starting any new pen name or series.
---

# Niche research

Goal: find niches where books **are selling now** and competition is **beatable**,
then score them so the owner can make a GO/NO-GO call.

## Inputs
- A seed topic, or "open search" (no seed: scan Kindle non-fiction bestseller
  categories for opportunities).
- `docs/kdp-rules.md` and CLAUDE.md constraints (avoid risky-advice niches, etc.).

## Procedure
1. **Generate candidates.** For open search, list 10–15 candidate sub-niches from
   Amazon Kindle bestseller/new-release lists and autocomplete phrases
   ("how to …", "… for beginners", "… for women over 40"). Prefer specific
   audience + problem pairs over broad topics.
2. **Collect evidence per candidate** (web search/fetch; if Amazon blocks access, ask
   the owner to paste the page-1 results or screenshots). For the main keyword's
   page-1 Kindle results, record for the top 10:
   title, BSR (Kindle store), price, KU yes/no, review count, rating, publish date,
   page count, cover quality (1–5).
3. **Mine pain.** Read 1–3★ reviews of the top 3–5 books. Log recurring complaints.
   These are the gaps our book will fill.
4. **Score** each candidate using `templates/niche-scorecard.md` (0–100).
5. **Series check.** List 3+ follow-up book ideas for the best candidates.
6. **Write the report** to `research/niches/<YYYY-MM-DD>-<niche-slug>.md` from the
   template: evidence table, pain list, score breakdown, series map, recommendation.
7. **Present** a ranked shortlist (top 3) with a clear recommendation and ask the owner
   for GO/NO-GO. Don't start `new-book` until they say GO.

## Rough BSR → sales guide (Kindle store, US: ballpark only)
| BSR | ≈ sales/day |
|---|---|
| < 5,000 | 30+ |
| 5k–20k | 10–30 |
| 20k–50k | 3–10 |
| 50k–100k | 1–3 |
| 100k–300k | < 1 |

## Rules
- Record the date collected. Stale data (> 30 days) must be refreshed before a GO.
- Never fabricate BSRs or review counts. Mark missing data as `?` and say so.
- Hard NO: niches built on trademarks/franchises, personalized medical/legal/financial
  advice, or trends likely to fade in < 12 months.
