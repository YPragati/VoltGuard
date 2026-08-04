# Test Report — VoltGuard

## Project Name
VoltGuard – Physics-Aware ICS/SCADA Intrusion Detection System

## Testing Summary
This report summarizes the automated and manual testing performed to verify
the correctness, stability, and integration of the VoltGuard pipeline
(parser → physics engine → decision engine → dashboard) ahead of the
Week 4 submission.

---

## Test Environment
- Operating System: Windows 11
- IDE: Visual Studio Code
- Backend: Python
- Test Framework: pytest
- Version Control: Git & GitHub

---

## Automated Test Results

| Module | Test File | Tests | Result |
|--------|-----------|-------|--------|
| Decision Engine | `tests/test_decision.py` | 6 | ✅ All Passed |
| Parser | `tests/test_parser.py` | 4 | ✅ All Passed |
| Physics Engine | `tests/test_physics.py` | 10 | ✅ All Passed |
| Validator | `tests/test_validator.py` | 9 | ✅ All Passed |
| **Total** | | **29** | ✅ **29/29 Passed** |

Run command:
```bash
py -m pytest tests/ -v
```

---

## Manual / Integration Testing — Dashboard

Full pipeline (parser → physics → decision → dashboard) verified manually
by feeding commands through the dashboard and observing the Event Log panel.

| Test Case | Input | Expected Result | Status |
|-----------|-------|------------------|--------|
| SAFE command | Command within all limits | Dashboard shows ALLOW, 🟢 SAFE status | ✅ Passed |
| WARNING command | Command near threshold (e.g. low pressure / high flow rate) | Dashboard shows 🟡 WARNING, logged correctly | ✅ Passed |
| DANGER command | Command over limit (e.g. RPM 9000) | Decision Engine returns BLOCK, dashboard shows 🔴 DANGER + alarm | ✅ Passed |
| Multiple alerts in sequence | SAFE → WARNING → DANGER back to back | All events logged correctly with timestamps, no UI freeze | ✅ Passed |

**Result: End-to-end pipeline confirmed working — parser output correctly
flows through physics validation, decision logic, and dashboard display.**

---

## Merge / Integration History

| Merge | Description |
|-------|-------------|
| Leader branch → main | Dashboard module update |
| Member-1 branch → main | Modbus/TCP parser (C++ + Python) |
| Decision module → main | New decision engine added |

Commit reference: `3495ba2` — "Merge parser and decision modules, all 29 tests passing"

---

## Issues Found During This Testing Cycle

- `test_physics.py` had an indentation bug — fixed before final run (see `BUG_REPORT.md`).
- `output.json` caused repeated merge conflicts since it's a generated file
  tracked in Git — recommended to add it to `.gitignore` (not yet done).

---

## Overall Result

All planned automated and manual testing activities for Week 4 were completed
successfully. No blocking issues remain open.

**Final Status: ✅ 29/29 Automated Tests Passed | Manual Dashboard Testing Passed**