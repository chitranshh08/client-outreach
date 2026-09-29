---
name: catalog-review
description: Monthly (or on-demand) review of the whole catalog. Update the tracker, spot winners and losers, and decide what to write next. Use when the owner says "catalog review", "monthly review", "how are my books doing", "what's working", or pastes KDP sales/royalty reports.
---

# Catalog review

## Inputs
- KDP Reports data (the owner pastes the dashboard export or screenshots): units,
  KENP read, royalties per book per marketplace.
- Amazon Ads report (spend, sales, ACoS per campaign).
- Current review counts/ratings per book.

## Procedure
1. Update `tracker/catalog.csv` for every live book (reviews, rating, last-month royalty).
2. Classify each book:
   - **Winner**: royalty ≥ $100/month or rising steadily → write the next series book,
     expand keywords and ads, consider hardcover.
   - **Promising**: some sales, good rating → fix listing/cover/ads, then re-check next month.
   - **Dud** after 90 days despite fixes → stop ads. Consider a new cover/title once,
     then leave it and move on.
3. Diagnose weak books in funnel order: impressions (keywords/categories/ads) → clicks
   (cover/title/price) → conversion (description, reviews, Look Inside quick win) →
   satisfaction (rating, read-through).
4. Check progress toward the $1,000–2,000/month target. Report the total, the trend, and
   what's needed to close the gap (more books in the winning series vs. new niches).
5. Output a short report in `research/catalog-reviews/<YYYY-MM>.md` with the next 1–3 actions.
