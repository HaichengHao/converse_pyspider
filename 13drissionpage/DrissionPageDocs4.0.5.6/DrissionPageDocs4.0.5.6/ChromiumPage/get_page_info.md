---
id: get_page_info
title: '🚤 获取网页信息'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

成功访问网页后，可使用`ChromiumPage`自身属性和方法获取页面信息。

操控浏览器除了`ChromiumPage`，还有`ChromiumTab`和`ChromiumFrame`两种页面对象分别对应于标签页对象和`<iframe>`元素对象，后面会有单独章节介绍。

## ✅️️ 页面信息

### 📌 `html`

此属性返回当前页面 html 文本。

:::info 注意
    html 文本不包含`<iframe>`元素内容。
:::

**返回类型：**`str`

---

### 📌 `json`

此属性把请求内容解析成 json。

假如用浏览器访问会返回 `*.json` 文件的 url，浏览器会把 json 数据显示出来，这个参数可以把这些数据转换为`dict`格式。

如果是API返回的json字符串，请使用 SessionPage 对象而不是 `ChromiumPage`。

**返回类型：**`dict`

---

### 📌 `title`

此属性返回当前页面`title`文本。

**返回类型：**`str`

---

### 📌 `user_agent`

此属性返回当前页面 user agent 信息。  

**返回类型：**`str`

---

### 📌 `browser_version`

此属性返回当前浏览器版本号。  

**返回类型：**`str`

---

### 📌 `save()`

把当前页面保存为文件，同时返回保存的内容。

如果`path`和`name`参数都为`None`，只返回内容，不保存文件。

Page 对象和 Tab 对象有这个方法。

|    参数名称    |       类型        |   默认值   | 说明                                       |
|:----------:|:---------------:|:-------:|------------------------------------------|
|   `path`   | `str`<br/>`Path` | `None`  | 保存路径，为`None`且`name`不为`None`时保存到当前路径      |
|   `name`   |      `str`      | `None`  | 保存的文件名，为`None`且`path`不为`None`时使用 title 值 |
|  `as_pdf`  |     `bool`      | `False` | 为`Ture`保存为 pdf，否则保存为 mhtml 且忽略`kwargs`参数 |
| `**kwargs` |       多种        |    无    | pdf 生成参数                                 |

pdf 生成参数包括：`landscape`, `displayHeaderFooter`, `printBackground`, `scale`, `paperWidth`, `paperHeight`, `marginTop`, `marginBottom`, `marginLeft`, `marginRight`, `pageRanges`, `headerTemplate`, `footerTemplate`, `preferCSSPageSize`, `generateTaggedPDF`, `generateDocumentOutline`

|  返回类型   |              说明              |
|:-------:|:----------------------------:|
|  `str`  | `as_pdf`为`False`时返回 mhtml 文本 |
| `bytes` |   `as_pdf`为`True`时返回文件字节数据   |

---

## ✅️️ 运行状态信息

### 📌 `url`

此属性返回当前访问的 url。

**返回类型：**`str`

---

### 📌 `address`

此属性返回当前对象控制的页面地址和端口。

**返回类型：**`str`

```python
print(page.address)
```

**输出：**

```
127.0.0.1:9222
```

---

### 📌 `tab_id`

**返回类型：**`str`

此属性返回当前标签页的 id。

---

### 📌 `process_id`

此属性返回浏览器进程 id。

**返回类型：**`int`、`None`

---

### 📌 `states.is_loading`

此属性返回页面是否正在加载状态。

**返回类型：**`bool`

---

### 📌 `states.is_alive`

此属性返回页面是否仍然可用，标签页已关闭则返回`False`。

**返回类型：**`bool`

---

### 📌 `states.ready_state`

此属性返回页面当前加载状态，有 4 种：

- 'connecting'： 网页连接中
- `'loading'`：表示文档还在加载中
- `'interactive'`：DOM 已加载，但资源未加载完成
- `'complete'`：所有内容已完成加载

**返回类型：**`str`

---

### 📌 `url_available`

此属性以布尔值返回当前链接是否可用。

**返回类型：**`bool`

---

### 📌 `states.has_alert`

此属性以布尔值返回页面是否存在弹出框。

**返回类型：**`bool`

---

## ✅️️ 窗口信息

### 📌 `rect.size`

以`tuple`返回页面大小，格式：(宽, 高)。

**返回类型：**`Tuple[int, int]`

---

### 📌 `rect.window_size`

此属性以`tuple`返回窗口大小，格式：(宽, 高)。

**返回类型：**`Tuple[int, int]`

---

### 📌 `rect.window_location`

此属性以`tuple`返回窗口在屏幕上的坐标，左上角为(0, 0)。

**返回类型：**`Tuple[int, int]`

---

### 📌 `rect.window_state`

此属性以返回窗口当前状态，有`'normal'`、`'fullscreen'`、`'maximized'`、 `'minimized'`几种。

**返回类型：**`str`

---

### 📌 `rect.viewport_size`

此属性以`tuple`返回视口大小，不含滚动条，格式：(宽, 高)。

**返回类型：**`Tuple[int, int]`

---

### 📌 `rect.viewport_size_with_scrollbar`

此属性以`tuple`返回浏览器窗口大小，含滚动条，格式：(宽, 高)。

**返回类型：**`Tuple[int, int]`

---

### 📌 `rect.page_location`

此属性以`tuple`返回页面左上角在屏幕中坐标，左上角为(0, 0)。

**返回类型：**`Tuple[int, int]`

---

### 📌 `rect.viewport_location`

此属性以`tuple`返回视口在屏幕中坐标，左上角为(0, 0)。

**返回类型：**`Tuple[int, int]`

---

## ✅️️ 配置参数信息

### 📌 `timeout`

此属性为整体默认超时时间，包括元素查找、点击、处理提示框、列表选择等需要用到超时设置的地方，都以这个数据为默认值。  
默认为 10，可对其赋值。

**返回类型：**`int`、`float`

```python
# 创建页面对象时指定
page = ChromiumPage(timeout=5)

# 修改 timeout
page.timeout = 20
```

---

### 📌 `timeouts`

此属性以字典方式返回三种超时时间。

- `'base'`：与`timeout`属性是同一个值
- `'page_load'`：用于等待页面加载
- `'script'`：用于等待脚本执行

**返回类型：**`dict`

```python
print(page.timeouts)
```

**输出：**

```
{'base': 10, 'page_load': 30.0, 'script': 30.0}
```

---

### 📌 `retry_times`

此属性为网络连接失败时的重试次数。默认为 3，可对其赋值。

**返回类型：**`int`

```python
# 修改重试次数
page.retry_times = 5
```

---

### 📌 `retry_interval`

此属性为网络连接失败时的重试等待间隔秒数。默认为 2，可对其赋值。

**返回类型：**`int`、`float`

```python
# 修改重试等待间隔时间
page.retry_interval = 1.5
```

---

### 📌 `load_mode`

此属性返回页面加载策略，有 3 种：

- `'normal'`：等待页面所有资源完成加载
- `'eager'`：DOM 加载完成即停止
- `'none'`：页面完成连接即停止

**返回类型：**`str`

---

## ✅️️ cookies 和缓存信息

### 📌 `cookies()`

此方法返回 cookies 信息。

| 参数名称          | 类型     | 默认值     | 说明                                                                                           |
|:-------------:|:------:|:-------:|----------------------------------------------------------------------------------------------|
| `as_dict`     | `bool` | `False` | 是否以字典方式返回结果。为`True`时返回由`{name: value}`键值对组成的`dict`，且`all_info`参数无效；为`False`返回 cookie 组成的`list` |
| `all_domains` | `bool` | `False` | 是否返回所有 cookies，为`False`只返回当前 url 的                                                           |
| `all_info`    | `bool` | `False` | 返回的 cookies 是否包含所有信息，`False`时只包含`name`、`value`、`domain`信息                                    |

| 返回类型   | 说明                                  |
|:------:| ----------------------------------- |
| `dict` | `as_dict`为`True`时，返回字典格式 cookies    |
| `list` | `as_dict`为`False`时，返回 cookies 组成的列表 |

**示例：**

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('http://www.baidu.com')

for i in page.cookies(as_dict=False):
    print(i)
```

**输出：**

```
{'domain': '.baidu.com', 'domain_specified': True, ......}
......
```

---

### 📌 `session_storage()`

此方法用于获取 sessionStorage 信息，可获取全部或单个项。

| 参数名称   | 类型    | 默认值    | 说明                         |
|:------:|:-----:|:------:| -------------------------- |
| `item` | `str` | `None` | 要获取的项目，为`None`则返回全部项目组成的字典 |

| 返回类型   | 说明                     |
|:------:| ---------------------- |
| `dict` | `item`参数为`None`时返回所有项目 |
| `str`  | 指定`item`时返回该项目内容       |

---

### 📌 `local_storage()`

此方法用于获取 localStorage 信息，可获取全部或单个项。

| 参数名称   | 类型    | 默认值    | 说明                         |
|:------:|:-----:|:------:| -------------------------- |
| `item` | `str` | `None` | 要获取的项目，为`None`则返回全部项目组成的字典 |

| 返回类型   | 说明                     |
|:------:| ---------------------- |
| `dict` | `item`参数为`None`时返回所有项目 |
| `str`  | 指定`item`时返回该项目内容       |

---

## ✅️️ 内嵌对象

### 📌 `driver`

此属性返回当前页面对象使用的`Driver`对象。

**返回类型：**`Driver`
