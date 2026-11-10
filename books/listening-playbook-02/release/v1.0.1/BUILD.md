# The Listening Playbook: Release v1.0.1 (2026-11-10)

**Page-size fix only.** Same book as v1.0. No text, fonts, styles, images, links, footnotes or
layout changed. Full print specs, checks and rebuild steps: `../v1.0/BUILD.md`.

| File | Change from v1.0 |
|---|---|
| `The-Listening-Playbook_Kindle.docx` | **Page size set to the 6 × 9 in trim.** v1.0 had no page size, so Word and KDP read it as US Letter (8.5 × 11 in). Now 6.000 × 9.000 in, mirrored margins matching the PDF: inside 0.8 in, outside 0.6 in, top 0.7 in, bottom 0.8 in |
| `The-Listening-Playbook_Paperback-Interior_6x9.pdf` | **None.** Byte-identical copy of v1.0. It was already exact: all 99 pages are 432 × 648 pt (6.000 × 9.000 in), with matching TrimBox and BleedBox; nearest content to any edge is 0.475 in (KDP minimum 0.25 in) |

SHA-256:
- DOCX `137753254c183d8aa636335fd67e9d9acc8038995ce9a90b953131ec2f576510`
- PDF  `aad727750dd50b0f9f1ea222b71dddf62110767e1509aca0d66847d694cc71a6` (same as v1.0)

## What exactly changed in the DOCX
Made with `tools/book_build/docx_trim.py`, which edits two XML parts and copies the other 13
parts byte for byte:
- `word/document.xml`: added `<w:pgSz w:w="8640" w:h="12960"/>` and
  `<w:pgMar w:top="1008" w:right="864" w:bottom="1152" w:left="1152" w:header="432" w:footer="432" w:gutter="0"/>`
  to the one section. Removing those two tags gives back v1.0's file exactly.
- `word/settings.xml`: added `<w:mirrorMargins/>` (inside and outside swap on facing pages).
  Removing it gives back v1.0's file exactly.
- Same 1,220 paragraphs with identical text. python-docx reads 6.000 × 9.000 in.
- LibreOffice opens it as 114 pages at 6.000 × 9.016 in. LibreOffice snaps the height to the
  nearest millimetre (229 mm) on export; the value stored in the file is exactly 9 in. Word
  and KDP read the stored value.

## Uploading
- **Kindle ebook:** this DOCX (Kindle ignores page size; the content is unchanged).
- **Paperback:** the PDF is the recommended interior file. In KDP choose trim **6 × 9 in**,
  **No Bleed**, white paper, black-and-white. If KDP still reports a size mismatch with this
  PDF, check the bleed setting first: "Bleed" expects 6.125 × 9.25 in.
- Future builds: `build.py` now applies the same page setup to every DOCX it writes.
