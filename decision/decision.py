class DecisionError(Exception):
    pass


def make_decision(verdict):
    actions = {
        "SAFE": "ALLOW",
        "WARNING": "ALERT",
        "DANGER": "BLOCK",
    }
    return actions.get(str(verdict), "BLOCK")


def evaluate_command(command, process_command):
    try:
        verdict = process_command(command)
    except Exception:
        return {
            "packet_id": command.get("packet_id"),
            "command": command,
            "verdict": "INVALID",
            "action": "BLOCK",
        }

    return {
        "packet_id": command.get("packet_id"),
        "command": command,
        "verdict": verdict,
        "action": make_decision(verdict),
    }
