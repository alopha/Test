#!/usr/bin/env python3
"""
Test script for Baidu Search Tool
This script tests the SerpAPI integration with the provided API key
"""

import requests
import json

def test_serpapi_baidu_search():
    """Test Baidu search using SerpAPI"""
    
    # Your SerpAPI key
    api_key = "896a71fcca4f2d3e7b96926a43b81194cbf39d4c096bccd02e31ff07b6a1cefd"
    
    # Test search parameters
    test_query = "coffee"
    num_results = 5
    
    print(f"Testing Baidu search for: '{test_query}'")
    print(f"API Key: {api_key[:10]}...{api_key[-10:]}")
    print("-" * 50)
    
    try:
        # Make API request to SerpAPI
        url = "https://serpapi.com/search.json"
        params = {
            "engine": "baidu",
            "q": test_query,
            "api_key": api_key,
            "num": num_results
        }
        
        print("Making request to SerpAPI...")
        response = requests.get(url, params=params, timeout=30)
        
        print(f"Response status code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            # Check for API errors
            if "error" in data:
                print(f"❌ SerpAPI error: {data['error']}")
                return False
            
            # Process and display results
            print("✅ Search successful!")
            print(f"Total results found: {data.get('search_information', {}).get('total_results', 'Unknown')}")
            
            # Display organic results
            organic_results = data.get("organic_results", [])
            print(f"\nFound {len(organic_results)} organic results:")
            
            for i, result in enumerate(organic_results[:3], 1):  # Show first 3 results
                print(f"\n{i}. {result.get('title', 'No title')}")
                print(f"   Link: {result.get('link', 'No link')}")
                print(f"   Snippet: {result.get('snippet', 'No snippet')[:100]}...")
            
            # Check for answer box
            answer_box = data.get("answer_box")
            if answer_box:
                print(f"\n📋 Answer Box found:")
                print(f"   Title: {answer_box.get('title', 'No title')}")
                print(f"   Answer: {answer_box.get('answer', 'No answer')[:100]}...")
            
            return True
            
        elif response.status_code == 401:
            print("❌ Invalid SerpAPI key. Please check your API key.")
            return False
        elif response.status_code == 429:
            print("❌ Rate limit exceeded. Please try again later.")
            return False
        else:
            print(f"❌ Request failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to connect to SerpAPI: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Baidu Search Tool with SerpAPI")
    print("=" * 50)
    
    success = test_serpapi_baidu_search()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ Test completed successfully! Your SerpAPI key is working.")
        print("The Baidu Search Tool plugin is ready to use in Dify.")
    else:
        print("❌ Test failed. Please check your SerpAPI key and try again.") 