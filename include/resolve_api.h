#pragma once
#include <string>
#include <vector>

namespace resolve {

class ResolveAPI {
public:
    bool connect();
    bool unlock_full_features();
    std::vector<std::string> get_available_features();
    bool apply_license(const std::string& license_key);
};

} // namespace resolve