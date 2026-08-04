# Testing Guide — VoltGuard

This document describes how we test each module of VoltGuard, our test cases, 
and current test results as of Week 4 (Final Submission).

## Testing Strategy

VoltGuard follows a staged processing workflow that begins with packet parsing, continues through physics validation, and ends with a dashboard decision and display. Testing covers each stage of the pipeline.

| Module | What we test | Test type |
|--------|--------------|-----------|
| Packet Interceptor | Correctly parses valid Modbus/DNP3 packets, rejects malformed ones | Unit test |
| Physics Engine | Correctly flags unsafe commands (e.g., negative pressure, over-limit RPM) | Unit test |
| Decision Engine | Blocks unsafe commands within required latency (<10ms) | Integration test |
| Dashboard | Displays blocked commands and system status correctly | Manual test |

## How to Run Tests

### Prerequisites
```bash
py -m pip install -r requirements.txt
py -m pip install pytest
```

### Run all tests
```bash
py -m pytest tests/ -v
```

---

## Test Cases — Physics Engine ✅ (Automated — 10/10 Passing)

| Test ID | Test Name | Description | Status |
|---------|-----------|--------------|--------|
| test_safe | Safe command | Normal safe command approved, no alert | ✅ Pass |
| test_danger_rpm | Dangerous RPM | Over-limit RPM (9000) flagged as DANGER | ✅ Pass |
| test_warning_low_pressure | Low pressure warning | Pressure below MIN_PRESSURE flagged as WARNING | ✅ Pass |
| test_danger_high_pressure | High pressure danger | Pressure above MAX_PRESSURE flagged as DANGER | ✅ Pass |
| test_warning_high_flow_rate | High flow rate warning | Flow rate above MAX_FLOW_RATE flagged as WARNING | ✅ Pass |
| test_boundary_rpm_at_limit | RPM boundary | RPM exactly at MAX_RPM (5000) still SAFE | ✅ Pass |
| test_boundary_pressure_at_max | Pressure upper boundary | Pressure exactly at MAX_PRESSURE (120.0) still SAFE | ✅ Pass |
| test_boundary_pressure_at_min | Pressure lower boundary | Pressure exactly at MIN_PRESSURE (20.0) still SAFE | ✅ Pass |
| test_boundary_flow_rate_at_max | Flow rate boundary | Flow rate exactly at MAX_FLOW_RATE (1000.0) still SAFE | ✅ Pass |
| test_danger_rpm_takes_priority | Priority logic | When multiple limits breached, RPM check takes priority, returns DANGER | ✅ Pass |

**Result: 10/10 tests PASSED** ✅ (run via `py -m pytest tests/test_physics.py -v`)

## Test Cases — Packet Interceptor ✅ (Automated — 4/4 Passing)

| Test ID | Input | Expected Output | Status |
|---------|-------|------------------|--------|
| TC-01 | Valid Modbus TCP packet | Parsed successfully | ✅ Pass |
| TC-02 | Malformed hex payload | Rejected with error | ✅ Pass |
| TC-03 | Empty/truncated packet | Rejected safely, no crash | ✅ Pass |
| TC-04 | Valid DNP3 packet | Parsed successfully | ✅ Pass |

**Result: 4/4 tests PASSED** ✅ (run via `py -m pytest tests/test_parser.py -v`)

## Test Cases — Decision Engine ✅ (Automated — 6/6 Passing)

| Test ID | Input | Expected Output | Status |
|---------|-------|------------------|--------|
| TC-09 | Unsafe command from Physics Engine | Packet dropped within 10ms | ✅ Pass |
| TC-10 | Safe command from Physics Engine | Packet allowed through | ✅ Pass |
| TC-11 | High packet volume (stress test) | No latency breach, no crash | ✅ Pass |

**Result: 6/6 tests PASSED** ✅ (run via `py -m pytest tests/test_decision.py -v`)

## Test Cases — Dashboard ✅ (Manual — Completed)

| Test ID | Input | Expected Output | Status |
|---------|-------|------------------|--------|
| TC-12 | Blocked command event | Displayed in dashboard log with timestamp | ✅ Pass |
| TC-13 | Normal system status | Green/OK (SAFE) status shown correctly | ✅ Pass |
| TC-14 | Multiple alerts in sequence | All alerts (SAFE/WARNING/DANGER) logged correctly in Event Log panel, no UI freeze | ✅ Pass |

**Result: 3/3 manual dashboard tests PASSED** ✅
Verified by manually running `python dashboard/dashboard.py` and observing the Event Log panel respond correctly to changing RPM, Pressure, and Flow Rate values with SAFE (🟢) / WARNING (🟡) / DANGER (🔴) status, correct timestamps, and no crashes.

---

## Overall Test Summary

| Module | Tests | Result |
|--------|-------|--------|
| Decision Engine | 6 | ✅ All Passed |
| Parser | 4 | ✅ All Passed |
| Physics Engine | 10 | ✅ All Passed |
| Validator | 9 | ✅ All Passed |
| Dashboard (manual) | 3 | ✅ All Passed |
| **Total (automated)** | **29** | ✅ **29/29 Passed** |

## Notes
- Physics Engine, Parser, Decision Engine, and Validator all have automated unit tests, run using pytest (29/29 passing).
- Dashboard has been fully manually verified for SAFE/WARNING/DANGER flows end-to-end.