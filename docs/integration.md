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

```
User Input / Parser
        │
        ▼
 Physics Module
        │
        ▼
SAFE / WARNING / DANGER
        │
        ▼
 PyQt Dashboard
```

## Developed By

- Team Lead
- Physics Module Developer
- Dashboard Developer (Member 3 responsibilities completed after member left)