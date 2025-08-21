"""
@File    :06自定义验证.py
@Editor  : 百年
@Date    :2025/8/16 16:14 
"""

'''
在某些情况下，您可能需要进行一些自定义验证，而这些验证无法通过上述参数完成。

在这种情况下，您可以使用一个自定义验证器函数，该函数在正常验证之后应用（例如，在验证值是 str 之后）。

您可以使用 Annotated 内部的 Pydantic 的 AfterValidator 来实现这一点。
'''

#tips: 例如，此自定义验证器检查项目 ID 是否以 isbn- 开头（用于ISBN 书号）或以 imdb- 开头（用于IMDB 电影 URL ID）
import uvicorn
import random
from fastapi import FastAPI
from typing import Annotated
from pydantic import AfterValidator

app = FastAPI()
data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id:str):
    if not id.startswith(('isbn-','imdb-')):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"''Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

@app.get('/items/')
async def read_items(
        id:Annotated[str|None,AfterValidator(check_valid_id)]=None
):
    if id:
        item = data.get(id)
    else:
        id,item = random.choice(list(data.items()))

    return {'id':id,'name':item}
if __name__ == '__main__':
    uvicorn.run('06自定义验证:app', reload=True, log_level='debug', host='127.0.0.1', port=8099)

'''
通过 data.items()，我们得到一个可迭代对象，其中包含每个字典项的键和值的元组。


我们将这个可迭代对象通过 list(data.items()) 转换为一个真正的 list。
[ ("isbn-9781529046137", "The Hitchhiker's Guide to the Galaxy"),
    ("imdb-tt0371724", "The Hitchhiker's Guide to the Galaxy"),
    ("isbn-9781439512982", "Isaac Asimov: The Complete Stories, Vol. 2)"]
然后使用 random.choice()，我们可以从列表中获取一个随机值，因此，我们得到一个包含 (id, name) 的元组。它会是类似 ("imdb-tt0371724", "The Hitchhiker's Guide to the Galaxy") 的东西。

然后我们将元组的这两个值分配给变量 id 和 name。

所以，如果用户没有提供项目 ID，他们仍然会收到一个随机建议。

……我们在一个简单的行中完成了所有这些。'''

'''
总结¶
您可以为参数声明附加验证和元数据。

通用验证和元数据

alias
title
description
deprecated
字符串特有的验证

min_length
max_length
pattern
使用 AfterValidator 的自定义验证!!!!!!!

在这些示例中，您看到了如何声明 str 值的验证。

请参阅后续章节，了解如何声明其他类型（如数字）的验证。'''