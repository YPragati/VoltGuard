cmake_minimum_required(VERSION 3.10)

project(ModbusParser)

set(CMAKE_CXX_STANDARD 17)

include_directories(include)

add_executable(parser
    src/main.cpp
    src/modbus_parser.cpp
)