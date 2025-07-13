#!/usr/bin/env python3
"""
测试百度搜索工具 - 搜索第30届白玉兰奖信息
"""

import requests
import json

def simulate_baidu_search_tool(query, num_results=10):
    """
    模拟百度搜索工具的功能
    """
    # 使用您提供的SerpAPI密钥
    api_key = "896a71fcca4f2d3e7b96926a43b81194cbf39d4c096bccd02e31ff07b6a1cefd"
    
    print(f"🔍 正在使用百度搜索工具搜索: '{query}'")
    print(f"📊 请求结果数量: {num_results}")
    print("-" * 60)
    
    try:
        # 构建API请求参数
        url = "https://serpapi.com/search.json"
        params = {
            "engine": "baidu",
            "q": query,
            "api_key": api_key,
            "num": num_results
        }
        
        print("📡 正在连接SerpAPI...")
        response = requests.get(url, params=params, timeout=30)
        
        print(f"📊 响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            # 检查API错误
            if "error" in data:
                print(f"❌ SerpAPI错误: {data['error']}")
                return
            
            # 处理搜索结果
            results = process_search_results(data)
            
            # 显示摘要
            organic_count = len(results.get('organic_results', []))
            print(f"✅ 搜索成功! 找到 {organic_count} 个搜索结果")
            print(f"📈 总结果数: {results.get('total_results', '未知')}")
            
            # 显示搜索结果
            print("\n📋 搜索结果:")
            print("=" * 60)
            
            organic_results = results.get('organic_results', [])
            for i, result in enumerate(organic_results[:5], 1):
                print(f"\n{i}. {result.get('title', '无标题')}")
                print(f"   🔗 链接: {result.get('link', '无链接')}")
                print(f"   📝 摘要: {result.get('snippet', '无摘要')}")
                if result.get('displayed_link'):
                    print(f"   🌐 显示链接: {result.get('displayed_link')}")
            
            # 显示特色答案（如果有）
            answer_box = results.get('answer_box')
            if answer_box:
                print(f"\n🎯 特色答案:")
                print(f"   标题: {answer_box.get('title', '无标题')}")
                print(f"   答案: {answer_box.get('answer', '无答案')}")
                print(f"   类型: {answer_box.get('type', '未知')}")
            
            # 显示相关问题（如果有）
            related_questions = results.get('related_questions', [])
            if related_questions:
                print(f"\n❓ 相关问题:")
                for i, q in enumerate(related_questions[:3], 1):
                    print(f"   {i}. {q.get('question', '无问题')}")
                    print(f"      答案: {q.get('answer', '无答案')[:100]}...")
            
            return results
            
        elif response.status_code == 401:
            print("❌ SerpAPI密钥无效，请检查您的API密钥")
            return None
        elif response.status_code == 429:
            print("❌ 请求频率超限，请稍后再试")
            return None
        else:
            print(f"❌ 请求失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ 连接SerpAPI失败: {str(e)}")
        return None
    except Exception as e:
        print(f"❌ 处理搜索结果时出错: {str(e)}")
        return None

def process_search_results(data):
    """
    处理SerpAPI返回的搜索结果
    """
    processed_results = {
        "query": data.get("search_parameters", {}).get("q", ""),
        "total_results": data.get("search_information", {}).get("total_results", 0),
        "organic_results": [],
        "answer_box": None,
        "related_questions": []
    }
    
    # 处理有机搜索结果
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
    
    # 处理答案框
    answer_box = data.get("answer_box")
    if answer_box:
        processed_results["answer_box"] = {
            "title": answer_box.get("title", ""),
            "answer": answer_box.get("answer", ""),
            "type": answer_box.get("type", ""),
            "link": answer_box.get("link", "")
        }
    
    # 处理相关问题
    related_questions = data.get("related_questions", [])
    for question in related_questions:
        processed_results["related_questions"].append({
            "question": question.get("question", ""),
            "answer": question.get("answer", ""),
            "link": question.get("link", "")
        })
    
    return processed_results

if __name__ == "__main__":
    print("🏆 百度搜索工具测试 - 第30届白玉兰奖信息查询")
    print("=" * 60)
    
    # 搜索第30届白玉兰奖信息
    search_query = "第30届白玉兰奖是什么时候"
    results = simulate_baidu_search_tool(search_query, num_results=10)
    
    print("\n" + "=" * 60)
    if results:
        print("✅ 搜索完成！百度搜索工具运行正常")
        print("📋 您可以在Dify中使用此工具进行百度搜索")
    else:
        print("❌ 搜索失败，请检查网络连接和API密钥") 