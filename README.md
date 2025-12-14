# The Chaos Bringer of Schools Doom

A collection of chaotic tools for schools, including an ad blocker, a 4K game, a chatbot, and wifi tools.

## Setup

Run `./setup.sh` to install dependencies and make scripts executable.

## Ad Blocker Extension

## Ad Blocker Extension

A simple Chrome extension that blocks ads.

### Installation

1. Open Chrome and go to `chrome://extensions/`
2. Enable "Developer mode" in the top right.
3. Click "Load unpacked" and select this folder.
4. The extension should now be installed and active.

### How it works

- Uses Declarative Net Request to block network requests to known ad domains.
- Content script hides ad elements and elements asking for money (donate, subscribe, paywall, etc.) on web pages based on selectors.

### Customization

- Edit `rules.json` to add more blocking rules.
- Edit `content.js` to add more selectors for hiding ads and money-requesting elements.

## 4K Chaos Game

A simple Pong-like game that runs in 4K resolution (3840x2160).

### Requirements

- Python 3
- Pygame

### Installation

1. Install dependencies: `pip install -r requirements.txt`

### Running

Run `python chaos_game.py`

Use arrow keys to move the paddle, ESC to quit.

Note: Requires a display capable of 4K. In a dev container, may not display properly.

## Chaos AI Chatbot

A simple rule-based AI chatbot with a chaotic personality.

### Running

Run `python chaos_ai.py`

Type messages and get responses. Type 'quit' to exit.

## WiFi Attractor Script

A bash script to scan for available WiFi networks.

### Running

Run `./attract_wifi.sh` (may require sudo for scanning).