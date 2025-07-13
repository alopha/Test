import requests
import re

def find_exact_ceremony_date(query):
    """使用更精确的关键词和分析逻辑来查找颁奖典礼的确切日期"""
    
    api_key = "896a71fcca4f2d3e7b96926a43b81194cbf39d4c096bccd02e31ff07b6a1cefd"
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "baidu",
        "q": query,
        "api_key": api_key,
        "num": 10
    }
    
    print(f"🔍 正在进行更正性搜索: '{query}'")
    
    try:
        response = requests.get(url, params=params, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                print(f"❌ API返回错误: {data['error']}")
                return None, None
            
            print("✅ 搜索成功! 正在深度分析结果...")
            
            all_text = ""
            results = data.get("organic_results", [])
            for result in results:
                all_text += result.get('title', '') + " "
                all_text += result.get('snippet', '') + " "

            # 寻找 "X月X日晚" 或 "X月X日举行" 的模式，这通常指向颁奖典礼
            # 例如: "6月28日晚"
            match = re.search(r'(\d{1,2}月\d{1,2}日)(晚|举行|颁奖)', all_text)
            
            if match:
                date_found = match.group(1)
                print(f"📅 从结果中提取到最可能的颁奖日期: {date_found}")
                return date_found, results
            else:
                print("❌ 未能从搜索结果中自动提取到确切的颁奖日期。")
                return None, results
        else:
            print(f"❌ 请求失败，状态码: {response.status_code}")
            return None, None
            
    except Exception as e:
        print(f"❌ 发生异常: {e}")
        return None, None

def display_final_analysis(date, results):
    """展示最终的分析结论"""
    print("\n" + "="*60)
    if date:
        print(f"🎉 **最终结论：第30届白玉兰奖颁奖典礼的日期是 {date}。**")
        print('这个日期是通过分析多个搜索结果的标题和摘要，并匹配"举行"或"晚"等关键词得出的，可信度较高。')
    else:
        print("ℹ️ **最终结论：**")
        print("抱歉，经过重新搜索，依然未能 **自动提取** 出一个100%确切的颁奖日期。")
        print("这通常意味着日期信息没有以标准格式出现在搜索结果的摘要中。")

    if results:
        print("\n以下是最相关的搜索结果，供您参考：")
        for i, result in enumerate(results[:3], 1):
            print(f"\n{i}. {result.get('title', '无标题')}")
            print(f"   🔗 链接: {result.get('link', '无链接')}")
            snippet = result.get('snippet', '(无)')
            print(f"   📝 摘要: {snippet}")
    print("="*60)


if __name__ == "__main__":
    # 使用最精确的关键词
    search_query = "第30届上海电视节白玉兰奖 颁奖典礼 日期"
    extracted_date, search_results = find_exact_ceremony_date(search_query)
    display_final_analysis(extracted_date, search_results) 