from dotenv import load_dotenv
from my_llm import MyLLM

# 加载环境变量
load_dotenv()

# 创建LLM实例 - 框架自动检测provider
llm = MyLLM(provider="modelscope")
# 准备消息
messages = [{"role": "user", "content": "你好，请介绍一下你自己。"}]

# 发起调用，think等方法都已从父类继承，无需重写
response_stream = llm.think(messages)

# 打印响应
print("ModelScope Response:")
for chunk in response_stream:
    # chunk 已经是文本片段，可以直接使用
    print(chunk, end="", flush=True)