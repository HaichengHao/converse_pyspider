---
id: visit
title: '🚄 访问网页'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

`SessionPage`和`WebPage`的 s 模式基于 requests 进行网络连接，因此可使用 requests 内置的所有请求方式，包括`get()`、`post()`、`head()`、`options()`、`put()`
、`patch()`、`delete()`。不过本库目前只对`get()`和`post()`做了封装和优化，其余方式可通过调用页面对象内置的`Session`对象使用。这里只对`SessionPage`
进行说明，后面章节再单独介绍`WebPage`。

## ✅️️ `get()`

### 📌 访问在线网页

`get()`方法语法与 requests 的`get()`方法一致，在此基础上增加了连接失败重试功能。与 requests 不一样的是，它不返回`Response`对象。

| 参数名称          | 类型               | 默认值     | 说明                          |
|:-------------:|:----------------:|:-------:| --------------------------- |
| `url`         | `str`            | 必填      | 目标 url                      |
| `show_errmsg` | `bool`           | `False` | 连接出错时是否显示和抛出异常              |
| `retry`       | `int`            | `None`  | 重试次数，为`None`时使用页面参数，默认 3    |
| `interval`    | `float` | `None`  | 重试间隔（秒），为`None`时使用页面参数，默认 2 |
| `timeout`     | `float` | `None`  | 加载超时时间（秒）                   |
| `**kwargs`    | -                | `None`  | 连接所需其它参数，具体见 requests 用法    |

| 返回类型   | 说明     |
|:------:|--------|
| `bool` | 是否连接成功 |

`**kwargs`参数与 requests 中该参数使用方法一致，但有一个特点，如果该参数中设置了某一项（如`headers`），该项中的每个项会覆盖从配置中读取的同名项，而不会整个覆盖。  
就是说，如果想继续使用配置中的`headers`信息，而只想修改其中一项，只需要传入该项的值即可。这样可以简化代码逻辑。

实用功能：

- 程序会根据要访问的网址自动在`headers`中加入`Host`和`Referer`项
- 程序会自动从返回内容中确定编码，一般情况无需手动设置

普通访问网页：

```python
from DrissionPage import SessionPage

page = SessionPage()
page.get('http://g1879.gitee.io/drissionpage')
```

使用连接参数访问网页：

```python
from DrissionPage import SessionPage

page = SessionPage()

url = 'https://www.baidu.com'
headers = {'referer': 'gitee.com'}
cookies = {'name': 'value'}
proxies = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
page.get(url, headers=headers, cookies=cookies, proxies=proxies)
```

---

### 📌 读取本地文件

`get()`的`url`参数可指向本地文件，实现本地 html 解析。

```python
from DrissionPage import SessionPage

page = SessionPage()
page.get(r'D:\demo.html')
```

---

## ✅️️ `post()`

此方法是用 post 方式请求页面。用法与`get()`一致。

| 参数名称          | 类型              | 默认值     | 说明                          |
|:-------------:|:---------------:|:-------:| --------------------------- |
| `url`         | `str`           | 必填      | 目标url                       |
| `show_errmsg` | `bool`          | `False` | 连接出错时是否显示和抛出异常              |
| `retry`       | `int`           | `None`  | 重试次数，为`None`时使用页面参数，默认 3    |
| `interval`    | `float`         | `None`  | 重试间隔（秒），为`None`时使用页面参数，默认 2 |
| `**kwargs`    | -               | `None`  | 连接所需其它参数，具体见 requests 用法    |

| 返回类型   | 说明    |
|:------:| ----- |
| `bool` | 是否连接成功 |

```python
from DrissionPage import SessionPage

page = SessionPage()
data = {'username': '****', 'pwd': '****'}

page.post('http://example.com', data=data)
# 或
page.post('http://example.com', json=data)
```

`data`参数和`json`参数都可接收`str`和`dict`格式数据，即有以下 4 种传递数据的方式：

```python
# 向 data 参数传入字符串
page.post(url, data='abc=123')

# 向 data 参数传入字典
page.post(url, data={'abc': '123'})

# 向 json 参数传入字符串
page.post(url, json='abc=123')

# 向 json 参数传入字典
page.post(url, json={'abc': '123'})
```

具体使用哪种，按服务器要求而定。

---

## ✅️️ 其它请求方式

本库只针对常用的 get 和 post 方式作了优化，但也可以通过提取页面对象内的`Session`对象以原生 requests 代码方式执行其它请求方式。

```python
from DrissionPage import SessionPage

page = SessionPage()
# 获取内置的 Session 对象
session = page.session
# 以 head 方式发送请求
response = session.head('https://www.baidu.com')
print(response.headers)
```

**输出：**

```shell
{'Accept-Ranges': 'bytes', 'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'keep-alive', 'Content-Length': '277', 'Content-Type': 'text/html', 'Date': 'Tue, 04 Jan 2022 06:49:18 GMT', 'Etag': '"575e1f72-115"', 'Last-Modified': 'Mon, 13 Jun 2016 02:50:26 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18'}
```
