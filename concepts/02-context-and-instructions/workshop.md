# Workshop: Baue ein kleines Agent Contract File

## Ziel

Du formulierst dauerhafte Repo-Regeln, die ein Agent wirklich nutzen kann.

## Dauer

25 bis 30 Minuten.

## Schritt 1: Reibung sammeln

Notiere drei Dinge, die Coding Agents in Projekten oft falsch machen.

Beispiele:

- Sie editieren zu viele Dateien.
- Sie vergessen Tests.
- Sie installieren Dependencies ohne Grund.
- Sie ignorieren vorhandene Patterns.
- Sie erklären viel, aber liefern keinen Beweis.

## Schritt 2: Regeln operationalisieren

Wandle jede Reibung in eine prüfbare Regel um.

Schlecht:

```text
Be careful with tests.
```

Besser:

```text
Before saying done, run the narrowest relevant test command.
If tests cannot run, report the exact blocker.
```

## Schritt 3: Mini-AGENTS.md schreiben

Erstelle in einer Scratch-Datei oder direkt im Prompt:

```markdown
# Agent Instructions

## Project Shape

- This task runs in `playground/incident-triage-hub/`.
- Zero external dependencies (Python 3.9+ Standard Library only).
- Business rules live in `triage/rules.py`; data model in `triage/models.py`.

## Work Rules

- Read `README.md`, `triage/models.py`, `triage/rules.py`, and `tests/test_rules.py` before editing.
- Keep changes scoped to `triage/rules.py` unless a spec requires otherwise.
- Do not read `SOLUTION.md` before diagnosing.
- Do not add dependencies or weaken existing tests.
- Before saying done, run:
  `python3 -m unittest discover -s playground/incident-triage-hub/tests -v`

## Done Means

- All tests pass, or the exact blocker is reported.
- The final answer names changed files and verification evidence.
```

Vergleiche deinen Entwurf auch mit der [AGENTS.md](../../AGENTS.md) im Repo-Root.

## Schritt 4: Agent damit arbeiten lassen (Read-Only Plan-Test)

Gib deinem Agenten zuerst die Instruktionen, dann den Auftrag (noch als Plan ohne Datei-Edits, damit wir das Projekt in Modul 05/06 bzw. im Mini-Hackathon mit Spec umsetzen können):

```text
Use the following agent instructions for this task:

<paste mini instructions>

Task: Read the relevant files in playground/incident-triage-hub and propose a 3-step plan to fix the failing tests. Do not edit files yet.
```

## Schritt 5: Scope-Check

Frage den Agenten nach Abschluss:

```text
Audit your own work against the agent instructions. Which rules did you follow, and what remains unverified?
```

## Ergebnis

Du hast eine erste Version eines Repo-Agent-Contracts und ein Gefühl dafür, welche Regeln wirklich helfen.
