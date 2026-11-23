# Prompt Cards

Diese Karten sind zum Kopieren gedacht.

## 1. Solider Coding-Agent-Auftrag

```text
Goal:
<Was soll am Ende anders sein?>

Context:
<Welche Dateien, Fehlermeldungen, Docs, Beispiele sind relevant?>

Constraints:
<Was darf nicht passieren? Welche Patterns, Technologien, Limits gelten?>

Done when:
<Welche Tests, Checks, Diffs oder sichtbaren Verhaltensänderungen beweisen Erfolg?>

Work style:
Read first. Make a short plan. Keep changes small. Report exact verification.
```

## 2. Read-Only Codebase Scout

```text
Do not edit files.
Map the relevant code path for <problem>.
Return:
1. likely entry points
2. files to inspect
3. risky assumptions
4. the smallest next action
Use file references and line numbers where possible.
```

## 3. SDD Step 1 — Repo-Lokale Spec erstellen (Specify)

```text
We are using Spec-Driven Development (SDD).
Do not edit any production code or test files yet.

1. Explore the relevant files for <problem or feature>.
2. Create a concise spec file at <path, e.g. playground/incident-triage-hub/specs/001-change.md> including:
   - problem & current behavior
   - desired behavior
   - explicit non-goals
   - testable acceptance criteria & edge cases
   - 3-step implementation plan (exact files to change vs. files not to touch)
   - exact verification command(s)

Keep it under 250 words and wait for my review.
```

## 4. SDD Step 2 — Plan Lock & Execute (Plan Mode)

```text
Read the approved spec at <path to spec.md>.
1. Plan Lock: If there is a true blocker, ask at most ONE question; otherwise restate the locked 3-step plan and wait for confirmation.
2. Execute: Once confirmed, implement only the locked scope — respect all non-goals.
3. Halt: Run the verification command from the spec, stop immediately, and report changed files, exact test output, and residual risk.
```

## 5. SDD Step 3 — Unabhängiges Spec-Audit (Verify)

```text
Act as a skeptical reviewer. Do not edit any files.
Audit the current git diff and test output against <path to spec.md>:
- Which acceptance criteria are proven by tests?
- Were any non-goals violated or unrelated files touched?
- Were any existing tests weakened?
- What edge cases or risks remain unverified?
Lead with findings, not reassurance.
```

## 6. Skill Extraction Prompt

```text
We repeated this workflow twice. Turn it into an Agent Skill.
Create:
- name and description with clear trigger words
- step-by-step workflow
- inputs and outputs
- edge cases
- references or scripts only if they improve reliability
Keep it focused on one job.
```

## 7. Incident Triage Hub — Bugfix Contract (Track A)

```text
Goal:
Fix the failing tests in playground/incident-triage-hub.

Context:
Read playground/incident-triage-hub/README.md,
playground/incident-triage-hub/triage/models.py,
playground/incident-triage-hub/triage/rules.py,
and playground/incident-triage-hub/tests/test_rules.py first.

Constraints:
Do not read SOLUTION.md before diagnosing.
Do not change or weaken existing tests.
Keep the fix scoped to playground/incident-triage-hub/triage/rules.py.
Do not add external dependencies.

Done when:
python3 -m unittest discover -s playground/incident-triage-hub/tests -v passes.

Work style:
Read first. Explain the root causes. Propose a short plan. Then edit.
Report exact verification output and changed files.
```

## 7b. Incident Triage Hub — Spec-First Feature (Track B)

```text
We want to implement one feature from playground/incident-triage-hub/BACKLOG.md:
<Name des Backlog-Items, z.B. "4. On-Call Handover Report" oder "5. Eskalations-Warnung (Near Breach)">

Do not edit any files yet.
First inspect playground/incident-triage-hub/README.md, triage/models.py, triage/rules.py, and cli.py.
Then write a compact mini-spec (under 250 words):
- problem & desired behavior
- explicit non-goals (no external dependencies, keep existing CLI/API working)
- acceptance criteria & edge cases
- exact verification command(s)

Wait for my confirmation before proposing the 3-step plan and writing code.
```

## 8. Greenfield Puzzle PRD Prompt

```text
We want to build a highly polished professional minimalistic puzzle game as a web app.
The puzzle game idea should be novel and addictive: easy to understand and play, hard to master.

Requirements:
- procedural/generative levels, no handcrafted levels
- infinite replayability
- fair losing condition
- mobile and desktop web
- playable without sound
- professional minimalistic look and feel
- extensive unit tests
- extensive browser automation tests
- production-ready enough to deploy and publish

Do not implement yet.
Search the web for puzzle game design best practices and browser-game testing guidance.
Return three concepts, recommend one, then write a PRD for the recommended concept.
```

## 9. Greenfield Slice Lock Prompt

```text
From the approved PRD, mechanics spec, and test plan, define the first implementation slice.

Rules:
- playable in browser
- one core mechanic only
- deterministic seed mode
- unit-testable game logic separated from UI
- one losing condition
- one restart flow
- no sound dependency
- no online services

Return:
- files likely to create
- acceptance criteria
- tests to write first
- explicit non-goals
Do not implement yet.
```

## 10. Browser Verification Prompt

```text
Use browser automation or Playwright MCP to verify the app manually.

Check:
- page loads without console errors
- core move works
- losing condition can be reached
- restart works
- mobile viewport is usable
- no sound is required

Report exact evidence and screenshots or observations.
Do not call it production-ready unless these checks pass.
```

## 11. Superpowers Tiny Fix Prompt

```text
Use Superpowers for this change.

Goal:
Fix the failing tiny issue tracker search test.

Context:
Read playground/tiny-issue-tracker/README.md,
playground/tiny-issue-tracker/issue_tracker.py,
and playground/tiny-issue-tracker/tests/test_issue_tracker.py.

Constraints:
Keep the public Issue and IssueTracker API stable.
Do not add dependencies.
Do not broaden search semantics beyond case-insensitive substring matching.

Done when:
python -m unittest discover -s playground/tiny-issue-tracker/tests passes.

Work style:
Follow the relevant Superpowers skills for debugging, TDD, verification, and review.
Show the gates you used, not just the final patch.
```

## 12. OpenSpec Tiny Change Prompt

```text
/opsx:propose "Fix tiny issue tracker search so title and body matching are case-insensitive without changing the public API"
```

Review the generated OpenSpec artifacts before implementation:

```text
Check proposal.md, specs, design.md, and tasks.md.
Non-goals must exclude fuzzy search, ranking, persistence, UI changes, and API changes.
Only then run /opsx:apply.
```

## 13. Failure Mode Intervention Prompt

```text
Stop.
Classify the current failure mode:
- editing too early
- scope creep
- weak spec
- fake verification
- weakened test
- architecture theater
- ignored project rules
- unsafe tool trust

Then recover:
1. name the specific evidence for that failure mode
2. restate the approved scope
3. list required vs optional vs out-of-scope changes
4. continue only with the required work
```

## 14. Workbook Final Handoff Prompt

```text
Fill the final handoff:
- what changed
- why it changed
- how it was verified
- what did not change
- what remains risky
- next useful step

Use exact file names, commands, and results.
Do not claim completion without verification evidence.
```
