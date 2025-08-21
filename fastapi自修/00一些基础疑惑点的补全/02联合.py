# @Author    : 百年
# @FileName  :02联合.py
# @DateTime  :2025/8/20 22:09

'''
联合¶
您可以声明一个变量可以是**多种类型**中的任何一种，例如，`int` 或 `str`。

在 Python 3.6 及以上版本（包括 Python 3.10）中，您可以使用 `typing` 模块中的 `Union` 类型，并在方括号中放入可接受的类型。

在 Python 3.10 中，还有一种**新语法**，您可以用竖线（|）分隔可能的类型。
'''

#新的就这么写

def func_n(item:int|str):
    return item

#旧的得这么写
from typing import Union
def func_o(item:Union[int,str]):
    return item


