#include "../include/modbus_parser.hpp"

int main()
{
    ModbusParser parser;

    unsigned char packet[] = {
    0x00, 0x01,
    0x00, 0x00,
    0x00, 0x06,
    0x01,
    0x06,
    0x00, 0x10,
    0x00, 0xFF
};

    parser.parsePacket(packet, sizeof(packet));

    return 0;
}