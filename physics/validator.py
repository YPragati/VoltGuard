def validate_command(command):

    required = ["rpm", "pressure", "flow_rate"]

    for field in required:
        if field not in command:
            raise ValueError(f"Missing {field}")

    rpm = command["rpm"]
    pressure = command["pressure"]
    flow = command["flow_rate"]

    # Negative value checks
    if rpm < 0:
        raise ValueError("RPM cannot be negative")

    if pressure < 0:
        raise ValueError("Pressure cannot be negative")

    if flow < 0:
        raise ValueError("Flow rate cannot be negative")

   