---
name: wikipedia
description: "Search Wikipedia and retrieve article summaries in multiple languages. Supports Chinese, English, Japanese, and Korean."
metadata: {"openclaw":{"emoji":"📚","requires":{"bins":["python3"],"pip":["requests"]},"install":[{"id":"python-brew","kind":"brew","formula":"python","bins":["python3"],"label":"Install Python (brew)"},{"id":"pip-requests","kind":"pip","package":"requests","label":"Install requests library"}]}}
---

# Wikipedia Skill

Search Wikipedia and retrieve article summaries in multiple languages. This skill allows you to access Wikipedia content programmatically through OpenClaw.

## Features

- Search Wikipedia articles in multiple languages (Chinese, English, Japanese, Korean)
- Retrieve article summaries with customizable length
- Get article titles, descriptions, and direct links
- Multi-language search capability

## Requirements

- Python 3
- `requests` library

## Usage

### Command Line Interface

```bash
# Basic search in Chinese (default)
python3 {baseDir}/scripts/search.py "人工智能"

# Search in English
python3 {baseDir}/scripts/search.py "artificial intelligence" --lang en

# Search in multiple languages (Chinese and English)
python3 {baseDir}/scripts/search.py "量子计算" --multi-lang

# Get more sentences (default is 3)
python3 {baseDir}/scripts/search.py "区块链" --sentences 5
```

### From OpenClaw

The skill provides functions to search Wikipedia programmatically. When you ask questions about general knowledge, this skill will automatically be used to fetch information from Wikipedia.

## Examples

```bash
# Search for "Superman" in English
python3 {baseDir}/scripts/search.py "Superman" --lang en

# Search for "太阳系" in Chinese
python3 {baseDir}/scripts/search.py "太阳系"

# Compare results in multiple languages
python3 {baseDir}/scripts/search.py "爱因斯坦" --multi-lang
```

## Parameters

- `query`: Search term(s) to look up on Wikipedia
- `--lang`: Language code (zh=Chinese, en=English, ja=Japanese, ko=Korean) (default: zh)
- `--sentences`: Number of sentences to retrieve from the summary (default: 3)
- `--multi-lang`: Search in multiple languages simultaneously

## Output

The tool returns a JSON object containing:
- `success`: Boolean indicating if the search was successful
- `title`: Article title
- `extract`: Article summary/extract
- `url`: Direct URL to the Wikipedia article
- `description`: Brief description of the topic
- `lang`: Language of the article

## Error Handling

- If an article is not found, the tool returns an error with code 404
- Network errors are caught and reported appropriately
- Invalid inputs are handled gracefully