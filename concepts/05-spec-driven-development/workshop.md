# Workshop: Spec-Driven Development (SDD) in der Praxis

## Ziel

Du erstellst mit deinem Agenten eine **repo-lokale Spec-Datei** (`specs/*.md`), schärfst Non-Goals und Edge Cases, und gibst den Plan frei — bevor eine einzige Zeile Produktivcode geändert wird.

Wähle **einen** der beiden Tracks:
- **Track A (Empfohlen — Brownfield am `incident-triage-hub`):** Spec für den Bugfix-Sprint oder für ein neues Feature aus [`BACKLOG.md`](../../playground/incident-triage-hub/BACKLOG.md).
- **Track B (Greenfield Puzzle Game):** PRD, Mechanics Spec und erste Slice für ein neues Web-Puzzle-Spiel.

## Dauer

25 bis 30 Minuten.

---

## Track A: Brownfield SDD am `incident-triage-hub`

### Schritt 1: Vorbild & Template anschauen (2 Min)

Wirf einen kurzen Blick auf:
- [playground/incident-triage-hub/specs/_TEMPLATE.md](../../playground/incident-triage-hub/specs/_TEMPLATE.md)
- [playground/incident-triage-hub/specs/EXAMPLE-near-breach-warning.md](../../playground/incident-triage-hub/specs/EXAMPLE-near-breach-warning.md)

Beachte: Die Spec beschreibt **beobachtbares Verhalten, Non-Goals, Edge Cases und den 3-Schritte-Plan**, nicht schon den fertigen Python-Code.

### Schritt 2: Spec-Datei vom Agenten entwerfen lassen (Explore -> Specify)

Wähle dein Ziel:
- **Für Beginner:** Die 3 Bugs (4 fehlschlagenden Tests) in `tests/test_rules.py` spezifizieren (`specs/001-fix-core-rules.md`).
- **Für Intermediate / PM / QA:** Ein neues Feature oder Test-Audit aus [`BACKLOG.md`](../../playground/incident-triage-hub/BACKLOG.md) spezifizieren (z.B. `specs/002-handover-report.md` oder `specs/002-csv-export.md`).

Gib deinem Agenten diesen Prompt:

```text
We are using Spec-Driven Development (SDD).
Do not edit any production code or test files yet.

1. Explore: Read playground/incident-triage-hub/README.md, triage/models.py, triage/rules.py, tests/test_rules.py, and specs/_TEMPLATE.md.
2. Specify: Create a concise spec file at playground/incident-triage-hub/specs/001-my-spec.md following specs/_TEMPLATE.md for:
   <Dein Ziel: z.B. "fixing the 4 failing tests in tests/test_rules.py" ODER "Backlog item #4: On-Call Handover Report">

Keep it under 250 words. Stop after writing the spec file so I can review it.
```

### Schritt 3: Menschliches Spec-Review (Der wichtigste SDD-Moment!)

Lies die erzeugte Datei `playground/incident-triage-hub/specs/001-my-spec.md` kritisch durch:

- **Verhalten statt Wunschdenken:** Sind die Acceptance Criteria konkret testbar?
- **Non-Goals scharf genug?** Steht klar drin, was *nicht* geändert werden darf (keine neuen Dependencies, keine Änderung an unbeteiligten Dateien)?
- **Edge Cases bedacht?** (z.B. leere Liste, unbekannte Severity, Groß-/Kleinschreibung, `resolved` vs. `open`?)
- **Plan Lock realistisch?** Nennt der 3-Schritte-Plan die exakten Dateien?

Wenn etwas zu vage oder zu aufgebläht ist, lass den Agenten die Spec schärfen (oder editiere die Markdown-Datei direkt selbst!):

```text
Update playground/incident-triage-hub/specs/001-my-spec.md:
- Remove any scope not strictly required.
- Add an explicit edge case for <dein Edge Case>.
- Set Status to Approved.
Do not edit production code yet.
```

---

## Track B: Greenfield SDD (`Greenfield Puzzle Game`)

Nutze [../../resources/greenfield-puzzle-game.md](../../resources/greenfield-puzzle-game.md), wenn du SDD ohne bestehende Codebase üben möchtest:

1. **Konzeptoptionen:** Lass den Agenten 3 unterschiedliche Spielmechaniken vorschlagen (ohne Code!) und wähle eine aus.
2. **PRD & Mechanics Spec als Datei speichern:** Lass den Agenten `playground/puzzle-spec.md` mit Core Loop, Board/State-Modell, Losing Condition, deterministischem Seed-Modus und expliziten Non-Goals anlegen.
3. **Erste Slice & Testvertrag locken:** Definiere in derselben Spec-Datei die kleinste spielbare und testbare erste Scheibe.

Review-Frage für beide Tracks:

> „Könnte jetzt ein anderer Agent (oder ein Teammitglied) in einer frischen Session allein mit dieser Spec-Datei genau das Richtige bauen?“

Wenn ja: Deine Spec ist bereit für **Modul 06 (Plan-Execute-Verify & Orchestration)**!
