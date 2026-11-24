# Mini-Hackathon Challenges & Show-and-Tell

Dieser Guide strukturiert den **Praxis-Sprint (45–75 Minuten)** am Ende des Halbtags-Workshops (oder als verlängerter Nachmittags-Hackathon).

Das Ziel ist **nicht**, in 60 Minuten möglichst viel Code zu generieren. Das Ziel ist zu zeigen, wie gut du einen Agenten **führst, begrenzt und verifizierst**.

## Wähle deinen Track

Du kannst alleine oder im Duo (Driver + Navigator) arbeiten. Wähle den Track, der zu deiner Erfahrung und Rolle passt:

### Track A — Beginner: Bugfix & Agent Contract (empfohlen für Einsteiger)
- **Arbeitsfläche:** [playground/incident-triage-hub/](../playground/incident-triage-hub/README.md)
- **Aufgabe:**
  1. Führe die Tests aus (`python3 -m unittest discover -s playground/incident-triage-hub/tests -v`) und analysiere die Fehler **ohne** `SOLUTION.md` zu lesen.
  2. Nutze [workbook.md](workbook.md) (Abschnitte 2, 3, 7, 8) für einen sauberen Agent Contract und eine Read-Only Map.
  3. Behebe die 3 Bugs in `triage/rules.py`, ohne die bestehenden Tests abzuschwächen.
  4. **Bonus:** Schreibe eine kurze `AGENTS.md` für `playground/incident-triage-hub/` mit Projektregeln und Testbefehl.
- **Done when:** Alle 9 Tests grün, kleiner sauberer `git diff`, kurzes Handoff ausgefüllt.

### Track B — Intermediate: Spec-Driven Feature-Sprint (SDD)
- **Arbeitsfläche:** [playground/incident-triage-hub/](../playground/incident-triage-hub/README.md) (siehe [BACKLOG.md](../playground/incident-triage-hub/BACKLOG.md) & Vorbild [specs/EXAMPLE-near-breach-warning.md](../playground/incident-triage-hub/specs/EXAMPLE-near-breach-warning.md))
- **Aufgabe:**
  1. Wähle **ein** Intermediate-Feature aus `BACKLOG.md` (z.B. *On-Call Handover Report*, *Near-Breach-Eskalation bei 80 % SLA*, *Web-UI-Filter* oder *Alert-Deduplizierung*).
  2. **Specify:** Erstelle zuerst eine Spec-Datei `playground/incident-triage-hub/specs/002-<feature>.md` nach [`specs/_TEMPLATE.md`](../playground/incident-triage-hub/specs/_TEMPLATE.md) (Problem, Desired Behavior, Non-Goals, Acceptance Criteria, 3-Schritte-Plan, Verification Command) und reviewe sie.
  3. **Plan & Execute:** Setze das Feature nach dem **SDD Execution Loop** (`Explore -> Specify -> Plan -> Execute -> Verify`) inkl. neuer Unit-Tests um.
  4. **Verify:** Lass einen Reviewer-Prompt (oder Subagent) den `git diff` gegen deine Spec-Datei prüfen und teste CLI oder Web-UI (`cli.py serve`).
- **Done when:** Spec-Datei liegt im Repo, neue + alte Tests laufen grün, Spec-Audit zeigt keine Verletzung der Non-Goals.

### Track C — Cross-Functional: QA, PM, DevOps & Data
Ideal für Teilnehmende, die nicht den ganzen Tag Produktivcode schreiben — aber täglich mit Specs, Tests, Reports oder Team-Workflows arbeiten:

- **Option C1 (QA / Testing):** Lass den Agenten `incident-triage-hub` im Read-Only-Modus auf Test-Lücken und Edge-Cases prüfen (leere Daten, ungültige Inputs, HTML-Escaping/XSS, Grenzfälle). Erstelle eine kompakte Test-Spec in `specs/002-edge-case-audit.md` und ergänze 5 echte Regressionstests.
- **Option C2 (PM / Produkt / Ops):** Schreibe mithilfe des Agenten eine saubere Spec-Datei (`specs/002-executive-digest.md`) oder PRD + Mechanics Spec für das [Greenfield Puzzle Game](greenfield-puzzle-game.md) — inklusive Non-Goals und Acceptance Criteria — und lass eine erste kleine, lokal prüfbare Slice bauen.
- **Option C3 (DevOps / Team-Enablement):** Baue eine eigene, wiederverwendbare **Agent Skill** (`SKILL.md`, siehe [examples/skills/repo-cartographer](../examples/skills/repo-cartographer/SKILL.md)) für einen echten Workflow aus deinem Alltag (z.B. *Incident-Postmortem-Draft*, *SDD-Spec-Generator*, *PR-Review-Checkliste*) und teste sie am Projekt.

### Track D — Fast Teams / Advanced: Greenfield SDD Puzzle Slice
- **Arbeitsfläche:** [Greenfield Puzzle Game](greenfield-puzzle-game.md) (in einem neuen Unterordner, z.B. `playground/puzzle-slice/`)
- **Aufgabe:** Spezifiziere PRD, Mechanics Spec und Testvertrag als Markdown-Spec für ein minimalistisches Web-Puzzle-Spiel und baue die erste deterministisch testbare, im Browser spielbare Slice über den SDD Execution Loop (`Specify -> Plan -> Execute -> Verify`).

> **Tipp:** Falls du während der vorherigen Workshop-Module schon Dateien im Playground verändert hast, kannst du jederzeit mit `git checkout -- playground/` sauber auf den Startzustand zurücksetzen.

---

## Show-and-Tell Format (3 Minuten pro Team/Person)

Am Ende stellt jedes Team kurz vor — Fokus liegt auf dem **Prozess**, nicht auf einer Hochglanz-Demo:

1. **Auftrag & Track (30 Sek.):** Was war das Ziel und was war das wichtigste *Non-goal*?
2. **Aha-Moment oder gestoppter Fehler (60 Sek.):** Wo wollte der Agent abdriften (siehe [agent-failure-modes.md](agent-failure-modes.md)) und wie hast du ihn eingefangen?
3. **Beweis (60 Sek.):** Kurzer Blick auf Testausgabe, `git diff` oder Demo (UI/CLI/Skill).
4. **Takeaway (30 Sek.):** Welche Regel nimmst du morgen mit in deinen Arbeitsalltag?

## Bewertungs- / Feedback-Rubrik (Agent Leadership)

Wenn ihr den Sprint als kleinen Hackathon mit Voting oder Feedback-Runde spielt, bewertet diese 4 Dimensionen (je 1–5 Punkte):

| Dimension | Woran erkennt man starke Agentenführung? |
| --- | --- |
| **1. Auftrag & Spec** | Klares Ziel, konkrete Dateien/Kontext, explizite Non-goals statt vagem Wunsch. |
| **2. Steuerung & Disziplin** | Read-first, Plan-Freigabe eingehalten, Scope Creep oder vorschnelle Edits aktiv gestoppt. |
| **3. Verifikation & Ehrlichkeit** | Echte Test-/CLI-/UI-Beweise statt „looks good“, sauberer kleiner Diff, Restrisiken benannt. |
| **4. Praxisnutzen / Reuse** | Ergebnis oder Artefakt (`AGENTS.md`, `SKILL.md`, Spec, Tests) ist direkt im Team weiterverwendbar. |
