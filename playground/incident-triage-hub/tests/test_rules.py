import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from triage.models import Incident
from triage.rules import (
    build_summary,
    filter_incidents,
    find_sla_breaches,
    prioritize_open_incidents,
    render_markdown_report,
)
from triage.storage import load_incidents


class IncidentRulesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.incidents = load_incidents()

    def test_prioritize_orders_by_severity_then_oldest_first(self) -> None:
        ordered = prioritize_open_incidents(self.incidents)
        ids = [inc.id for inc in ordered]
        # INC-101 (sev1, 45m) must come before INC-103 (sev1, 15m)
        # INC-102 (sev2, 180m) must come before INC-107 (sev2, 65m)
        # Resolved INC-105 must be excluded
        self.assertEqual(ids, ["INC-101", "INC-103", "INC-102", "INC-107", "INC-104", "INC-106"])

    def test_unknown_severity_sorts_after_known_severities(self) -> None:
        items = [
            Incident("INC-900", "Mystery alert", "misc", "unknown", "open", "ops", 500, []),
            Incident("INC-901", "Critical DB down", "db", "sev1", "open", "ops", 5, []),
        ]
        ordered = prioritize_open_incidents(items)
        self.assertEqual([inc.id for inc in ordered], ["INC-901", "INC-900"])

    def test_find_sla_breaches_excludes_resolved_incidents(self) -> None:
        breaches = find_sla_breaches(self.incidents)
        ids = [inc.id for inc in breaches]
        # INC-101 (sev1, 45m > 30m) and INC-102 (sev2, 180m > 120m) are open breaches.
        # INC-105 (sev1, 210m) is already resolved and must NOT be listed.
        self.assertEqual(ids, ["INC-101", "INC-102"])

    def test_filter_query_is_case_insensitive_and_matches_tags(self) -> None:
        by_title = filter_incidents(self.incidents, query="checkout")
        self.assertEqual([inc.id for inc in by_title], ["INC-101"])

        by_tag = filter_incidents(self.incidents, query="REDIS")
        self.assertEqual([inc.id for inc in by_tag], ["INC-103"])

    def test_filter_by_service_and_open_only(self) -> None:
        billing_open = filter_incidents(self.incidents, service="Billing", open_only=True)
        self.assertEqual([inc.id for inc in billing_open], ["INC-102"])

    def test_render_markdown_report_contains_header_and_open_items(self) -> None:
        report = render_markdown_report(self.incidents)
        self.assertIn("# Incident Status Report", report)
        self.assertIn("INC-101", report)
        self.assertIn("Open incidents: 6", report)

    def test_build_summary_counts_total_and_open(self) -> None:
        summary = build_summary(self.incidents)
        self.assertEqual(summary["total"], 7)
        self.assertEqual(summary["open"], 6)


if __name__ == "__main__":
    unittest.main()
