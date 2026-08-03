# Bug Report Log — VoltGuard

**Maintained by:** Member 3 (QA / Bug Reporting & Verification)

This is the running log of every bug found. Each bug should **also** be filed as a GitHub Issue (labeled by module and severity) — this file is the consolidated summary for reporting purposes.

---

## How to Log a Bug

Copy this template for each new entry:

```
### BUG-XXX: Short description

- **Module:** (parser / physics-engine / decision-engine / dashboard)
- **Severity:** Critical / Major / Minor
- **Found by:** 
- **Date found:** 
- **Steps to reproduce:**
  1. 
  2. 
- **Expected result:** 
- **Actual result:** 
- **Status:** Open / In Progress / Fixed / Verified / Won't Fix
- **GitHub Issue:** #

**Verification notes:** (fill in once a fix is submitted — did you confirm it's actually fixed?)
```

Severity guide:
- **Critical** — crashes the system, or a genuinely unsafe command gets through undetected.
- **Major** — a feature doesn't work as intended, but the system doesn't crash.
- **Minor** — cosmetic, UI text, non-blocking issue.

---

## Active Bug Log

### BUG-001: Stray `VoltGuard.git` file committed to repo root

- **Module:** repository / general
- **Severity:** Minor
- **Found by:** Member 3
- **Date found:** 2026-07-22
- **Steps to reproduce:**
  1. Open the `main` branch file listing.
  2. Observe a file named `VoltGuard.git` alongside `README.md`.
- **Expected result:** Repo root should only contain project files, no stray `.git` artifacts.
- **Actual result:** A `VoltGuard.git` file is present, likely committed by accident.
- **Status:** Open
- **GitHub Issue:** _(create and link here)_

**Verification notes:** _(pending)_

---

## Fixed / Closed Bugs

_(move entries here once verified fixed, keep for the record)_

---

## Summary Stats

| Severity | Open | Fixed | Total |
|----------|------|-------|-------|
| Critical | 0 | 0 | 0 |
| Major | 0 | 0 | 0 |
| Minor | 1 | 0 | 1 |

*(Update this table as bugs are added/resolved.)*
