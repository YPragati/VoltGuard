# Bug Report — VoltGuard

This document tracks bugs found during development and testing, along with
their status and resolution.

---

## BUG-001: Stray `VoltGuard.git` file in repo root
- **Severity:** Minor
- **Found in:** Week 1
- **Description:** An extra `VoltGuard.git` file was accidentally committed to the repository root.
- **Status:** ✅ Resolved — file removed from repo.

---

## BUG-002: `capture.py` missing `flow_rate` field
- **Severity:** Major
- **Found in:** Week 1
- **Description:** `capture/capture.py` did not generate the `flow_rate` field required by `physics/validator.py`, causing validator checks to fail on generated traffic.
- **Status:** ✅ Resolved — `capture.py` updated to include `flow_rate`. Confirmed with a regression test in `tests/test_validator.py`.

---

## BUG-003: `test_physics.py` indentation error
- **Severity:** Major (blocked test suite from running)
- **Found in:** Week 4, during merge of parser and decision modules
- **Description:** After merging in the Member-1 and decision branches, `tests/test_physics.py` had an indentation error that caused the full pytest run to fail before any tests could execute.
- **Status:** ✅ Resolved — indentation fixed, full suite re-run and passed (29/29).

---

## BUG-004: `output.json` causing repeated merge conflicts
- **Severity:** Minor / process issue
- **Found in:** Week 4, during branch merges
- **Description:** `output.json` is a generated runtime output file that is tracked in Git. Since multiple branches (leader, Member-1) each generated their own version locally, merging `main` triggered conflicts on this file twice.
- **Status:** ⚠️ Open — recommend adding `output.json` to `.gitignore` so generated files stop being tracked and causing conflicts.

---

## BUG-005: README role labeling issue
- **Severity:** Minor
- **Found in:** Week 4
- **Description:** README.md had incorrect/outdated role labeling for team members.
- **Status:** ✅ Resolved — corrected in README.md.

---

## Summary

| Bug ID | Severity | Status |
|--------|----------|--------|
| BUG-001 | Minor | ✅ Resolved |
| BUG-002 | Major | ✅ Resolved |
| BUG-003 | Major | ✅ Resolved |
| BUG-004 | Minor | ✅ Resolved|
| BUG-005 | Minor | ✅ Resolved |

**Open issues remaining: 0