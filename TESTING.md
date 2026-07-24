# Testing Guide — VoltGuard

This document describes how we test each module of VoltGuard, our test cases, 
and current test results as of the Mid-Project Review.

## Testing Strategy

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

## Test Cases — Physics Engine ✅ (Automated)

| Test ID | Test Name | Description | Status |
|---------|-----------|--------------|--------|
| test_safe | Safe command | Verifies a normal, safe command is approved with no alert | ✅ Pass |
| test_danger_rpm | Dangerous RPM | Verifies a command requesting over-limit RPM is flagged as unsafe | ✅ Pass |
| test_warning_low_pressure | Low pressure warning | Verifies a low-pressure condition is correctly flagged | ✅ Pass |

**Result: 3/3 tests PASSED** (run via `pytest tests/test_physics.py -v`)

## Test Cases — Packet Interceptor (Manual — In Progress)

| Test ID | Input | Expected Output | Status |
|---------|-------|------------------|--------|
| TC-01 | Valid Modbus TCP packet | Parsed successfully | ⬜ Pending |
| TC-02 | Malformed hex payload | Rejected with error | ⬜ Pending |
| TC-03 | Empty/truncated packet | Rejected safely, no crash | ⬜ Pending |
| TC-04 | Valid DNP3 packet | Parsed successfully | ⬜ Pending |

## Test Cases — Decision Engine (Manual — In Progress)

| Test ID | Input | Expected Output | Status |
|---------|-------|------------------|--------|
| TC-09 | Unsafe command from Physics Engine | Packet dropped within 10ms | ⬜ Pending |
| TC-10 | Safe command from Physics Engine | Packet allowed through | ⬜ Pending |
| TC-11 | High packet volume (stress test) | No latency breach, no crash | ⬜ Pending |

## Test Cases — Dashboard (Manual — In Progress)

| Test ID | Input | Expected Output | Status |
|---------|-------|------------------|--------|
| TC-12 | Blocked command event | Displayed in dashboard log with timestamp | ⬜ Pending |
| TC-13 | Normal system status | Green/OK status shown | ⬜ Pending |
| TC-14 | Multiple alerts in sequence | All alerts logged correctly, no UI freeze | ⬜ Pending |

---

## Mid-Project Review — Test Summary (as of 27 July 2026)

- **Physics Engine:** 3/3 automated unit tests PASSED ✅
- **Packet Interceptor:** Manual testing in progress
- **Decision Engine:** Manual testing in progress
- **Dashboard:** Manual testing in progress
- **Known bugs / issues:** See [GitHub Issues](https://github.com/YPragati/VoltGuard/issues)

## Notes
- Physics Engine has automated unit tests in `tests/test_physics.py`, run using pytest.
- Parser, Decision Engine, and Dashboard modules are being verified manually; automated test files to be added next.
