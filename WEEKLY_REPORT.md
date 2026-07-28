# Weekly Report — VoltGuard

**Maintained by:** Member 3 (QA / Documentation)

Fill in one section per week. This feeds directly into the Final Report at the end of the internship.

---

## Week 1 — Protocol Parsing + Baseline Physics

**Reporting period:** _(fill in start–end date)_

**What the team built this week:**
- Implemented the initial project modules: Physics Engine (`physics/constants.py`, `physics/validator.py`, `physics/simulation.py`, `physics/physics.py`) and a mock traffic generator (`capture/capture.py`).
- Modbus/TCP parser (C++) developed separately on `Member-1---Shivanshu` branch — pending merge to `main`.
- Improved overall project structure (modular `physics/`, `capture/`, `decision/`, `dashboard/`, `parser/`, `tests/` folders).

**What I (Member 3) did this week:**
- Set up full project tracking documentation: `TESTING.md`, `CHANGELOG.md`, `TEST_REPORT.md`, `BUG_REPORT.md`, `WEEKLY_REPORT.md`, `USER_GUIDE.md`.
- Reviewed repo structure across `main` and all feature branches to establish an accurate baseline of what's actually implemented vs. planned.
- Wrote and added `tests/test_validator.py` (8 pytest test cases) to close a coverage gap — `validator.py` previously had zero tests.
- Identified and logged 2 bugs (see Bugs section below).
- Pushed multiple commits to GitHub reflecting Week 1 documentation and testing progress on the `Member-3---Magisha` branch.

**Tests run / results:**
- `tests/test_physics.py` — 3 existing tests covering `simulation.evaluate()`.
- `tests/test_validator.py` — 8 new tests added (missing-field checks, negative-value checks, valid input, boundary case for zero values).
- Full details logged in `TEST_REPORT.md`.

**Bugs found:**
- BUG-001: Stray `VoltGuard.git` file committed to repo root (Minor).
- BUG-002: `capture.py` does not generate the `flow_rate` field required by `physics/validator.py` — will cause a crash when the two modules are connected (Major).
- Full details in `BUG_REPORT.md`.

**Blockers / risks:**
- Parser (C++, `Member-1---Shivanshu` branch) not yet merged into `main` — blocks Week 2 bridge integration work from starting on schedule.
- Team's implementation stack (Python throughout) differs from the original spec (C++/Rust/Qt) — needs sign-off from team lead so it isn't flagged as a deviation later.

**Plan for next week:**
- Confirm parser merge timeline with Member 1 / team lead.
- Once merged, run integration tests to verify parser output feeds correctly into the physics engine (and confirm BUG-002 is fixed before that handoff).
- Begin Week 2 test cases (W2-01 to W2-04) as bridge integration work lands.

---

## Week 2 — Bridge Integration + Dashboard Foundation

**Reporting period:** _(dates)_

**What the team built this week:**
- 

**What I (Member 3) did this week:**
- 

**Tests run / results:**
- 

**Bugs found:**
- 

**Blockers / risks:**
- 

**Plan for next week:**
- 

---

## Week 3 — Inline Blocking (IPS) + Real-Time Graphs

**Reporting period:** _(dates)_

**What the team built this week:**
- 

**What I (Member 3) did this week:**
- 

**Tests run / results:**
- 

**Bugs found:**
- 

**Blockers / risks:**
- 

**Plan for next week:**
- 

---

## Week 4 — Deployment + Polish

**Reporting period:** _(dates)_

**What the team built this week:**
- 

**What I (Member 3) did this week:**
- 

**Tests run / results:**
- 

**Bugs found:**
- 

**Blockers / risks:**
- 

**Final status:**
- 

---

*Tip: fill each section in at the end of every week while it's fresh — this makes the Final Report almost write itself.*
