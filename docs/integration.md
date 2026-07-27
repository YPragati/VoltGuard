Physics Module Integration Guide

Input:
- rpm
- pressure
- flow_rate

Output:
- SAFE
- WARNING
- DANGER

How to Run:
python -m physics.physics

Example Input:
{
  "rpm": 5000,
  "pressure": 80,
  "flow_rate": 500
}

Expected Output:
SAFE