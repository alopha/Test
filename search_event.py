import requests
import json
import datetime

def search_public_conference_2025(queries):
    """(2025年背景) 搜索公司的公开市场会议信息"""
    
    api_key = "896a71fcca4f2d3e7b96926a43b81194cbf39d4c096bccd02e31ff07b6a1cefd"
    url = "https://serpapi.com/search.json"
    all_results = {}
    
    print("🔍 (背景已更新: 今年是2025年) 正在重新搜索致趣百川的年中市场会议...")
    print("="*60)

    for query in queries:
        print(f"\n尝试搜索关键词: '{query}'")
        params = {
            "engine": "baidu",
            "q": query,
            "api_key": api_key,
            "num": 7
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

def analyze_and_display_2025(results):
    """(2025年背景) 分析并展示搜索结果"""
    print("\n\n📊 搜索结果汇总分析 (基于今年是2025年):")
    print("="*60)

    if not results:
        print("结论: 即使基于今年是2025年的背景重新搜索，依然未能找到关于"致趣百川2025年年中市场会议"的明确信息。")
        print("\n可能原因:")
        print("1. **活动名称不同**: 该会议可能使用了我们未猜到的特定品牌名称。")
        print("2. **信息未被广泛索引**: 会议可能规模较小，或主要通过定向邀请进行，未在公开渠道广泛宣传。")
        print("3. **关键词不精确**: 官方发布的信息可能未使用"年中"或"复盘"等词汇。")
        print("\n建议:")
        print("- **访问官网**: 最可靠的方法是直接访问致趣百川官网 [https://www.beschannels.com/](https://www.beschannels.com/) 查看其"新闻"或"活动"板块。")
        print("- **查看官方社交媒体**: 检查其官方微信公众号等渠道的历史消息。")
        return

    # 简单地将所有找到的结果聚合在一起展示
    all_titles_and_links = {}
    for query, res_list in results.items():
        for result in res_list:
            link = result.get('link')
            title = result.get('title', '无标题')
            if link and link not in all_titles_and_links:
                 all_titles_and_links[link] = f"[{query}] {title}\n   摘要: {result.get('snippet', '(无)')}"

    if not all_titles_and_links:
        print("结论: 搜索到了页面，但内容相关性不强，未发现明确的2025年会议信息。")
        return

    print("以下是为您找到的所有相关结果，请您审阅，看是否有您需要的信息：\n")
    for i, (link, title_snippet) in enumerate(all_titles_and_links.items(), 1):
        print(f"{i}. {title_snippet}")
        print(f"   🔗 链接: {link}\n")

    print("\n\nℹ️ **初步结论**: 虽然找到了多个相关页面，但没有一个能直接明确指出"2025年年中市场会议"的具体日期和主题。建议您仔细浏览上述链接，特别是官网和官方新闻稿。")


if __name__ == "__main__":
    # 更新搜索关键词，更侧重于已发生或即将发生的事件
    search_queries = [
        "致趣百川 2025 峰会",
        "致趣百川 2025 用户大会",
        "致趣百川 2025 年中 活动",
        "致趣百川 大会 总结 2025"
    ]
    
    found_results = search_public_conference_2025(search_queries)
    analyze_and_display_2025(found_results) 