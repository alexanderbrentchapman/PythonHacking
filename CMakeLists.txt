cmake_minimum_required(VERSION 3.8)
project(PythonHacking)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        CPP_Files/nbproject/private/c_standard_headers_indexer.c
        CPP_Files/nbproject/private/cpp_standard_headers_indexer.cpp
        CPP_Files/NetworkTools/NetSpeed/main.cpp
        Crypto/ShiftCipher/generalShift.py
        Crypto/ShiftCipher/rot13.py
        Crypto/Specific_Encodings/base64.py
        Crypto/Specific_Encodings/hexadecimal_encryption.py
        Crypto/Specific_Encodings/octal_encryption.py
        Crypto/Substitution_Cyphers/substitution_cypher.py
        docs/index.html
        docs/mainstylesheet.css
        NetworkTools/netspeed.cpp
        WebsiteTools/Requests/get_requests.py
        WebsiteTools/Requests/post_requests.py
        WebsiteTools/Sockets/tcp_connection.py
        README.md)

add_executable(PythonHacking ${SOURCE_FILES})