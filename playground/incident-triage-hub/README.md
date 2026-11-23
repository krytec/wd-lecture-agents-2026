# Incident Triage Hub

Ein selbstenthaltenes, dependency-freies Praxisprojekt für den Workshop und Mini-Hackathon.

Es simuliert ein kleines internes Tool für Engineering, QA, DevOps und Produktteams: eingehende Incidents werden geladen, priorisiert, auf SLA-Verletzungen geprüft, als CLI-Report ausgegeben und über eine kleine lokale Web-UI angezeigt.

## Warum dieses Projekt?

- **Zero-Setup:** Nur Python 3 (Standard Library), keine externen Pakete, kein Internet nötig.
- **Realistisch:** Mehrere Dateien, Datenmodell, Business-Logik, CLI, Mini-HTTP-UI und Tests.
- **Für alle Rollen:** Bugs zum Debuggen, Features im [BACKLOG.md](BACKLOG.md), fehlende Edge-Case-Tests für QA und Produkt-Specs für PM/Ops.

## Schnellstart

Alle Befehle funktionieren vom Repo-Root:

```bash
# 1. Tests ausführen (im Startzustand schlagen 4 Tests durch 3 bewusste Bugs fehl)
python3 -m unittest discover -s playground/incident-triage-hub/tests -v

# 2. CLI-Zusammenfassung anzeigen
python3 playground/incident-triage-hub/cli.py summary

# 3. SLA-Verletzungen anzeigen
python3 playground/incident-triage-hub/cli.py breaches

# 4. Markdown-Report ausgeben
python3 playground/incident-triage-hub/cli.py report

# 5. Lokale Status-UI starten (http://127.0.0.1:8080)
python3 playground/incident-triage-hub/cli.py serve
```

## Struktur

```text
playground/incident-triage-hub/
├── README.md
├── BACKLOG.md           # Ideen & Challenges für Beginner bis Intermediate
├── SOLUTION.md          # Spoiler-Notizen für Facilitators (erst am Ende lesen!)
├── sample_incidents.json
├── cli.py               # CLI-Einstiegspunkt
├── specs/               # Spec-Driven Development (SDD) Artefakte im Repo
│   ├── _TEMPLATE.md     # Vorlage für eigene Bugfix- und Feature-Specs
│   └── EXAMPLE-near-breach-warning.md
├── triage/
│   ├── __init__.py
│   ├── models.py        # Incident-Datenmodell und Konstanten
│   ├── storage.py       # JSON laden/speichern
│   ├── rules.py         # Priorisierung, SLA-Prüfung, Filter, Report-Logik
│   └── server.py        # Lokale Status-UI + JSON-API
└── tests/
    ├── test_rules.py    # Unit-Tests für Business-Logik (4 Fails / 3 Bugs)
    └── test_cli.py      # Basis-Tests für CLI & Storage
```

## Typischer Einstieg mit einem Agenten

Gib deinem Agenten **nicht** einfach „Fix all bugs“. Nutze stattdessen einen klaren Agent Contract:

```text
Goal: Diagnose and fix the failing tests in playground/incident-triage-hub.
Context: Start by reading playground/incident-triage-hub/README.md, triage/models.py, triage/rules.py, and tests/test_rules.py.
Constraints:
- Do not read SOLUTION.md.
- Do not add external dependencies.
- Do not weaken or delete existing tests.
Done when: python3 -m unittest discover -s playground/incident-triage-hub/tests -v passes and you summarize each root cause and fix.
Work style: Read first. Explain the root causes and propose a short plan before editing any files.
```
