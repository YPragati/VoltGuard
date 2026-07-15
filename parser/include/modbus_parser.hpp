#pragma once

class ModbusParser {
public:
    bool parsePacket(const unsigned char* data, int length);
};