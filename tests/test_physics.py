from physics.physics import process_command

test_cases = [
    {
        "name": "SAFE Test",
        "command": {
            "rpm": 3000,
            "pressure": 80,
            "flow_rate": 500
        }
    },
    {
        "name": "DANGER Test",
        "command": {
            "rpm": 7000,
            "pressure": 80,
            "flow_rate": 500
        }
    },
    {
        "name": "Invalid RPM",
        "command": {
            "rpm": -100,
            "pressure": 80,
            "flow_rate": 500
        }
    }
]

for test in test_cases:
    print(test["name"])

    try:
        result = process_command(test["command"])
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

    print("-" * 30)