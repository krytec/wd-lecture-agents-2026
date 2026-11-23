# 06 SDD Execution, Plan Mode & Orchestration

## One-liner

Eine gute Spec ist die halbe Miete — Orchestrierung sorgt dafür, dass der Agent beim Umsetzen der Spec in kontrollierten Phasen bleibt: **`Explore -> Specify -> Plan -> Execute -> Verify`**.

## Warum das wichtig ist

Selbst mit einer guten Spec wirkt ein einziger ungebremster Agent-Lauf verlockend:

```text
"Implement everything and tell me when you're done."
```

Aber lange, unstrukturierte Läufe driften:

- Das Context Window füllt sich mit Such- und Fehlversuchen.
- Zwischenentscheidungen weichen leise von der Spec ab.
- Derselbe Agent, der den Code geschrieben hat, ist blind für seine eigenen Fehler („Confirmation Bias“).
- Am Ende steht ein großer Diff, den niemand mehr sicher reviewen kann.

## Der SDD Execution Loop (Plan Mode in modernen Harnesses)

Statt kryptischer Prompt-Rituale nutzen wir den Ablauf, den moderne Coding Agents (GitHub Copilot Agent Mode, Claude Code, Cursor, Codex, Antigravity) heute nativ durch **Plan Mode** und **Execution Gates** unterstützen:

```text
1. Explore & Specify  (Read-Only)  -> Codebase lesen, max. 1 Blocker-Frage stellen, Spec schreiben
2. Plan & Lock        (Plan Mode)  -> Max. 3 Schritte + betroffene Dateien festlegen -> Mensch gibt frei
3. Execute            (Build)      -> Kleinste Slice exakt nach Spec implementieren + Tests ausführen
4. Verify & Audit     (Review)     -> git diff und Test-Output unbestechlich gegen die Spec-Datei prüfen
```

### Warum der „Plan Lock“ vor Schritt 3 entscheidend ist

Zwischen **Plan** und **Execute** liegt ein bewusster kurzer Stopp:
- Welche Dateien werden angefasst?
- Welche Dateien dürfen **nicht** angefasst werden?
- Welcher Test wird zuerst geschrieben oder ausgeführt?

Wenn der Plan falsch abbiegt, korrigierst du ihn in 10 Sekunden — bevor 5 Dateien umgeschrieben wurden.

## Rollen-Trennung & Subagents (Orchestration)

Ein einzelner Chat-Verlauf wird schnell betriebsblind. Da unsere **Spec als Datei im Repo** (`specs/*.md`) liegt, können wir die Arbeit sauber auf drei Rollen aufteilen — entweder über echte **Subagents / Custom Agents** deines Harnesses oder durch frische Sessions/Rollen-Prompts:

1. **Architect / Spec-Writer (Read-Only):**
   Erkundet den Code und erstellt oder schärft `specs/001-...md`. Darf keinen Produktivcode ändern.
2. **Implementer (Fokussierter Builder):**
   Bekommt **nur** den Pfad zur freigegebenen Spec-Datei (`Implement playground/incident-triage-hub/specs/001-...md`). Baut die kleinste Lösung und lässt die Tests laufen.
3. **Skeptical Reviewer / QA (Unabhängiger Prüfer):**
   Vergleicht `git diff` und die Testausgabe Punkt für Punkt mit den *Acceptance Criteria* und *Non-Goals* in der Spec-Datei.

## Brownfield vs. Greenfield im SDD-Loop

| Phase | Brownfield (`incident-triage-hub`) | Greenfield (`Puzzle Game`) |
| --- | --- | --- |
| **1. Explore & Specify** | `AGENTS.md`, bestehenden Code & rote Tests lesen -> Bug-/Feature-Spec in `specs/` | Produktwunsch klären -> PRD, Mechanics Spec & Testvertrag als Datei anlegen |
| **2. Plan & Lock** | Exakte Änderungsstellen (z.B. nur `triage/rules.py` + `tests/test_rules.py`) locken | Erste spielbare Slice (Logik getrennt von UI, deterministischer Seed) locken |
| **3. Execute** | Kleinster Fix oder Feature-Slice + Unit-Tests | Erste Slice implementieren + Unit- & UI-Checks |
| **4. Verify & Audit** | `git diff` + `unittest`-Output gegen `specs/*.md` prüfen | Production-Ready Gates + Browser-Check gegen PRD prüfen |

## Takeaway

Gute Orchestrierung bedeutet nicht, möglichst viele autonome Agenten gleichzeitig losrennen zu lassen. **Gute Orchestrierung ist saubere Phasentrennung rund um eine gemeinsame Spec-Datei.**
