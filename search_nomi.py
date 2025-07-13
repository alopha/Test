import requests
import json

def search_product(queries):
    """搜索特定的产品或服务信息"""
    
    api_key = "896a71fcca4f2d3e7b96926a43b81194cbf39d4c096bccd02e31ff07b6a1cefd"
    url = "https://serpapi.com/search.json"
    all_results = {}
    
    print("🔍 正在搜索 'Nomi-Cursor for Sales' 相关信息...")
    print("="*60)

    for query in queries:
        print(f"\n尝试搜索关键词: '{query}'")
        params = {
            "engine": "baidu",  # 继续使用百度搜索引擎
            "q": query,
            "api_key": api_key,
            "num": 5
        }
        
        try:
            response = requests.get(url, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                if "error" in data:
                    print(f"  ❌ API返回错误: {data['error']}")
                    continue
                
                results = data.get("organic_results", [])
                if results:
                    print(f"  ✅ 找到 {len(results)} 条相关结果。")
                    all_results[query] = results
                else:
                    print("  ℹ️ 未找到相关结果。")
            else:
                print(f"  ❌ 请求失败，状态码: {response.status_code}")
                
        except Exception as e:
            print(f"  ❌ 发生异常: {e}")
            
    return all_results

def analyze_and_summarize(results):
    """分析并总结搜索结果"""
    print("\n\n📊 搜索结果汇总分析:")
    print("="*60)

    if not results:
        print("结论: 搜索完成，但未能找到任何关于 'Nomi-Cursor for Sales' 的明确公开信息。")
        print("\n可能的情况:")
        print("1. **产品名称错误**: 这可能不是该产品或服务的确切名称。")
        print("2. **内部项目或概念**: 这可能是一个非常早期、未公开的内部项目，或者只是一个概念名称。")
        print("3. **新发布的产品**: 如果产品刚刚发布，搜索引擎可能还没有广泛索引相关信息。")
        print("\n建议:")
        print("- **检查名称**: 确认 'Nomi-Cursor for Sales' 是否是准确的名称。")
        print("- **提供更多上下文**: 如果您有关于它的更多信息（例如来自哪个公司），我可以进行更精确的搜索。")
        return

    # 将所有找到的结果聚合在一起展示
    all_links = {}
    for query, res_list in results.items():
        for result in res_list:
            link = result.get('link')
            title = result.get('title', '无标题')
            if link and link not in all_links:
                 all_links[link] = f"[{query}] {title}\n   摘要: {result.get('snippet', '(无)')}"

    if not all_links:
        print("结论: 虽有返回，但内容相关性不强，未发现明确信息。")
        return

    print("以下是为您找到的相关结果，请您审阅：\n")
    for i, (link, title_snippet) in enumerate(all_links.items(), 1):
        print(f"{i}. {title_snippet}")
        print(f"   🔗 链接: {link}\n")

    print("\n\nℹ️ **初步结论**: 搜索到了一些包含 'Cursor' 或 'Sales' 的页面，但没有找到直接名为 'Nomi-Cursor for Sales' 的特定产品或服务。请您查看上面的链接，判断是否与您想找的信息相关。")


if __name__ == "__main__":
    search_queries = [
        "Nomi-Cursor for Sales",
        "Nomi AI for Sales",
        "Cursor for Sales Teams",
        "Nomi AI platform"
    ]
    
    found_results = search_product(search_queries)
    analyze_and_summarize(found_results) 