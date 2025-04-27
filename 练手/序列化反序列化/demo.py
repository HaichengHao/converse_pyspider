"""
@File    :demo.py
@Editor  : 百年
@Date    :2025/4/26 15:50 
"""
import json
json_str='''
{
  "usrname": "3380136198",
  "title": "\u4e70\u80a1"
}'''
print(type(json_str))

# 反序列化，将json字符串转化为python字典
j_s=json.loads(json_str)
print(type(j_s))
print(j_s)