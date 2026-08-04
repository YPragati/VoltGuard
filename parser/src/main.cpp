#include "../include/modbus_parser.hpp"

int main()
{
    ModbusParser parser;

  unsigned char packet[] = {
    0x00, 0x01,   // Transaction ID
    0x00, 0x00,   // Protocol ID
    0x00, 0x0B,   // Length
    0x01,         // Unit ID
    0x10,         // Function Code (Write Multiple Registers)
    0x00, 0x10,   // Starting Address = 16
    0x00, 0x02,   // Quantity of registers = 2
    0x04,         // Byte Count = 4
    0x00, 0x0A,   // Register 1 = 10
    0x00, 0x14    // Register 2 = 20
};

    parser.parsePacket(packet, sizeof(packet));

    return 0;
}