 

#### 文章目录

*   [一、序列化和反序列化](#_8)
*   *   [1\. 序列化是什么？](#1_09_10)
    *   [2\. 反序列化是什么？](#2_09_14)
    *   [3\. 为什么要序列化？](#3_09_18)
*   [二、JSON](#JSON_44)
*   *   [1\. 简介](#1_09_46)
    *   [2\. 为什么用JSON？](#2_09JSON_56)
    *   [3\. JSON的两种结构](#3_09JSON_64)
    *   [4\. JSON的形式](#4_09JSON_74)
    *   *   [1、值（value）](#1value_76)
        *   [2、字符串（string）](#2string_83)
        *   [3、数值（number）](#3number_91)
        *   [4、对象（object）](#4object_97)
        *   [5、数组（array）](#5array_106)
    *   [5\. 格式转化表](#5_09_113)
*   [三、JSON模块](#JSON_119)
*   *   [1\. dump函数](#1_09dump_127)
    *   [2\. dumps函数](#2_09dumps_165)
    *   [3\. load函数](#3_09load_176)
    *   [4\. loads函数](#4_09loads_199)
*   [四、JSON模块实例](#JSON_213)
*   *   [1\. dump和dumps函数](#1_09dumpdumps_215)
    *   [2\. load和loads函数](#2_09loadloads_255)
    *   [3\. 读取多行的JSON文件](#3_09JSON_280)
*   [结语](#_339)

一、序列化和[反序列化](https://so.csdn.net/so/search?q=%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96&spm=1001.2101.3001.7020)
----------------------------------------------------------------------------------------------------------

### 1\. 序列化是什么？

**序列化** (Serialization)是将**对象的状态信息**转换为**可以存储或传输的形式**的过程。

### 2\. 反序列化是什么？

**反序列化** (Deserialization)是将**有序的二进制序列**转换成**某种对象**（字典，列表等）的过程。

### 3\. 为什么要序列化？

**1、存储**

一个软件/程序的执行就在处理一系列状态的变化。

在编程语言中，“状态”会以各种各样有结构的**数据类型**(也可简单的理解为**变量**)的形式被保存在内存中。

**内存**无法永久保存数据，当程序运行一段时间，断电或者重启程序，内存中关于这个程序的一些数据就被**清空**了。

在断电或重启程序之前将程序当前内存中所有的数据都**保存**下来，以便于下次程序执行能够从文件中载入之前的数据就是**序列化**。

**2、传输**

因为TCP/IP协议**只支持字节数组**的传输，不能直接传**对象**。

对象序列化的结果一定是字节数组！

当两个进程在进行远程通信时，彼此可以发送各种类型的数据。无论是何种类型的数据，都会以**二进制序列**的形式在网络上传送。

发送方需要把这个对象转换为字节序列，才能在网络上传送；接收方则需要把字节序列再恢复为对象。

如果收发的双方约定好实用一种序列化的格式，那么便**打破了平台/语言差异化**带来的限制，实现了**跨平台数据交互**！

![](https://i-blog.csdnimg.cn/blog_migrate/6b0bc32f20b813d56a111b8cf1b9caea.png)

二、JSON
------

### 1\. 简介

**JSON**(JavaScript Object Notation, **JS 对象简谱**) 是一种轻量级的**数据交换格式**。

它基于 ECMAScript (欧洲计算机协会制定的js规范)的一个子集，采用**完全独立于编程语言的文本格式**来存储和表示数据。

简洁和清晰的层次结构使得 JSON 成为理想的**数据交换语言**。

易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。

### 2\. 为什么用JSON？

如果我们要**在不同的编程语言之间传递对象**，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON。

因为JSON表示出来就是一个**字符串**，**可以被所有语言读取**，也可以方便地**存储**到磁盘或者通过网络**传输**。

JSON不仅是标准格式，并且比XML更快，而且可以**直接在Web页面中读取**，非常方便。

### 3\. JSON的两种结构

**1、 “名称/值”对的集合（A collection of name/value pairs**）

不同的编程语言中，它被理解为对象（object），纪录（record），结构（struct），字典（dictionary），哈希表（hash table），有键列表（keyed list），或者关联数组 （associative array）。

**2、 值的有序列表（An ordered list of values）**

在大部分语言中，它被实现为数组（array），矢量（vector），列表（list），序列（sequence）。

### 4\. JSON的形式

#### 1、值（value）

值（value） 可以是双引号括起来的字符串（string）、数值(number)、true、false、 null、对象（object）或者数组（array）。  
这些结构可以嵌套。

![](https://i-blog.csdnimg.cn/blog_migrate/124825a849bf479762c1169c9802f217.png)

#### 2、字符串（string）

字符串（string） 是由 **双引号** 包围的任意数量Unicode字符的集合，使用反斜线**转义**。

一个字符（character）即一个单独的字符串（character string）。

![](https://i-blog.csdnimg.cn/blog_migrate/8aafb3c73ea2d7ccdde5959e82eb53e3.png)

#### 3、数值（number）

JSON的数值没有使用八进制与十六进制格式。

![](https://i-blog.csdnimg.cn/blog_migrate/a112c41fbbc72d1242863d6b99eb7354.png)

#### 4、对象（object）

对象（object） 是一个无序的“‘名称/值’对”集合。

一个对象以“{”（左括号）开始，“}”（右括号）结束。

每个“名称”后跟一个“:”（冒号）；“‘名称/值’ 对”之间使用“,”（逗号）分隔。

![](https://i-blog.csdnimg.cn/blog_migrate/fc0b106b58676a009ce87bb1f6dc25b6.png)

#### 5、数组（array）

数组（array） 是值（value）的有序集合。一个数组以“\[”（左中括号）开始，“\]”（右中括号）结束。值之间使用“,”（逗号）分隔。

![](https://i-blog.csdnimg.cn/blog_migrate/d60c7d2d124e32014ab5856334cdd62c.png)  
参考来源：[JSON中国](http://www.json.org.cn/)

### 5\. 格式转化表

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

![](https://i-blog.csdnimg.cn/blog_migrate/7752994800a0099a8c18ac6e1a68fe08.png)

三、JSON模块
--------

Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它主要提供了四个方法： dump、dumps、load、loads。

dump和dumps对python对象进行**序列化**。将一个Python对象进行JSON格式的编码。

load和loads反序列化方法，将json格式数据解码为Python对象。

### 1\. dump函数

```python
json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
```

1、obj  
表示要序列化的**对象**。

2、fp  
**文件描述符**，将序列化的str保存到文件中。  
json模块总是生成str对象，而不是字节对象；因此，fp.write（）必须支持str输入。

3、skipkeys  
默认为False。如果skipkeys是True则将**跳过不是基本类型（str，int，float，bool，None）的dict键**，不会引发TypeError。

4、ensure\_ascii  
默认值为True，能将所有传入的非ASCII字符**转义输出**。如果ensure\_ascii为False，则这些字符将按**原样输出**。ensure\_ascii=False，让文件中的中文可以直接显示！

5、check\_circular  
默认值为True。如果check\_circular为False，则将**跳过对容器类型的循环引用检查**，循环引用将导致OverflowError。

6、allow\_nan  
默认值为True。如果allow\_nan为True，则将使用它们的JavaScript等效项（NaN，Infinity，-Infinity）。  
如果allow\_nan为False，则**严格遵守JSON规范**，序列化超出范围的浮点值（nan，inf，-inf）会引发ValueError。

7、indent  
设置缩进格式，默认值为None，选择的是**最紧凑**的表示。如果indent是非负整数或字符串，那么JSON数组元素和对象成员将使用该缩进级别进行输入；indent为0，负数或“”仅插入换行符；indent使用正整数缩进多个空格；如果indent是一个字符串（例如“\\t”），则该字符串用于缩进每个级别。

8、separators  
**去除分隔符后面的空格**，默认值为None。如果指定，则分隔符应为（item\_separator，key\_separator）元组。如果缩进为None，则默认为（’，’，’：’）；要获得最紧凑的JSON表示，可以指定（’，’，’:’）以消除空格。

9、default  
默认值为None。如果指定，则default应该是为**无法以其他方式序列化的对象**调用的函数。它应返回对象的JSON可编码版本或引发TypeError。如果未指定，则引发TypeError。

10、sort\_keys  
默认值为False。如果sort\_keys为True，则字典的输出将**按键值排序**。

### 2\. dumps函数

```python
json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
```

dumps函数**不需要传文件描述符(fp)**，其他的参数和dump函数的一样。

![](https://i-blog.csdnimg.cn/blog_migrate/d797eb7c8b3a96d0ec84b77f161c59da.png)

### 3\. load函数

```python
json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
```

1、fp  
文件描述符，将fp（.read（）支持包含JSON文档的文本文件或二进制文件）反序列化为Python对象。

2、object\_hook  
默认值为None，object\_hook是一个可选函数，此功能可用于实现自定义解码器。指定一个函数，该函数负责把反序列化后的基本类型对象转换成自定义类型的对象。

3、parse\_float  
默认值为None。如果指定了parse\_float，用来对JSON float字符串进行解码，这可用于为JSON浮点数使用另一种数据类型或解析器。

4、parse\_int  
默认值为None。如果指定了parse\_int，用来对JSON int字符串进行解码，这可以用于为JSON整数使用另一种数据类型或解析器。

5、parse\_constant  
默认值为None,如果指定了parse\_constant,对-Infinity,Infinity,NaN字符串进行调用。如果遇到了无效的JSON符号，会引发异常。

如果进行反序列化（解码）的数据不是一个有效的JSON文档，将会引发 JSONDecodeError异常。

### 4\. loads函数

```python
json.loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
```

1、s  
将s（包含JSON文档的str，bytes或bytearray实例）反序列化为Python对象。

2、encoding  
指定一个编码的格式。

loads也**不需要文件描述符**，其他参数的含义和load函数的一致。

四、JSON模块实例
----------

### 1\. dump和dumps函数

```python
import json

# dumps可以格式化所有的基本数据类型为字符串
data1 = json.dumps([])         # 列表
print(data1, type(data1))
data2 = json.dumps(2)          # 数字
print(data2, type(data2))
data3 = json.dumps('3')        # 字符串
print(data3, type(data3))
dict = {"name": "Tom", "age": 18}   # 字典
data4 = json.dumps(dict)
print(data4, type(data4))

with open("test.json", "w", encoding='utf-8') as f:
    # indent 格式化保存字典，默认为None，小于0为零个空格。indent=4缩进4个空格
    f.write(json.dumps(dict, indent=4))
    json.dump(dict, f, indent=4)  # 传入文件描述符，和dumps一样的结果
```

得到的输出结果如下（格式化所有的数据类型为str类型）：

```python
[] <class 'str'>
2 <class 'str'>
"3" <class 'str'>
{"name": "Tom", "age": 18} <class 'str'>
```

test.json中的内容：

```python
{
    "name": "Tom",
    "age": 18
}
```

### 2\. load和loads函数

```python
import json

dict = '{"name": "Tom", "age": 18}'   # 将字符串还原为dict
data1 = json.loads(dict)
print(data1, type(data1))

with open("test.json", "r", encoding='utf-8') as f:
    data2 = json.loads(f.read())    # load的传入参数为字符串类型
    print(data2, type(data2))
    f.seek(0)                       # 将文件游标移动到文件开头位置
    data3 = json.load(f)
    print(data3, type(data3))
```

运行结果如下：

```python
{'name': 'Tom', 'age': 18} <class 'dict'>
{'name': 'Tom', 'age': 18} <class 'dict'>
{'name': 'Tom', 'age': 18} <class 'dict'>
```

### 3\. 读取多行的JSON文件

假如要读取一个多行的JSON文件：

```python
{"坂": ["坂5742"]}
{"构": ["构6784"]}
{"共": ["共5171"]}
{"钩": ["钩94a9"]}
{"肮": ["肮80ae"]}
{"孤": ["孤5b64"]}
```

如果直接使用：

```python
    with open(json_path, 'r') as f:
        json_data = json.load(f)
```

就会报错：抛出异常**JSONDecodeError**。  
表示数据错误，数据太多。

**因为json只能读取一个文档对象**，有两个解决办法：  
1、单行读取文件,一次读取一行文件。  
2、保存数据源的时候，格式写为一个对象。

1、**单行读取文件**

```python
with open(json_path, 'r') as f:
 	for line in f.readlines():
        line = line.strip()   # 使用strip函数去除空行
        if len(line) != 0:
            json_data = json.loads(line)
```

2、**合并为一个对象**

将json文件处理成一个对象文件：

```python
{"dict": [
{"坂": ["坂5742"]},
{"构": ["构6784"]},
{"共": ["共5171"]},
{"钩": ["钩94a9"]},
{"肮": ["肮80ae"]},
{"孤": ["孤5b64"]}
]}
```

然后再用：

```python
    with open(json_path, 'r') as f:
        json_data = json.loads(f.read())
```

结语
--

以上就是Python序列化与反序列化详解（包括json和json模块详解）的全部内容啦，希望对大家有所帮助。 如果大家有任何疑问请给我留言，我会尽快回复的。在此也非常感谢大家对CSDN的支持！  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/9c13dd98eac66f07bd40847f7395349f.png)

本文转自 <https://blog.csdn.net/Hardworking666/article/details/112725423>，如有侵权，请联系删除。