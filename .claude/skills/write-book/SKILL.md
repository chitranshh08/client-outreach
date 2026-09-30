---
name: write-book
description: Draft the full manuscript chapter by chapter from an approved outline, then self-check it against the quality bar. Use when the owner says "write the book", "draft chapter N", "continue writing", or "revise chapter N".
---

# Write the manuscript

## Inputs
- `books/<slug>/brief.md` and `outline.md` (approved).
- `pen-names/<name>.md` for voice.
- `docs/quality-bar.md`.

## Procedure
1. **Files:** `books/<slug>/manuscript/00-front-matter.md`, `01-introduction.md`,
   `02-<chapter-slug>.md` … `99-back-matter.md`. One chapter per file, `# ` heading
   for the chapter title, `## ` for sections.
2. **Draft in order**, one chapter at a time. Before each chapter re-read the brief,
   the outline entry, and the previous chapter's ending so the book flows.
3. **Each chapter must:** open with a hook tied to the reader's problem, teach with
   concrete steps/examples, and end with an action step or checklist.
4. **Facts:** every statistic or study gets a real, checkable source, collected in
   `books/<slug>/sources.md`. If a source can't be verified, rewrite the claim without it.
5. **After each chapter**, update `books/<slug>/progress.md` with: word count, open
   questions for the owner, and a short **continuity** list of defined terms (e.g. "Calm
   Words Formula"), running examples, and promises made to the reader ("see Chapter 12").
   Read that list before drafting the next chapter so terms and examples stay consistent
   across sessions. Record owner decisions in `books/<slug>/sessions/YYYY-MM-DD_topic.md`.
6. **Full-book pass** when all chapters are done. Reviews return findings; nothing is
   rewritten until the owner approves (see `docs/editorial-workflow.md`):
   - Read-through for repetition, contradictions, and pacing.
   - Structure: `narrative-nonfiction` Stage 3 arc-integrity check on the manuscript.
   - Terms and readability: `prose-mechanics` invented-term-consistency and readability audits.
   - AI patterns: `avoid-ai-writing` in detect mode with `--style docs/house-style.json`.
   - Confirm the quick win lands within the first 10% of the total word count.
   - Tick every box in `docs/quality-bar.md` sections 1–3 and record the result in
     `progress.md`.
   - Apply only owner-approved findings, then stop (max 2 review → revise cycles per lens).
7. **Gate:** hand to the owner for their edit pass. Status → `editing` in the tracker.
   Apply their edits when they return comments.

## Word count check
`cat books/<slug>/manuscript/*.md | wc -w`
