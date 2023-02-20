#!/bin/bash

echo "Removing:"
tree cache
echo
tree ./__pycache__
echo

read -p "Are you sure? [Y/N] " user_input
echo


if [ "${user_input}" == "y" ] || [ "${user_input}" == "Y" ]; then
    cd cache
    rm -rf *
    cd ../__pycache__
    rm -rf *
    echo "Cache cleared"
    exit 0

elif [ "${user_input}" == "n" ] || [ "${user_input}" == "N" ]; then
    echo "Exiting..."
    exit 0

else
    echo "Invalid input. Exiting..."
    exit 1
fi

echo "Done."