# Modbus Packet Parser

This module implements the Modbus/TCP packet parser for VoltGuard.

Current status:
- Project structure initialized
- Basic parser class created
- Sample packet test added

Next steps:
- Parse MBAP header
- Decode Modbus function codes
- Extract register addresses and values
- Validate malformed packets
## JSON Output

The parser exports parsed Modbus packet fields to `parser/output.json`.

Example:

```json
{
  "transaction_id": 1,
  "protocol_id": 0,
  "length": 6,
  "unit_id": 1,
  "function_code": 3,
  "start_address": 0,
  "quantity": 1
}
```