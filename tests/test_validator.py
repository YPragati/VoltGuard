"""
Tests for physics/validator.py

Covers:
- Missing required fields (rpm, pressure, flow_rate)
- Negative value rejection
- Valid command passes validation
"""

import pytest
from physics.validator import validate_command


# ---------- Valid input ----------

def test_valid_command_passes():
    command = {"rpm": 3000, "pressure": 100, "flow_rate": 200}
    assert validate_command(command) is True


# ---------- Missing fields ----------

def test_missing_rpm_raises():
    command = {"pressure": 100, "flow_rate": 200}
    with pytest.raises(ValueError, match="Missing rpm"):
        validate_command(command)


def test_missing_pressure_raises():
    command = {"rpm": 3000, "flow_rate": 200}
    with pytest.raises(ValueError, match="Missing pressure"):
        validate_command(command)


def test_missing_flow_rate_raises():
    command = {"rpm": 3000, "pressure": 100}
    with pytest.raises(ValueError, match="Missing flow_rate"):
        validate_command(command)


def test_empty_command_raises():
    command = {}
    with pytest.raises(ValueError):
        validate_command(command)


# ---------- Negative values ----------

def test_negative_rpm_raises():
    command = {"rpm": -100, "pressure": 100, "flow_rate": 200}
    with pytest.raises(ValueError, match="RPM cannot be negative"):
        validate_command(command)


def test_negative_pressure_raises():
    command = {"rpm": 3000, "pressure": -10, "flow_rate": 200}
    with pytest.raises(ValueError, match="Pressure cannot be negative"):
        validate_command(command)


def test_negative_flow_rate_raises():
    command = {"rpm": 3000, "pressure": 100, "flow_rate": -50}
    with pytest.raises(ValueError, match="Flow rate cannot be negative"):
        validate_command(command)


# ---------- Boundary case ----------

def test_zero_values_are_allowed():
    """
    Zero is not negative, so this should currently pass validation.
    NOTE: flagging this as a QA observation, not necessarily a bug —
    confirm with the team whether rpm/pressure/flow_rate of exactly 0
    should be considered a valid physical state.
    """
    command = {"rpm": 0, "pressure": 0, "flow_rate": 0}
    assert validate_command(command) is True
