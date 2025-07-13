from typing import Any
import requests

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

class BaiduProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            # Check if api_key is provided in credentials
            if "api_key" not in credentials or not credentials.get("api_key"):
                raise ToolProviderCredentialValidationError("SerpAPI key is required.")
            
            # Try to authenticate with SerpAPI using a simple test query
            try:
                api_key = credentials.get("api_key")
                test_url = "https://serpapi.com/search.json"
                params = {
                    "engine": "baidu",
                    "q": "test",
                    "api_key": api_key
                }
                
                response = requests.get(test_url, params=params, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    if "error" in data:
                        raise ToolProviderCredentialValidationError(f"SerpAPI error: {data['error']}")
                    # If we get here, the API key is valid
                elif response.status_code == 401:
                    raise ToolProviderCredentialValidationError("Invalid SerpAPI key. Please check your API key.")
                else:
                    raise ToolProviderCredentialValidationError(f"SerpAPI request failed with status code: {response.status_code}")
                    
            except requests.exceptions.RequestException as e:
                raise ToolProviderCredentialValidationError(f"Failed to connect to SerpAPI: {str(e)}")
            except Exception as e:
                raise ToolProviderCredentialValidationError(f"Error validating SerpAPI credentials: {str(e)}")
                
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e)) 