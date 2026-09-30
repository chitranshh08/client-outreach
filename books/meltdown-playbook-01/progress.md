# Progress: The Meltdown Playbook

**Status:** drafting · Part 1 drafted 2026-09-30 · awaiting owner read-through
**Working title (not final):** The Meltdown Playbook: The Exact Words to Calm Tantrums and
Big Feelings: Emotional Regulation Scripts for Parents of Kids 2 to 7 (option A in `brief.md`)

## Chapter status

| File | Chapter | Words (target) | Status |
|---|---|---|---|
| 00-front-matter.md | Title, copyright + disclaimer, Find Your Moment, Contents | 600 | Drafted. Update the Find Your Moment page numbers/links at packaging |
| 01-introduction.md | Start Here | 761 (1,200) | Drafted |
| 02-calm-is-contagious.md | Part 1 opener + Ch 1 Calm Is Contagious | 1,415 (1,800) | Drafted |
| 03-having-a-hard-time.md | Ch 2 Your Child Isn't Giving You a Hard Time | 1,599 (2,200) | Drafted |
| 04-four-sentences.md | Ch 3 Four Sentences That Calm Almost Any Storm | 1,895 (2,500) | Drafted |
| 05–10 | Part 2, Ch 4–10 (30 script cards) | (≈17,200) | Not started |
| 11–13 | Part 3, Ch 11–13 | (≈5,100) | Not started |
| 99-back-matter.md | Cheat sheet, sources, review ask, next book, bio | (≈1,200) | Not started |

Part 1 total ≈ 5,670 words vs ≈ 7,700 planned: written short on purpose for tired readers
(quality bar: never pad). Expect the full book to land around 25–28k words (≈ 120–130
pages at 6×9). Re-run the cover spine calculation at packaging.

## Self-check results (2026-09-30, Part 1)
- Detector (avoid-ai-writing `analyzeText`): scores 1–2, "Minimal AI signals" per chapter.
  Remaining flags: bold phrases (intentional SAY THIS scripts) and low vocabulary diversity
  (expected for plain, grade-5 wording). One "truly" fixed.
- House-style check: 0 hard violations. Advisories: section headings are sentence case
  while house style says title case (chapter titles are title case). **Owner decision
  pending**; see open questions.
- Approx. Flesch-Kincaid grade: Intro 4.1 · Ch1 3.4 · Ch2 5.4 · Ch3 4.8 (target ≤ 8). Approximate syllable counter.
- Quick win: the 3-Line Meltdown Script starts at ≈ word 1,450 of ~26k, well inside the first 10%.
- Pen-name honesty: removed an implied "I'm a parent too" line from the intro. The pen
  name never claims parenthood or credentials.

## Continuity (read before drafting the next chapter)

**Defined terms (use exactly these names):**
- **60-Second Reset**: 4 steps: plant your feet · breathe out slowly · soften your face · drop your voice (Ch 1)
- **3-Line Meltdown Script**: "I see you're ___." / "I'm right here." / "I won't let you ___." then stay close, stay quiet (Ch 1)
- **Calm Words Formula**: Connect → Name it → Hold the limit → Offer a way out (Ch 3). Way out = a choice, comfort, or a plan
- **co-regulation**: lowercase; "your child borrows your nervous system / your calm" (Ch 1)
- **upstairs brain / downstairs brain**: attributed to Siegel & Bryson (Ch 2)
- **tantrum** = about getting something (hold the limit); **meltdown** = overwhelmed (comfort and safety first) (Ch 2). The book uses "meltdown" loosely elsewhere as the umbrella word.
- **HALT + transitions**: Hungry, Angry, Lonely, Tired, plus transitions (Ch 2)
- **After-the-storm talk**: What happened? How did you feel? What could we do next time? (Ch 3)
- **"safe mad" list**: promised for Ch 5
- **dragon breath**: mentioned once in Ch 3 as a comfort option. Define it in Ch 11 (kid breathing) or cut it
- **Your 5-Minute Action**: the heading used for every chapter's end-of-chapter action

**Running examples / characters (illustrative composites):**
- Intro: 4-year-old boy, elevator button, face-down on the kitchen floor at 5:40 pm
- Ch 1: **Maya**, 3, toast cut into rectangles (and her dad)
- Ch 2: **Leo**, 5, no snack before dinner (and his mom)
- Ch 3: **Ava**, 6, and friend **Zoe**, end of playdate; worked example of a 5-year-old and the tablet

**Promises made to the reader (must be delivered):**
- Ch 10: signs it's time to talk to the pediatrician (promised in the intro, Ch 2 and the disclaimer)
- Ch 11: more feelings words for kids (promised in Ch 2)
- Ch 12: how to repair after yelling (promised in the intro and Ch 1)
- Part 2: 30 moments, each with the same layout, script in bold (intro)
- Printables: pocket card (Ch 1 ✓), meltdown tracker (Ch 2 ✓), fill-in card (Ch 3 ✓), calm-down corner checklist (Ch 11), routine chart (Ch 7), 30-day plan and Calm-Down Plan (Ch 13), cheat sheet (back matter)
- Back cover promises "25+ moments" (30 planned ✓), "60-second reset" (✓ Ch 1), "age-by-age tips" (Part 2 age tweaks), "printable calm-down plan" (Ch 13)

## Open questions for the owner
1. **Title:** confirm option A (used here), or pick B/C. If A, update the cover subtitle to match.
2. **Title clash:** search Amazon for "The Meltdown Playbook" (couldn't check automatically).
3. **Section heading style:** keep sentence case for section headings (common in non-fiction), or switch to title case? Update `docs/house-style.json` to match the decision.
4. **Sources S3 and S5:** skim the ACF report and *The Whole-Brain Child* reference (links in `sources.md`) before publishing.
5. **Length:** happy with a shorter, faster Part 1 (≈ 5.7k words), or want more examples added?

## How to work on this book (owner guide)
- **Read:** open the `manuscript/` files in order (00 → 04) on GitHub or in the Claude app.
- **Give edits:** reply in chat with the file + what to change ("Ch 2: cut the reality-check
  section", "make the intro warmer"), or edit the file directly on GitHub and tell Claude.
  Your edits are never overwritten; Claude re-reads files before each session.
- **Next chapter:** "draft chapter 4" (or "continue writing").
- **Reviews (findings only, nothing rewritten until you approve):**
  - "Review the transformation arc in books/meltdown-playbook-01/manuscript" (structure)
  - "Run readability audit on books/meltdown-playbook-01/manuscript/03-having-a-hard-time.md"
  - "Scan 02-calm-is-contagious.md for AI patterns, detect only, --style docs/house-style.json"
  - Then: "fix findings 1 and 3" to apply only the ones you approve.
