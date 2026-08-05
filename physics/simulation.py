from .constants import *


def evaluate(rpm, pressure, flow_rate):

    reasons = []

    if rpm > MAX_RPM:
        reasons.append("RPM exceeds physical limit")

    if pressure > MAX_PRESSURE:
        reasons.append("Pressure exceeds physical limit")

    if pressure < MIN_PRESSURE:
        reasons.append("Pressure below safe operating range")

    if flow_rate > MAX_FLOW_RATE:
        reasons.append("Flow rate exceeds physical limit")


    if "RPM exceeds physical limit" in reasons or \
       "Pressure exceeds physical limit" in reasons:

        return {
            "status": "DANGER",
            "security_alert": "Possible Modbus manipulation detected",
            "reason": reasons
        }


    if reasons:
        return {
            "status": "WARNING",
            "security_alert": "Abnormal machine behaviour detected",
            "reason": reasons
        }


    return {
        "status": "SAFE",
        "security_alert": "None",
        "reason": "Machine operating normally"
    }