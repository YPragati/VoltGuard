#include "../include/modbus_parser.hpp"
#include <iostream>

bool ModbusParser::parsePacket(const unsigned char* data, int length)
{
    if (length < 8)
    {
        std::cout << "Invalid Modbus packet." << std::endl;
        return false;
    }

    int transactionId = (data[0] << 8) | data[1];
    int protocolId = (data[2] << 8) | data[3];
    int modbusLength = (data[4] << 8) | data[5];
    int unitId = data[6];
    int functionCode = data[7];

    std::cout << "Transaction ID: " << transactionId << std::endl;
    std::cout << "Protocol ID: " << protocolId << std::endl;
    std::cout << "Modbus Length: " << modbusLength << std::endl;
    std::cout << "Unit ID: " << unitId << std::endl;
    std::cout << "Function Code: " << functionCode << std::endl;
    
    std::cout << "Packet received." << std::endl;
    std::cout << "Packet Length: " << length << std::endl;

    return true;
}