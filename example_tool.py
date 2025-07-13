from collections.abc import Generator
from typing import Any
import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class YourTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Main implementation of your tool
        """
        # Get parameters
        input_param = tool_parameters.get("input_parameter", "")
        optional_param = tool_parameters.get("optional_parameter", 10)
        
        # Validate parameters
        if not input_param:
            yield self.create_text_message("Input parameter is required.")
            return
            
        if optional_param < 1 or optional_param > 100:
            yield self.create_text_message("Optional parameter must be between 1 and 100.")
            return
            
        try:
            # Get API key from credentials
            api_key = self.runtime.credentials.get("api_key")
            if not api_key:
                yield self.create_text_message("API key is required.")
                return
                
            # Make API request to your service
            try:
                url = "https://your-service.com/api/endpoint"
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                }
                data = {
                    "input": input_param,
                    "limit": optional_param
                }
                
                response = requests.post(url, headers=headers, json=data, timeout=30)
                
                if response.status_code == 200:
                    result_data = response.json()
                    
                    # Check for API errors
                    if "error" in result_data:
                        yield self.create_text_message(f"Service error: {result_data['error']}")
                        return
                    
                    # Process results
                    processed_results = self._process_results(result_data)
                    
                    # Create response
                    summary = f"Successfully processed '{input_param}' with {len(processed_results.get('items', []))} results"
                    yield self.create_text_message(summary)
                    yield self.create_json_message(processed_results)
                    
                elif response.status_code == 401:
                    yield self.create_text_message("Invalid API key. Please check your API key.")
                    return
                elif response.status_code == 429:
                    yield self.create_text_message("Rate limit exceeded. Please try again later.")
                    return
                else:
                    yield self.create_text_message(f"Service request failed with status code: {response.status_code}")
                    return
                    
            except requests.exceptions.RequestException as e:
                yield self.create_text_message(f"Failed to connect to service: {str(e)}")
                return
            except Exception as e:
                yield self.create_text_message(f"Error processing results: {str(e)}")
                return
                
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
            return
    
    def _process_results(self, data: dict) -> dict:
        """
        Process and format results from your service response
        """
        processed_results = {
            "query": data.get("query", ""),
            "total_count": data.get("total_count", 0),
            "items": []
        }
        
        # Process items
        items = data.get("items", [])
        for item in items:
            processed_item = {
                "id": item.get("id", ""),
                "title": item.get("title", ""),
                "description": item.get("description", ""),
                "url": item.get("url", ""),
                "score": item.get("score", 0)
            }
            processed_results["items"].append(processed_item)
        
        return processed_results 