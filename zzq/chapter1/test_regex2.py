import re

# 测试修改后的正则表达式
test_strings = [
    "city: 'Beijing'",
    "city='Beijing'",
    "city: \"Beijing\"",
    "city=\"Beijing\"",
    "keywords: '故宫', city: 'Beijing'"
]

print("测试修改后的正则表达式: r'(\\w+)\\s*[:=]\\s*[\\\'\"]([^\\\'"]*)[\\\'"]'")
for test_str in test_strings:
    print(f"\n测试字符串: {test_str}")
    matches = re.findall(r'(+)\s*[:=]\s*[\'"]' + r'([^\'"]*)' + r'[\'"]', test_str)
    kwargs = dict(matches)
    print(f"匹配结果: {matches}")
    print(f"转换为字典: {kwargs}")

# 模拟完整的解析过程
print("\n\n模拟完整解析过程:")
test_cases = [
    "Action: search_poi(city: 'Beijing')",
    "Action: search_poi(city='Beijing')",
    "Action: search_poi(keywords: '故宫', city: 'Beijing')"
]

for full_action in test_cases:
    print(f"\n完整Action字符串: {full_action}")
    
    action_match = re.search(r"Action: (.*)", full_action, re.DOTALL)
    if action_match:
        action_str = action_match.group(1).strip()
        print(f"提取的action_str: {action_str}")
        
        tool_name = re.search(r"(\w+)\(", action_str).group(1)
        args_str = re.search(r"\((.*)\)", action_str).group(1)
        print(f"提取的工具名: {tool_name}")
        print(f"提取的参数串: {args_str}")
        
        result = re.findall(r'(+)\s*[:=]\s*[\'"]' + r'([^\'"]*)' + r'[\'"]', args_str)
        kwargs = dict(result)
        print(f"解析后的参数: {kwargs}")
