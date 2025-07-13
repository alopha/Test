import requests
import re

def find_award_date(query):
    """使用精确查询来查找颁奖典礼日期"""
    
    api_key = "896a71fcca4f2d3e7b96926a43b81194cbf39d4c096bccd02e31ff07b6a1cefd"
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "baidu",
        "q": query,
        "api_key": api_key,
        "num": 10  # 获取更多结果以便分析
    }
    
    print(f"🔍 正在精确搜索: '{query}'")
    
    try:
        response = requests.get(url, params=params, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                print(f"❌ API返回错误: {data['error']}")
                return None
            
            print("✅ 搜索成功! 正在分析结果...")
            
            # 优先检查答案框
            answer_box = data.get("answer_box")
            if answer_box and 'answer' in answer_box:
                answer = answer_box['answer']
                print(f"🎯 找到特色答案: {answer}")
                # 尝试从答案中提取日期
                match = re.search(r'(\d{4}年)?(\d{1,2}月\d{1,2}日)', answer)
                if match:
                    date_found = match.group(0)
                    print(f"📅 从特色答案中提取的日期: {date_found}")
                    return date_found
            
            # 如果没有答案框，分析搜索结果的标题和摘要
            all_text = ""
            for result in data.get("organic_results", []):
                all_text += result.get('title', '') + " "
                all_text += result.get('snippet', '') + " "

            # 使用正则表达式匹配日期格式，如 "6月28日" 或 "2024年6月28日"
            # 匹配 "X月X日"
            match = re.search(r'(\d{1,2}月\d{1,2}日)', all_text)
            if match:
                date_found = match.group(1)
                print(f"📅 从搜索结果中提取的日期: {date_found}")
                return date_found
            
            print("❌ 未能从搜索结果中直接提取到明确的日期。")
            
            # 如果没有找到明确日期，打印出最相关的结果摘要
            print("\n可供参考的相关摘要:")
            for result in data.get("organic_results", [])[:3]:
                print(f"- {result.get('title', '')}: {result.get('snippet', '')}")

            return None
        else:
            print(f"❌ 请求失败，状态码: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ 发生异常: {e}")
        return None

if __name__ == "__main__":
    search_query = "第30届上海电视节白玉兰奖 颁奖典礼 日期"
    extracted_date = find_award_date(search_query)
    
    print("\n" + "="*50)
    if extracted_date:
        print(f"🎉 结论: 第30届白玉兰奖的颁奖日期是 {extracted_date}")
    else:
        print("ℹ️ 结论: 未能自动提取具体日期，请参考上面的摘要信息。") 