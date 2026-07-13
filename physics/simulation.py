from .constants import *

def evaluate(rpm, pressure, flow_rate):

    if rpm > MAX_RPM:
        return "DANGER"

    if pressure > MAX_PRESSURE:
        return "DANGER"

    if pressure < MIN_PRESSURE:
        return "WARNING"

    if flow_rate > MAX_FLOW_RATE:
        return "WARNING"

    return "SAFE"