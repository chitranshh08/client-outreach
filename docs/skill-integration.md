# Skill Integration Report

_Date: 2026-09-30 · Claude Code 2.1.285 · cloud session_

Third-party writing skills added to this repo's KDP pipeline: what was installed, why,
from where, how it was verified, and what is still missing. Day-to-day routing lives in
`docs/editorial-workflow.md`; this file is the record.

## 1. Starting point
- **Existing workflow (kept):** 6 project skills in `.claude/skills/` covering the whole
  pipeline (`niche-research`, `new-book`, `write-book`, `kdp-package`, `launch-plan`,
  `catalog-review`) plus `docs/quality-bar.md`. Drafting already had a primary workflow
  (`write-book`); what was missing was **independent review**: structural/developmental
  review, readability/term checks, and a disciplined AI-pattern audit that reports before
  it edits.
- **Active book:** `books/meltdown-playbook-01` is at blueprint stage (brief, outline, cover
  brief; no manuscript yet). Nothing in `books/`, `research/` or `pen-names/` was modified.
- **Persistence:** the container is ephemeral; the Git repo is the only durable store.
  User-level `~/.claude` does not survive a fresh cloud session, so everything is vendored
  into the repo as project skills (Git-tracked, pinned). No marketplace/plugin install,
  since that would be user-scoped, unpinned and pull in unrelated skills.
- **Runtime:** project skills in `.claude/skills/<name>/SKILL.md` are discovered by the
  runtime. The new skills appeared in the session's skill list immediately after copying,
  with no restart.

## 2. Installed skills

| Skill (invocation name) | Local path | Role here | Source | Pinned commit | License |
|---|---|---|---|---|---|
| `avoid-ai-writing` v3.36.0 | `.claude/skills/avoid-ai-writing/` | AI-pattern prose audit (detect-first) and approved minimal edits | github.com/conorbronsdon/avoid-ai-writing, dir `plugins/avoid-ai-writing/skills/avoid-ai-writing` (the Claude Code plugin package) | `9b8d030ce5c846af9520a4f6e5eb7d3b8d80ff43` (2026-09-29) | MIT © 2026 Conor Bronsdon |
| `narrative-nonfiction` | `.claude/skills/narrative-nonfiction/` | Structural/developmental review: arc integrity, teaching, voice, exercise design | github.com/rhavekost/author-toolkit, dir `skills/narrative-nonfiction` (plugin v1.3.1) | `b78287003edf52e5f0784ee2b4a004111173358f` (2026-07-14) | MIT © 2026 rhavekost |
| `prose-mechanics` | `.claude/skills/prose-mechanics/` | Readability (Flesch-Kincaid) and term-case audits; other sentence-level audits on request | same repo, dir `skills/prose-mechanics` | same commit | MIT © 2026 rhavekost |
| (support file) | `.claude/references/finding-schema.json` | Finding format that both author-toolkit skills reference as `../../references/finding-schema.json` | author-toolkit `references/finding-schema.json` | same commit | MIT |

**Dependencies**
- `avoid-ai-writing`: optional Node ≥ 18 scripts (`detector/`, `scripts/`), dependency-free
  (no npm install). Node v22 is present in this cloud image. Without Node the skill runs
  model-only and must say so. The scripts were reviewed: they read files, and
  `normalize-quotes.js` writes only the file passed with `--write`. No network, no child
  processes, no environment or credential access.
- author-toolkit skills: none. `prose-mechanics` optionally calls a `scriptorium` CLI if
  present; it is **not** installed, so audits run from the reference files (the skill's
  documented fallback).

**Local modifications:** none to upstream files. Each skill directory is byte-identical to
its pinned upstream directory, with one file added: `LICENSE` (the upstream MIT notice,
which the license requires). All project-specific behavior lives in files we own:
`docs/editorial-workflow.md`, `docs/house-style.json` (avoid-ai-writing's supported
`--style` config), and small edits to `CLAUDE.md`, `write-book`, `new-book` and `kdp-package`.

**Update procedure**
```bash
# example for avoid-ai-writing; same pattern for author-toolkit skills
git clone https://github.com/conorbronsdon/avoid-ai-writing /tmp/aaw && cd /tmp/aaw
git log --oneline <pinned-commit>..HEAD -- plugins/avoid-ai-writing/skills/avoid-ai-writing   # review changes
grep -rn "child_process\|http\|fetch(\|writeFile\|process.env" plugins/avoid-ai-writing/skills/avoid-ai-writing
rsync -a --delete --exclude LICENSE plugins/avoid-ai-writing/skills/avoid-ai-writing/ <repo>/.claude/skills/avoid-ai-writing/
# then: update the pinned commit in this file, re-run the checks in section 5, commit
```

## 3. Candidates skipped or deferred

| Candidate | Decision | Reason (from inspecting SKILL.md, references and scripts) |
|---|---|---|
| luquiluke/claude-book-skill (`41466d6`, MIT; skill name `book`) | Skipped | Competing primary workflow: broad triggers ("write the next chapter", "outline", "review") collide with `write-book`/`new-book`; stores books under `~/Documents/Books` (outside the repo, lost between cloud sessions); runs 5–8 subagents per chapter with `model: "opus"` overrides, which conflicts with bounded review; its voice system needs author writing samples (we write under a pen name with no corpus). Its continuity idea (terms, examples, promises) was adopted as a short list in `write-book` step 5 (no files copied). Its `compile_book.py` (stdlib only) outputs US-Letter DOCX, not 6×9 or EPUB. |
| rhavekost/author-toolkit, other skills | Not installed | `fiction-workshop`, `story-structure`, `character-archetypes` are fiction-only. Its bundled copy of `avoid-ai-writing` (v3.3.1) would duplicate the name of the newer standalone v3.36.0. |
| labarba/sciwrite (`64b128b`, CC BY 4.0; skill name `manuscript-writing-review`) | Skipped | Written for scientific papers (Methods/Results, "We" as actor, journal submission). Its broad triggers ("review my writing", "check my manuscript", "clean up the prose") would capture ordinary requests here. Its keyword-consistency pass is useful, but it isn't worth a third broad-trigger reviewer. |
| swiftugandan/book-writing-skill (`9a763dd`, MIT) | Deferred to packaging | Produces hand-paginated HTML → PDF (Playwright + pypdf + Pillow); requires a `drafts/` source corpus; no EPUB (Kindle needs reflowable EPUB/DOCX); default page 7×10 in. Could be revisited for a designed 6×9 paperback interior PDF, with its own review and a test run. |
| blader/humanizer (`225a6f3`, MIT, v3.1.0) | Skipped | Rewrite-first (no separate detect mode), permits restructuring and added "opinion or reaction", and removes decorative bold, which conflicts with our bold-script readability rule. `avoid-ai-writing` already incorporates its patterns with a stricter editing contract; two automatic cleanup passes would be redundant. |

All 6 sources were reachable and inspected at the commits above. Quality was not inferred
from stars or self-reported scores.

## 4. Routing (summary)
Brief & outline: `new-book` · arc review of outline: `narrative-nonfiction` · drafting:
`write-book` · structural review: `narrative-nonfiction` · readability & terms:
`prose-mechanics` · AI-pattern audit: `avoid-ai-writing` detect mode ·
approved revisions: `avoid-ai-writing` edit mode / `prose-mechanics` approved-fixes ·
fact verification: manual, against `sources.md` · export: `kdp-package`. Full rules,
finding format and cycle limits: `docs/editorial-workflow.md`.

## 5. Verification (2026-09-30)

**Structural checks: run, passed**
- All 9 skills have valid frontmatter; `name` equals the directory name; no duplicate names
  (also none among user-level skills: only `session-start-hook`).
- Every reference file named in the three SKILL.md files resolves, including
  `../../references/finding-schema.json`, which parses as JSON.
- `diff -r` against the pinned upstream directories: 0 differences besides the added LICENSE.
- No symlinks, executable bits or hidden files in the vendored directories.
- `docs/house-style.json` accepted by `node scripts/check-style.js`: 0 unrecognized keys.
- **Runtime discovery:** after copying, the session's available-skill list showed
  `avoid-ai-writing`, `narrative-nonfiction` and `prose-mechanics` with their upstream
  descriptions. Edited project skills were re-registered live as well. No restart was needed.

**Behavioral trial:** synthetic 4-paragraph budgeting passage in the session scratchpad
(not the manuscript), planted with an unsupported claim ("Studies show … save 40%"), a
term inconsistency ("Grocery Plan System" vs "Kitchen Budget Method"), an inflated
paragraph, and one clear paragraph that should stay unchanged. Deleted after the trial.

| # | What ran | How | Result |
|---|---|---|---|
| A | `avoid-ai-writing` detector engine (`analyzeText`) | Deterministic Node script | Flagged `game-changing`, `robust`, `holistic`, `Moreover`, `Furthermore`, `In today's`, `truly`, and "Studies show" as **critical** vague attribution. Nothing flagged in the clear paragraph. Score 15, "Minimal AI signals" (a signal, not a verdict). Did not detect the term swap (not its job). |
| B | `avoid-ai-writing` in detect mode with `--style docs/house-style.json` | Invoked through the Skill tool; the audit itself was performed by the session model following the loaded instructions | Findings only, 0 edits. Caught the unsourced 40% claim (told to name the source or cut, and not to keep the 40% as the author's own assertion), the inflated paragraph, and the term swap as synonym cycling. Rated the clear paragraph clean. Stated that verifying 40% is outside its scope. No evidence was invented. |
| C | `prose-mechanics` invented-term-consistency audit | Invoked through the Skill tool; `scriptorium` absent, so reference-file procedure | **No findings, correct per its spec.** The reference says it only catches capitalization drift against a canonical list; the renamed term is out of scope. Routing was updated accordingly. |
| C2 | `prose-mechanics` readability metric | Flesch-Kincaid computed with an approximate syllable counter (script) | Inflated paragraph ≈ grade 11 (over the 6–9 self-help target); clear paragraph ≈ grade 4. |
| D | Style-only revision under `avoid-ai-writing` rewrite rules (explicit revision request), then `normalize-quotes.js` and `validate.js --residual-policy warn` | Model edit + deterministic scripts | 2 spans changed (inflated paragraph; renamed term restored). The 40% sentence was kept verbatim and still reported as a source-blocked residual. The clear paragraph is byte-identical. Validator: **PASS, no mechanical preservation errors**. Detector score 15 → 7. |

**What these checks do and don't show**
- A, C2 and the D scripts are deterministic tool runs. B, C and the D edit are the session
  model executing a skill after the runtime loaded it. That shows invocation works and
  the instructions produce in-scope behavior on this sample, but it is not independent or
  human validation, and one synthetic passage is a small sample.
- `narrative-nonfiction` was verified structurally and for discovery only; it was not
  behaviorally tested (a 4-paragraph passage can't exercise an arc review). Its first real
  use should be the Book 1 outline review.
- No skill verifies facts. The trial confirms the style skill *preserves* the claim, not
  that the claim is true.

## 6. Unresolved limitations
1. **Cross-chapter renamed terms** have no automated check: prose-mechanics only catches
   case drift, and avoid-ai-writing synonym cycling is paragraph-scoped. The mitigation is the
   continuity list in `progress.md` plus a manual check before the full-book pass.
2. **Export tooling:** `pandoc` is not installed in the cloud image, so `kdp-package` can't
   build EPUB/DOCX yet. Not installed now because no manuscript exists. When needed, install
   per session (for example `pip install pypandoc_binary`, or `apt-get install -y pandoc`);
   neither command has been tested here.
3. **Node-dependent checks** (detector, marks normalizer, validator, style checker) rely on
   Node being present in the image. They are optional; without Node the skill must label
   its output model-only.
4. **Upstream example with an uncited statistic** in `narrative-nonfiction` (voice example).
   `docs/editorial-workflow.md` says not to imitate it.
5. avoid-ai-writing's upstream default mode is **rewrite**; our routing requires saying
   "detect only". A request that omits it could rewrite text. The CLAUDE.md note and this
   doc are the guard; the upstream file was left unmodified.
