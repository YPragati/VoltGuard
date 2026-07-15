from .validator import validate_command
from .simulation import evaluate

def process_command(command):

    validate_command(command)

    return evaluate(
        command["rpm"],
        command["pressure"],
        command["flow_rate"]
    )


if __name__ == "__main__":

    command = {
        "rpm": -5000,
        "pressure": 80,
        "flow_rate": 500
    }

    print(process_command(command))

    