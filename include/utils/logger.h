#pragma once
#include <string>
#include <fmt/core.h>

namespace utils {

class Logger {
public:
    static void log(const std::string& message);
    static void error(const std::string& message);
};

} // namespace utils