# Incident Triage Hub — Backlog (Spec-Driven Development)

Nutze dieses Backlog für **Modul 05 (Spec-Driven Development)**, **Modul 06 (Plan-Execute-Verify & Orchestration)** und den **Mini-Hackathon**.

**Der SDD-Grundsatz:** Wir schreiben keinen Code auf Zuruf („Vibe Coding“).
Lege für deine gewählte Aufgabe zuerst eine Spec-Datei in [`specs/`](specs/_TEMPLATE.md) an (Vorbild: [`specs/EXAMPLE-near-breach-warning.md`](specs/EXAMPLE-near-breach-warning.md)). Erst wenn Problem, Desired Behavior, Non-goals, Acceptance Criteria und der 3-Schritte-Plan stehen, darf der Agent implementieren.

## Beginner-Aufgaben (15–30 Min)

1. **Bugfix-Sprint:** Alle 4 fehlschlagenden Tests (3 Bugs) in `tests/test_rules.py` per sauberem Agent Contract diagnostizieren und beheben.
2. **Agent Contract fürs Projekt:** Eine kompakte `AGENTS.md` (oder `CLAUDE.md` / `.github/copilot-instructions.md`) speziell für `playground/incident-triage-hub/` schreiben und testen, ob ein neuer Agent-Lauf dadurch schneller und präziser wird.
3. **CSV-Export:** Ein CLI-Subcommand `export-csv` hinzufügen, das offene priorisierte Incidents als CSV auf stdout ausgibt (inkl. Unit-Test).

## Intermediate-Aufgaben (30–60 Min)

4. **On-Call Handover Report:** Ein neues Subcommand `handover --owner team-billing` (oder optional ohne Owner), das einen strukturierten Schichtübergabe-Report in Markdown erzeugt (offene Incidents des Teams, SLA-Risiken, ältestes Ticket, leere Bereiche klar benannt).
5. **Eskalations-Warnung („Near Breach“):** Incidents, die bereits ≥ 80 % ihrer SLA-Zeit verbraucht haben, aber noch kein Breach sind, als `at_risk` markieren — in `rules.py`, `summary`, Markdown-Report und Web-UI (inkl. Tests für Grenzfälle wie exakt 80 % und 100 %).
6. **Web-UI erweitern:** In `triage/server.py` einen Filter für `severity` und `open_only` ergänzen, plus einen kleinen Smoke-Test gegen den HTTP-Handler (ohne Browser-Abhängigkeiten).
7. **Alert-Ingest mit Deduplizierung:** Eine Funktion `ingest_incident(existing, new_incident)` bauen, die doppelte offene Incidents für denselben `service` + ähnlichen `title` erkennt, statt Duplikate anzulegen.

## Cross-Functional Aufgaben (QA, PM, DevOps, Data)

8. **QA — Edge-Case & Test-Audit:** Den Agenten im Read-Only-Modus nach fehlenden Testfällen suchen lassen (leere JSON-Liste, ungültige Severity, negative `age_minutes`, XSS-Sonderzeichen in der HTML-UI, fehlende Felder), eine Testmatrix als Spec erstellen und 5 neue Regressionstests umsetzen.
9. **PM / Ops — PRD & Prototyp:** Eine PRD + Mini-Spec für ein „Executive Status Digest“-Feature schreiben (Zielgruppe: Management/Stakeholder, Non-goals, KPIs, Beispiel-Output) und als erste kleine Slice umsetzen lassen.
10. **DevOps / Team — Wiederverwendbare Skill:** Eine eigene `SKILL.md` (z.B. `incident-postmortem-draft` oder `triage-briefing`) schreiben, die aus dem Output von `cli.py report` ein standardisiertes Postmortem-Template oder Slack-Update generiert.
