# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.20.0)

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(lvgl)

FILE(GLOB lvglui_sources ui/*.py)
add_custom_target(lvglui_gen
    COMMAND poetry run python -m ui
    WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}
    COMMENT "Generate lvglui sources"
    DEPENDS ${lvglui_sources}
)
add_dependencies(app lvglui_gen)

FILE(GLOB lvglui_gen_sources src/ui/*.c)
target_sources(app PRIVATE src/main.c ${lvglui_gen_sources})
