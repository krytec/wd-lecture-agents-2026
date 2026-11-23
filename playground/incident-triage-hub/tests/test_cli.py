import json
import subprocess
import sys
import unittest
from pathlib import Path

CLI_PATH = Path(__file__).resolve().parents[1] / "cli.py"


class IncidentCliTest(unittest.TestCase):
    def test_summary_command_returns_valid_json(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CLI_PATH), "summary"],
            capture_output=True,
            text=True,
            check=True,
        )
        data = json.loads(proc.stdout)
        self.assertEqual(data["total"], 7)
        self.assertEqual(data["open"], 6)

    def test_list_command_filters_by_service(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CLI_PATH), "list", "--service", "auth"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("INC-103", proc.stdout)
        self.assertNotIn("INC-101", proc.stdout)


if __name__ == "__main__":
    unittest.main()
