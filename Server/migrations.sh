#!/bin/bash

if [ "$0" = "" ]; then
    echo "Enter 'up' or 'down' to run/revert migrations"
    exit 1
fi

if [ "$1" = up ]; then 
    find sql -name 'up.sql' -exec psql -U server -d server -a -f {}  \;
elif [ "$1" = down ]; then
    find sql -name 'down.sql' -exec psql -U server -d server -a -f {} \;
else
    echo "that was not up or down..."
    exit 1
fi
