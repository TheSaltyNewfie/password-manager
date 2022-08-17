#include <iostream>
#include <stdexcept>
#include <stdio.h>
#include <string>

inline std::string exec(std::string cmd) {
    char buffer[128];
    std::string result = "";
    std::cout << "cmd = " << cmd << std::endl;
    FILE* pipe = popen(cmd.c_str(), "r");
    if (!pipe) throw std::runtime_error("popen() failed!");
    try {
        while (fgets(buffer, sizeof buffer, pipe) != NULL) {
            result += buffer;
        }
    } catch (...) {
        pclose(pipe);
        throw;
    }
    pclose(pipe);
    std::cout << "result = " << result << std::endl;
    return result;
}
