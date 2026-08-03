# User Guide — VoltGuard

**For:** Plant operators / non-technical users of the VoltGuard dashboard
**Maintained by:** Member 3 (Documentation)

> This guide will be filled in as the Native Dashboard (Week 2–4) is built. Structure is ready now so it can be completed incrementally instead of all at once at the end.

---

## 1. What is VoltGuard?

VoltGuard is a safety system that watches industrial network commands (sent to equipment like pumps and valves) and blocks any command that would push the equipment outside safe physical limits — before it ever reaches the machine.

You don't need to understand the technical details to use the dashboard. This guide covers what you'll see on screen and what to do when an alert appears.

---

## 2. Getting Started

_(To be completed once the dashboard exists)_

- How to open the dashboard
- What you'll see when it starts up
- Basic layout overview (screenshot placeholder)

---

## 3. Understanding the Dashboard

_(To be completed alongside Week 2–3 dashboard development)_

- **Traffic Log** — what it shows
- **Blocked Commands panel** — what it means when a command appears here
- **Physical Stress Graphs** — how to read "predicted vs actual" state

---

## 4. What to Do When You See an Alert

_(To be completed once the alerting/blocking logic — Week 3 — is built)_

1. 
2. 
3. 

---

## 5. Frequently Asked Questions

**Q: Does VoltGuard need an internet connection?**
A: No — it's designed to run fully offline/air-gapped.

**Q: What happens to a blocked command?**
A: _(to be filled in)_

**Q: Who do I contact if something looks wrong?**
A: _(to be filled in with team/support contact)_

---

## 6. Glossary

| Term | Meaning |
|------|---------|
| Modbus/DNP3 | Communication protocols used by industrial equipment |
| ICS/SCADA | Industrial Control Systems / Supervisory Control and Data Acquisition — the systems VoltGuard protects |
| Physics Firewall | VoltGuard's core concept: checking commands against a physics simulation before allowing them |

---

*Update each section as the corresponding feature is built — don't wait until Week 4 to write this all at once.*
