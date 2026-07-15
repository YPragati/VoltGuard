from physics.simulation import evaluate

def test_safe():
    assert evaluate(rpm=3000, pressure=100, flow_rate=200) == "SAFE"

def test_danger_rpm():
    assert evaluate(rpm=9000, pressure=100, flow_rate=200) == "DANGER"

def test_warning_low_pressure():
    assert evaluate(rpm=3000, pressure=10, flow_rate=200) == "WARNING"