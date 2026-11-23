"""Minimal zero-dependency HTTP server for Incident Triage Hub."""

from __future__ import annotations

import html
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from triage.models import SLA_MINUTES
from triage.rules import build_summary, filter_incidents, prioritize_open_incidents
from triage.storage import DEFAULT_DATA_PATH, load_incidents


def _render_html(incidents, *, service_filter: str = "", query_filter: str = "") -> str:
    summary = build_summary(incidents)
    filtered = filter_incidents(
        incidents,
        service=service_filter or None,
        query=query_filter or None,
    )
    rows = []
    for inc in filtered:
        sla = SLA_MINUTES.get(inc.severity, 1440)
        breached = inc.is_open and inc.age_minutes > sla
        badge = "BREACH" if breached else inc.status
        rows.append(
            "<tr>"
            f"<td><code>{html.escape(inc.id)}</code></td>"
            f"<td><strong>{html.escape(inc.severity.upper())}</strong></td>"
            f"<td>{html.escape(inc.service)}</td>"
            f"<td>{html.escape(inc.title)}</td>"
            f"<td>{html.escape(inc.owner)}</td>"
            f"<td>{inc.age_minutes}m</td>"
            f"<td>{html.escape(badge)}</td>"
            "</tr>"
        )
    table_body = "\n".join(rows) or "<tr><td colspan='7'>No matching incidents.</td></tr>"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Incident Triage Hub</title>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 960px; margin: 2rem auto; padding: 0 1rem; color: #1f2937; }}
    .cards {{ display: flex; gap: 1rem; flex-wrap: wrap; margin: 1rem 0; }}
    .card {{ border: 1px solid #d1d5db; border-radius: 8px; padding: 0.75rem 1rem; min-width: 140px; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: 1rem; }}
    th, td {{ text-align: left; padding: 0.5rem; border-bottom: 1px solid #e5e7eb; }}
    form {{ display: flex; gap: 0.5rem; flex-wrap: wrap; margin: 1rem 0; }}
    input, button {{ padding: 0.4rem 0.6rem; font-size: 0.95rem; }}
  </style>
</head>
<body>
  <h1>Incident Triage Hub</h1>
  <div class="cards">
    <div class="card"><div>Total</div><strong>{summary['total']}</strong></div>
    <div class="card"><div>Open</div><strong>{summary['open']}</strong></div>
    <div class="card"><div>SLA Breaches</div><strong>{summary['sla_breaches']}</strong></div>
  </div>
  <form method="get" action="/">
    <input name="service" placeholder="Service (e.g. billing)" value="{html.escape(service_filter)}" />
    <input name="q" placeholder="Search title or tag..." value="{html.escape(query_filter)}" />
    <button type="submit">Filter</button>
    <a href="/">Reset</a>
  </form>
  <table>
    <thead>
      <tr><th>ID</th><th>Severity</th><th>Service</th><th>Title</th><th>Owner</th><th>Age</th><th>Status</th></tr>
    </thead>
    <tbody>
      {table_body}
    </tbody>
  </table>
</body>
</html>"""


class TriageHandler(BaseHTTPRequestHandler):
    data_path = DEFAULT_DATA_PATH

    def _send(self, status: int, content_type: str, body: str) -> None:
        payload = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        incidents = load_incidents(self.data_path)

        if parsed.path == "/health":
            self._send(200, "application/json", json.dumps({"status": "ok"}))
            return

        if parsed.path == "/api/summary":
            self._send(200, "application/json", json.dumps(build_summary(incidents), indent=2))
            return

        if parsed.path == "/api/incidents":
            ordered = prioritize_open_incidents(incidents)
            data = [inc.__dict__ for inc in ordered]
            self._send(200, "application/json", json.dumps(data, indent=2))
            return

        if parsed.path == "/":
            service = params.get("service", [""])[0]
            query = params.get("q", [""])[0]
            page = _render_html(incidents, service_filter=service, query_filter=query)
            self._send(200, "text/html; charset=utf-8", page)
            return

        self._send(404, "application/json", json.dumps({"error": "Not found"}))


def run_server(host: str = "127.0.0.1", port: int = 8080) -> None:
    server = HTTPServer((host, port), TriageHandler)
    print(f"Incident Triage Hub running at http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
    finally:
        server.server_close()
