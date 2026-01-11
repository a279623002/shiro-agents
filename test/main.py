import dotenv
import os
from openai import OpenAI

dotenv.load_dotenv()

model_id = os.getenv("LLM_MODEL_ID")
api_key = os.getenv("LLM_API_KEY")
base_url = os.getenv("LLM_BASE_URL")    

llm = OpenAI(
    api_key=api_key,
    base_url=base_url,
)       

prompt = """你是一个专业的旅游助手，你的任务是根据用户的目的地{destination},生成详细的旅行计划。
请严格按照以下JSON格式返回旅行计划:
```json
{{
    "destinations": [
        {{
            "name": "目的地名称",
            "days": 1,
            "activities": [
                "活动1",
                "活动2",
                "活动3"
            ]
        }}
    ]
}}   
```
"""

# 获取用户输入
user_input = input("请输入您的目的地: ")

# 构建完整的提示
full_prompt = prompt.format(destination=user_input)

print(f"🧠 正在调用 {model_id} 模型...")
try:
    response = llm.chat.completions.create(
        model=model_id,
        messages=[
            {"role": "system", "content": "你是一个专业的旅游助手"},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.7,
        max_tokens=1024,
        stream=True,
    )

    # 处理流式响应
    print("✅ 大语言模型响应成功:")
    for chunk in response:
        content = chunk.choices[0].delta.content or ""
        if content:
            print(content, end="", flush=True)
    print()  # 在流式输出结束后换行

except Exception as e:
    print(f"❌ 调用LLM API时发生错误: {e}")
    raise Exception(f"LLM调用失败: {str(e)}")
