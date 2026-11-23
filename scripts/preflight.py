#!/usr/bin/env python3
"""Zero-dependency pre-flight check for the AI Coding Agents Workshop."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def print_status(level: str, label: str, detail: str) -> None:
    icons = {"OK": "[OK]  ", "INFO": "[INFO]", "WARN": "[WARN]", "FAIL": "[FAIL]"}
    print(f"{icons.get(level, '[INFO]')} {label}: {detail}")


def check_python() -> bool:
    major, minor = sys.version_info[:2]
    version_str = f"{major}.{minor}.{sys.version_info[2]}"
    if (major, minor) >= (3, 9):
        print_status("OK", "Python", f"{version_str} ({sys.executable})")
        return True
    print_status("FAIL", "Python", f"{version_str} gefunden — benötigt wird Python 3.9+")
    return False


def check_git() -> bool:
    git_bin = shutil.which("git")
    if not git_bin:
        print_status("WARN", "Git", "Nicht im PATH gefunden (für Diffs & Branches empfohlen)")
        return False
    res = subprocess.run([git_bin, "--version"], capture_output=True, text=True)
    print_status("OK", "Git", res.stdout.strip())
    return True


def check_playground(name: str, tests_rel_path: str, expected_fail: bool) -> bool:
    tests_path = ROOT / tests_rel_path
    if not tests_path.exists():
        print_status("FAIL", name, f"Testpfad fehlt: {tests_rel_path}")
        return False
    res = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(tests_path)],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    if expected_fail and res.returncode != 0:
        output = f"{res.stdout}\n{res.stderr}"
        has_failures = "FAILED (" in output and "failures=" in output
        has_errors = "errors=" in output or "Traceback (most recent call last):" in output and "FAIL:" not in output
        if has_failures and not has_errors:
            print_status("OK", name, "Startzustand bereit (bewusste Übungs-Fails aktiv)")
            return True
        print_status("FAIL", name, "Unerwarteter Fehler/Crash beim Ausführen der Tests")
        return False
    if res.returncode == 0:
        note = "Alle Tests grün (wurden bereits gelöst oder geändert)" if expected_fail else "Alle Tests grün"
        print_status("OK", name, note)
        return True
    print_status("WARN", name, f"Unerwarteter Test-Exit-Code {res.returncode}")
    return False


def check_optional_tools() -> None:
    agents = {
        "claude": "Claude Code CLI",
        "codex": "OpenAI Codex CLI",
        "gh": "GitHub CLI (Copilot)",
        "gemini": "Gemini CLI",
        "agy": "Antigravity CLI",
        "cursor": "Cursor CLI",
    }
    found = [label for cmd, label in agents.items() if shutil.which(cmd)]
    if found:
        print_status("INFO", "Erkannte CLI-Tools", ", ".join(found))
    else:
        print_status(
            "INFO",
            "CLI-Agents",
            "Keine CLI-Agents im PATH erkannt — IDE-Agents (VS Code Copilot, Cursor, Windsurf etc.) funktionieren genauso gut",
        )

    if shutil.which("node"):
        print_status("INFO", "Optionale Extras", "Verfügbar: node (für optionales OpenSpec-Lab)")
    else:
        print_status("INFO", "Optionale Extras", "node nicht gefunden — für den Haupt-Workshop nicht nötig")


def main() -> int:
    print("=== AI Coding Agents Workshop — Pre-Flight Check ===\n")
    ok_py = check_python()
    check_git()
    ok_tiny = check_playground(
        "Warm-up (tiny-issue-tracker)",
        "playground/tiny-issue-tracker/tests",
        expected_fail=True,
    )
    ok_hub = check_playground(
        "Praxisprojekt (incident-triage-hub)",
        "playground/incident-triage-hub/tests",
        expected_fail=True,
    )
    check_optional_tools()

    print()
    if ok_py and ok_tiny and ok_hub:
        print("Ergebnis: Alles bereit für den Workshop!")
        return 0
    print("Ergebnis: Bitte die [FAIL]-Punkte oben vor dem Workshop klären.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
