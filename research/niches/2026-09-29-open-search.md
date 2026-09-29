# Niche Report: Open Search, Round 1

- **Date collected:** 2026-09-29
- **Marketplace:** Amazon.com (Kindle Store)
- **Raw data:** `research/raw/2026-09-29-page1.json` (page-1 top 10 per keyword, organic only)
- **Status:** **Partial.** 4 of 15 planned keywords collected. Amazon then served its
  automated-access block page ("To discuss automated access to Amazon data please
  contact api-services-support@amazon.com"), and the scan stopped rather than work around
  it. The 11 unscanned keywords are listed at the bottom.

## Candidates scanned

Keywords were chosen from Amazon Kindle autocomplete (all four are real buyer phrases).

### 1. "how to stop overthinking": ~9,000 results
| Signal | Value |
|---|---|
| Top-10 with BSR < 50k | 4 (1,744 · 2,033 · 9,549 · 25,103) |
| Top-3 with BSR < 20k | 2 |
| Top-10 with < 100 reviews | 6, but those 6 all rank 210k–850k (≈ 0–1 sales/day) |
| KU share | 7/10 |
| Median ebook price | $2.98 (many $0.99 books) |
| Median length | ~174 pages |

Market shape: owned by established brands (Nick Trenton: 15,804 and 1,704 reviews;
Daniel Chidiac: #1,744 at $9.99). **Key signal:** *The Peace of Letting Go* (Judy Dyer,
2026) ranks **#9,549 with only 23 reviews at $9.99**, so a new, well-packaged book can
still break in. The low-review books losing here are generic "How to Stop Overthinking"
clones with the keyword as the title.

### 2. "nervous system regulation": ~6,000 results
| Signal | Value |
|---|---|
| Top-10 with BSR < 50k | 2 (26,711 · 35,630) |
| Top-3 with BSR < 20k | 0 |
| Top-10 with < 100 reviews | 7 |
| KU share | 2/10 (a non-KU niche) |
| Median ebook price | $4.99 |
| 2025–26 releases on page 1 | 9/10 |

Market shape: a young, trending niche flooded with 2026 releases, most of them selling
under 1/day. Page 1 is dominated by credentialed authors ("Dr.", "LGSW"): this is health
content and falls under CLAUDE.md rule 4 (risky advice).

### 3. "emotional regulation for adults": ~4,000 results
| Signal | Value |
|---|---|
| Top-10 with BSR < 50k | 2 (19,253 is Nicole LePera, a traditional bestseller; 33,966) |
| Top-3 with BSR < 20k | 0 |
| Top-10 with < 100 reviews | 8 |
| KU share | 9/10 |
| Median ebook price | $3.99 |
| 2025–26 releases on page 1 | 9/10 |

Market shape: saturated with 2026 look-alike books (keyword-as-title, $0.99–5.99), almost
all at 100k–600k BSR. Easy to reach page 1, but page 1 doesn't pay here.

### 4. "emotional regulation for parents": ~3,000 results
| Signal | Value |
|---|---|
| Top-10 with BSR < 50k | 3 (4,405 · 7,060 · 27,566) |
| Top-3 with BSR < 20k | 0 |
| Top-10 with < 100 reviews | 6 |
| KU share | 8/10 |
| Median ebook price | $8.34 (buyers pay $11.99–14.99 here) |

Market shape: parents pay premium prices. **T.R. Fosters** runs a series split by child
age (general → middle school → high school → 6-in-1 bundle at $26.99). That's the series
model we want, and it shows the audience can be split by age. The top sellers are strong
traditional/expert books (*Tiny Humans, Big Emotions* #7,060; *How to Stop Losing Your
Sh\*t with Your Kids* #27,566).

## Scorecards (template: `templates/niche-scorecard.md`)

| Factor (max) | Overthinking | Nervous system | Emo-reg adults | Emo-reg parents |
|---|---|---|---|---|
| Demand (30) | 24 | 12 | 10 | 16 |
| Beatable competition (25) | 13 | 17 | 18 | 14 |
| Profitability (15) | 7 | 11 | 7 | 14 |
| Series potential (15) | 13 | 11 | 10 | 14 |
| Evergreen (10) | 10 | 6 | 7 | 10 |
| Fit (5) | 4 | 1 | 4 | 4 |
| **Total (100)** | **71** | **58** | **56** | **72** |
| Verdict | Borderline GO | NO | NO | Borderline GO |

Scoring notes:
- *Beatable competition* counts only low-review books that **also sell**. Many low-review
  books on page 1 that don't sell means the niche is crowded, not beatable.
- Overthinking loses profitability points because the market is anchored at $0.99–3.99.
- Parents scores best on money (high prices, clear age-based series), but demand relies on
  a few strong expert books.

## Recommendation (provisional)

**Leading candidate: emotional regulation for parents (72).** The angle is an age-specific
series ("for parents of toddlers / 5–8-year-olds / tweens"), practical scripts parents can
say in the moment, priced at $4.99–6.99 ebook and $14.99 paperback. Second: overthinking
(71), but only with a strong premium angle and cover, not another keyword clone.

**Not yet a GO.** Before committing:
1. Scan the 11 remaining candidates (below). A hobby niche may beat both.
2. Scan the age-split keywords for the parents niche (e.g. "toddler tantrums",
   "emotional regulation for kids") to confirm the series has demand at each age.
3. Mine the 1–3★ reviews of the top 5 parent books (page access needed).

## Not yet scanned (blocked)
people pleasing · self discipline · how to talk to anyone at work · gut health for women ·
raised bed gardening for beginners · container gardening · backyard chickens ·
homesteading for beginners · sourdough cookbook for beginners · decluttering with adhd ·
caring for aging parents
