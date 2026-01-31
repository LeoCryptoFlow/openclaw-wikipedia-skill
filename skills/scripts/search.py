#!/usr/bin/env python3
"""
Wikipedia search tool for OpenClaw
Allows searching Wikipedia and retrieving article summaries
"""

import argparse
import json
import requests
import urllib.parse
from typing import Dict, Optional


def search_wikipedia(query: str, lang: str = "zh", sentences: int = 3) -> Dict:
    """
    Search Wikipedia for a given query
    
    Args:
        query: Search term
        lang: Language code (default: zh for Chinese)
        sentences: Number of sentences to return (default: 3)
    
    Returns:
        Dictionary with search results
    """
    # Construct the Wikipedia API URL
    base_url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/"
    encoded_query = urllib.parse.quote(query.replace(' ', '_'))
    url = f"{base_url}{encoded_query}"
    
    headers = {
        "User-Agent": "OpenClaw-Wikipedia-Tool/1.0 (contact@openclaw.ai)"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        return {
            "success": True,
            "title": data.get("title", ""),
            "extract": data.get("extract", ""),
            "url": data.get("content_urls", {}).get("desktop", {}).get("page", ""),
            "description": data.get("description", ""),
            "lang": lang
        }
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {
                "success": False,
                "error": f"Page '{query}' not found in {lang} Wikipedia",
                "error_code": 404
            }
        else:
            return {
                "success": False,
                "error": f"HTTP error occurred: {e}",
                "error_code": e.response.status_code
            }
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"Request error occurred: {e}",
            "error_code": None
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"An unexpected error occurred: {e}",
            "error_code": None
        }


def search_multiple_languages(query: str, languages: list = ["zh", "en"]) -> Dict:
    """
    Search Wikipedia in multiple languages
    
    Args:
        query: Search term
        languages: List of language codes to search
    
    Returns:
        Dictionary with results from all languages
    """
    results = {}
    
    for lang in languages:
        result = search_wikipedia(query, lang)
        results[lang] = result
    
    return results


def main():
    parser = argparse.ArgumentParser(description='Search Wikipedia and retrieve article summaries')
    parser.add_argument('query', nargs='+', help='Search terms')
    parser.add_argument('--lang', default='zh', choices=['zh', 'en', 'ja', 'ko'], 
                       help='Language for search (default: zh)')
    parser.add_argument('--sentences', type=int, default=3, 
                       help='Number of sentences to return (default: 3)')
    parser.add_argument('--multi-lang', action='store_true',
                       help='Search in multiple languages (Chinese and English)')
    
    args = parser.parse_args()
    
    query = ' '.join(args.query)
    
    if args.multi_lang:
        results = search_multiple_languages(query, ['zh', 'en'])
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        result = search_wikipedia(query, args.lang, args.sentences)
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()