import socket

HOST = "127.0.0.1"
PORT = 502

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # Example Modbus TCP packet
    packet = bytes([
        0x00, 0x01,   # Transaction ID
        0x00, 0x00,   # Protocol ID
        0x00, 0x06,   # Length
        0x01,         # Unit ID
        0x03,         # Function Code (Read Holding Registers)
        0x00, 0x00,   # Start Address
        0x00, 0x02    # Quantity
    ])

    s.send(packet)
    print("Modbus packet sent!")

    s.close()

except Exception as e:
    print("Error:", e)