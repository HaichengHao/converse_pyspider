"""
@File    :03eval妙用.py
@Editor  : 百年
@Date    :2025/5/22 23:03 
"""
"""
var obj={
            name:'jojo',
            age:8,
            gender:'male',
            hobby:'the world'
        }
        有时候遇到这种对象,我们可能会想把它转成python
        """
import json
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen,encoding='utf-8')

import execjs

with open('./jsfile/eval妙用.js','r',encoding='utf-8') as jsf:
    ctx = execjs.compile(jsf.read())

res = ctx.eval('obj')
print(res)
print('类型是',type(res))
# {'name': 'jojo', 'age': 8, 'gender': 'male', 'hobby': 'the world'}
# 类型是 <class 'dict'>
# important:可以发现，都加上引号了，这样我们就可以把它转换成json格式的数据

json_str = json.dumps(res) #序列化,python字符串化
print(type(json_str))
print(json_str)

#尝试反序列化，json字典化
json_dic = json.loads(json_str)
print(type(json_dic))

''' 运行结果
{'name': 'jojo', 'age': 8, 'gender': 'male', 'hobby': 'the world'}
<class 'str'>
{"name": "jojo", "age": 8, "gender": "male", "hobby": "the world"}
<class 'dict'>
'''