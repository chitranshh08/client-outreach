---
name: new-book
description: Turn an approved niche into a book blueprint (brief + title + outline). Use when the owner says GO on a niche, "start a new book", "plan book 2 of the series", or "outline <book>".
---

# New book blueprint

## Inputs
- An approved niche report in `research/niches/`.
- The pen name for that niche in `pen-names/`. If none exists yet, create one from
  `templates/pen-name.md` and have the owner approve it first.

## Procedure
1. **Create the folder** `books/<slug>/` and copy in `templates/book-brief.md` and
   `templates/outline.md` (as `brief.md`, `outline.md`).
2. **Fill `brief.md`:**
   - Reader avatar: who, situation, what they've tried, what they want.
   - One-sentence promise.
   - Competitor gap list (from the niche report's 1–3★ review mining), with how we beat each.
   - Positioning: why buy ours over the top 3.
   - Format decisions: target word count, trim size, KDP Select yes/no plus the reason,
     launch price.
   - Series placement: book N of M, what the next book is.
3. **Title options.** Draft 5 title + subtitle combos. Title short and memorable;
   subtitle carries the main search phrase and the promise. Check each against
   `docs/kdp-rules.md` (length, no banned terms). Recommend one.
4. **Outline** (`outline.md`): chapter list with each chapter's goal, key points,
   the reader action at the end, and planned extras (templates/checklists).
   Put the **quick win** inside the first 10% of the book.
5. **Log it** in `tracker/catalog.csv` with status `blueprint`.
6. **Gate:** present title pick, promise, and outline. Wait for owner approval, then set
   status `drafting`.
