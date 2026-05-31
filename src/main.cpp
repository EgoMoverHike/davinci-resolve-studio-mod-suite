#include <iostream>
#include "resolve_api.h"
#include "license_manager.h"
#include "utils/logger.h"

int main() {
    utils::Logger::log("Starting DaVinci Resolve Studio Mod Suite 2026");

    resolve::ResolveAPI api;
    if (!api.connect()) {
        utils::Logger::error("Failed to connect to DaVinci Resolve");
        return 1;
    }

    license::LicenseManager lm;
    std::string license_key = lm.generate_2026_license();
    if (!lm.validate_license(license_key)) {
        utils::Logger::error("Generated license is invalid");
        return 1;
    }

    if (!api.apply_license(license_key)) {
        utils::Logger::error("Failed to apply license");
        return 1;
    }

    utils::Logger::log("DaVinci Resolve Studio successfully unlocked");
    return 0;
}