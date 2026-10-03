# The Listening Playbook: Release v1.0 (2026-10-03)

| File | What it is |
|---|---|
| `The-Listening-Playbook_Kindle.docx` | Kindle eBook upload (reflowable) |
| `The-Listening-Playbook_Paperback-Interior_6x9.pdf` | Paperback interior, print-ready |

SHA-256 at release (a rebuild can differ byte-for-byte because of embedded timestamps; content is checked by `verify.py`):
- DOCX `c512d4ca2a6a4f32380a215520802a01127f21a9458add77ecc5b66104cd6a57`
- PDF  `aad727750dd50b0f9f1ea222b71dddf62110767e1509aca0d66847d694cc71a6`

**Title:** The Listening Playbook · **Subtitle:** The Exact Words to Get Kids to Listen Without Yelling, Nagging or Bribes: Toddler and Child Discipline Scripts for Ages 2 to 7 · **Author:** Hannah Rowe · **Series:** Calm Words Parenting, Book 2

Built from the manuscript after the 2026-10-03 review's six warning fixes (W1–W6). The
owner's human edit pass is still the gate before upload: any edits → rebuild with the
commands below.

## Paperback print specifications
Identical to Book 1, so the two books match on the shelf.

| Setting | Value |
|---|---|
| Trim | 6 × 9 in (every page checked) |
| Bleed | None (text-only interior) |
| Paper / ink | White paper, black-and-white interior |
| Pages | **99** |
| Margins | Inside 0.8 in (gutter), outside 0.6 in, top 0.7 in, bottom 0.8 in, mirrored. KDP minimum for 24–150 pages: 0.375 in inside, 0.25 in outside |
| Fonts | Source Serif 4 (body), Nunito (headings), SIL OFL 1.1, 6 subsets, all embedded TrueType |
| Running heads | Left: book title · Right: short chapter title · none on title, copyright, index/contents, part and chapter-opening pages |
| Folios | Bottom outside corner from Start Here (p. 6); front matter unnumbered but counted |
| Contents / Find Your Moment | Page numbers computed from the final layout; every entry is a clickable link in the PDF |
| Script cards | "Say this:" label, *[action notes]* in italics, script lines in bold, each on its own line |
| Printables | 6 boxed cards, each kept whole on one page |

## Kindle DOCX
- 24 chapter-level sections use Word **Heading 1** (starts a new page); 30 moments use Heading 2.
- Contents and Find Your Moment are 52 hyperlinks to heading bookmarks (0 broken). No Word TOC field, since Kindle doesn't update fields.
- No headers, footers, page numbers or page references. 39 real Word footnotes (Kindle shows them as linked notes).
- Section separators are a centred "· · ·" paragraph. Document properties: title, author, language en-US.

## How the build differs from the manuscript (build time only; the manuscript is unchanged)
- Curly quotes and apostrophes (pandoc `smart`). Write-in blanks print as underscores.
- `book.json` → `build.script_lines`: card labels, `[action]` notes and script lines become separate paragraphs; actions print in italics.
- `book.json` → `build.print_css`: the 25-entry Contents is set slightly tighter so it fits one page (otherwise every printed page number is off by one).
- **Placeholders removed while `book.json` links are empty:** the "Leave a review on Amazon" link line (the review request stays) and the "Instagram: @HANDLE" line. Fill `links.review_url` / `links.instagram_handle` and rebuild.
- Print only: page numbers in Contents/Find Your Moment, running heads, per-page footnotes, and the closing sections (series page, Stay Connected, About the Author) sharing pages.

## Rebuild
```bash
pip install -r tools/book_build/requirements.txt
python3 tools/book_build/build.py books/listening-playbook-02          # writes this folder
python3 tools/book_build/verify.py books/listening-playbook-02         # exit code 0 = all checks pass
```

## Checks run for this release (2026-10-03)
| Check | Tool | Result |
|---|---|---|
| Content vs manuscript (missing, duplicated or reordered words) | `verify.py` | DOCX 18,609/18,609 words, 0 differences · PDF 18,609/18,609, 0 differences |
| Footnotes | `verify.py` | All 28 source notes present in DOCX and PDF |
| PDF page size and count | PyMuPDF | 99 pages, all 6.000 × 9.000 in, no blank pages |
| Contents/index page numbers + links | `verify.py` | 158 link areas: each printed number = link target page, and the target page carries that heading |
| Text within margins · stranded headings · printable cards | `verify.py` | 0 problems · 6/6 cards boxed |
| DOCX structure | python-docx / XML | 52 links, 0 broken; 0 header/footer parts; 0 PAGE/TOC fields |
| Visual check of the PDF | All 99 pages rendered to contact sheets + key spreads at readable size | Defects found and fixed during QA: contents spilling to a second page (page numbers off by one), two printables not closed in the manuscript (one boxed the "Thank You" page), tracker blanks wrapping, 5 index labels not matching their moments |
| Visual check of the DOCX | mammoth → HTML → phone-width render (**proxy**) | Script cards, italic actions, printables, footnote links inspected |
| Book 1 regression | `verify.py books/meltdown-playbook-01` | Still passes (exit 0) after the shared build-tool changes |

**Not run:** Kindle Previewer and KDP's Print Previewer (not available here). Run them during upload.

## Remaining KDP steps
1. **Owner edit pass** on the manuscript, then rebuild + verify.
2. **eBook:** upload the DOCX; in the previewer check the title page, Contents links, a chapter opening, a script card, a footnote and the last pages on phone, tablet and e-reader views.
3. **Paperback:** 6 × 9 in, white paper, black & white, no bleed; upload the interior PDF; clear every flag in Print Previewer.
4. **Paperback cover wrap** for 99 pages on white paper: spine **0.223 in** (99 × 0.002252), full wrap **12.473 × 9.25 in** with 0.125 in bleed (3742 × 2775 px at 300 DPI). Spine text: KDP Help currently allows it on books over 79 pages, but `docs/kdp-rules.md` says 100+ **(verify)**. Check KDP Help before adding title + author to the spine. If KDP reports a different page count, recompute.
5. **eBook cover:** front cover at 2560 × 1600 px, matching Book 1's cover family (`cover-brief.md` to be written at packaging).
