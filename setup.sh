#!/bin/bash

# Setup script for The Chaos Bringer of Schools Doom
# Installs Python dependencies and sets up the tools

echo "Setting up The Chaos Bringer..."

# Install Python dependencies
if command -v pip &> /dev/null; then
    pip install -r requirements.txt
    echo "Python dependencies installed."
else
    echo "pip not found. Please install Python and pip."
    exit 1
fi

# Make scripts executable
chmod +x attract_wifi.sh

echo "Setup complete. You can now run the scripts:"
echo "- python chaos_ai.py for the chatbot"
echo "- python chaos_game.py for the game (requires display)"
echo "- ./attract_wifi.sh for wifi scanning"
echo "- Load the extension folder in Chrome for ad blocking"