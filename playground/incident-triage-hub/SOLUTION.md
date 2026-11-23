# Solution Notes — Incident Triage Hub

Spoiler-Blatt für Facilitators und Selbstlernende. Erst nach eigener Diagnose lesen.

## Erwarteter Startzustand

```bash
python3 -m unittest discover -s playground/incident-triage-hub/tests -v
```

Es laufen 9 Tests: **5 grün, 4 rot** (entsprechend 3 klaren Root Causes in `triage/rules.py`):

1. `test_prioritize_orders_by_severity_then_oldest_first` — **FAIL**
2. `test_unknown_severity_sorts_after_known_severities` — **FAIL**
3. `test_find_sla_breaches_excludes_resolved_incidents` — **FAIL**
4. `test_filter_query_is_case_insensitive_and_matches_tags` — **FAIL**

## Die 3 Root Causes in `triage/rules.py`

### 1. `prioritize_open_incidents`
- **Problem:** Sortiert `age_minutes` aufsteigend (jüngste zuerst statt älteste zuerst) und nutzt `0` als Default für unbekannte Severities (wodurch `unknown` vor `sev1` landet).
- **Kleinster Fix:**
  ```python
  return sorted(
      open_items,
      key=lambda inc: (SEVERITY_ORDER.get(inc.severity, 99), -inc.age_minutes),
  )
  ```

### 2. `find_sla_breaches`
- **Problem:** Prüft alle Incidents statt nur offene (`inc.is_open`), wodurch `INC-105` (`resolved`, 210m) fälschlich als SLA-Breach gemeldet wird.
- **Kleinster Fix:**
  ```python
  def find_sla_breaches(incidents: list[Incident]) -> list[Incident]:
      breaches = [
          inc
          for inc in incidents
          if inc.is_open and inc.age_minutes > SLA_MINUTES.get(inc.severity, 1440)
      ]
      return prioritize_open_incidents(breaches)
  ```

### 3. `filter_incidents`
- **Problem:** `query`-Suche ist case-sensitive und durchsucht `inc.tags` nicht.
- **Kleinster Fix:**
  ```python
  if query:
      needle = query.strip().casefold()
      result = [
          inc
          for inc in result
          if needle in inc.title.casefold()
          or needle in inc.service.casefold()
          or any(needle in tag.casefold() for tag in inc.tags)
      ]
  ```

## Worauf Facilitators achten können

- Hat der Agent zuerst `README.md`, `models.py`, `rules.py` und `test_rules.py` gelesen, bevor er editiert hat?
- Blieben die Tests unverändert (kein „weakened test“ Failure Mode)?
- Hat der Agent nur `triage/rules.py` geändert statt unnötig `models.py`, `server.py` oder `cli.py` umzubauen?
- Wurde der vollständige `unittest`-Befehl als Beweis ausgeführt?
