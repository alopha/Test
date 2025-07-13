from collections.abc import Generator
from typing import Any
import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class BaiduSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Search for information on Baidu using SerpAPI
        """
        # Get parameters
        query = tool_parameters.get("query", "")
        num_results = tool_parameters.get("num_results", 10)
        
        # Validate parameters
        if not query:
            yield self.create_text_message("Search query is required.")
            return
            
        if num_results < 1 or num_results > 100:
            yield self.create_text_message("Number of results must be between 1 and 100.")
            return
            
        try:
            # Get API key from credentials
            api_key = self.runtime.credentials.get("api_key")
            if not api_key:
                yield self.create_text_message("SerpAPI key is required.")
                return
                
            # Make API request to SerpAPI
            try:
                url = "https://serpapi.com/search.json"
                params = {
                    "engine": "baidu",
                    "q": query,
                    "api_key": api_key,
                    "num": num_results
                }
                
                response = requests.get(url, params=params, timeout=30)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Check for API errors
                    if "error" in data:
                        yield self.create_text_message(f"SerpAPI error: {data['error']}")
                        return
                    
                    # Process search results
                    results = self._process_search_results(data)
                    
                    # Create response
                    summary = f"Found {len(results.get('organic_results', []))} search results for '{query}'"
                    yield self.create_text_message(summary)
                    yield self.create_json_message(results)
                    
                elif response.status_code == 401:
                    yield self.create_text_message("Invalid SerpAPI key. Please check your API key.")
                    return
                elif response.status_code == 429:
                    yield self.create_text_message("Rate limit exceeded. Please try again later.")
                    return
                else:
                    yield self.create_text_message(f"SerpAPI request failed with status code: {response.status_code}")
                    return
                    
            except requests.exceptions.RequestException as e:
                yield self.create_text_message(f"Failed to connect to SerpAPI: {str(e)}")
                return
            except Exception as e:
                yield self.create_text_message(f"Error processing search results: {str(e)}")
                return
                
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
            return
    
    def _process_search_results(self, data: dict) -> dict:
        """
        Process and format search results from SerpAPI response
        """
        processed_results = {
            "query": data.get("search_parameters", {}).get("q", ""),
            "total_results": data.get("search_information", {}).get("total_results", 0),
            "organic_results": [],
            "answer_box": None,
            "related_questions": []
        }
        
        # Process organic results
        organic_results = data.get("organic_results", [])
        for result in organic_results:
            processed_result = {
                "position": result.get("position", 0),
                "title": result.get("title", ""),
                "link": result.get("link", ""),
                "snippet": result.get("snippet", ""),
                "displayed_link": result.get("displayed_link", ""),
                "thumbnail": result.get("thumbnail", "")
            }
            processed_results["organic_results"].append(processed_result)
        
        # Process answer box if available
        answer_box = data.get("answer_box")
        if answer_box:
            processed_results["answer_box"] = {
                "title": answer_box.get("title", ""),
                "answer": answer_box.get("answer", ""),
                "type": answer_box.get("type", ""),
                "link": answer_box.get("link", "")
            }
        
        # Process related questions if available
        related_questions = data.get("related_questions", [])
        for question in related_questions:
            processed_results["related_questions"].append({
                "question": question.get("question", ""),
                "answer": question.get("answer", ""),
                "link": question.get("link", "")
            })
        
        return processed_results 