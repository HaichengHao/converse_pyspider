"""
@File    :02数值验证.py
@Editor  : 百年
@Date    :2025/8/16 17:41 
"""
'''
数值验证：大于或等于¶
使用 Query 和 Path（以及你稍后会看到的其他内容），你可以声明数值约束。

这里，使用 ge=1，item_id 需要是一个“greater than or equal”（大于或等于）1 的整数。
'''

import uvicorn
from pydantic import AfterValidator
from typing import Annotated
from fastapi import FastAPI,Path,Query

app = FastAPI()


@app.get('/items/{item_id}')
async def read_items(
        item_id:Annotated[int,Path(title="The ID of the item to get",ge=1)],
        q:str,
        size:Annotated[float,Query(gt=0,lt=10.5)]
):
    results = {'item_id':item_id}
    if q:
        results.update({"q":q})
    if size:
        results.update({'size':size})
    return results
if __name__ == '__main__':
    uvicorn.run('02数值验证:app',host='127.0.0.1',port=8090,reload=True,log_level='debug')

'''
gt：greater than (大于)
le：less than or equal (小于或等于)

总结¶
使用 Query、Path（以及你尚未见过的其他内容），你可以像 查询参数和字符串验证 那样声明元数据和字符串验证。

你也可以声明数值验证：

gt：greater than (大于)
ge：greater than or equal (大于或等于)
lt：less than (小于)
le：less than or equal (小于或等于)

'''

#tips:
# Query、Path 以及你稍后将看到的其他类都是一个共同的 Param 类的子类。
# 所有这些类都共享你已经看到过的用于额外验证和元数据的相同参数。

'''
当你从 fastapi 导入 Query、Path 和其他内容时，它们实际上是函数。

当它们被调用时，会返回同名类的实例。

所以，你导入的是 Query 函数。当你调用它时，它会返回一个同样名为 Query 的类的实例。

提供这些函数（而不是直接使用类）是为了让你的编辑器不会标记关于其类型的错误。

这样，你就可以使用你常用的编辑器和编码工具，而无需添加自定义配置来忽略这些错误。
'''