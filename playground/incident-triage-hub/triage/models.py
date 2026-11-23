"""Data models and SLA definitions for Incident Triage Hub."""

from __future__ import annotations

from dataclasses import dataclass

# Highest urgency = lowest rank number
SEVERITY_ORDER: dict[str, int] = {
    "sev1": 1,
    "sev2": 2,
    "sev3": 3,
    "sev4": 4,
}

# Target resolution time in minutes per severity
SLA_MINUTES: dict[str, int] = {
    "sev1": 30,
    "sev2": 120,
    "sev3": 480,
    "sev4": 1440,
}

OPEN_STATUSES: set[str] = {"open", "investigating"}


@dataclass
class Incident:
    id: str
    title: str
    service: str
    severity: str
    status: str
    owner: str
    age_minutes: int
    tags: list[str]

    @property
    def is_open(self) -> bool:
        return self.status in OPEN_STATUSES
