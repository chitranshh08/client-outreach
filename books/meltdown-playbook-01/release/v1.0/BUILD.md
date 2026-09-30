# The Meltdown Playbook: Release v1.0 (2026-09-30)

| File | What it is |
|---|---|
| `The-Meltdown-Playbook_Kindle.docx` | Kindle eBook upload (reflowable) |
| `The-Meltdown-Playbook_Paperback-Interior_6x9.pdf` | Paperback interior, print-ready |

SHA-256 at release (a rebuild can differ byte-for-byte because of embedded timestamps; content is checked by `verify.py`):
- DOCX `fd77d21b0dcbce159622317ea2b39838ad4f8d487d3bad439fa66de45544e78b`
- PDF  `f8e1ed42cf6748c067cf92b21b16241ca7e7870b0c1e802f853c8dd7e06d2a20`

**Title:** The Meltdown Playbook · **Subtitle:** The Exact Words to Calm Tantrums and Big Feelings: Emotional Regulation Scripts for Parents of Kids 2 to 7 · **Author:** Hannah Rowe · **Series:** Calm Words Parenting, Book 1

## Paperback print specifications
| Setting | Value |
|---|---|
| Trim | 6 × 9 in (432 × 648 pt on every page) |
| Bleed | None (text-only interior) |
| Paper / ink | White paper, black-and-white interior |
| Pages | **103** |
| Margins | Inside 0.8 in (gutter), outside 0.6 in, top 0.7 in, bottom 0.8 in. Mirrored for left and right pages; KDP's minimum for 24–150 pages is 0.375 in inside, 0.25 in outside |
| Fonts | Source Serif 4 (body), Nunito (headings), both SIL OFL 1.1, subset-embedded as TrueType |
| Running heads | Left pages: book title; right pages: short chapter title. None on title, copyright, index/contents or part pages, or on chapter-opening pages |
| Folios | Bottom outside corner from the Introduction (p. 7); front matter unnumbered but counted |
| Contents / index | Page numbers computed from the final layout (`target-counter`); entries are clickable links in the PDF |

## Kindle DOCX
- Chapter-level sections use Word **Heading 1**, which starts a new page; moments and sections use Heading 2/3.
- The in-book Contents (23 entries) and Find Your Moment (30 entries) are hyperlinks to heading bookmarks; no Word TOC field, because Kindle doesn't update fields.
- No headers, footers, page numbers or page references. Footnotes are real Word footnotes; Kindle shows them as linked notes.
- Section separators are a centred "· · ·" paragraph. Word's graphic horizontal rules (VML) were deliberately not used.
- Document properties: title, author and language (en-US) set.

## How the build differs from the manuscript (build-time only; the manuscript is unchanged)
- Straight quotes are typeset as curly quotes and apostrophes (pandoc `smart`).
- Write-in blanks (`___`) print as underscores, not Markdown emphasis.
- Printable cards: one line per source line; boxed and kept on one page in print.
- A blank line is added before lists that directly follow a text line (7 cases in cards), so they parse as lists.
- **Placeholders removed while `book.json` links are empty:** the "Leave a review on Amazon" link line (the review request text stays) and the "Instagram: @HANDLE" line. Fill in `links.review_url` / `links.instagram_handle` in `../../book.json` and rebuild to include them.
- Print only: contents/index page numbers, running heads, per-page footnotes, and What's Next / Stay Connected / About the Author sharing a page.

## Rebuild
```bash
pip install -r tools/book_build/requirements.txt      # weasyprint 70.0, pypandoc_binary (pandoc 3.9), python-docx, pymupdf
python3 tools/book_build/build.py books/meltdown-playbook-01          # writes this folder
python3 tools/book_build/verify.py books/meltdown-playbook-01         # exit code 0 = all checks pass
```
Add `--keep-work` to `build.py` to keep the intermediate Markdown, HTML and CSS in `_work/` (git-ignored).

## Checks run for this release (2026-09-30)
| Check | Tool | Result |
|---|---|---|
| Content vs manuscript: missing, duplicated or reordered words | `verify.py` (difflib on normalised word sequences) | DOCX 21,403/21,403 words, 0 differences · PDF 21,403/21,403, 0 differences |
| Footnotes | `verify.py` | 9/9 in DOCX (Word footnotes) and 9/9 in PDF (page-foot notes) |
| PDF page size and count | PyMuPDF | 103 pages, all 6.000 × 9.000 in |
| Embedded fonts | PyMuPDF | 6 subsets, all embedded TrueType; no fallback fonts |
| Contents/index page numbers + links | `verify.py` | 168 link areas checked: each printed number = link target page, and the target page carries that heading |
| Text within margins / on page | `verify.py` | 0 problems (a two-digit list-number overhang was found and fixed) |
| Blank pages · stranded headings · printable cards on one page | `verify.py` | none · none · 10/10 cards boxed and intact |
| DOCX internal links | python-docx / XML | 53 hyperlinks, 0 broken anchors; 0 header/footer parts; 0 PAGE/TOC fields |
| Visual check of the PDF | Every page rendered to contact sheets, plus key pages at readable size | Title, copyright, index, contents, part pages, chapter openers, scripts, cards, footnotes and final pages inspected; defects found and fixed during QA: title hyphenation, write-in blanks, wrongly bold paragraphs, run-on card lines, list parsing, list numbering, running-head length, heading at page foot |
| Visual check of the DOCX | mammoth → HTML → phone-size render (**proxy**) | Title page, linked contents/index, chapter headings, scripts, cards, cheat-sheet numbering and endnotes inspected. LibreOffice rendering was **not** possible: its loader fails on every file in this environment |

**Not run:** Kindle Previewer and KDP's online Print Previewer. Neither is available here. Run them as part of the upload (below).

## Remaining KDP steps
1. **eBook:** upload the DOCX in KDP, open the launch previewer, and check the title page, the contents links, a chapter opening, a script card, a footnote and the final pages on phone, tablet and Kindle e-reader views.
2. **Paperback:** choose 6 × 9 in, white paper, black & white, no bleed; upload the interior PDF; review every flagged item in KDP's Print Previewer.
3. **Paperback cover:** not included, because no approved cover image is in the project. Supply the approved front cover (or a finished full wrap) and build the wrap at **12.482 × 9.25 in (3745 × 2775 px at 300 DPI)**, spine **0.232 in**, for 103 pages on white paper; see `../../cover-brief.md`. If KDP reports a different page count after upload, recompute the spine as pages × 0.002252 in.
4. **eBook cover:** upload the approved front cover (ideal 2560 × 1600 px) separately in KDP.
