# Workshop: SDD Execution Loop — Von der Spec zum verifizierten Code

## Ziel

Du nimmst deine freigegebene Spec-Datei aus [Modul 05](../05-spec-driven-development/workshop.md) und führst deinen Agenten kontrolliert durch **Plan Lock -> Execute -> Independent Spec-Audit**.

## Dauer

25 bis 30 Minuten.

---

## Track A: Brownfield SDD Execution (`incident-triage-hub`)

Voraussetzung: Du hast eine Spec-Datei in `playground/incident-triage-hub/specs/` (entweder deine eigene aus Modul 05 oder das fertige Beispiel [`specs/EXAMPLE-near-breach-warning.md`](../../playground/incident-triage-hub/specs/EXAMPLE-near-breach-warning.md)).

### Schritt 1: Plan & Scope Lock (Plan Mode nutzen!)

Schalte deinen Harness nach Möglichkeit in den **Plan Mode** (oder nutze den Read-Only-Zusatz unten). Der Agent soll die Spec lesen, höchstens **eine** echte Blocker-Frage stellen und den konkreten Änderungsplan locken:

```text
Read playground/incident-triage-hub/specs/<deine-spec-datei>.md and the referenced code files.
Do not edit any files yet.

1. If anything in the spec is ambiguous or blocking, ask at most ONE question. Otherwise state "No blocker".
2. Propose a locked execution plan (max 3 steps):
   - exact files to modify
   - files that must NOT be modified
   - exact tests to add or run
   - done criteria

Wait for my confirmation before editing.
```

Prüfe den Plan kurz: Will der Agent unnötige Dateien anfassen oder die Spec ausweiten? Wenn alles passt, gib grünes Licht:

```text
Approved. Execute only the locked plan and run the verification command.
```

### Schritt 2: Execute & Halt (Implementierung mit Beweis)

Lass den Agenten den gelockten Plan umsetzen. Achte darauf, dass er nach dem Ausführen des Testbefehls (`python3 -m unittest discover -s playground/incident-triage-hub/tests -v`) stoppt und nicht ungefragt das nächste Feature anfängt.

Falls er direkt einen vollständigen Execute-Prompt braucht:

```text
Execute the approved plan from playground/incident-triage-hub/specs/<deine-spec-datei>.md:
- Implement only what is required by the Acceptance Criteria.
- Respect all Non-Goals.
- Run: python3 -m unittest discover -s playground/incident-triage-hub/tests -v
- Stop immediately after verification and report changed files, exact test output, and any remaining risks.
```

### Schritt 3: Unabhängiges Spec-Audit (Reviewer-Rolle / Subagent)

Jetzt kommt der stärkste SDD-Trick: Lass denselben Stand von einer **skeptischen Reviewer-Rolle** (gerne als Subagent oder in einem neuen Chat-Tab!) streng gegen deine Spec-Datei prüfen:

```text
Act as a skeptical code reviewer. Do not edit any files.
Compare the current git diff and test status in playground/incident-triage-hub against playground/incident-triage-hub/specs/<deine-spec-datei>.md.

Check and report:
1. Are all Acceptance Criteria genuinely covered by tests?
2. Were any Non-Goals violated or unrelated lines changed?
3. Were any existing tests weakened?
4. What edge cases or residual risks remain?
Lead with concrete findings, not praise.
```

---

## Track B: Greenfield SDD Execution (`Puzzle Game Slice`)

Wenn du in Modul 05 die Greenfield-Puzzle-Spec geschrieben hast:

1. **Plan & Lock:** Lass den Agenten aus deiner Puzzle-Spec nur die **allererste spielbare Slice** (reine Spiellogik getrennt von UI, deterministischer Seed, 1 Losing Condition, 1 Restart-Flow) als 3-Schritte-Plan locken.
2. **Execute:** Lass ihn nur diese erste Slice inkl. Unit-Tests für Generator, Züge und Losing Condition implementieren.
3. **Verify against Spec:** Prüfe mit dem Reviewer-Prompt oben, ob die Spielregeln wirklich ohne DOM/UI unit-getestet sind und alle Non-Goals eingehalten wurden.

## Ergebnis

Du hast erlebt, wie **Spec-Driven Development + Phasen-Orchestrierung** zusammenwirken:
- Die **Spec-Datei im Repo** verhindert Missverständnisse vor der ersten Code-Zeile.
- Der **Plan Lock** verhindert Scope Creep.
- Das **Spec-Audit** am Ende deckt Lücken auf, die in einer normalen Chat-Zusammenfassung untergehen würden.
