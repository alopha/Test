import requests

def search_baidu(query):
    api_key = "896a71fcca4f2d3e7b96926a43b81194cbf39d4c096bccd02e31ff07b6a1cefd"
    
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "baidu",
        "q": query,
        "api_key": api_key,
        "num": 10
    }
    
    try:
        response = requests.get(url, params=params, timeout=30)
        print(f"状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            if "error" in data:
                print(f"API错误: {data['error']}")
                return
            
            print(f"\n搜索查询: {data.get('search_parameters', {}).get('q', '')}")
            print(f"总结果数: {data.get('search_information', {}).get('total_results', '未知')}")
            print("\n搜索结果:")
            print("-" * 80)
            
            organic_results = data.get("organic_results", [])
            for i, result in enumerate(organic_results[:5], 1):
                print(f"\n{i}. {result.get('title', '无标题')}")
                print(f"   链接: {result.get('link', '无链接')}")
                print(f"   摘要: {result.get('snippet', '无摘要')}")
            
            # 检查是否有答案框
            answer_box = data.get("answer_box")
            if answer_box:
                print(f"\n📋 特色答案:")
                print(f"   标题: {answer_box.get('title', '无标题')}")
                print(f"   答案: {answer_box.get('answer', '无答案')}")
                
        else:
            print(f"请求失败，状态码: {response.status_code}")
            
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    print("搜索AdventureX2025相关信息...")
    search_baidu("AdventureX2025 举办时间 地点 时间 日期") 