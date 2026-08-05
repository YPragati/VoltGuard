import json

from ips.firewall import inspect_packet

from physics.physics import process_command


def load_parser_data():

    with open("parser/output.json", "r") as file:
        return json.load(file)


def convert_sensor_data(parser_data):

    registers = parser_data["register_values"]

    command = {
        "rpm": registers[0] * 100,
        "pressure": registers[1],
        "flow_rate": 500
    }

    return command


if __name__ == "__main__":

    parser_data = load_parser_data()

    command = convert_sensor_data(parser_data)

    print("Machine Values:")
    print(command)

    result = process_command(command)

    firewall_result = inspect_packet(result)

    print("\nMachine Status:")
    print(result["status"])

    print("\nSecurity Alert:")
    print(result["security_alert"])

    print("\nReason:")
    print(result["reason"])

    print("\nIPS Action:")
    print(firewall_result["action"])