import requests
import json

def verify_serpapi_key():
    """验证SerpAPI密钥是否有效"""
    
    # 您的SerpAPI密钥
    api_key = "896a71fcca4f2d3e7b96926a43b81194cbf39d4c096bccd02e31ff07b6a1cefd"
    
    print("🔑 正在验证SerpAPI密钥...")
    print(f"密钥: {api_key[:10]}...{api_key[-10:]}")
    print("-" * 50)
    
    # 测试URL
    url = "https://serpapi.com/search.json"
    
    # 简单的测试参数
    params = {
        "engine": "baidu",
        "q": "test",
        "api_key": api_key,
        "num": 1
    }
    
    try:
        print("📡 正在发送测试请求...")
        response = requests.get(url, params=params, timeout=15)
        
        print(f"📊 响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            # 检查是否有错误信息
            if "error" in data:
                error_msg = data["error"]
                print(f"❌ API返回错误: {error_msg}")
                
                if "Invalid API key" in error_msg or "401" in error_msg:
                    print("🔴 结论: SerpAPI密钥无效")
                    return False
                elif "quota" in error_msg.lower() or "limit" in error_msg.lower():
                    print("🟡 结论: SerpAPI密钥有效，但已达到配额限制")
                    return True
                else:
                    print("🟡 结论: SerpAPI密钥可能有效，但有其他错误")
                    return True
            else:
                print("✅ API密钥验证成功!")
                print(f"📈 找到 {len(data.get('organic_results', []))} 个搜索结果")
                print("🟢 结论: SerpAPI密钥有效且工作正常")
                return True
                
        elif response.status_code == 401:
            print("❌ 401 未授权错误")
            print("🔴 结论: SerpAPI密钥无效或已过期")
            return False
            
        elif response.status_code == 429:
            print("❌ 429 请求频率超限")
            print("🟡 结论: SerpAPI密钥有效，但请求过于频繁")
            return True
            
        else:
            print(f"❌ 请求失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text[:200]}...")
            print("🟡 结论: 无法确定密钥有效性")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ 请求超时")
        print("🟡 结论: 网络连接问题，无法验证密钥")
        return False
        
    except requests.exceptions.ConnectionError:
        print("❌ 连接错误")
        print("🟡 结论: 网络连接问题，无法验证密钥")
        return False
        
    except Exception as e:
        print(f"❌ 未知错误: {str(e)}")
        print("🟡 结论: 无法验证密钥")
        return False

def test_baidu_search():
    """测试百度搜索功能"""
    
    api_key = "896a71fcca4f2d3e7b96926a43b81194cbf39d4c096bccd02e31ff07b6a1cefd"
    
    print("\n🔍 测试百度搜索功能...")
    print("-" * 50)
    
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "baidu",
        "q": "第30届白玉兰奖",
        "api_key": api_key,
        "num": 3
    }
    
    try:
        response = requests.get(url, params=params, timeout=20)
        
        if response.status_code == 200:
            data = response.json()
            
            if "error" not in data:
                results = data.get("organic_results", [])
                print(f"✅ 搜索成功! 找到 {len(results)} 个结果")
                
                for i, result in enumerate(results[:2], 1):
                    print(f"\n{i}. {result.get('title', '无标题')}")
                    print(f"   链接: {result.get('link', '无链接')}")
                    print(f"   摘要: {result.get('snippet', '无摘要')[:100]}...")
                
                return True
            else:
                print(f"❌ 搜索失败: {data['error']}")
                return False
        else:
            print(f"❌ 搜索请求失败: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ 搜索测试失败: {str(e)}")
        return False

if __name__ == "__main__":
    print("🔍 SerpAPI密钥验证工具")
    print("=" * 50)
    
    # 验证密钥
    key_valid = verify_serpapi_key()
    
    # 如果密钥有效，测试搜索功能
    if key_valid:
        search_works = test_baidu_search()
        
        print("\n" + "=" * 50)
        if search_works:
            print("🎉 总结: SerpAPI密钥有效，百度搜索功能正常!")
            print("✅ 您的百度搜索工具可以正常使用")
        else:
            print("⚠️  总结: SerpAPI密钥有效，但搜索功能可能有问题")
    else:
        print("\n" + "=" * 50)
        print("❌ 总结: SerpAPI密钥无效")
        print("🔧 请检查您的API密钥或联系SerpAPI支持") 