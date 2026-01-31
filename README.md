# OpenClaw Wikipedia Skill

A skill for OpenClaw that allows searching Wikipedia and retrieving article summaries in multiple languages.

## Features

- Search Wikipedia articles in multiple languages (Chinese, English, Japanese, Korean)
- Retrieve article summaries with customizable length
- Get article titles, descriptions, and direct links
- Multi-language search capability

## Requirements

- OpenClaw
- Python 3
- `requests` library

## Installation

### Method 1: Using the .skill file

1. Download the `wikipedia.skill` file from releases
2. Place it in your OpenClaw skills directory
3. Restart OpenClaw

### Method 2: Manual installation

1. Clone this repository
2. Copy the `wikipedia` folder to your OpenClaw skills directory
3. Install dependencies: `pip3 install requests`

## Usage

Once installed, you can use this skill to search Wikipedia content:

```bash
# Search in Chinese (default)
python3 {baseDir}/scripts/search.py "人工智能"

# Search in English
python3 {baseDir}/scripts/search.py "artificial intelligence" --lang en

# Search in multiple languages
python3 {baseDir}/scripts/search.py "Sun Wukong" --multi-lang
```

## License

MIT License