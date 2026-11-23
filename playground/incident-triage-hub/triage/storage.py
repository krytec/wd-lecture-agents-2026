"""JSON storage helpers for Incident Triage Hub."""

from __future__ import annotations

import json
from pathlib import Path

from triage.models import Incident

DEFAULT_DATA_PATH = Path(__file__).resolve().parents[1] / "sample_incidents.json"


def load_incidents(path: Path | str = DEFAULT_DATA_PATH) -> list[Incident]:
    """Load incidents from a JSON file."""
    data_path = Path(path)
    raw_items = json.loads(data_path.read_text(encoding="utf-8"))
    return [
        Incident(
            id=item["id"],
            title=item["title"],
            service=item["service"],
            severity=item["severity"],
            status=item["status"],
            owner=item["owner"],
            age_minutes=int(item["age_minutes"]),
            tags=list(item.get("tags", [])),
        )
        for item in raw_items
    ]
