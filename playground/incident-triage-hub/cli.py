#!/usr/bin/env python3
"""CLI entrypoint for Incident Triage Hub."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from triage.rules import (
    build_summary,
    filter_incidents,
    find_sla_breaches,
    render_markdown_report,
)
from triage.server import run_server
from triage.storage import DEFAULT_DATA_PATH, load_incidents


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Incident Triage Hub CLI")
    parser.add_argument(
        "--data",
        default=str(DEFAULT_DATA_PATH),
        help="Path to incidents JSON file",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("summary", help="Show JSON summary of current incidents")
    sub.add_parser("breaches", help="List open incidents breaching SLA")
    sub.add_parser("report", help="Render a Markdown status report")

    list_cmd = sub.add_parser("list", help="List incidents with optional filters")
    list_cmd.add_argument("--service", help="Filter by service name")
    list_cmd.add_argument("--severity", help="Filter by severity (sev1..sev4)")
    list_cmd.add_argument("--query", help="Free-text search in title, service, or tags")
    list_cmd.add_argument("--open-only", action="store_true", help="Only open incidents")

    serve_cmd = sub.add_parser("serve", help="Start local web UI")
    serve_cmd.add_argument("--host", default="127.0.0.1")
    serve_cmd.add_argument("--port", type=int, default=8080)

    args = parser.parse_args(argv)
    incidents = load_incidents(args.data)

    if args.command == "summary":
        print(json.dumps(build_summary(incidents), indent=2))
        return 0

    if args.command == "breaches":
        breaches = find_sla_breaches(incidents)
        for inc in breaches:
            print(f"{inc.id} [{inc.severity}] {inc.service} ({inc.age_minutes}m): {inc.title}")
        return 0

    if args.command == "report":
        print(render_markdown_report(incidents))
        return 0

    if args.command == "list":
        filtered = filter_incidents(
            incidents,
            service=args.service,
            severity=args.severity,
            query=args.query,
            open_only=args.open_only,
        )
        for inc in filtered:
            print(f"{inc.id} [{inc.severity}] ({inc.status}) {inc.service}: {inc.title}")
        return 0

    if args.command == "serve":
        run_server(host=args.host, port=args.port)
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
