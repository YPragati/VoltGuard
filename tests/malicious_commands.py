import json


def normal_command():
    return {
        "rpm": 3000,
        "pressure": 80,
        "flow_rate": 500
    }


def high_rpm_attack():
    return {
        "rpm": 9000,
        "pressure": 80,
        "flow_rate": 500
    }


def negative_pressure_attack():
    return {
        "rpm": 3000,
        "pressure": -50,
        "flow_rate": 500
    }


def excessive_flow_attack():
    return {
        "rpm": 3000,
        "pressure": 80,
        "flow_rate": 5000
    }


tests = {
    "Normal Command": normal_command(),
    "High RPM Attack": high_rpm_attack(),
    "Negative Pressure Attack": negative_pressure_attack(),
    "Excessive Flow Attack": excessive_flow_attack()
}


for name, data in tests.items():
    print("\nTest:", name)
    print(json.dumps(data, indent=4))