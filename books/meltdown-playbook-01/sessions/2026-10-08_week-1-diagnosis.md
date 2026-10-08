# 2026-10-08: Week 1 with no sales. Diagnosis and next moves

Owner: "roughly one week no sales of first title, and I am uploading the second one today.
Analyze." Amazon answered direct requests again today, so this uses live data collected
2026-10-08 with `tools/amazon_research.py` (Kindle Store, amazon.com).

## What the live page shows (2026-10-08)

| Item | Ebook (B0HLT7YGF9) | Paperback (B0HLTHYPVN) |
|---|---|---|
| Published | October 2, 2026 | linked on the same page ✓ |
| Price | **$3.99**, Kindle Unlimited ✓ | $14.99, 103 pages |
| Title as shown | **"The Meltdown Playbook: he Exact Words to Calm Tantrums…"** | same typo |
| Reviews | 0 | 0 |
| Best Sellers Rank | **none shown** | none shown |
| Series label ("Book 1 of …") | **not shown** | — |
| Author link | goes to a plain search for "Hannah Rowe" (no Author Central page, no Follow button) | — |

No Best Sellers Rank means Amazon has recorded **no sale and no Kindle Unlimited borrow**. So
the KDP dashboard's zero is real. It isn't a reporting delay.

## Where the book shows up in search (Kindle Store, page 1, organic results)

| Search | Results | Meltdown Playbook on page 1? |
|---|---|---|
| meltdown playbook | 257 | **#2** (found only by its own title) |
| toddler tantrums | 150 | no |
| toddler meltdowns | 249 | no |
| how to stop yelling at your kids | 455 | no |
| calm parenting | 8,000 | no |
| gentle parenting toddlers | 3,000 | no |
| what to say to kids | 2,000 | no |
| parenting scripts | 10,000 | no |
| emotional regulation for parents | (page didn't return results) | — |

**Who is on page 1 for "toddler tantrums"** (a real autocomplete phrase; 373 results; collected
2026-10-08, first 10 organic results):

| # | Title (short) | BSR | Price | Reviews | Published |
|---|---|---|---|---|---|
| 1 | A Practical Guide to Toddler Tantrums | 231,066 | $4.99 | 99 | Oct 2025 |
| 2 | Tantrums to Tranquility | 2,110,799 | $3.99 | 10 | Jan 2023 |
| 3 | Tiny Humans, Big Emotions | 8,200 | $14.99 | 1,273 | Oct 2023 |
| 4 | The Toddler Tantrum Toolkit | 3,561,894 | $0.99 | **0** | Dec 2025 |
| 5 | Toddler Tantrums: Go From Meltdowns to Peaceful Days | 1,534,312 | $7.99 | 16 | Oct 2024 |
| 6 | Toddler Tantrum Survival Guide | 2,815,142 | $2.99 | 1 | Jul 2025 |
| 7 | The Happiest Toddler on the Block | 220,291 | $9.99 | 2,467 | 2008 |
| 8 | Toddler Tantrum Reset | 805,846 | $2.99 | **0** | **Sep 21, 2026** |
| 9 | Toddler Tantrums: How to Get Through Meltdowns… | none | $3.99 | **0** | **Sep 19, 2026** |
| 10 | The Whole-Brain Child | 1,278 | $2.99 | 21,638 | 2011 |

Two lessons:
1. **Exact title words matter.** Three page-1 books have **zero reviews**, and two of them are
   as new as ours. What they have that we don't is the shopper's exact phrase, "Toddler
   Tantrum(s)", in the title. *The Meltdown Playbook*'s subtitle says "Tantrums" but never
   "toddler", the word parents actually type ("toddler tantrums" and "toddler meltdown" are
   both Amazon autocomplete suggestions).
2. **Page 1 alone doesn't sell.** Those zero-review books rank #800k–#3.5M, meaning almost no
   sales. The books that sell (#1,278, #8,200) have hundreds or thousands of reviews. Being
   found gets the click; reviews get the sale.

## Diagnosis

**The problem is traffic, not the book.** Sales come from shoppers who see the book, click it and
buy it. Right now almost no shopper *sees* it:
1. **Search:** it isn't on page 1 for any buyer phrase we checked. A new book with no sales and
   no reviews starts at the back of the line, and Amazon moves it forward only after people
   buy or borrow it. That's the chicken-and-egg every new KDP book faces.
2. **Outside traffic:** none yet. No social accounts, ARC readers or email list are live, so
   nothing sends shoppers to the page.
3. **Amazon's own boosts:** not switched on. There's no series link, no Author Central page,
   and no promotion (free days or Countdown) has run.

So zero sales in week one is the normal result of launching with no traffic. It is **not**
evidence that the niche, the cover or the content is wrong. We can't judge the cover or the
description until a few hundred shoppers have seen the page.

**One real defect that hurts every shopper who does see it:** the live subtitle reads
"**he** Exact Words" on both formats. That's a missing "T" in the KDP title field (our files
say "The Exact Words"). In a parenting book whose promise is "the exact words", a typo in the
title costs trust.

## The typo: options

KDP Help (checked 2026-10-08): ebook title and subtitle are **locked after publishing**;
paperback title and subtitle can be edited only **within 72 hours** of going live, and Book 1
went live on October 2, so both are locked. After that, KDP's route is a **new edition**.
([KDP Help G200736410](https://kdp.amazon.com/en_US/help/topic/G200736410))

| Option | What it costs | Recommendation |
|---|---|---|
| A. Ask KDP Support to correct the one-letter typo (Contact Us → book details) | 10 minutes; may be refused | **Try first, today.** Authors report support sometimes fixes metadata errors; not guaranteed |
| B. Publish a corrected new edition, then unpublish the old one | New ASINs and ~1 hour of setup | **Do this if A is refused, or choose it outright to also fix the search problem.** With 0 sales and 0 reviews, the old ASIN has nothing to lose, and this is the cheapest moment it will ever be. It also restarts the new-release window alongside Book 2, and lets the subtitle carry "toddler" (below) |
| C. Leave it | Every shopper sees the typo | Not recommended |

**If we republish anyway, use the chance to add the search word.** Suggested subtitle (owner
approval needed; it must match the cover and the interior title page, which I'd rebuild):
`The Exact Words to Calm Toddler Tantrums and Big Feelings: Emotional Regulation Scripts for Parents of Kids 2 to 7`
(135 characters with the title; "Toddler" added, nothing else changed). This is the one change
with direct evidence behind it (lesson 1 above). Option A can only fix the missing "T".

Ask KDP Support before doing B. Ask how to republish an ebook enrolled in KDP Select (the
90-day term) and whether the paperback needs a new ISBN (KDP's free ISBN is fine). Do the
fix **before** any promo, ARC push or social link goes to Book 1, so every review and link
lands on the final ASIN.

## Book 2 upload today: checklist

1. **Copy and paste** the title and subtitle from `books/listening-playbook-02/listing.md`.
   Don't retype them. Before you click Publish, read the preview line letter by letter.
   - Title: `The Listening Playbook`
   - Subtitle: `The Exact Words to Get Kids to Listen Without Yelling, Nagging or Bribes: Toddler and Child Discipline Scripts for Ages 2 to 7`
2. **Series:** in KDP (Bookshelf → Series), create **Calm Words Parenting** and add Book 1 as
   #1 and Book 2 as #2. If Book 1 is going to be republished, add the new edition once it
   exists.
3. **Price:** ebook **$2.99** for the launch window (plan: $5.99 after 14 days), paperback
   $14.99. KDP Select: Yes.
4. **Keywords and categories:** from `listing.md`. Check the categories in the KDP picker.
5. **AI disclosure:** text = **Yes** (AI-generated). Images = Yes if the cover used AI imagery.
6. **Files:** `release/v1.0/` (Kindle DOCX + 6×9 PDF; spine 0.223 in, wrap 12.473 × 9.25 in).
   Check both in Kindle Previewer and the print previewer before submitting.
7. **Don't add links to Book 1 yet.** Book 2's back matter says "Search for *The Meltdown
   Playbook* by Hannah Rowe", which works whatever Book 1's final ASIN turns out to be.
   Direct links go in during the planned launch + 14 days update.
8. Then **set up Author Central** for Hannah Rowe and claim both books. It's free and switches
   on the author page and the Follow button.

## Next 14 days: get the first 100 shoppers to the page

Ordered by impact per hour (details in `docs/zero-budget-marketing.md`):
1. **Fix the subtitle** (option A, then B) and the **series link**.
2. **Honest ARC readers for both books:** 20–30 parents, free copy, no review required.
   Reviews are the bottleneck. Shoppers rarely buy a parenting book with 0 reviews, and many
   promo sites require some.
3. **Pinterest first:** 1 script-card pin a day from the 60 scripts, each pin linking to the
   book through an Amazon Attribution link.
4. **Free days on Book 1** (KDP Select, up to 5 per 90 days), about a week after Book 2 is live,
   with 1–2 free promo-site submissions a week ahead. A free run gives the book a rank, some
   downloads and readers who then find Book 2.
5. **Don't keep changing prices.** Each change restarts the 30-day clock for Countdown Deals.
   Pick the long-term price now: Book 1 at $2.99 permanently (recommended) or $3.99.

## What to send me, so the next diagnosis uses real numbers
- **KDP Reports:** orders, KENP pages read, and free-promo downloads per day (a screenshot is
  fine).
- **Book 1's 3 categories** (KDP Bookshelf → Edit details), so we know which lists it can rank
  on.
- **The Book 2 ASIN** once it's live.

## Honest expectations
Most KDP books sell little, and the first weeks with no audience are the slowest. The
milestones for the next 30 days are **first 5 honest reviews, a rank in Child Discipline
during the free days, and Book 2 borrowed by Book 1 readers**. Royalties follow those. They
don't come before them.
