#!/usr/bin/env python3
"""Collect page-1 Kindle evidence for niche research (niche-research skill, step 2).

Usage:
  python3 tools/amazon_research.py suggest "gut health"            # autocomplete phrases
  python3 tools/amazon_research.py keyword "gut health for beginners" [--top 10]
  python3 tools/amazon_research.py batch keywords.txt --out research/raw/<date>.json

`keyword` and `batch` fetch the Kindle search results for a phrase, then each of the top
N product pages, and print/save: title, author, BSR (Kindle Store), price, KU, reviews,
rating, publication date, print length. Requests are throttled; on a captcha it stops
rather than retrying, so the data is never partly guessed.
"""
import argparse
import datetime
import subprocess
import html
import json
import os
import random
import re
import sys
import time
import urllib.parse

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
BASE = "https://www.amazon.com"


class Blocked(Exception):
    pass


def fetch(url, tries=3):
    # curl, not urllib: Amazon answers urllib with 503s but serves curl normally.
    for attempt in range(tries):
        p = subprocess.run(
            ["curl", "-sS", "--compressed", "--max-time", "30", "-w", "\n%{http_code}",
             "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9", url],
            capture_output=True, text=True, errors="ignore")
        text, _, code = p.stdout.rpartition("\n")
        if code == "200":
            break
        time.sleep(10 * (attempt + 1))
    else:
        raise Blocked(f"{url} (HTTP {code})")
    if "captcha" in text.lower() and "productTitle" not in text:
        raise Blocked(url)
    return text


def pause():
    time.sleep(random.uniform(6.0, 12.0))


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def suggest(prefix):
    q = urllib.parse.urlencode({"mid": "ATVPDKIKX0DER", "alias": "digital-text", "prefix": prefix})
    data = json.loads(fetch(f"https://completion.amazon.com/api/2017/suggestions?{q}"))
    return [x["value"] for x in data.get("suggestions", [])]


def search(keyword, top):
    q = urllib.parse.urlencode({"k": keyword, "i": "digital-text"})
    s = fetch(f"{BASE}/s?{q}")
    asins = []
    # Organic results only: judge "Sponsored" within each result's own block, since a
    # wider window runs into neighbouring ad blocks and drops real results.
    hits = list(re.finditer(r'data-asin="([A-Z0-9]{10})"[^>]*data-component-type="s-search-result"', s))
    for i, m in enumerate(hits):
        asin = m.group(1)
        block = s[m.end():hits[i + 1].start() if i + 1 < len(hits) else len(s)]
        if re.search(r'>\s*Sponsored\s*<', block) or asin in asins:
            continue
        asins.append(asin)
    total = re.search(r'([\d,]+) results for', s) or re.search(r'of (?:over )?([\d,]+) results', s)
    return asins[:top], (total.group(1) if total else "?")


def attr(s, name):
    m = re.search(r'rpi-attribute-book_details-' + name + r'".{0,1500}?rpi-attribute-value[^>]*>(.*?)</div>', s, re.S)
    return clean(m.group(1)) if m else "?"


def product(asin):
    s = fetch(f"{BASE}/dp/{asin}")
    g = lambda p, d="?": (clean(m.group(1)) if (m := re.search(p, s, re.S)) else d)
    bsr = g(r"Best Sellers Rank:?\s*(?:</span>)?\s*#?([\d,]+) in Kindle Store")
    return {
        "asin": asin,
        "title": g(r'id="productTitle"[^>]*>(.*?)</span>'),
        "author": g(r'class="author[^"]*".*?<a[^>]*>(.*?)</a>'),
        "bsr_kindle": int(bsr.replace(",", "")) if bsr != "?" else None,
        # KU books show $0.00 in the Kindle slot and "or $X to buy" beside it.
        "price": g(r'or <span class="a-color-price">(\$[\d.]+)</span> to buy',
                   g(r'Kindle(?: Edition)? Format:.{0,300}?slot-price.{0,200}?(\$[\d.]+)')),
        "paperback": g(r'Paperback Format:.{0,300}?slot-price.{0,200}?(\$[\d.]+)'),
        "ku": "Read for Free" in s or "kindle-unlimited-badge" in s.lower(),
        "reviews": int(g(r'id="acrCustomerReviewText"[^>]*>\(?([\d,]+)', "0").replace(",", "")),
        "rating": g(r'id="acrPopover"[^>]*title="([\d.]+) out of 5'),
        "pub_date": attr(s, "publication_date"),
        "pages": attr(s, "ebook_pages"),
    }


def keyword(kw, top):
    asins, total = search(kw, top)
    books = []
    for a in asins:
        pause()
        books.append(product(a))
    return {"keyword": kw, "collected": datetime.date.today().isoformat(),
            "total_results": total, "books": books}


def show(r):
    print(f"\n## {r['keyword']}  (results: {r['total_results']}, collected {r['collected']})")
    print("| # | Title | Author | BSR | Price | KU | Reviews | Rating | Pub | Pages |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for i, b in enumerate(r["books"], 1):
        bsr = f"{b['bsr_kindle']:,}" if b["bsr_kindle"] else "?"
        print(f"| {i} | {b['title'][:60]} | {b['author']} | {bsr} | {b['price']} | "
              f"{'Y' if b['ku'] else 'N'} | {b['reviews']} | {b['rating']} | {b['pub_date']} | {b['pages']} |")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["suggest", "keyword", "batch"])
    ap.add_argument("arg")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--out")
    a = ap.parse_args()
    try:
        if a.mode == "suggest":
            print("\n".join(suggest(a.arg)))
            return
        kws = [a.arg] if a.mode == "keyword" else [l.strip() for l in open(a.arg) if l.strip()]
        results = []
        if a.out and os.path.exists(a.out):
            # Resume: keep keywords already collected, fetch only the rest.
            results = json.load(open(a.out))
        done = {r["keyword"] for r in results}
        for kw in kws:
            if kw in done:
                continue
            r = keyword(kw, a.top)
            results.append(r)
            show(r)
            sys.stdout.flush()
            if a.out:
                json.dump(results, open(a.out, "w"), indent=1)
            pause()
    except Blocked as e:
        sys.exit(f"BLOCKED by Amazon (captcha) at {e}. Stop and retry later; do not guess data.")


if __name__ == "__main__":
    main()
