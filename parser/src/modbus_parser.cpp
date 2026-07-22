#include "../include/modbus_parser.hpp"
#include <iostream>
#include <fstream>

bool ModbusParser::parsePacket(const unsigned char* data, int length)
{
    if (length < 8)
    {
        std::cout << "Invalid Modbus packet." << std::endl;
        return false;
    }
//-------------
// MBAP Header
//-------------
    int transactionId = (data[0] << 8) | data[1];
    int protocolId = (data[2] << 8) | data[3];
    int modbusLength = (data[4] << 8) | data[5];
    int unitId = data[6];
//-------------    
//  Modbus PDU 
//-------------   
    int functionCode = data[7];
    int startAddress = (data[8] << 8) | data[9];
    int quantity = (data[10] << 8) | data[11];

    std::ofstream out("parser/output.json", std::ios::out | std::ios::trunc);

    if (!out.is_open())
{
    std::cout << "Failed to open output.json" << std::endl;
    return false;
}

std::cout << "output.json opened successfully" << std::endl;

    out << "{\n";
    out << "  \"transaction_id\": " << transactionId << ",\n";
    out << "  \"protocol_id\": " << protocolId << ",\n";
    out << "  \"length\": " << modbusLength << ",\n";
    out << "  \"unit_id\": " << unitId << ",\n";
    out << "  \"function_code\": " << functionCode << ",\n";
    out << "  \"start_address\": " << startAddress << ",\n";
    out << "  \"quantity\": " << quantity << "\n";
    out << "}\n";
    
    std::cout << "Transaction ID: " << transactionId << std::endl;
    std::cout << "Protocol ID: " << protocolId << std::endl;
    std::cout << "Modbus Length: " << modbusLength << std::endl;
    std::cout << "Unit ID: " << unitId << std::endl;
    std::cout << "Function Code: " << functionCode << std::endl;
    std::cout << "Starting Address: " << startAddress << std::endl;
    std::cout << "Quantity: " << quantity << std::endl;
    
    std::cout << "Packet received." << std::endl;
    std::cout << "Packet Length: " << length << std::endl;

    out.close();

    return true;
}