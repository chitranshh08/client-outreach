# 2026-10-05: Review of Parts 1 and 2 (findings only)

Owner asked: "re review part 1 and 2". Per `docs/editorial-workflow.md`, this review returns
findings and changes no manuscript text. Lenses, in order: structure and teaching →
consistency and facts → readability. Severity: **warning** (fix before publishing) ·
**suggestion** (worth fixing) · **note** (optional).

Scope: `00-front-matter.md` to `11-when-it-wont-stop.md` (Start Here, Ch 1–10, 27 moments).

## Readability verdict: easy to read

| Check | Result | Target |
|---|---|---|
| Reading grade (approx. Flesch-Kincaid) | 3.5–5.5 per chapter (front matter 10.8, from its index lists) | ≤ 8 (brand bible: 6–8) |
| Average sentence length | 9.7–13.2 words | < 18 |
| Prose paragraphs over 5 lines | 1 (Rachel's "Now rewind" story, 6 lines; fine) | ≤ 3–5 lines |
| Tables / em dashes in the ebook text | 0 / 0 | 0 / 0 |
| Same six-part card for all 27 moments, self-talk lines in bold | Yes, 27/27 | Yes |
| Find Your Spiral labels = moment headings | 27/27, same order, same words | Exact |
| Footnote references = definitions | Every file | Every file |
| AI-pattern detector (detect only, house style) | Score 1 ("minimal") on every chapter file; 0 hard style violations | Minimal |
| Quick win inside the Look Inside sample | Word 1,497 ≈ 8.8% of a ~17k book | ≤ 10% |

The structure works: Part 1 teaches one model and eight tools, and every Part 2 card uses
them. The flaws are a handful of **claims that sound like research but aren't sourced**,
some **over-confident generalizations**, and small consistency points.

---

## Warnings (fix before publishing)

**W1. Five lines state facts about the mind with no source behind them.**
CLAUDE.md rule 3: every factual claim is real and cited, or it's cut or softened.
- `05-the-replay.md`, Ch 4 opener, L38: *"The Replay is the most common spiral there is"*
  → **Fix:** *"The Replay may be the spiral you know best"*.
- `05-the-replay.md`, Moment 1, L53–54: *"Each replay also changes the memory a little,
  usually toward the worst version."* → **Fix:** *"And each pass can make it feel a little
  worse."*
- `09-night-loop.md`, Moment 23, L30–31: *"Ironically, the effort of holding them keeps you
  awake."* → **Fix:** *"Holding on to all of them can keep you awake."*
- `09-night-loop.md`, Moment 24, L63: *"Tired, half-awake minds are very bad judges of how
  serious things are."* → **Fix:** *"A tired, half-awake mind isn't a good judge of how
  serious things are."*
- `09-night-loop.md`, Moment 23, L40: *"There's good evidence for this one."* It's one
  study (S7). → **Fix:** *"There's research behind this one."*
- Why it matters: these read like findings. A reader who knows the research, or a
  reviewer, can call them out, and they break the book's own "every claim is sourced" rule.

**W2. Four over-confident generalizations.**
- `06-texts-and-silences.md`, Moment 7, L29: *"No reply feels like information. It almost
  never is."* → *"It usually isn't."*
- `07-what-ifs.md`, Moment 14, L101: *"Most missed check-ins are a dead phone."* → *"Often
  it's just a dead phone."*
- `06-texts-and-silences.md`, Moment 11: *"most posts get little attention for reasons that
  have nothing to do with you"* → *"posts often get little attention for reasons…"*
- `05-the-replay.md`, Moment 6: *"Most replays that start at 11 p.m. look much smaller by
  11 a.m."* → *"Replays that start at 11 p.m. often look much smaller by 11 a.m."*
- Why it matters: same rule as W1. The softer wording is still reassuring and is honest.

**W3. The Part 2 opener promises every tool takes "about two minutes", and several don't.**
- `05-the-replay.md`, "How to use a moment card", L11: *"**Try this:** the tool to use, in
  about two minutes."* Moment 20 asks for research "until Sunday", Moment 10 spans days of
  waiting, and Moment 23 is a five-minute brain dump.
- Why it matters: the brief bans speed overpromises ("in 60 seconds"). Readers mark down
  promises the book doesn't keep.
- Fix: *"**Try this:** the tool to use, step by step."*

---

## Suggestions (worth fixing)

**S1. Four British words in a US-English book** (KDP language en-US, US marketplace first).
- Ch 2, L83 "the wait in a **queue**" → "line" · Moment 10 "a **film**" → "a movie" ·
  Ch 7 opener "her online **basket**" → "cart" · Moment 27 "students who **carried on** as
  usual" → "kept using it as usual".

**S2. The reassurance line appears three times, almost word for word.**
- Ch 2 ("can bring relief for a few minutes, and then the question comes back"), Moment 9
  ("The relief lasts a few minutes, then the question comes back"), Ch 10 snag 3 (same).
- Fix: keep Ch 2 and Ch 10; in Moment 9 say *"Asking again won't settle it. Take their
  answer as the answer."*

**S3. Moment 22 is the only card whose "Try this" doesn't name one of the eight tools.**
- `08-cant-decide.md`, Moment 22: *"**Try this:** Limit the asking, then decide."* Its
  backup, the coin flip, is a ninth technique in a book that promises eight.
- Fix: *"**Try this:** The Good-Enough Rule, with a limit on asking."* Keep the coin flip
  (it's useful and short), or cut it to keep the toolkit pure. Owner's call.

**S4. The "It isn't X. It's Y." reframe appears six times in prose.**
- Start Here ("It feels like problem-solving. It isn't."; "Getting help isn't failing at
  this book. It's using every tool you have."), Ch 3 Tool 8, Moment 6 ("This isn't
  pretending. It's correcting…"), Ch 10 twice.
- Why it matters: used often, this rhythm reads as formulaic (a known AI pattern).
- Fix: rephrase two or three in prose (e.g. Moment 6: *"You're not pretending, just
  correcting a review that only looks for mistakes."*). The bold self-talk lines that use
  the shape ("Quiet isn't a verdict") are deliberate and should stay.

---

## Notes (optional)

- **N1.** Moment 2 calls it "the word-repetition trick from Chapter 3"; Ch 3 presents it as
  an unnamed variation of the Thought Label. Option: *"the Thought Label's word-repetition
  variation (Chapter 3)"*.
- **N2.** Moment 16 puts the emergency-signs paragraph between "Try this" and "Say this",
  breaking the card order. This is deliberate (safety information stays visible).
  Recommend keeping it.
- **N3.** Ten of 27 cards have an italic line under the heading. They appear only where the
  label needs context. Fine as written.
- **N4.** Sources S3 and S7 still need volume and page numbers confirmed (already listed in
  `progress.md`).

## Clear as written (no change)
- **Card format and navigation:** consistent and easy to scan.
- **Characters:** each one is used once, and Rachel's return in Ch 10 closes her arc.
- **Disclaimer, Ch 10 and 988 text:** the line between general education and advice is
  clear.
- **Moments 15 and 16 (money and health):** they stay on the worry, not the money or the
  symptom.
- **Cross-references to Chapters 1–4:** all point to the right place.
- **Pen-name honesty:** no credentials and no personal-history claims.

## Owner decision needed
Which findings to apply? Recommended: W1–W3 + S1–S3 (all small, word-neutral or
shorter). S4 and the notes are optional.
