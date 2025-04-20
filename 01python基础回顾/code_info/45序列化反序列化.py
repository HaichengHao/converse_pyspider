"""
@File    :45序列化反序列化.py
@Editor  : 百年
@Date    :2025/4/19 16:19 
"""
import json

# 序列化 dumps() 可以将字符串转换为json字典
dic1 = {'name': 'Bob'}

res1 = json.dumps(dic1, indent=2)  # tips:其中indent可以指定序列化后的缩进
print(res1)

# 反序列化,python字典化
res2 = json.loads(res1)
print(res2)

#runtime_result:
'''
{
  "name": "Bob"
}
{'name': 'Bob'}'''

# 还有loads()和dumps()可以指定文件
