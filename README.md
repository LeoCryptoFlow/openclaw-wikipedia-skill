# OpenClaw Skills Collection

A collection of skills for OpenClaw that includes:

1. Wikipedia Skill - Search Wikipedia and retrieve article summaries in multiple languages
2. Gmail Skill - Manage Gmail inbox, read emails, and search messages

## Wikipedia Skill

### Features

- Search Wikipedia articles in multiple languages (Chinese, English, Japanese, Korean)
- Retrieve article summaries with customizable length
- Get article titles, descriptions, and direct links
- Multi-language search capability

### Installation

#### Method 1: Using the .skill file

1. Download the `wikipedia.skill` file from releases
2. Place it in your OpenClaw skills directory
3. Restart OpenClaw

#### Method 2: Manual installation

1. Clone this repository
2. Copy the `wikipedia` folder to your OpenClaw skills directory
3. Install dependencies: `pip3 install requests`

### Usage

Once installed, you can use this skill to search Wikipedia content:

```bash
# Search in Chinese (default)
python3 {baseDir}/scripts/search.py "人工智能"

# Search in English
python3 {baseDir}/scripts/search.py "artificial intelligence" --lang en

# Search in multiple languages
python3 {baseDir}/scripts/search.py "Sun Wukong" --multi-lang
```

## Gmail Skill

### Features

- List emails with custom queries
- View unread emails
- Search emails by sender, subject, date, etc.
- Read email details

### Installation

#### Method 1: Using the .skill file

1. Download the `gmail.skill` file from releases
2. Place it in your OpenClaw skills directory
3. Restart OpenClaw

#### Method 2: Manual installation

1. Clone this repository
2. Copy the `gmail` folder to your OpenClaw skills directory
3. Install dependencies: `pip3 install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2`

### Setup

Before using the Gmail skill, you need to:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API for your project
4. Create credentials (OAuth 2.0 Client IDs)
5. Download the credentials JSON file
6. Save it as `~/.openclaw/gmail_credentials.json`

### Usage

```bash
# List all emails
python3 {baseDir}/scripts/gmail_basic.py list

# List emails from a specific sender
python3 {baseDir}/scripts/gmail_basic.py list "from:someone@example.com" 5

# List unread emails
python3 {baseDir}/scripts/gmail_basic.py unread 10
```

## License

MIT License