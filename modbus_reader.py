from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=502)

if client.connect():
    print("Connected to ModbusPal!")

    result = client.read_holding_registers(
        address=0,
        count=3,
        device_id=1
    )

    print(result)

    if not result.isError():
        print("RPM      :", result.registers[0])
        print("Pressure :", result.registers[1])
        print("Flow Rate:", result.registers[2])
    else:
        print("Read Error:", result)

    client.close()

else:
    print("Connection failed.")