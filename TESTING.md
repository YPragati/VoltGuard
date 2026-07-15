# Testing Guide — VoltGuard

This document describes how we test each module of VoltGuard.

## Testing Strategy

| Module | What we test | Test type |
|--------|--------------|-----------|
| Packet Interceptor | Correctly parses valid Modbus/DNP3 packets, rejects malformed ones | Unit test |
| Physics Engine | Correctly flags unsafe commands (e.g., negative pressure, over-limit RPM) | Unit test |
| Decision Engine | Blocks unsafe commands within required latency (<10ms) | Integration test |
| Dashboard | Displays blocked commands and system status correctly | Manual test |

## How to Run Tests
