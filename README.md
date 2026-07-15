
#vloutguard
# VoltGuard: Physics-Aware ICS/SCADA Intrusion Detection System

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
C++, Rust, Python, OpenModelica, Scapy, Qt

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
