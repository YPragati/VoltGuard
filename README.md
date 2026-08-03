
# ⚡ VoltGuard


VoltGuard is an industrial machine-monitoring and safety system developed in Python. The project monitors machine parameters, analyses them using a physics-based decision engine, and displays the machine condition through an interactive PyQt5 dashboard.

The system classifies machine health into:

- 🟢 SAFE
- 🟡 WARNING
- 🔴 DANGER


## Problem Statement
Standard IT firewalls analyze packets, but they don't understand physics. If malware sends a perfectly formatted command telling industrial equipment (like a pump) to operate outside safe limits, a normal firewall allows it because the syntax is correct — this can cause real physical damage.

## The Idea
VoltGuard acts as a **"Physics Firewall."** It reads incoming industrial network commands (Modbus/DNP3) and runs them through a real-time physics simulation *before* they reach the actual machinery. If the simulation predicts the command will cause an unsafe state (like pressure exceeding safe limits), it blocks the command and raises an alarm.

## Key Modules
- **Packet Interceptor (C++ & Scapy):** Reads and parses raw SCADA/Modbus network traffic.
- **Physics Engine (Python & OpenModelica):** Simulates the physical constraints (pressure, flow limits) of a mock industrial pipeline.
- **Decision Engine (Rust):** Fast logic that blocks commands if the simulation predicts failure.
- **Native Dashboard (C++/Qt):** Offline desktop dashboard for operators to view blocked commands and system health.



## 🛠 Tech Stack

### Languages
- Python

### GUI Framework
- PyQt5

### Version Control
- Git
- GitHub

### Development Environment
- Visual Studio Code
- PowerShell

### Programming Concepts
- Object-Oriented Programming (OOP)
- Modular Programming

### Python Libraries
- PyQt5
- sys
- os
- datetime
- json



# 📂 Project Structure

```
VoltGuard/
│
├── dashboard/
│   └── dashboard.py
│
├── parser/
│   ├── include/
│   ├── src/
│   └── output.json
│
├── physics/
│   ├── physics.py
│   ├── validator.py
│   ├── calculations.py
│   └── simulation.py
│
├── docs/
│   └── integration.md
│
├── tests/
│
├── logs/
│
├── main.py
│
└── README.md
```

---

# ⚙ System Workflow

```
Machine Inputs
      │
      ▼
 Packet Parser
      │
      ▼
 Physics Engine
      │
      ▼
 Safety Decision
      │
      ▼
 Dashboard Display
      │
      ▼
 Event Log & Alarm

# 🚀 Features

✅ Industrial Dashboard

✅ Machine Parameter Input

- RPM
- Pressure
- Flow Rate

✅ Physics Engine Integration

✅ Machine Health Indicator

✅ Alarm Panel

✅ Event Log

✅ Sensor Progress Bars

✅ Digital Clock

✅ Status Detection

- SAFE
- WARNING
- DANGER

---

# ▶ Running the Project

Clone repository

```bash
git clone <repository-url>
```

Open project

```bash
cd VoltGuard
```

Install dependencies

```bash
pip install PyQt5
```

Run dashboard

```bash
python -m dashboard.dashboard
```

---

# 📊 Sample Input

| RPM | Pressure | Flow Rate |
|-----|----------|-----------|
|3000|80|500|

Output

🟢 SAFE

---

| RPM | Pressure | Flow Rate |
|-----|----------|-----------|
|6000|160|700|

Output

🟡 WARNING

---

| RPM | Pressure | Flow Rate |
|-----|----------|-----------|
|8000|220|950|

Output

🔴 DANGER

---

# 📷 Dashboard

(Add dashboard screenshot here)

---

# 👥 Team Members

| Member | Responsibility |
|---------|----------------|
| Member 1 | Packet Parser |
| Member 2 (Team Lead) | Physics Engine, Git Management, Dashboard Development, Module Integration, Documentation |
| Member 3 | Testing & Documentation |

---

# 📄 Documentation

Additional project documentation is available in:

```
docs/integration.md
```

---

# 🔮 Future Improvements

- Real sensor integration
- Database connectivity
- Live industrial monitoring
- Historical data analysis
- Email/SMS alert system
- AI-based predictive maintenance

---

## Status
## 📌 Status

✅ Week 4 Completed

Current Features:
- Dashboard Integration
- Physics Engine
- Alarm Panel
- Event Log
- Machine Health Indicator
- Sensor Monitoring
- Git Integration

Project Status: Under Final Testing
