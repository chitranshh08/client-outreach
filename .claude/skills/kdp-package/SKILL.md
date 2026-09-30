---
name: kdp-package
description: Produce everything needed to upload a finished manuscript to KDP (listing copy, keywords, categories, cover brief, back matter, EPUB/DOCX builds). Use when the owner says "package the book", "write the listing", "keywords", "description", "cover brief", or "build the ebook file".
---

# Package for KDP

## Inputs
- Approved, edited manuscript in `books/<slug>/manuscript/`.
- `brief.md`, niche report, `docs/kdp-rules.md`.

## Procedure
1. **Listing** → `books/<slug>/listing.md` from `templates/listing.md`:
   - Final title + subtitle (character count shown).
   - Description (≤ 4,000 chars, KDP-allowed HTML): hook line in bold, pain, promise,
     5–7 benefit bullets, who it's for, call to action. The first 2 lines must make
     sense on their own because that's what shows before "Read more".
   - 7 keyword slots: buyer phrases from Amazon autocomplete, no words repeated from the
     title, none banned by `docs/kdp-rules.md`.
   - 3 categories per format: where top competitors rank but the #1 BSR is beatable.
   - Prices: ebook + paperback per marketplace, with the royalty maths shown.
2. **Cover brief** → `books/<slug>/cover-brief.md` from `templates/cover-brief.md`:
   genre conventions from the top 10 covers, title hierarchy, color and imagery
   direction, thumbnail test. Owner makes it in Canva or hires a designer
   ($30–100 budget). If AI imagery is used, note it for the AI disclosure.
3. **Back matter** → finalize `manuscript/99-back-matter.md` from
   `templates/back-matter.md` (review ask, next book, socials, bio).
4. **Build files** (if `pandoc` is available):
   - Ebook EPUB: `pandoc books/<slug>/manuscript/*.md -o books/<slug>/build/<slug>.epub --toc --metadata title="<Title>" --metadata author="<Pen Name>"`
   - DOCX for paperback interior: build DOCX, then the owner finalizes in Word/Kindle
     Create at the chosen trim size, or uses a KDP interior template.
   - If pandoc is missing, tell the owner and suggest Kindle Create or uploading DOCX.
     (It is not installed in the default cloud image; see the export note in
     `docs/skill-integration.md`.)
5. **Gate:** owner approves listing and cover. Then they upload using the checklist in
   `docs/kdp-rules.md`. Status → `in-review`.
