# AI Coding Agents — 1-Page Cheatsheet

Dein Spickzettel für den Arbeitsalltag nach dem Workshop.

---

## 1. Der Agent Contract (statt vager Einzeiler)

```text
Goal:        Was soll am Ende konkret anders sein?
Context:     Welche Dateien, Fehler, Logs oder Tests soll der Agent zuerst lesen?
Constraints: Was darf NICHT passieren? (Non-goals, keine neuen Dependencies, API stabil)
Done when:   Welcher exakte Test-/Build-Befehl beweist den Erfolg?
Work style:  Read first. Propose a short plan. Keep changes small. Report exact verification.
```

---

## 2. Die Kontext-Leiter (Wohin gehört welches Wissen?)

| Wenn das Wissen ... | ... dann gehört es in: | Beispiele |
| --- | --- | --- |
| **Fast immer** im Repo gilt | `AGENTS.md` / `CLAUDE.md` / `.github/copilot-instructions.md` | Testbefehle, Architektur-Grenzen, Package Manager, No-Gos |
| **Manchmal** als Methode gebraucht wird | Agent Skill (`SKILL.md`) | Codebase-Mapping, PR-Review-Checkliste, Postmortem-Draft, Migration |
| **Live außerhalb** des Repos liegt | MCP Server (Tools / Resources) | Issue-Tracker, Datenbank-Schema, Browser/Playwright, Logs |
| **Einmalig** für diese Aufgabe gilt | Task-Prompt / Mini-Spec | Konkreter Bug, Feature-Slice, heutige Akzeptanzkriterien |

---

## 3. Der SDD Execution Loop (Spec-Driven Development)

Statt „Vibe Coding“ im Endlos-Chat führst du größere Änderungen über eine **repo-lokale Spec-Datei** (`specs/*.md`) und **Plan Mode**:

1. **Explore & Specify (Read-Only):** *„Read the relevant files and create `specs/001-<name>.md` (Problem, Desired Behavior, Non-Goals, Acceptance Criteria). Do not edit code yet.“*
2. **Plan & Lock (Plan Mode):** *„Based on the approved spec, propose a 3-step execution plan (files to change, files not to touch, tests to run). Ask at most 1 blocking question. Wait for approval.“*
3. **Execute (Build):** *„Implement only the locked plan and run the verification command. Stop immediately after.“*
4. **Verify against Spec (Reviewer / Subagent):** *„Compare `git diff` and test output against `specs/001-<name>.md`. Check every acceptance criterion and non-goal.“*

---

## 4. Top-5 Stopp-Signale (Failure Modes sofort einfangen)

| Warnsignal beim Agenten | Dein 1-Satz-Gegenmittel |
| --- | --- |
| **Editiert sofort los**, ohne Dateien/Tests zu kennen | `Stop editing. Map the relevant files, flow, and tests first (read-only).` |
| **Scope Creep** (baut ungefragt Refactors / Features ein) | `Stop. Classify changes into required vs. out-of-scope against our spec. Keep only required.` |
| **Schwächt Tests ab**, damit sie grün werden | `Revert test changes. Explain what behavior the test protects and fix production code instead.` |
| **Behauptet „should work“** ohne echten Testlauf | `Do not claim completion without evidence. Run the exact test command and show the output.` |
| **Architektur-Theater** (neue Layer für 10-Zeilen-Fix) | `Find the smallest local change using existing patterns. Explain which abstractions you skipped.` |

---

## 5. Sicherheits- & Review-Checkliste vor dem Commit

- [ ] **Keine Secrets / PII:** Wurden versehentlich Tokens, Passwörter oder Kundendaten in Prompts, Tests oder Configs geschrieben?
- [ ] **`git diff` gelesen:** Verstehe ich jede geänderte Zeile und würde ich meinen Namen unter den PR setzen?
- [ ] **Tests echt gelaufen:** Habe ich die Testausgabe gesehen (nicht nur die Zusammenfassung des Agenten)?
- [ ] **Unrelated Files sauber:** Wurden nur Dateien geändert, die wirklich zur Aufgabe gehören?
