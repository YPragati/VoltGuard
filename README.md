
#VoltGuard


#VoltGuard is an industrial machine-monitoring and safety system developed in Python. The project monitors machine parameters, analyses them using a physics-based decision engine, and displays the machine condition through an interactive PyQt5 dashboard.

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

## Tech Stack
 Python 3
- PyQt5
- Git & GitHub
- Object-Oriented Programming


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
| Team Lead | Git Management, Dashboard Development, Module Integration, Documentation |
| Member 1 | Packet Parser |
| Member 2 | Physics Engine |
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

## Development Plan
| Week | Engineering Focus | Simulation & UI Focus |
|------|--------------------|------------------------|
| 1 | Parse mock Modbus traffic, generate test commands | Build basic pressure/fluid physics model |
| 2 | Connect network parser to physics engine | Build native Qt dashboard foundation |
| 3 | Build inline packet-blocking logic (sub-10ms) | Add real-time graphs to dashboard |
| 4 | Deploy on edge device (Raspberry Pi) | Polish UI for factory floor use |

## Team Roles
- Testing, documentation, README, reports, bug fixing, and integration support — maintained by Member 4.
## How to Run

1. Clone the repository.
2. Install the required dependencies.
3. Run the project using:
   ```
   python main.py
   ```
4. Open the dashboard and monitor the results.

## Testing

- Run the parser module with sample Modbus packets.
- Test the physics engine using normal and malicious inputs.
- Verify that unsafe commands are detected and logged.

## Future Improvements

- Improve dashboard UI.
- Add support for more industrial protocols.
- Optimize real-time detection performance.
## Status
🚧 Project in progress — Week 1 in development.
