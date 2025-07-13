import requests

# Test the API key
api_key = "896a71fcca4f2d3e7b96926a43b81194cbf39d4c096bccd02e31ff07b6a1cefd"

print("Testing SerpAPI key...")

url = "https://serpapi.com/search.json"
params = {
    "engine": "baidu",
    "q": "test",
    "api_key": api_key
}

try:
    response = requests.get(url, params=params, timeout=10)
    print(f"Status code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            print(f"Error: {data['error']}")
        else:
            print("✅ API key is working!")
            print(f"Found {len(data.get('organic_results', []))} results")
    else:
        print(f"Failed with status: {response.status_code}")
        
except Exception as e:
    print(f"Exception: {e}") 