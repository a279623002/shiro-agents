import re

# 测试简化后的正则表达式
args_str = "city: 'Beijing'"
print(f"测试字符串: {args_str}")

# 使用简化后的正则表达式
pattern = r'([a-zA-Z_][a-zA-Z0-9_]*)\s*[:=]\s*["\']([^"\']*)["\']'
result = re.findall(pattern, args_str)
kwargs = dict(result)

print(f"正则表达式: {pattern}")
print(f"匹配结果: {result}")
print(f"转换为字典: {kwargs}")

# 测试包含多个参数的情况
args_str2 = "keywords: '故宫', city: 'Beijing'"
print(f"\n测试字符串2: {args_str2}")
result2 = re.findall(pattern, args_str2)
kwargs2 = dict(result2)

print(f"匹配结果2: {result2}")
print(f"转换为字典2: {kwargs2}")
