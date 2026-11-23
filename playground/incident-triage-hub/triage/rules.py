"""Business rules for incident prioritization, SLA checks, filtering, and reporting."""

from __future__ import annotations

from triage.models import Incident, SEVERITY_ORDER, SLA_MINUTES


def prioritize_open_incidents(incidents: list[Incident]) -> list[Incident]:
    """Return open incidents sorted by severity (sev1 first), then oldest first."""
    open_items = [inc for inc in incidents if inc.is_open]
    return sorted(
        open_items,
        key=lambda inc: (SEVERITY_ORDER.get(inc.severity, 0), inc.age_minutes),
    )


def find_sla_breaches(incidents: list[Incident]) -> list[Incident]:
    """Return open incidents whose age exceeds their severity SLA target."""
    breaches: list[Incident] = []
    for inc in incidents:
        target = SLA_MINUTES.get(inc.severity, 1440)
        if inc.age_minutes > target:
            breaches.append(inc)
    return breaches


def filter_incidents(
    incidents: list[Incident],
    *,
    service: str | None = None,
    severity: str | None = None,
    query: str | None = None,
    open_only: bool = False,
) -> list[Incident]:
    """Filter incidents by service, severity, free-text query, and open status."""
    result = list(incidents)
    if open_only:
        result = [inc for inc in result if inc.is_open]
    if service:
        service_norm = service.strip().casefold()
        result = [inc for inc in result if inc.service.casefold() == service_norm]
    if severity:
        sev_norm = severity.strip().casefold()
        result = [inc for inc in result if inc.severity.casefold() == sev_norm]
    if query:
        needle = query.strip()
        result = [
            inc
            for inc in result
            if needle in inc.title or needle in inc.service
        ]
    return result


def build_summary(incidents: list[Incident]) -> dict[str, object]:
    """Build a compact summary dictionary for CLI and JSON API."""
    open_items = prioritize_open_incidents(incidents)
    breaches = find_sla_breaches(incidents)
    by_severity: dict[str, int] = {sev: 0 for sev in SEVERITY_ORDER}
    for inc in open_items:
        by_severity[inc.severity] = by_severity.get(inc.severity, 0) + 1

    return {
        "total": len(incidents),
        "open": len(open_items),
        "sla_breaches": len(breaches),
        "by_severity": by_severity,
        "top_incident_id": open_items[0].id if open_items else None,
    }


def render_markdown_report(incidents: list[Incident]) -> str:
    """Render a compact Markdown status report for standups or handovers."""
    summary = build_summary(incidents)
    open_items = prioritize_open_incidents(incidents)
    breaches = find_sla_breaches(incidents)

    lines = [
        "# Incident Status Report",
        "",
        f"- Total incidents: {summary['total']}",
        f"- Open incidents: {summary['open']}",
        f"- SLA breaches: {summary['sla_breaches']}",
        "",
        "## Prioritized Open Queue",
        "",
    ]
    if not open_items:
        lines.append("_No open incidents._")
    else:
        for inc in open_items:
            sla = SLA_MINUTES.get(inc.severity, 1440)
            breach_flag = " [SLA BREACH]" if inc.age_minutes > sla else ""
            lines.append(
                f"- **{inc.id}** ({inc.severity.upper()}, {inc.service}, "
                f"{inc.age_minutes}m, owner: {inc.owner}): {inc.title}{breach_flag}"
            )

    if breaches:
        lines.extend(["", "## Immediate Action (SLA Breaches)", ""])
        for inc in breaches:
            lines.append(f"- {inc.id}: {inc.title} ({inc.service}, {inc.age_minutes}m)")

    return "\n".join(lines)
