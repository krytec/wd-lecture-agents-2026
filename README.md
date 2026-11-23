# AI Coding Agents: Interner Praxis-Workshop & Mini-Hackathon

Dieses Repo ist ein kompletter, harness-neutraler Workshop-Kit für einen **3- bis 4-stündigen internen Praxis-Workshop mit Mini-Hackathon** — konzipiert für **Beginner bis Intermediate AI-Agent-User** in gemischten Teams (Software Engineering, QA, DevOps, Data und tech-affine Produkt-/Ops-Rollen).

**Ziel:** Teilnehmende sollen nicht nur sehen, dass Agents Code oder Texte generieren können. Sie sollen praktisch erleben, dass **Agentenführung ein eigener Skill** ist: präzisen Kontext geben, Werkzeuge sinnvoll einsetzen, wiederholbare Skills bauen, Specs schärfen, Loops kontrollieren und Ergebnisse verlässlich verifizieren.

Der Workshop ist bewusst **harness-neutral**. Alle Übungen funktionieren mit **GitHub Copilot (Agent Mode), Claude Code, OpenAI Codex, Cursor, Windsurf, Cline, Gemini CLI / Antigravity** und ähnlichen Umgebungen.

---

## Start Here (5 Minuten vor dem Workshop)

1. **Setup prüfen (1 Befehl):**
   ```bash
   python3 scripts/preflight.py
   ```
   Details & Troubleshooting: [Setup & Pre-Flight Check](resources/setup-and-preflight.md)
2. **Deinen Pfad wählen:**
   - **Beginner (erste echte Agent-Erfahrungen):** Starte mit dem 10-Minuten-Warm-up [tiny-issue-tracker](playground/tiny-issue-tracker/README.md) und wechsle danach in Track A von [Mini-Hackathon Challenges](resources/hackathon-challenges.md) auf dem lokalen [Incident Triage Hub](playground/incident-triage-hub/README.md).
   - **Intermediate (nutzt Agents bereits im Alltag):** Nutze das Warm-up nur kurz als Kalibrierung und springe direkt in Track B (Spec-First Feature-Sprint im [Incident Triage Hub](playground/incident-triage-hub/BACKLOG.md)) oder Track D ([Greenfield Puzzle Game](resources/greenfield-puzzle-game.md)).
   - **QA, PM, DevOps & Data:** Alle Kernkonzepte (Agent Contract, Specs, Skills, Verification) gelten 1:1 auch für Test-Audits, PRDs, Runbooks und Automatisierung — siehe **Track C** in [Mini-Hackathon Challenges](resources/hackathon-challenges.md).

---

## Die wichtigsten Arbeitsflächen

- [AGENTS.md](AGENTS.md): Lebendes Dogfooding-Beispiel für dauerhafte Repo-Instruktionen (und Schutz gegen Spoiler im Workshop).
- [Setup & Pre-Flight Check](resources/setup-and-preflight.md): 5-Minuten-Checkliste, Smoke-Test und Troubleshooting.
- [Mini-Hackathon Challenges & Show-and-Tell](resources/hackathon-challenges.md): Gestaffelte Tracks (Beginner, Intermediate, Cross-Functional, Greenfield) + Bewertungsrubrik.
- [1-Page Cheatsheet](resources/cheatsheet.md): Kompakter Spickzettel für den Arbeitsalltag nach dem Workshop.
- `playground/tiny-issue-tracker`: Mini-Warm-up (1 Datei, dependency-free) für den ersten Agent Contract in Modul 01.
- `playground/incident-triage-hub`: **Selbstenthaltenes Praxisprojekt** (CLI + lokale Web-UI + Tests, 100 % offline & dependency-free) mit 3 realistischen Bugs und Feature-Backlog.
- [Workbook](resources/workbook.md): Arbeitsfläche für Agent Contract, Read-Only Map, Mini-Spec, Verification und Handoff.
- [Prompt Cards](resources/prompt-cards.md): Kopierbare Standard-Prompts für den Alltag.
- [Agent Failure Modes Catalog](resources/agent-failure-modes.md): Typische Agentenfehler erkennen und sofort stoppen.
- [Harness Matrix](resources/harness-matrix.md): Wie sich Konzepte auf Copilot, Claude Code, Codex & Co. abbilden.

**Optionale Vertiefungs-Tracks (für schnelle Teams oder Follow-up-Sessions):**
- [Greenfield Puzzle Game](resources/greenfield-puzzle-game.md): Neues Produkt erst spezifizieren, dann in eine kleine Slice schneiden.
- [Superpowers Hands-on](resources/superpowers-hands-on.md) & [OpenSpec Hands-on](resources/openspec-hands-on.md) & [Workflow Comparison Lab](resources/workflow-comparison-lab.md): Installierbare Skill- und Spec-Workflows im Vergleich.

---

## Lernversprechen

Nach 3–4 Stunden können Teilnehmende:

- einen AI Agent wie einen schnellen Junior-Kollegen mit Werkzeugen führen, statt ihn wie eine Suchmaschine zu befragen
- stabile Kontextregeln formulieren (`AGENTS.md`, `CLAUDE.md`, Copilot instructions)
- MCP als Werkzeug- und Kontextbrücke einordnen und sinnvoll nutzen
- eine kleine, wiederverwendbare Agent Skill im offenen `SKILL.md`-Format erstellen
- **Spec-Driven Development (SDD)** mit repo-lokalen Spec-Dateien (`specs/*.md`) als Anti-Drift-Mechanik einsetzen
- den **SDD Execution Loop** (`Explore -> Specify -> Plan -> Execute -> Verify`) mit Plan Mode und Rollen-Trennung / Subagents praktisch anwenden
- Agent-Ergebnisse mit Tests, Diffs, Spec-Audits und Sicherheitschecks sauber absichern

---

## Halbtags-Agenda (3,5–4h inkl. Mini-Hackathon)

*(Kompakte 3h-Variante und Moderationshinweise im [Facilitator Guide](resources/facilitator-guide.md).)*

| Zeit | Block | Kernfrage | Praxis-Output |
| --- | --- | --- | --- |
| 00:00–00:15 | Kickoff & Pre-Flight | Was ist heute anders als Autocomplete? Läuft alles? | gemeinsames Mentalmodell + grüner Pre-Flight |
| 00:15–00:40 | [01 Agent Mindset](concepts/01-agent-mindset/README.md) | Wie führt man einen Agenten? | erster Agent Contract am `tiny-issue-tracker` |
| 00:40–01:05 | [02 Context and Instructions](concepts/02-context-and-instructions/README.md) | Was gehört dauerhaft in den Kontext? | kleines `AGENTS.md` / Contract File |
| 01:05–01:30 | [03 MCP Tooling](concepts/03-mcp-tooling/README.md) & [04 Skills](concepts/04-agent-skills-and-plugins/README.md) | Wann Tools (MCP), wann Methoden (Skills)? | eigene `SKILL.md`-Skizze |
| 01:30–01:45 | Pause | Kopf lüften & Track wählen | Kaffee + Team-/Track-Wahl |
| 01:45–02:15 | [05 Spec-Driven Development](concepts/05-spec-driven-development/README.md) & [06 SDD Execution & Orchestration](concepts/06-sdd-execution-and-orchestration/README.md) | Wie steuert man Agents über Specs, Plan Mode & Subagents? | eigene Spec-Datei (`specs/*.md`) & Plan Lock |
| 02:15–02:30 | [07 Verification & Safety](concepts/07-verification-and-safety/README.md) | Wie beweist man Qualität & schützt interne Daten? | Spec-Audit & Verifikations-Checkliste |
| 02:30–03:25 | **Mini-Hackathon Sprint (55 Min)** | SDD End-to-End am [Incident Triage Hub](playground/incident-triage-hub/README.md) (Tracks A–D) | Spec + geprüfter Fix, Feature, Tests oder Skill |
| 03:25–03:50 | **Show & Tell (3 Min/Team)** | Was hat funktioniert, welcher Fehler wurde gestoppt? | Demo + kurzes Feedback nach Rubrik |
| 03:50–04:00 | Wrap-up | Was nehmt ihr morgen in euren Workflow mit? | persönliche Agent-Regel |

---

## Repo-Struktur

```text
AGENTS.md                    # Repo-weite Agent-Guardrails (Dogfooding & Spoiler-Schutz)
scripts/
  preflight.py               # Zero-dependency Setup-Check
concepts/
  01-agent-mindset/          # je Modul: README.md, workshop.md, further-reading.md
  ...
  07-verification-and-safety/
playground/
  tiny-issue-tracker/        # Warm-up für Modul 01 (1 Datei, 5-10 Min)
  incident-triage-hub/       # Selbstenthaltenes Praxisprojekt (CLI + Web-UI + Tests + Backlog)
examples/
  skills/
  plugins/
  mcp/
resources/
  setup-and-preflight.md
  hackathon-challenges.md
  cheatsheet.md
  facilitator-guide.md
  workbook.md
  prompt-cards.md
  agent-failure-modes.md
  harness-matrix.md
  greenfield-puzzle-game.md
  superpowers-hands-on.md
  openspec-hands-on.md
  workflow-comparison-lab.md
  research-notes.md
```

---

## Grundhaltung

Dieser Workshop ist kein Prompt-Museum. Alles hier ist so gebaut, dass Teilnehmende direkt mit ihrem eigenen Agenten an realistischen Aufgaben arbeiten können.

> **Die Grundregel:** Ein Agent ist kein Orakel. Ein Agent ist ein sehr schneller Mitarbeiter mit unvollständigem Situationsbewusstsein. Deine Aufgabe ist es, die Situation so zu bauen, dass gute Arbeit wahrscheinlicher wird.

## Quellenbasis

Siehe [resources/research-notes.md](resources/research-notes.md) für die belegten offiziellen Quellen (OpenAI Codex, Anthropic Claude Code, GitHub Copilot, MCP, Agent Skills).
