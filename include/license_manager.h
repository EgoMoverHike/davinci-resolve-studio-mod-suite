#pragma once
#include <string>

namespace license {

class LicenseManager {
public:
    bool validate_license(const std::string& key);
    std::string generate_2026_license();
    bool patch_binary(const std::string& resolve_path);
};

} // namespace license