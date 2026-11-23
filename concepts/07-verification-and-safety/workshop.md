# Workshop: Abschluss-Audit für Agentenarbeit

## Ziel

Du lernst, eine Agent-Änderung nicht nur anzunehmen, sondern gegen Auftrag, Diff und Tests zu prüfen.

Nutze bei auffälligem Verhalten zusätzlich den [Failure Modes Catalog](../../resources/agent-failure-modes.md), um das Problem zu benennen und den Lauf zu korrigieren.

## Dauer

20 bis 25 Minuten.

## Schritt 1: Diff anzeigen

Nach einer Agent-Änderung:

```bash
git diff
```

Frage:

- Sind nur erwartete Dateien geändert?
- Ist die Änderung kleiner als gedacht?
- Gibt es neue Dependencies?
- Hat der Agent Tests angepasst, statt Verhalten zu fixen?

## Schritt 2: Tests ausführen

Für das lokale Praxisprojekt (`incident-triage-hub`):

```bash
python3 -m unittest discover -s playground/incident-triage-hub/tests -v
```

*(Oder für das Warm-up: `python3 -m unittest discover -s playground/tiny-issue-tracker/tests`.)*

Wenn der Agent sagt "tests pass", aber du keinen Output gesehen hast, zählt es nicht.

## Schritt 3: Agenten-Self-Review erzwingen

```text
Review your own diff as if you were blocking a risky PR.
Lead with findings.
Check:
- behavior vs original request
- unrelated changes
- missing tests
- edge cases
- security or data risks
If no issues, say that clearly and name residual risk.
```

## Schritt 4: Menschliche Entscheidung

Entscheide:

```text
Ship:
  evidence is enough

Revise:
  small issue remains

Rollback:
  wrong direction or too much unrelated change

Ask:
  requirement unclear
```

## Schritt 5: Abschlussnotiz

Schreibe:

```text
Changed:
Verified:
Not verified:
Would improve next:
```

## Ergebnis

Du hast eine Agent-Änderung wie Engineering behandelt: mit Diff, Test, Review und Restrisiko.
