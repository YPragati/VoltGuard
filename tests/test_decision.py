from decision.decision import make_decision, evaluate_command


def test_safe_maps_to_allow():
    assert make_decision("SAFE") == "ALLOW"


def test_warning_maps_to_alert():
    assert make_decision("WARNING") == "ALERT"


def test_danger_maps_to_block():
    assert make_decision("DANGER") == "BLOCK"


def test_invalid_maps_to_block():
    assert make_decision("INVALID") == "BLOCK"


def test_unknown_verdict_fails_safe_to_block():
    assert make_decision("SOMETHING_UNEXPECTED") == "BLOCK"


def test_evaluate_command_full_flow():
    fake_command = {"packet_id": 42, "rpm": 3000, "pressure": 100, "flow_rate": 200}

    def fake_process_command(cmd):
        return "SAFE"

    result = evaluate_command(fake_command, fake_process_command)
    assert result["packet_id"] == 42
    assert result["verdict"] == "SAFE"
    assert result["action"] == "ALLOW"
