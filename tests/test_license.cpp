#include <gtest/gtest.h>
#include "license_manager.h"

TEST(LicenseTest, GenerateAndValidate) {
    license::LicenseManager lm;
    std::string license_key = lm.generate_2026_license();
    EXPECT_TRUE(lm.validate_license(license_key));
    EXPECT_EQ(license_key.size(), 32);
}

TEST(LicenseTest, InvalidLicense) {
    license::LicenseManager lm;
    EXPECT_FALSE(lm.validate_license("INVALID_KEY"));
}