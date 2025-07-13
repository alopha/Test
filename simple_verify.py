import requests

api_key = "896a71fcca4f2d3e7b96926a43b81194cbf39d4c096bccd02e31ff07b6a1cefd"

print("Testing SerpAPI key...")

try:
    response = requests.get("https://serpapi.com/search.json", params={
        "engine": "baidu",
        "q": "test",
        "api_key": api_key
    })
    
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            print(f"Error: {data['error']}")
        else:
            print("Key is valid!")
    else:
        print(f"Failed: {response.status_code}")
        
except Exception as e:
    print(f"Exception: {e}") 