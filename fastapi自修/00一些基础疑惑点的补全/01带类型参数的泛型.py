# @Author    : 百年
# @FileName  :01带类型参数的泛型.py
# @DateTime  :2025/8/20 21:54

'''
带类型参数的泛型¶
有些数据结构可以包含其他值，如 `dict`、`list`、`set` 和 `tuple`。内部的值也可以有自己的类型。

这些具有内部类型的类型被称为“**泛型**”类型。并且可以声明它们，即使是带有它们的内部类型。

要声明这些类型和内部类型，可以使用标准的 Python 模块 `typing`。它专门用于支持这些类型提示。

Python 的新版本¶
使用 `typing` 的语法**兼容**所有版本，从 Python 3.6 到最新版本，包括 Python 3.9、Python 3.10 等。

随着 Python 的发展，**新版本**对这些类型注解提供了改进的支持，在许多情况下，您甚至不需要导入和使用 `typing` 模块来声明类型注解。

如果您的项目可以选择使用较新版本的 Python，您将能够利用这种额外的简洁性。

在所有文档中，都有与每个 Python 版本兼容的示例（当存在差异时）。

例如，“**Python 3.6+**”表示它兼容 Python 3.6 或更高版本（包括 3.7、3.8、3.9、3.10 等）。而“**Python 3.9+**”表示它兼容 Python 3.9 或更高版本（包括 3.10 等）。

如果您可以使用 **最新版本的 Python**，请使用最新版本的示例，这些示例将具有**最佳和最简单的语法**，例如，“**Python 3.10+**”。
'''

#定义一个变量为str类型的list

def process_items(items:list[str]):
    '''
    方括号中的这些内部类型被称为“类型参数”。

在这种情况下，`str` 是传递给 `List`（或 Python 3.9 及以上版本的 `list`）的类型参数。
    '''
    for item in items:
        print(item)

#如果是3.9以下3.8以上可以这么写
from typing import List
def process_item_old(items:List[str]):
    for item in items:
        print(item)



#定义元组和集合类型参数
def process_items_tuplenset(item_tup:tuple[int,int,str],items_s:set[bytes]):
    return item_tup,items_s

#如果是3.9以下3.8以上可以这么写
from typing import Tuple,Set
def process_items_tuplenset_old(items_tup:Tuple[int,int,str],items_s:Set[bytes]):
    return items_tup, items_s


#定义字典

def process_Dic(price:dict[str,float]):
    print(price.items())
    for itemname,item_price in price.items(): #.items可以将可迭代对象返回为元组
        print(itemname,item_price)
        '''dict_items([('藿香正气水', 32.4)])
        藿香正气水
        32.4'''

if __name__ == '__main__':
    process_Dic({'藿香正气水':32.4})
