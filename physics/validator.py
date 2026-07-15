def validate_command(command):
    required = ["rpm", "pressure", "flow_rate"]

    for field in required:
        if field not in command:
            raise ValueError(f"Missing {field}")

    if command["rpm"] < 0:
        raise ValueError("RPM cannot be negative")

    if command["pressure"] < 0:
        raise ValueError("Pressure cannot be negative")

    if command["flow_rate"] < 0:
        raise ValueError("Flow rate cannot be negative")

    return True