# 05 Spec-Driven Development (SDD)

## One-liner

Spec-Driven Development (SDD) dreht die Arbeitsrichtung mit AI Agents um: **Nicht der Code ist die erste Wahrheit, sondern eine prüfbare Spec im Repo.**

## Warum SDD mit Coding Agents der größte Hebel ist

Agenten sind schnell genug, um vage Ideen in Sekunden in 400 Zeilen Code zu verwandeln („Vibe Coding“).
Das Problem: **400 Zeilen generierten Code zu reviewen dauert 30 Minuten — eine 25-zeilige Spec zu reviewen dauert 45 Sekunden.**

Ohne SDD passiert fast immer:

```text
Vage Idee -> Agent generiert viel Code -> Mensch entdeckt Missverständnis -> Patch auf Patch (Drift)
```

Mit SDD arbeitet das Team in einer klaren Kette:

```text
Explore -> Specify (Datei im Repo) -> Plan Lock -> Execute -> Verify gegen Spec
```

Das ist kein bürokratischer Papierkram, sondern **Drift-Kontrolle** und die gemeinsame Sprache zwischen **Engineering, QA, DevOps und Produkt/PM**.

## Warum die Spec als Datei ins Repo gehört (nicht nur in den Chat)

Ein häufiger Anfängerfehler ist, Specs nur im Chat-Verlauf zu diskutieren. In echtem SDD lebt die Spec als Markdown-Datei im Projekt (z.B. `playground/incident-triage-hub/specs/001-my-change.md`):

1. **Kein Gedächtnisverlust:** Chat-Kontexte laufen voll oder werden komprimiert — eine Datei im Repo bleibt präzise und jederzeit nachlesbar.
2. **Handoff an Subagents & Teamkollegen:** Ein zweiter Agent (z.B. Reviewer oder Tester) oder eine Kollegin kann die Spec-Datei direkt lesen, ohne deinen Chat-Verlauf zu kennen.
3. **Gemeinsame Arbeitsfläche für alle Rollen:**
   - **PM / Produkt / Ops** schärft *Problem, Desired Behavior & Non-Goals*.
   - **QA** prüft und ergänzt *Acceptance Criteria & Edge Cases*.
   - **Engineering / DevOps** prüft den *3-Schritte-Plan & Verification Command* und lässt den Agenten die Änderung umsetzen.

## Was eine gute SDD-Spec enthält

Siehe unsere Vorlage [playground/incident-triage-hub/specs/_TEMPLATE.md](../../playground/incident-triage-hub/specs/_TEMPLATE.md) und das ausgefüllte Beispiel [EXAMPLE-near-breach-warning.md](../../playground/incident-triage-hub/specs/EXAMPLE-near-breach-warning.md):

1. **Problem & Current Behavior:** Was passiert aktuell im Code?
2. **Desired Behavior:** Welches beobachtbare Verhalten wollen wir stattdessen?
3. **Explicit Non-Goals:** Was lassen wir bewusst weg? (Der wichtigste Schutz gegen Scope Creep!)
4. **Acceptance Criteria & Edge Cases:** Konkrete, testbare Bedingungen (inkl. Grenzfälle).
5. **Implementation Plan (Plan Lock):** Max. 3 Schritte + welche Dateien geändert werden (und welche *nicht*).
6. **Verification Command(s):** Exakter Befehl, der den Erfolg beweist.

Im Workshop unterscheiden wir zwei SDD-Szenarien:

- **Brownfield SDD (`incident-triage-hub`):** Die Spec begrenzt eine Änderung in einer bestehenden Codebase (Bugfix oder Feature aus `BACKLOG.md`), schützt bestehende Schnittstellen und definiert gezielte Tests.
- **Greenfield SDD (`greenfield-puzzle-game`):** Es gibt noch keinen Code. Die Spec erschafft erst die Produktform (PRD -> Mechanics Spec -> Testvertrag -> erste kleine Slice).

## Von leichtgewichtig bis Tool-gestützt

SDD lässt sich in drei Reifegraden betreiben:

```text
Stufe 1: Repo-lokale Spec-Dateien (specs/_TEMPLATE.md)  -> Sofort in jedem Harness nutzbar, 0 Setup
Stufe 2: Methodik-Skills (z.B. Superpowers)             -> Erzwingt Spec -> Plan -> TDD als Agent-Gewohnheit
Stufe 3: Dediziertes Spec-CLI (z.B. OpenSpec / Spec Kit) -> Verwaltet Proposals, Spec-Deltas und Task-Archive
```

Optionale Vertiefungen für Stufe 2 & 3:
- [Superpowers Hands-on](../../resources/superpowers-hands-on.md)
- [OpenSpec Hands-on](../../resources/openspec-hands-on.md)
- [Workflow Comparison Lab](../../resources/workflow-comparison-lab.md)

## Live-Demo

Zeige zuerst das fertige Beispiel [EXAMPLE-near-breach-warning.md](../../playground/incident-triage-hub/specs/EXAMPLE-near-breach-warning.md) und stelle die Frage:

> „Wenn ihr diesen 30-Zeilen-Text freigebt — wie hoch ist die Wahrscheinlichkeit, dass der Agent danach genau das Richtige baut?“

Lass danach live aus einem Einzeiler eine Spec-Datei für ein anderes Backlog-Item generieren (noch **ohne** Code-Edits!):

```text
Do not edit any production or test files yet.
Read playground/incident-triage-hub/README.md, triage/models.py, triage/rules.py, and specs/_TEMPLATE.md.
Create a spec file at playground/incident-triage-hub/specs/001-fix-triage-bugs.md for fixing the failing tests in tests/test_rules.py.
Keep it under 250 words and wait for my review.
```

## Takeaway

Specs machen Agenten nicht langsamer. **Specs verhindern, dass der Agent mit Höchstgeschwindigkeit in die falsche Richtung rennt.**
