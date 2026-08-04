# VoltGuard Physics Module Integration Guide

## Overview

The Physics Module processes machine sensor values and determines the operating condition of the machine.

## Inputs

The module accepts the following parameters:

- RPM (Revolutions Per Minute)
- Pressure
- Flow Rate

Example:

```json
{
  "rpm": 5000,
  "pressure": 80,
  "flow_rate": 500
}
```

## Processing

1. The input values are validated.
2. Missing or negative values generate an error.
3. Valid inputs are passed to the simulation engine.
4. The simulation evaluates the machine condition.

## Outputs

The module returns one of the following:

- SAFE
- WARNING
- DANGER

## Running the Physics Module

```bash
python -m physics.physics
```

## Running the Dashboard

```bash
python -m dashboard.dashboard
```

## Project Workflow

The VoltGuard integration workflow is designed for a physics-aware industrial monitoring pipeline.

```
Raw Packet Input
        │
        ▼
Parser Layer (parser/parser.py)
        │
        ▼
Normalized Command
        │
        ▼
Physics Validation + Simulation (physics/validator.py + physics/simulation.py)
        │
        ▼
Verdict: SAFE / WARNING / DANGER
        │
        ▼
Decision Mapping (decision/decision.py)
        │
        ▼
Dashboard / Live Monitoring (dashboard/dashboard_gui.py)
```

### Detailed flow

- `parser/parser.py` validates and parses raw packet payloads into numeric command fields.
- `physics/validator.py` checks for missing or negative values.
- `physics/simulation.py` evaluates the validated values against safety thresholds.
- `decision/decision.py` converts the physics verdict into a concrete action (`ALLOW`, `ALERT`, or `BLOCK`).
- The dashboard displays live events and logs the result.

## Developed By

- Team Lead
- Physics Module Developer
- Dashboard Developer (Member 3 responsibilities completed after member left)