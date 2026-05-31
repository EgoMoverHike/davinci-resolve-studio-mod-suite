cmake_minimum_required(VERSION 3.10)
project(davinci_resolve_studio_mod_suite)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(davinci_mod_suite
    src/main.cpp
    src/resolve_api.cpp
    src/license_manager.cpp
    src/utils/logger.cpp
)

target_include_directories(davinci_mod_suite PRIVATE include)
target_link_libraries(davinci_mod_suite PRIVATE fmt)