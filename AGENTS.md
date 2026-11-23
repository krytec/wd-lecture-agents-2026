# Agent Instructions (Workshop Repository)

Dieses Repository ist ein **Praxis-Workshop & Mini-Hackathon Kit** für Coding Agents.
Wenn du als AI Coding Agent in diesem Repo arbeitest, halte dich strikt an diese Regeln:

## 1. Projektstruktur & Tech-Stack

- **`playground/tiny-issue-tracker/`**: Kleines Warm-up-Projekt (Python 3.9+ Standard Library, keine externen Dependencies).
  - Testbefehl: `python3 -m unittest discover -s playground/tiny-issue-tracker/tests`
- **`playground/incident-triage-hub/`**: Selbstenthaltenes Brownfield-Praxisprojekt mit CLI, Mini-Web-UI und Tests (Python 3.9+ Standard Library, keine externen Dependencies).
  - Testbefehl: `python3 -m unittest discover -s playground/incident-triage-hub/tests -v`
  - CLI-Smoke-Check: `python3 playground/incident-triage-hub/cli.py summary`
- **`concepts/01..07/`**: Die 7 Workshop-Module (`README.md`, `workshop.md`, `further-reading.md`).
- **`resources/`**: Begleitmaterialien (`workbook.md`, `prompt-cards.md`, `agent-failure-modes.md`, `hackathon-challenges.md`, `cheatsheet.md`).

## 2. Verbindliche Arbeitsregeln (Guardrails)

- **Kein Spoilern:** Lies niemals `**/SOLUTION.md` oder `**/*facilitator*`, außer die Person fordert dich explizit dazu auf. Diagnostiziere Fehler immer aus dem Code und den Tests.
- **Read First:** Lies vor jeder Code-Änderung die jeweilige `README.md`, die betroffenen Implementierungsdateien und die Tests.
- **Keine ungefragten Edits:** Wenn ein Prompt nach Analyse, Mapping, PRD, Spec oder Plan fragt, editiere **keine** Dateien.
- **Zero Dependencies in Playgrounds:** Füge in `playground/` niemals externe Pakete (`pip`, `uv`, `npm`) hinzu. Nutze ausschließlich die Python Standard Library (kompatibel ab Python 3.9 mit `from __future__ import annotations`).
- **Tests schützen:** Schwäche oder lösche niemals bestehende Tests in `playground/**/tests/`, um einen Lauf grün zu bekommen.

## 3. Was „Done“ bedeutet

Ein Task gilt erst als abgeschlossen, wenn:
1. Der relevante Testbefehl tatsächlich ausgeführt wurde und die echte Ausgabe vorliegt.
2. Nur Dateien geändert wurden, die zum vereinbarten Scope gehören (`git diff` geprüft).
3. Die Abschlussantwort geänderte Dateien, den ausgeführten Verifikationsbefehl und offene Restrisiken benennt.
