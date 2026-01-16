import re

# 测试修改后的正则表达式
test_strings = [
    "city: 'Beijing'",
    "city='Beijing'",
    "city: \"Beijing\"",
    "city=\"Beijing\"",
    "keywords: '故宫', city: 'Beijing'"
]

pattern = r'(\w+)\s*[:=]\s*[\'"]([^\'"\)]*)[\'"]'
print("测试正则表达式: ", pattern)
for test_str in test_strings:
    print(f"\n测试字符串: {test_str}")
    matches = re.findall(pattern, test_str)
    kwargs = dict(matches)
    print(f"匹配结果: {matches}")
    print(f"转换为字典: {kwargs}")
