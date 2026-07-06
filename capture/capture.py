
import random

def generate_packet():
    packet = {
        "packet_id": random.randint(1000, 9999),
        "pressure": random.randint(20, 300),
        "rpm": random.randint(1000, 10000),
        "temperature": random.randint(20, 150)
    }

    return packet


if __name__ == "__main__":
    print(generate_packet())