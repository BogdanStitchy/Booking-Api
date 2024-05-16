#!/bin/bash

directories=(
    "app/tests/integration_tests/test_bookings/test_api_bookings.py"
    "app/tests/integration_tests/test_bookings/test_dao_bookings.py"
    "app/tests/integration_tests/test_hotels"
    "app/tests/integration_tests/test_rooms"
    "app/tests/integration_tests/test_users"
    "app/tests/unit_tests/test_users"
)

for dir in "${directories[@]}"; do
    echo "Running tests in $dir"
    pytest "$dir" -v -s -p no:warnings
done