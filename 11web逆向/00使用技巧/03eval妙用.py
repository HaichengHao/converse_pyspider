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
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen,encoding='utf-8')

import execjs

with open('./jsfile/eval妙用.js','r',encoding='utf-8') as jsf:
    ctx = execjs.compile(jsf.read())

res = ctx.eval('obj')
print(res)

# {'name': 'jojo', 'age': 8, 'gender': 'male', 'hobby': 'the world'}
# important:可以发现，都加上引号了，这样我们就可以把