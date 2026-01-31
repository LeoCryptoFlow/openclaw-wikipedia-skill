# Usage Examples for Wikipedia Skill

## Basic Usage

### Search in Chinese
```bash
python3 {baseDir}/scripts/search.py "人工智能"
```

### Search in English
```bash
python3 {baseDir}/scripts/search.py "artificial intelligence" --lang en
```

### Search in Japanese
```bash
python3 {baseDir}/scripts/search.py "人工知能" --lang ja
```

### Search in Korean
```bash
python3 {baseDir}/scripts/search.py "인공지능" --lang ko
```

## Advanced Usage

### Multi-language search
```bash
# Search for "Sun Wukong" in both Chinese and English
python3 {baseDir}/scripts/search.py "Sun Wukong" --multi-lang

# Search for "孙悟空" in both Chinese and English
python3 {baseDir}/scripts/search.py "孙悟空" --multi-lang
```

### Get more detailed results
```bash
# Get more sentences (default is 3)
python3 {baseDir}/scripts/search.py "machine learning" --sentences 5
```

## Integration with OpenClaw

Once installed, the skill can be used within OpenClaw workflows to:
- Fetch factual information
- Retrieve article summaries
- Gather knowledge for AI responses
- Cross-reference information in multiple languages

## Error Handling

The skill handles various error conditions:
- Page not found (returns 404 error)
- Network connectivity issues
- Invalid language codes
- API rate limiting (depends on Wikipedia's policies)