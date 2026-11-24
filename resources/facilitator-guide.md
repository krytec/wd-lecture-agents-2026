# Facilitator Guide

Dies ist der Spickzettel für die Person vorne im Raum.

## Didaktischer Kern

Die Session soll sich nicht anfühlen wie "Tool X kann Feature Y". Sie soll sich anfühlen wie:

> Ich kann einen Agenten so führen, dass aus unklarer Absicht ein prüfbarer Arbeitsstand wird.

Jedes Modul hat deshalb denselben Rhythmus:

1. Kurztheorie: 5 bis 7 Minuten.
2. Live-Demo oder Beispiel: 3 bis 5 Minuten.
3. Hands-on: 15 bis 25 Minuten.
4. Mini-Retro: 2 Minuten. Was hat den Agenten besser gemacht?

## Setup vor der Veranstaltung

- Schicke Teilnehmenden 1–2 Tage vorher den Link zu [setup-and-preflight.md](setup-and-preflight.md) mit dem Befehl `python3 scripts/preflight.py`.
- Stelle sicher, dass mindestens ein Agent-Harness verfügbar ist (GitHub Copilot, Claude Code, Codex, Cursor, Windsurf, Gemini CLI / Antigravity).
- Öffne das [Workbook](workbook.md) als gemeinsame Arbeitsfläche und [hackathon-challenges.md](hackathon-challenges.md) für den Praxis-Sprint.
- Halte den [Agent Failure Modes Catalog](agent-failure-modes.md) griffbereit, um schlechte Agentenläufe sofort zu benennen und zu korrigieren.
- Prüfe selbst einmal lokal:

```bash
python3 scripts/preflight.py
```

Beide lokalen Playgrounds (`tiny-issue-tracker` und `incident-triage-hub`) laufen **100 % offline ohne externe Pakete**. Ihre Tests sind am Anfang absichtlich rot — das sind die Übungsfälle.

Halte für schnelle Teams oder Vertiefung optional bereit:

```text
resources/greenfield-puzzle-game.md
resources/greenfield-facilitator-notes.md
resources/superpowers-hands-on.md
resources/openspec-hands-on.md
resources/workflow-comparison-lab.md
```

Der Greenfield-Track braucht kein vorbereitetes Repo. Teilnehmende können in einem leeren Ordner arbeiten. Wichtig ist: erst PRD und Mechanics Spec, dann eine kleine Slice.

### Didaktische Staffelung der Playgrounds über den Workshop
Damit Teilnehmende nicht schon in Modul 01 die Bugs des Hauptprojekts wegfixen, sind die Übungen bewusst gestaffelt:
1. **Modul 01 (Mindset):** Kurzer Bugfix am `playground/tiny-issue-tracker` (5–10 Min) + erste **Read-Only** Diagnose am `playground/incident-triage-hub`.
2. **Modul 02–04 (Context, MCP, Skills):** `AGENTS.md` entwerfen und `repo-cartographer` (Read-Only Mapping!) auf `playground/incident-triage-hub` anwenden — **noch ohne Edits**.
3. **Modul 05–07 & Mini-Hackathon:** Erst jetzt wird `playground/incident-triage-hub` nach dem **Spec-Driven Development (SDD)**-Prinzip verändert (zuerst Spec-Datei in `specs/*.md` anlegen, Planen, dann Track A Bugfix oder Track B/C Feature/Test-Suite aus `BACKLOG.md` umsetzen; Track D: `Greenfield Puzzle Game`).
4. **Schneller Reset jederzeit möglich:** `git checkout -- playground/` setzt beide Playgrounds sofort in den Startzustand zurück.

Optional für die Industrie-Workflow-Labs:

```bash
node --version
npm view @fission-ai/openspec version engines --json
```

Wenn du Superpowers live installierst, nutze den jeweiligen Harness-Installationsweg statt Shell-Magie:

- Claude Code: `/plugin install superpowers@claude-plugins-official`
- Codex: `/plugins` öffnen, nach `superpowers` suchen und installieren
- Gemini CLI: `gemini extensions install https://github.com/obra/superpowers`

Wichtig: Die Labs gehören in eine Kopie, einen Fork oder ein Worktree. OpenSpec erzeugt `openspec/` Artefakte im Projekt; Superpowers verändert das Agentenverhalten für den jeweiligen Harness.

## Live-Demo-Ideen

### Demo 1: Schlechter Prompt vs Agent Contract

Schlecht:

```text
Fix the app.
```

Besser:

```text
Goal: Diagnose and fix the failing tests in playground/incident-triage-hub.
Context: Start by reading playground/incident-triage-hub/README.md, triage/models.py, triage/rules.py, and tests/test_rules.py.
Constraints: Do not read SOLUTION.md. Do not change existing tests. Keep changes scoped to triage/rules.py.
Done when: python3 -m unittest discover -s playground/incident-triage-hub/tests -v passes and you summarize the changed behavior.
```

Der Effekt ist sofort sichtbar: Der Agent exploriert gezielter, macht kleinere Diffs und erklärt besser.

### Demo 2: Skill als Methodentransfer

Zeige [examples/skills/repo-cartographer/SKILL.md](../examples/skills/repo-cartographer/SKILL.md). Frage:

> Ist das "nur Prompting", oder ist das schon ein kleines Stück Team-Wissen?

Die Aha-Antwort: Es ist Team-Wissen als portable, agent-native Verpackung.

### Demo 3: Der SDD Execution Loop (Plan Mode & Spec-Datei)

An die Tafel:

```text
Explore -> Specify (specs/*.md) -> Plan -> Execute -> Verify gegen Spec
```

Dann mit einem Agenten live anwenden (oder an [`playground/incident-triage-hub/specs/EXAMPLE-near-breach-warning.md`](../playground/incident-triage-hub/specs/EXAMPLE-near-breach-warning.md) zeigen):

- **Explore & Specify:** Relevante Dateien lesen lassen und eine 25-zeilige Spec-Datei in `specs/` anlegen (45 Sekunden menschliches Review statt 30 Minuten Code-Review!).
- **Plan:** Im Plan Mode max. 3 Schritte + betroffene Dateien festlegen und abnicken.
- **Execute:** Nur die freigegebene Slice bauen und Tests ausführen.
- **Verify:** In einer zweiten Rolle (Reviewer / Subagent) `git diff` streng gegen die Spec-Datei prüfen.

### Demo 4: Greenfield vs Brownfield

Zeige die zwei Arbeitsarten nebeneinander:

```text
Greenfield Puzzle:
Erst PRD -> Mechanics Spec -> Testplan -> Slice -> Code

Brownfield Incident Triage Hub:
Erst Repo lesen -> Failure verstehen -> Scope locken -> Fix/Feature -> Beweis
```

Die Aha-Antwort: Greenfield braucht mehr explizite Produktform, Brownfield braucht mehr Respekt vor bestehender Form.

### Demo 5: Prompt-Disziplin vs installiertes Workflow-System

Zeige die manuelle Prompt-Karte aus Modul 05 und dann zwei aktuelle Werkzeuge:

```text
Superpowers:
Skill-Bündel erzwingt Methodik im Agenten.

OpenSpec:
Repo-Artefakte halten Proposal, Spec-Deltas, Design und Tasks fest.
```

Leitsatz:

> Man kann eine eigene Spec-driven-Development-Skill bauen. Im Workshop schauen wir uns bewusst zwei lebendige Standards an, damit Teilnehmende echte Arbeitsflächen sehen.

### Demo 6: Drei Wege, ein Change

Wenn genug Zeit ist, nutze [workflow-comparison-lab.md](workflow-comparison-lab.md):

```text
Manual:
Prompt-Karten und menschliche Gate-Kontrolle.

Superpowers:
Methodik als installiertes Agentenverhalten.

OpenSpec:
Spec und Tasks als repo-lokale Artefakte.
```

Die Aha-Antwort: Der beste Workflow hängt an Risiko, Teamgröße und Reviewbedarf, nicht am Tool-Namen.

## Zeitmanagement & Format-Varianten

### Variante 1: Standard-Halbtag (3,5–4h inkl. Mini-Hackathon)
- Erste Hälfte (ca. 2h15 inkl. Pause): Module 01–07 kompakt mit kurzen Live-Demos und `tiny-issue-tracker` als Warm-up.
- Zweite Hälfte (ca. 1h30): 60 Min Mini-Hackathon-Sprint ([hackathon-challenges.md](hackathon-challenges.md)) auf dem `incident-triage-hub` (Tracks A–D) + 25 Min Show & Tell + 10 Min Wrap-up.

### Variante 2: Kompakt-Workshop (3h)
- Modul 03 (MCP) und Modul 04 (Skills) auf 15 Min Kurz-Überblick komprimieren.
- Fokus auf Modul 01 (Agent Contract), 02 (`AGENTS.md`), 05 (Mini-Spec), 07 (Verification & Safety).
- 45 Min Praxis-Sprint + 15 Min Show & Tell.

### Anpassung nach Gruppe
Wenn die Gruppe überwiegend Beginner oder gemischt (inkl. PM/QA/Ops) ist:

- Modul 03 MCP kurz halten (konzeptuell statt Live-Server-Setup)
- Beim Sprint aktiv auf **Track A** (Bugfix) und **Track C** (QA / PM / Skill) verweisen
- Mehr Zeit für Modul 02 (`AGENTS.md`) und 07 (Verification & Datenschutz/Secrets) geben

Wenn die Gruppe überwiegend erfahren (Intermediate Engineers) ist:

- Modul 04 eigene Skill bauen lassen
- Im Sprint **Track B** (Feature aus `BACKLOG.md` mit Spec-Datei + SDD Execution Loop) oder **Track D** (`Greenfield Puzzle Game`) empfehlen
- Optional das dreiteilige Workflow Comparison Lab (Manual vs. Superpowers vs. OpenSpec) antesten
- Zwei parallele Agent-Rollen (Investigator / Builder / Reviewer) nutzen lassen

## Moderationssätze

- "Der Agent ist schnell. Wir müssen langsam genug sein, dass er nicht in die falsche Richtung schnell wird."
- "Wenn ihr den Prompt nicht reviewen könnt, könnt ihr den Output auch nicht gut reviewen."
- "MCP gibt Hände. Skills geben Gewohnheiten. Specs geben Richtung. Reviews geben Bremsen."
- "Wir wollen keine perfekten Prompts. Wir wollen robuste Arbeitsabläufe."
- "Ein-Datei-Snippets zeigen, dass Agents Code schreiben können. Multi-File-Projekte zeigen, ob wir Agents führen können."
- "Greenfield braucht Spec, weil noch keine Codebase widerspricht."
- "Wenn wir den Fehler benennen können, können wir ihn stoppen."
- "Manual, Superpowers und OpenSpec sind keine Religionen. Sie sind unterschiedliche Reibungsprofile."

## Abschlussfrage

Jede Person schreibt am Ende eine persönliche Regel:

```text
Ab morgen gebe ich meinem Coding Agent immer ...
```

Beispiele:

- "Done when" Kriterien.
- Den Testbefehl.
- Eine explizite Nicht-Anforderung.
- Den Auftrag, vor dem Editieren kurz den Plan zu zeigen.
