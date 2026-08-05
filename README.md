# VoltGuard

## Physics-Based Intrusion Prevention System for Industrial Control Networks

---

## 📌 Project Overview

**VoltGuard** is a physics-based Intrusion Prevention System (IPS) designed to protect Industrial Control Systems (ICS) and Operational Technology (OT) networks from malicious or unsafe control commands.

Traditional industrial cybersecurity solutions mainly depend on known attack signatures. VoltGuard introduces an additional security layer by validating incoming machine commands against physical operating limits.

The system monitors industrial parameters such as:

* Motor Speed (RPM)
* Pressure
* Flow Rate

and determines whether the command is:

* ✅ SAFE
* ⚠️ WARNING
* 🔴 DANGER

Unsafe commands are detected and blocked using an IPS decision engine.

---

# 🎯 Objectives

The main objectives of VoltGuard are:

* Parse industrial communication protocols such as Modbus/TCP
* Simulate normal and malicious industrial commands
* Validate commands using physics-based rules
* Detect abnormal machine behaviour
* Prevent unsafe commands from reaching industrial equipment
* Provide real-time monitoring through an industrial dashboard

---

# 🏗️ System Architecture

```
              Modbus TCP Traffic
                     |
                     ↓
            C++ Protocol Parser
                     |
                     ↓
              Python Controller
                     |
        -----------------------------
        |                           |
        ↓                           ↓
 Physics Validation            Security Engine
        |                           |
        ↓                           ↓
 SAFE / WARNING / DANGER     ALLOW / MONITOR / BLOCK
                     |
                     ↓
             PyQt Industrial Dashboard
                     |
                     ↓
       Real-Time Sensor Visualization
       Predicted vs Actual Monitoring
```

---

# ⚙️ Key Features

## 🔹 Modbus Communication Monitoring

* Parses simulated Modbus/TCP packets
* Extracts industrial register values
* Converts raw register data into machine parameters

Supported parameters:

| Parameter | Description     |
| --------- | --------------- |
| RPM       | Motor speed     |
| Pressure  | System pressure |
| Flow Rate | Fluid flow      |

---

## 🔹 Physics-Based Detection Engine

VoltGuard does not rely only on network signatures.

It checks whether commands are physically possible.

Example:

```
Pressure > Maximum Limit
        ↓
Possible Industrial Attack
        ↓
DANGER
```

Implemented safety limits:

```
Maximum RPM       : 5000
Maximum Pressure  : 120
Maximum Flow Rate : 1000
Minimum Pressure  : 20
```

---

## 🔹 IPS Firewall Decision Layer

The IPS evaluates the physics result and takes action:

| Machine Status | IPS Action |
| -------------- | ---------- |
| SAFE           | ALLOW      |
| WARNING        | MONITOR    |
| DANGER         | BLOCK      |

Example:

```
Malicious Command
        ↓
Physics Engine
        ↓
DANGER
        ↓
IPS BLOCK
```

---

# 🖥️ Industrial Dashboard

The VoltGuard dashboard is built using:

* PyQt5
* Matplotlib

Dashboard features:

✅ Machine status monitoring
✅ Sensor value display
✅ Health indicator
✅ Alarm panel
✅ Event logging
✅ Real-time sensor graph
✅ Network security monitoring
✅ Predicted vs Actual physics comparison

---

# 📂 Project Structure

```
VoltGuard/
│
├── dashboard/
│   └── dashboard.py
│
├── physics/
│   ├── physics.py
│   ├── validator.py
│   ├── simulation.py
│   └── constants.py
│
├── ips/
│   ├── firewall.py
│   └── __init__.py
│
├── parser/
│   ├── C++ Modbus Parser
│   └── output.json
│
├── modbus_reader.py
├── modbus_sender.py
├── scapy_test.py
├── main.py
│
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YPragati/VoltGuard.git
```

Move into project directory:

```bash
cd VoltGuard
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Required libraries:

* PyQt5
* Matplotlib
* Scapy
* pymodbus

---

# ▶️ Running the Project

## Run Physics Engine Test

```bash
python main.py
```

Example output:

```
Machine Values:
{
'rpm':3000,
'pressure':80,
'flow_rate':500
}

Machine Status:
SAFE

IPS Action:
ALLOW
```

---

## Run Dashboard

```bash
python -m dashboard.dashboard
```

The dashboard displays:

* Machine condition
* Sensor values
* Security status
* Real-time graphs

---

# 🧪 Testing Scenarios

## Test 1: Normal Command

Input:

```
RPM: 3000
Pressure: 80
Flow Rate: 500
```

Result:

```
SAFE
ALLOW
```

---

## Test 2: Abnormal Condition

Input:

```
Pressure: 10
```

Result:

```
WARNING
MONITOR
```

Reason:

```
Pressure below safe operating range
```

---

## Test 3: Malicious Command

Input:

```
RPM: 7000
Pressure: 150
```

Result:

```
DANGER
BLOCK
```

Reason:

```
Physical limit exceeded
Possible industrial attack detected
```

---

# 🔐 Cybersecurity Approach

VoltGuard provides security through:

### Traditional Approach

```
Packet Signature Detection
```

### VoltGuard Approach

```
Network Command
        +
Physical Behaviour Validation
        +
IPS Decision
```

This allows detection of attacks that may appear valid at the protocol level but are physically unsafe.

---

# 🌐 Future Deployment

The system architecture supports deployment on an edge computing device such as:

* Raspberry Pi
* Industrial Edge Gateway

Deployment concept:

```
PLC
 |
 |
Ethernet
 |
Raspberry Pi Edge Device
 |
 |-- Modbus Parser
 |-- Physics Engine
 |-- IPS Firewall
 |
Machine Network
```

The edge device can operate as a **bump-in-the-wire IPS**, inspecting commands before they reach industrial equipment.

---

# 👥 Team

**Team 03 - VoltGuard**

Project developed as part of an Industrial Cybersecurity Internship.

---

# 📌 Conclusion

VoltGuard demonstrates a physics-aware cybersecurity approach for industrial environments by combining:

* Industrial protocol analysis
* Physics-based anomaly detection
* Intrusion prevention
* Real-time monitoring

The project provides a foundation for protecting future Industrial Control Systems against cyber-physical attacks.
