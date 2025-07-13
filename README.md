# Baidu Search Tool

**Author:** alopha  
**Version:** 0.0.1  
**Type:** Plugin

## Description
The Baidu Search Tool is a Dify plugin that enables AI agents to search for information on Baidu using SerpAPI's service. This tool provides access to Baidu's search engine results, including organic search results, featured snippets, and answer boxes.

## Features
- Search Baidu for current information and news
- Retrieve organic search results with titles, links, and snippets
- Access featured snippets and answer boxes
- Configurable number of results (1-100)
- Multi-language support (English, Chinese, Portuguese, Japanese)
- Secure API key management

## Installation
1. Clone or download this plugin to your Dify plugins directory
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your SerpAPI key in the Dify interface

## Configuration
### Required Credentials
- **SerpAPI Key**: Your API key from SerpAPI dashboard
  - Get your key from: https://serpapi.com/dashboard
  - This key is used to authenticate with SerpAPI's service

### Parameters
- **Search Query** (required): The search term or phrase to search for on Baidu
- **Number of Results** (optional): Number of results to return (1-100, default: 10)

## Usage Examples

### Basic Search
```
Search for "coffee" on Baidu
```

### Search with Specific Number of Results
```
Search for "artificial intelligence" on Baidu and return 20 results
```

### Information Lookup
```
Find information about "climate change" on Baidu
```

## API Response Format
The tool returns search results in the following format:
```json
{
  "query": "search term",
  "total_results": 34600000,
  "organic_results": [
    {
      "position": 1,
      "title": "Result Title",
      "link": "https://example.com",
      "snippet": "Result description...",
      "displayed_link": "example.com",
      "thumbnail": "https://thumbnail-url.com"
    }
  ],
  "answer_box": {
    "title": "Featured Answer Title",
    "answer": "Featured answer content",
    "type": "answer_type",
    "link": "https://answer-link.com"
  },
  "related_questions": [
    {
      "question": "Related question",
      "answer": "Answer to related question",
      "link": "https://question-link.com"
    }
  ]
}
```

## Troubleshooting

### Common Issues
1. **Invalid API Key**: Ensure your SerpAPI key is correct and active
2. **Rate Limit Exceeded**: SerpAPI has rate limits. Wait and try again later
3. **No Results**: Some queries may not return results. Try different search terms

### Error Messages
- "SerpAPI key is required": Add your API key in the credentials
- "Invalid SerpAPI key": Check your API key in the SerpAPI dashboard
- "Rate limit exceeded": Wait before making another request

## Contributing
This plugin is open for contributions. Please ensure any changes maintain compatibility with the Dify plugin framework.

## License
This plugin is provided as-is for use with Dify.

## Support
For support or questions, please contact the plugin author: alopha 