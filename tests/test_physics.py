from physics.simulation import evaluate

def test_safe():
    assert evaluate(rpm=3000, pressure=100, flow_rate=200) == "SAFE"

def test_danger_rpm():
    assert evaluate(rpm=9000, pressure=100, flow_rate=200) == "DANGER"

def test_warning_low_pressure():
    assert evaluate(rpm=3000, pressure=10, flow_rate=200) == "WARNING"
    def test_danger_high_pressure():
    assert evaluate(rpm=3000, pressure=150, flow_rate=200) == "DANGER"

def test_warning_high_flow_rate():
    assert evaluate(rpm=3000, pressure=100, flow_rate=1500) == "WARNING"

def test_boundary_rpm_at_limit():
    assert evaluate(rpm=5000, pressure=100, flow_rate=200) == "SAFE"

def test_boundary_pressure_at_max():
    assert evaluate(rpm=3000, pressure=120.0, flow_rate=200) == "SAFE"

def test_boundary_pressure_at_min():
    assert evaluate(rpm=3000, pressure=20.0, flow_rate=200) == "SAFE"

def test_boundary_flow_rate_at_max():
    assert evaluate(rpm=3000, pressure=100, flow_rate=1000.0) == "SAFE"

def test_danger_rpm_takes_priority_over_pressure():
    assert evaluate(rpm=9000, pressure=150, flow_rate=200) == "DANGER"
