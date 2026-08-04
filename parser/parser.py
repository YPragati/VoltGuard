class PacketParseError(ValueError):
    pass


def _parse_float(value, name):
    try:
        return float(value)
    except (TypeError, ValueError):
        raise PacketParseError(f"Invalid {name}: {value}")


def parse_packet(raw):
    if not isinstance(raw, dict):
        raise PacketParseError("Packet must be a dict")

    required_fields = ["packet_id", "rpm", "pressure", "flow_rate"]
    for field in required_fields:
        if field not in raw:
            raise PacketParseError(f"Missing {field}")

    return {
        "packet_id": raw["packet_id"],
        "rpm": _parse_float(raw["rpm"], "rpm"),
        "pressure": _parse_float(raw["pressure"], "pressure"),
        "flow_rate": _parse_float(raw["flow_rate"], "flow_rate"),
    }
