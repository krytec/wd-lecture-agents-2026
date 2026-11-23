# Spec: Near-Breach Escalation Warning (`at_risk`)

- **Status:** Approved (Beispiel-Spec für Backlog-Item #5)
- **Target:** `playground/incident-triage-hub`

## 1. Problem & Current Behavior
Aktuell meldet `find_sla_breaches()` in `triage/rules.py` einen Incident erst dann, wenn `age_minutes > target` bereits überschritten ist. On-Call-Teams sehen dadurch keine Frühwarnung für offene Incidents, die kurz vor einer SLA-Verletzung stehen.

## 2. Desired Behavior
Offene Incidents (`inc.is_open == True`), die bereits **mindestens 80 %** ihrer SLA-Zeit erreicht oder überschritten haben, aber das SLA-Limit noch **nicht** überschritten haben (`0.8 * target <= age_minutes <= target`), gelten als **`at_risk`**:
1. Neue Hilfsfunktion `find_at_risk_incidents(incidents: list[Incident]) -> list[Incident]` in `triage/rules.py`, die offene `at_risk`-Incidents in priorisierter Reihenfolge (`prioritize_open_incidents`) zurückgibt.
2. `build_summary()` enthält zusätzlich das Feld `"at_risk": len(at_risk_items)`.
3. `render_markdown_report()` markiert betroffene Zeilen in der Open Queue mit ` [AT RISK]`.

## 3. Explicit Non-Goals
- Keine externen Dependencies.
- Keine Änderung der bestehenden SLA-Minutenwerte (`SLA_MINUTES` in `triage/models.py`).
- Keine Änderung an `sample_incidents.json`.
- Bereits gelöste Incidents (`status == "resolved"`) dürfen niemals `at_risk` sein.

## 4. Acceptance Criteria & Edge Cases
- [ ] Ein offener `sev1`-Incident (SLA = 30m) mit `age_minutes = 24` (exakt 80 %) und `age_minutes = 30` (exakt 100 %) wird als `at_risk` erkannt.
- [ ] Ein offener `sev1`-Incident mit `age_minutes = 23` (< 80 %) oder `age_minutes = 31` (> 100 %, bereits SLA Breach) wird **nicht** als `at_risk` gelistet.
- [ ] Ein `resolved`-Incident mit `age_minutes = 25` wird **nicht** als `at_risk` gelistet.
- [ ] `build_summary()` liefert den korrekten Integer-Wert unter `"at_risk"`.

## 5. Implementation Plan (Plan Lock — max. 3 Schritte)
1. **Regel & Summary ergänzen (`triage/rules.py`):** `find_at_risk_incidents()` implementieren, in `build_summary()` und `render_markdown_report()` einbinden.
2. **Unit-Tests schreiben (`tests/test_rules.py`):** Tests für 79 %, 80 %, 100 %, 101 % SLA sowie `resolved`-Status ergänzen.
3. **Unberührte Dateien:** `triage/models.py`, `triage/storage.py`, `sample_incidents.json` bleiben unverändert.

## 6. Verification Command(s)
```bash
python3 -m unittest discover -s playground/incident-triage-hub/tests -v
python3 playground/incident-triage-hub/cli.py summary
python3 playground/incident-triage-hub/cli.py report
```
