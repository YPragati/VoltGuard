def inspect_packet(result):

    status = result["status"]

    if status == "DANGER":
        return {
            "action": "BLOCK",
            "reason": result["reason"],
            "security_alert": result["security_alert"]
        }

    elif status == "WARNING":
        return {
            "action": "MONITOR",
            "reason": result["reason"],
            "security_alert": result["security_alert"]
        }

    else:
        return {
            "action": "ALLOW",
            "reason": "Normal machine operation",
            "security_alert": "None"
        }


if __name__ == "__main__":

    test_result = {
        "status": "DANGER",
        "security_alert": "Possible Modbus manipulation detected",
        "reason": ["Pressure exceeds physical limit"]
    }

    print(inspect_packet(test_result))