"""
VoltGuard Physics Engine
Week 1: Basic Physics Safety Evaluation
"""

MAX_PRESSURE = 120.0      # PSI
MIN_PRESSURE = 20.0       # PSI
MAX_RPM = 5000            # Pump RPM
MAX_FLOW_RATE = 1000.0    # L/min


def evaluate_command(rpm, pressure, flow_rate):
    """
    Evaluate whether an industrial command is safe.
    Returns:
        SAFE
        WARNING
        DANGER
    """

    if rpm > MAX_RPM:
        return "DANGER", "Pump RPM exceeds safe operating limit."

    if pressure > MAX_PRESSURE:
        return "DANGER", "Pressure exceeds safety threshold."

    if pressure < MIN_PRESSURE:
        return "WARNING", "Pressure below recommended level."

    if flow_rate > MAX_FLOW_RATE:
        return "WARNING", "Flow rate is higher than expected."

    return "SAFE", "Operating within normal limits."


if __name__ == "__main__":
    status, message = evaluate_command(
        rpm=3500,
        pressure=80,
        flow_rate=600
    )

    print(status)
    print(message)