# Workshop: Vom vagen Wunsch zum Agent Contract

## Ziel

Du wandelst einen schlechten Agent-Auftrag in einen robusten Arbeitsauftrag um:
1. Zuerst als schneller 5-Minuten-Fix am kleinen Warm-up (`playground/tiny-issue-tracker`).
2. Danach als **Read-Only Diagnose** am größeren Praxisprojekt (`playground/incident-triage-hub`) — noch **ohne** zu editieren, damit die Bugs für die späteren Module und den Mini-Hackathon erhalten bleiben.

## Dauer

20 bis 25 Minuten.

## Vorbereitung

Vom Repo-Root:

```bash
python3 -m unittest discover -s playground/tiny-issue-tracker/tests
python3 -m unittest discover -s playground/incident-triage-hub/tests -v
```

Die Tests dürfen fehlschlagen. Das ist Arbeitsmaterial.

Öffne zusätzlich das Workbook:

```text
resources/workbook.md
```

Es ist die gemeinsame Arbeitsfläche für Agent Contract, Mini-Spec, Verification Evidence und Handoff.

## Schritt 1: Schlechten Prompt bewusst ausprobieren

Gib deinem Agenten:

```text
Fix the failing tests.
```

Beobachte:

- Fragt der Agent nach dem richtigen Ordner (`tiny-issue-tracker` vs. `incident-triage-hub`)?
- Liest er die Tests zuerst?
- Macht er zu große Änderungen?
- Nennt er den Verifikationsbefehl?

Stoppe den Agenten, wenn er zu viel driftet (und setze versehentliche Edits mit `git checkout -- playground/` zurück).

## Schritt 2: Erster Agent Contract am Warm-up (`tiny-issue-tracker`)

Kopiere und führe aus:

```text
Goal:
Fix the failing test in playground/tiny-issue-tracker.

Context:
Read playground/tiny-issue-tracker/README.md,
playground/tiny-issue-tracker/issue_tracker.py,
and playground/tiny-issue-tracker/tests/test_issue_tracker.py first.

Constraints:
Do not read SOLUTION.md before diagnosing.
Do not change existing tests.
Do not add external dependencies.

Done when:
python3 -m unittest discover -s playground/tiny-issue-tracker/tests passes.

Work style:
Read first. Explain the root cause in two sentences. Then make the smallest fix and report exact verification.
```

## Schritt 3: Read-Only Diagnose am Praxisprojekt (`incident-triage-hub`)

Für das größere Projekt üben wir jetzt das Wichtigste vor jedem Edit: **Read-Only Scouting mit klarem Contract**.

```text
Goal:
Diagnose why 4 tests fail in playground/incident-triage-hub without editing any files yet.

Context:
Read playground/incident-triage-hub/README.md,
playground/incident-triage-hub/triage/models.py,
playground/incident-triage-hub/triage/rules.py,
and playground/incident-triage-hub/tests/test_rules.py.

Constraints:
Do not edit any files yet.
Do not read SOLUTION.md.

Done when:
You list the 3 root causes in triage/rules.py with exact line references and propose the smallest fix for each.
```

## Schritt 4: Mini-Retro

Vergleiche die beiden Läufe:

- Welche Dateien wurden gelesen?
- Wie groß war der Diff?
- Hat der Agent Done-Kriterien beachtet?
- War die Abschlussantwort prüfbar?

## Ergebnis

Du hast einen wiederverwendbaren Task-Prompt für Coding Agents und hast gesehen, warum echte Repos bessere Agentenführung erzwingen als Spielzeug-Code.

Speichere deine beste Version lokal in deinen Notizen oder in `resources/prompt-cards.md`, wenn du den Kurs weiterentwickelst.
