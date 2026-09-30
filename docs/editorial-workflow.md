# Editorial Workflow: Who Does What

How the writing, review and editing skills divide the work on a manuscript. CLAUDE.md
holds the pipeline; this file holds the editorial rules. Provenance and verification of
the third-party skills: `docs/skill-integration.md`.

## Routing by stage

| Stage | Skill | Mode / how to ask | Writes files? |
|---|---|---|---|
| Book brief & outline | `new-book` (project) | "start a new book", "outline <book>" | Yes: `brief.md`, `outline.md` |
| Outline / arc review | `narrative-nonfiction` (vendored) | "Review the transformation arc in books/<slug>/outline.md" (Stage 3) | No: findings only |
| Exercise design | `narrative-nonfiction` | "Design exercises for <concept> in chapter N" | No: 2–3 options, owner picks |
| Chapter drafting | `write-book` (project) | "draft chapter N", "continue writing" | Yes: `manuscript/*.md` |
| Structural / developmental review | `narrative-nonfiction` | "Evaluate the teaching in chapter N", "Check voice consistency in chapter N", "Review the transformation arc in the manuscript" | No: findings only |
| Technical clarity: readability & jargon | `prose-mechanics` | "Run readability audit on chapter N" (Flesch-Kincaid; target grade 6–8 per `docs/quality-bar.md`) | No: findings only |
| Technical clarity: defined terms | `prose-mechanics` + continuity list | "Run invented-term-consistency audit on chapter N". It reads `books/<slug>/invented-terms.txt` (one canonical term per line, seeded from the continuity list in `progress.md`) and **only catches capitalization drift**. Renamed terms ("Grocery Plan System" for "Kitchen Budget Method") are caught only within a paragraph by `avoid-ai-writing` synonym cycling; across chapters, check the continuity list by hand. | No: findings only |
| Prose audit (AI patterns) | `avoid-ai-writing` | "Scan chapter N for AI patterns, detect only, --style docs/house-style.json" | No, in detect mode |
| Approved prose revisions | `avoid-ai-writing` edit mode, or `prose-mechanics` approved-fixes pass | Only after the owner approves specific findings: "fix findings 2 and 5 in chapter N" | Yes: minimal edits |
| Fact verification | none (manual) | Check `sources.md`; see "Facts" below | — |
| Formatting & export | `kdp-package` (project) | "package the book", "build the ebook file" | Yes: `build/`, `listing.md` |

Use a skill by asking for it in plain words as above, or name it ("use avoid-ai-writing in
detect mode on …"). There are no custom slash commands in this repo.

## Review is not rewriting
1. **Default to findings.** Any review, audit, check or scan returns findings and stops.
   Text changes only when the owner explicitly asks for revision, naming the findings or
   scope. For `avoid-ai-writing` that means `detect` mode unless revision is requested
   (its own default is `rewrite`, so always say "detect only").
2. **One lens per pass.** Run one audit type per request. Don't stack prose-mechanics
   audits, and don't run avoid-ai-writing and a prose-mechanics "AI-isms" audit on the same
   text. `avoid-ai-writing` owns AI patterns.
3. **Bounded cycles.** A chapter gets at most **2 review → revise cycles** per lens. Stop when
   a pass returns no warning-level findings, when two cycles are used, or when the owner
   says stop. Report what's left instead of looping. No automatic multi-agent chains: run
   one skill per request unless the owner asks for a sequence.
4. **Order:** structure before sentences. Run `narrative-nonfiction` reviews before
   `prose-mechanics` or `avoid-ai-writing`, because polishing prose that's about to be cut is waste.

## Finding format (all reviewers)
Each finding must give:
- **Location:** file + chapter/section heading (+ line if known)
- **Excerpt:** a short quote (≤ 25 words) of the actual text
- **Problem:** what's wrong, naming the rule or pattern
- **Why it matters:** the effect on the reader or on KDP compliance
- **Proposed fix:** one or two options, not a mandate
- **Severity:** note / suggestion / warning

"No issue found" is a valid result. Reviewers must not manufacture criticism to fill a
report, and should say explicitly when a passage is clear and should stay as written.

## What edits must preserve
- Factual claims, numbers, conditions and certainty levels, as written
- Citations and `sources.md` references
- Approved examples, scripts (SAY THIS lines) and illustrative composites
- The pen name's voice (`pen-names/<name>.md`). Style rules never override clear,
  intentional writing; a flagged pattern that is deliberate stays and is noted as such.
- No edit may add a statistic, study, quote, name, anecdote or first-person experience.
  If a fix needs information that isn't there, flag the gap for the owner.

## Facts are checked separately
- None of the installed skills verify facts. `prose-mechanics` and `avoid-ai-writing`
  judge wording; `narrative-nonfiction`'s Content Editor mode can flag a claim as
  *unsupported*, but that is a prompt to check, not a verification.
- Verification = matching each claim to a real, checkable source in
  `books/<slug>/sources.md` (CLAUDE.md rule 3). Unverifiable claims are cut or rewritten.
- Note: the upstream `narrative-nonfiction` voice example includes an unsourced statistic
  ("One study tracked 500 knowledge workers…"). It illustrates tone only; never imitate
  its uncited numbers.

## No false validation
Simulated reader reactions, AI-pattern counts and model self-assessments are editorial
signals, not independent human validation. Never present them as reader testing, expert
review or proof that a book "doesn't read as AI". Human validation comes from the owner's
edit pass and, later, real reader reviews.

## Where upstream skills keep their state (this repo's mapping)
The vendored skills ask for project files. In this repo use:

| Upstream expects | Use here |
|---|---|
| `book-blueprint.md` (narrative-nonfiction) | `books/<slug>/brief.md` + `books/<slug>/outline.md` |
| `sessions/YYYY-MM-DD_topic.md` | `books/<slug>/sessions/YYYY-MM-DD_topic.md` (decisions + stopping point) |
| `audit-tracker.md` (prose-mechanics) | `books/<slug>/audit-tracker.md`, created from the skill's `assets/audit-tracker-template.md` on first audit |
| Chapter status / progress | `books/<slug>/progress.md` (write-book) and `tracker/catalog.csv` |

Create these only when a skill first needs them; don't pre-create empty files.
