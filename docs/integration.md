# VoltGuard Physics Engine Integration

## Input

The physics engine accepts a Python dictionary with:

```json
{
    "rpm": 3500,
    "pressure": 80,
    "flow_rate": 500
}
```

## Output

The engine returns one of:

- SAFE
- WARNING
- DANGER