import yaml
from tavily import TavilyClient

def get_attraction(city: str, weather: str) -> str:
    """
    根据城市和天气，使用Tavily Search API搜索并返回优化后的景点推荐。
    """
    # 1. 从YAML配置文件中读取API密钥
    try:
        with open('conf.yaml', 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            api_key = config.get('TAVILY', {}).get('TAVILY_API_KEY')
    except FileNotFoundError:
        return "错误:未找到conf.yaml配置文件。"
    except yaml.YAMLError as e:
        return f"错误:解析conf.yaml文件失败 - {e}"
    
    if not api_key:
        return "错误:未在conf.yaml中配置TAVILY.TAVILY_API_KEY"

    # 2. 初始化Tavily客户端
    tavily = TavilyClient(api_key=api_key)
    
    # 3. 构造一个精确的查询
    query = f"'{city}' 在'{weather}'天气下最值得去的旅游景点推荐及理由"
    
    try:
        # 4. 调用API，include_answer=True会返回一个综合性的回答
        response = tavily.search(query=query, search_depth="basic", include_answer=True)
        
        # 5. Tavily返回的结果已经非常干净，可以直接使用
        # response['answer'] 是一个基于所有搜索结果的总结性回答
        if response.get("answer"):
            return response["answer"]
        
        # 如果没有综合性回答，则格式化原始结果
        formatted_results = []
        for result in response.get("results", []):
            formatted_results.append(f"- {result['title']}: {result['content']}")
        
        if not formatted_results:
             return "抱歉，没有找到相关的旅游景点推荐。"

        return "根据搜索，为您找到以下信息:\n" + "\n".join(formatted_results)

    except Exception as e:
        return f"错误:执行Tavily搜索时出现问题 - {e}"