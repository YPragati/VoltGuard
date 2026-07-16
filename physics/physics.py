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
        "rpm": 3000,
        "pressure": 100,
        "flow_rate": 5000
    }

    try:
        print(process_command(command))
    except Exception as e:
        print("Error:", e)