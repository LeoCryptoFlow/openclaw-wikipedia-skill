# OpenClaw Wikipedia Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://github.com/openclaw/openclaw)

A skill for OpenClaw that allows searching Wikipedia and retrieving article summaries in multiple languages.

## 🚀 Features

- Search Wikipedia articles in multiple languages (Chinese, English, Japanese, Korean)
- Retrieve article summaries with customizable length
- Get article titles, descriptions, and direct links
- Multi-language search capability
- Easy integration with OpenClaw ecosystem

## 📋 Requirements

- [OpenClaw](https://github.com/openclaw/openclaw)
- Python 3.6+
- `requests` library

## 📦 Installation

### Option 1: Using the .skill file (Recommended)

1. Download the latest release from the [Releases](https://github.com/your-username/openclaw-wikipedia-skill/releases) page
2. Place the `.skill` file in your OpenClaw skills directory
3. Restart OpenClaw

### Option 2: Manual Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/openclaw-wikipedia-skill.git
   cd openclaw-wikipedia-skill
   ```

2. Run the installation script:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

### Option 3: Using the install script directly

```bash
curl -O https://raw.githubusercontent.com/your-username/openclaw-wikipedia-skill/main/install.sh
chmod +x install.sh
./install.sh
```

## 🔍 Usage

Once installed, you can use the skill in several ways:

### Command Line

```bash
# Search in Chinese (default)
python3 ~/.openclaw/workspace/skills/wikipedia/scripts/search.py "人工智能"

# Search in English
python3 ~/.openclaw/workspace/skills/wikipedia/scripts/search.py "artificial intelligence" --lang en

# Search in multiple languages
python3 ~/.openclaw/workspace/skills/wikipedia/scripts/search.py "Sun Wukong" --multi-lang

# Get more sentences (default is 3)
python3 ~/.openclaw/workspace/skills/wikipedia/scripts/search.py "machine learning" --sentences 5
```

### Integration with OpenClaw

The skill integrates seamlessly with OpenClaw and can be used to:
- Fetch factual information for AI responses
- Retrieve knowledge from Wikipedia
- Cross-reference information in multiple languages
- Enhance AI agent capabilities with up-to-date information

## 🌐 Supported Languages

- Chinese (zh) - Default
- English (en)
- Japanese (ja)
- Korean (ko)

## 🧪 Examples

Check out the [examples](./examples/) directory for more usage scenarios.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to Wikipedia for providing the API
- Thanks to the OpenClaw community for the amazing framework