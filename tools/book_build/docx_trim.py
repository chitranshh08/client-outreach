#!/usr/bin/env python3
"""Give a built DOCX the book's print trim size and margins, changing nothing else.

pandoc writes no page size into the DOCX, so Word and KDP read it as US Letter
(8.5 x 11 in). Kindle ignores page size, but a paperback made from the DOCX, or anyone
opening it in Word, needs the real trim. This patch touches only two XML parts:

  word/document.xml   final <w:sectPr>: adds <w:pgSz> (trim) and <w:pgMar> (margins
                      from book.json "print", inside = left, outside = right)
  word/settings.xml   adds <w:mirrorMargins/> so inside/outside swap on facing pages

Every other part of the package is copied byte for byte, in the same order.

Usage:
  python3 tools/book_build/docx_trim.py books/<slug> path/to/book.docx [--out patched.docx]
"""
import argparse, json, os, re, shutil, sys, tempfile, zipfile

TWIP = 1440  # twentieths of a point per inch


def page_xml(p):
    w, h = (round(x * TWIP) for x in p["trim_in"])
    m = {k: round(p[f"margin_{k}_in"] * TWIP) for k in ("top", "bottom", "inside", "outside")}
    pgsz = f'<w:pgSz w:w="{w}" w:h="{h}"/>'
    # header/footer distances sit inside the top/bottom margins; gutter stays 0
    pgmar = (f'<w:pgMar w:top="{m["top"]}" w:right="{m["outside"]}" w:bottom="{m["bottom"]}" '
             f'w:left="{m["inside"]}" w:header="432" w:footer="432" w:gutter="0"/>')
    return pgsz, pgmar


def patch_document(xml, pgsz, pgmar):
    sects = list(re.finditer(r"<w:sectPr\b[^>]*>(.*?)</w:sectPr>", xml, re.S))
    if not sects:
        sys.exit("no <w:sectPr> found in word/document.xml")
    out, last = [], 0
    for m in sects:
        body = re.sub(r"<w:pgSz\b[^>]*/>|<w:pgMar\b[^>]*/>", "", m.group(1))
        # schema order: header/footer refs, footnotePr, endnotePr, type, pgSz, pgMar, ...
        anchor = None
        for tag in ("w:type", "w:endnotePr", "w:footnotePr"):
            a = re.search(rf"<{tag}\b[^>]*/>|<{tag}\b[^>]*>.*?</{tag}>", body, re.S)
            if a:
                anchor = a.end()
                break
        if anchor is None:
            refs = list(re.finditer(r"<w:(?:header|footer)Reference\b[^>]*/>", body))
            anchor = refs[-1].end() if refs else 0
        body = body[:anchor] + pgsz + pgmar + body[anchor:]
        start = m.start(1)
        out += [xml[last:start], body]
        last = m.end(1)
    out.append(xml[last:])
    return "".join(out)


def patch_settings(xml):
    if "<w:mirrorMargins" in xml:
        return xml
    # schema order puts mirrorMargins after embedSystemFonts / saveSubsetFonts / saveFormsData
    for tag in ("w:saveFormsData", "w:saveSubsetFonts", "w:embedSystemFonts", "w:embedTrueTypeFonts", "w:zoom"):
        a = re.search(rf"<{tag}\b[^>]*/>", xml)
        if a:
            return xml[:a.end()] + "<w:mirrorMargins/>" + xml[a.end():]
    return re.sub(r"(<w:settings\b[^>]*>)", r"\1<w:mirrorMargins/>", xml, count=1)


def set_trim(docx_path, print_cfg, out_path=None):
    pgsz, pgmar = page_xml(print_cfg)
    out_path = out_path or docx_path
    fd, tmp = tempfile.mkstemp(suffix=".docx", dir=os.path.dirname(os.path.abspath(out_path)))
    os.close(fd)
    with zipfile.ZipFile(docx_path) as zin, zipfile.ZipFile(tmp, "w") as zout:
        for info in zin.infolist():
            data = zin.read(info.filename)
            if info.filename == "word/document.xml":
                data = patch_document(data.decode("utf-8"), pgsz, pgmar).encode("utf-8")
            elif info.filename == "word/settings.xml":
                data = patch_settings(data.decode("utf-8")).encode("utf-8")
            zout.writestr(info, data, compress_type=info.compress_type)
    shutil.move(tmp, out_path)
    return out_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book_dir")
    ap.add_argument("docx")
    ap.add_argument("--out")
    a = ap.parse_args()
    cfg = json.load(open(os.path.join(a.book_dir, "book.json"), encoding="utf-8"))
    print(set_trim(a.docx, cfg["print"], a.out))


if __name__ == "__main__":
    main()
