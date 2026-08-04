#include "../include/modbus_parser.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

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

    if (protocolId != 0)
{
    std::cout << "Invalid Modbus Protocol ID: " << protocolId << std::endl;
    return false;
}


    int modbusLength = (data[4] << 8) | data[5];

    if (modbusLength != length - 6)
{
    std::cout << "Invalid Modbus Length field." << std::endl;
    return false;
}


    int unitId = data[6];


//-------------    
//  Modbus PDU 
//-------------   
    int functionCode = data[7];
    std::string functionName;

    int startAddress = (data[8] << 8) | data[9];

    int value = (data[10] << 8) | data[11];

int byteCount = 0;

if (functionCode == 16)
{
    byteCount = data[12];
}

std::vector<int> registerValues;

if (functionCode == 16)
{
    for (int i = 13; i < 13 + byteCount; i += 2)
    {
        int regValue = (data[i] << 8) | data[i + 1];
        registerValues.push_back(regValue);
    }
}
    switch (functionCode)
{
    case 1:
        functionName = "Read Coils";
        break;

    case 2:
        functionName = "Read Discrete Inputs";
        break;

    case 3:
        functionName = "Read Holding Registers";
        break;

    case 4:
        functionName = "Read Input Registers";
        break;

    case 5:
        functionName = "Write Single Coil";
        break;

    case 6:
        functionName = "Write Single Register";
        break;

    case 16:
        functionName = "Write Multiple Registers";
        break;

    default:
        functionName = "Unknown";
}
if (functionName == "Unknown")
{
    std::cout << "Unsupported Function Code: "
              << functionCode << std::endl;
    return false;
}



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
    out << "  \"function_name\": \"" << functionName << "\",\n";
   out << "  \"start_address\": " << startAddress << ",\n";

if (functionCode == 6)
{
    out << "  \"register_value\": " << value << "\n";
}
else if (functionCode == 16)
{
    out << "  \"quantity\": " << value << ",\n";
    out << "  \"byte_count\": " << byteCount << ",\n";

    out << "  \"register_values\": [";

    for (size_t i = 0; i < registerValues.size(); i++)
    {
        out << registerValues[i];

        if (i != registerValues.size() - 1)
        {
            out << ", ";
        }
    }

    out << "]\n";
}
else
{
    out << "  \"quantity\": " << value << "\n";
}

    out << "}\n";
    out.flush();
    out.close();
    
    std::cout << "Transaction ID: " << transactionId << std::endl;
    std::cout << "Protocol ID: " << protocolId << std::endl;
    std::cout << "Modbus Length: " << modbusLength << std::endl;
    std::cout << "Unit ID: " << unitId << std::endl;

    std::cout << "Function Code: "
          << functionCode
          << " (" << functionName << ")"
          << std::endl;

   
   if (functionCode == 6)
{
    std::cout << "Register Address: " << startAddress << std::endl;
    std::cout << "Register Value: " << value << std::endl;
}
else if (functionCode == 16)
{
    std::cout << "Starting Address: " << startAddress << std::endl;
    std::cout << "Quantity: " << value << std::endl;
    std::cout << "Byte Count: " << byteCount << std::endl;
    std::cout << "Register Values: ";

for (int value : registerValues)
{
    std::cout << value << " ";
}

std::cout << std::endl;
}
else
{
    std::cout << "Starting Address: " << startAddress << std::endl;
    std::cout << "Quantity: " << value << std::endl;
} 
    std::cout << "Packet received." << std::endl;
    std::cout << "Packet Length: " << length << std::endl;

    return true;
}