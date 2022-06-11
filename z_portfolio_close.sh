#!/bin/bash

echo "Removing Docker files:"
docker-compose down
echo

echo "Removing all CSV files:"
rm -v outputs/*

echo "All files removed succesfully."