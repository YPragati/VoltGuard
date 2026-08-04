# Changelog

All notable changes to VoltGuard are documented in this file.

---

## [Week 4] — Integration, Testing & Final Submission

### Added
- Decision engine module (`decision/`) merged into `main`.
- `tests/test_decision.py` (6 tests) and `tests/test_parser.py` (4 tests).
- `__init__.py` files for `dashboard/`, `decision/`, `parser/`, `tests/` packages.
- Final documentation set: `TEST_REPORT.md`, `BUG_REPORT.md`, `CHANGELOG.md`, `WEEKLY_REPORT.md`, `TESTING.md`, `USER_GUIDE.md`.

### Merged
- Leader branch (dashboard update) → `main`.
- Member-1 branch (Modbus/TCP parser, C++ + Python) → `main`.
- Decision engine branch → `main`.
- Commit: `3495ba2` — "Merge parser and decision modules, all 29 tests passing"

### Fixed
- `tests/test_physics.py` indentation error that was blocking the full test suite from running (BUG-003).
- `capture/capture.py` missing `flow_rate` field required by the validator (BUG-002).
- Removed stray `VoltGuard.git` file from repo root (BUG-001).
- Corrected role labeling in `README.md` (BUG-005).

### Testing
- Full automated suite run: **29/29 tests passing**
  (Decision Engine 6, Parser 4, Physics Engine 10, Validator 9).
- Manual end-to-end dashboard testing: SAFE / WARNING / DANGER commands
  verified through the full pipeline (parser → physics → decision → dashboard).

### Known Issues
- `output.json` is a generated file currently tracked in Git, causing
  repeated merge conflicts — recommended fix: add to `.gitignore` (not yet applied).

Status: ✅ Passed

---

## [Week 3] — Inline Blocking (IPS) + Real-Time Graphs

### Added
- Inline blocking / intrusion prevention logic in `decision/`.
- Real-time graph rendering on the dashboard.

### Testing
- IPS decision logic tests — passed.
- Real-time graph data feed tests — passed.

---

## [Week 2] — Bridge Integration + Dashboard Foundation

### Added
- Dashboard module foundation (`dashboard/`).

### Merged
- Modbus/TCP parser (C++) → `main`, connected to Python physics engine.

### Fixed
- BUG-002 — `capture.py` missing `flow_rate` field.

---

## [Week 1] — Protocol Parsing + Baseline Physics

### Added
- Initial Physics Engine modules: `physics/constants.py`, `physics/validator.py`,
  `physics/simulation.py`, `physics/physics.py`.
- Mock traffic generator `capture/capture.py`.
- Project tracking docs: `TESTING.md`, `CHANGELOG.md`, `TEST_REPORT.md`,
  `BUG_REPORT.md`, `WEEKLY_REPORT.md`, `USER_GUIDE.md`.
- `tests/test_validator.py` (8 tests).

### Bugs Found
- BUG-001: Stray `VoltGuard.git` file in repo root (Minor).
- BUG-002: `capture.py` missing `flow_rate` field (Major).

---

## Version 1.0.0 — Final Submission
Release Status: ✅ Stable