#!/bin/bash

# Script to scan for available WiFi networks
# This "attracts" WiFi by listing nearby networks you can connect to

echo "Scanning for WiFi networks..."

nmcli device wifi list

echo "Scan complete. Use nmcli to connect to a network."