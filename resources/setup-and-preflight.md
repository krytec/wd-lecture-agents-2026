# Setup & Pre-Flight Check (5 Minuten vor dem Workshop)

Damit wir im Workshop keine Zeit mit Setup-Problemen verlieren, geh diese kurze Checkliste am besten **vor dem Start** einmal durch.

## 1. Voraussetzungen

- **Git** (um das Repo zu klonen und `git diff` zu nutzen)
- **Python 3.9+** (für beide lokalen Playgrounds — keine externen Pakete nötig!)
- **Ein AI Coding Agent deiner Wahl**, z.B.:
  - GitHub Copilot (VS Code Agent Mode)
  - Claude Code
  - OpenAI Codex
  - Cursor / Windsurf / Cline
  - Gemini CLI / Antigravity

> **Kein Python-Profi?** Kein Problem! Die Playgrounds sind bewusst klein und lesbar — der Punkt ist nicht Python, sondern **wie du deinen Agenten führst**.

## 2. Repo prüfen (1 Befehl)

Führe im geklonten Repo-Ordner den automatischen Pre-Flight-Check aus:

```bash
python3 scripts/preflight.py
```

*(Unter Windows ggf. `python scripts/preflight.py` oder `py scripts/preflight.py`.)*

Erwartetes Ergebnis:
- `[OK] Python`
- `[OK] Git`
- `[OK] Warm-up (tiny-issue-tracker): Startzustand bereit`
- `[OK] Praxisprojekt (incident-triage-hub): Startzustand bereit`

Dass die Playground-Tests am Anfang fehlschlagen, ist **Absicht** — das sind unsere Übungsfälle.

## 3. Agent-Smoke-Test (1 Minute)

Öffne das Repo in deinem bevorzugten Agent-Harness und teste diesen harmlosen Read-Only-Prompt:

```text
Do not edit any files.
Read playground/tiny-issue-tracker/README.md and tell me in two sentences what this playground is for and how to run its tests.
```

Wenn dein Agent die Datei liest und den `unittest`-Befehl nennt, bist du startklar!

## 4. Troubleshooting für häufige Stolpersteine

| Problem | Lösung |
| --- | --- |
| `python: command not found` (macOS/Linux) | Nutze `python3` statt `python`. |
| `python3` fehlt unter Windows | Installiere Python 3 aus dem Microsoft Store oder via `winget install Python.Python.3.12` (oder nutze `py`). |
| Mein Agent darf keine Terminal-Befehle ausführen | Kein Blocker: lass den Agenten den Befehl vorschlagen und führe ihn selbst im Terminal aus; kopiere die Ausgabe zurück in den Chat. |
| Firmen-Proxy / Firewall blockiert `npm` (`openspec`) oder externe Web-Suche | Ignoriere die optionalen Online-Extras — beide Haupt-Playgrounds (`tiny-issue-tracker` und `incident-triage-hub`) laufen **100 % offline ohne Downloads**. |
| Agent editiert sofort los, obwohl ich nur eine Analyse wollte | Starte den Prompt explizit mit `Do not edit any files yet.` und nutze Plan-Mode / Ask-Mode deines Harnesses. |
| Ich habe Dateien im Playground kaputt gespielt | Kein Stress — mit `git checkout -- playground/` setzt du die Übungsdateien sofort zurück. |

## 5. Sicherheit & Datenschutz im internen Workshop

- Füge **keine echten Firmen-Secrets, API-Keys, Passwörter oder Kundendaten (PII)** in Prompts oder Übungsdateien ein.
- Nutze nur die freigegebenen internen Agent-Tools/Accounts eures Unternehmens.
- Überprüfe vor dem Ausführen von Shell-Befehlen kurz, was der Agent vorschlägt (Human-in-the-Loop).
