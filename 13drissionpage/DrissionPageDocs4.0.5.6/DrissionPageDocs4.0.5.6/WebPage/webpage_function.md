---
id: function
title: '🛸 独有功能'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

本节介绍`Webpage`独有的功能。

`WebPage`是`ChromiumPage`和`SessionPage`的集成，因此拥有这两者全部功能。这些功能具体查看相关章节，这里只介绍`WebPage`独有的功能。

## ✅️️ cookies 处理

### 📌 `cookies_to_session()`

此方法把浏览器的 cookies 复制到`session`对象。

|       参数名称        |   类型   |  默认值   | 说明                 |
|:-----------------:|:------:|:------:|--------------------|
| `copy_user_agent` | `bool` | `True` | 是否复制 user agent 信息 |

**返回：**`None`

---

### 📌 `cookies_to_browser()`

此方法把`session`对象的 cookies 复制到浏览器。

**参数：** 无

**返回：**`None`

---

## ✅️️ 属性设置

`set_cookies()`、`set_headers()`、`set_user_agent()`方法设置的值，只对当前模式有效，即 d 模式时调用这些方法，会对浏览器进行设置，而不会对
Session 对象进行设置，反之亦然。

## ✅️️ 标签页

`WebPage`的`get_tab()`方法获取的标签页对象是`MixTab`，它与`WebPage`一样也能切换状态。除了不能控制标签页和浏览器的下载功能，其它功能与`WebPage`一致。

`MixTab`刚创建的时候处于 d 模式。

**示例：**

```python
from DrissionPage import WebPage

page = WebPage()
tab = page.new_tab('https://www.baidu.com')
tab.change_mode()  # Tab对象也能切换模式
tab.get('https://gitee.com')
print(tab.title)
```

## ✅️️ 关闭对象

### 📌 `close_driver()`

此方法关闭内置`Driver`对象及浏览器，并切换到 s 模式。

**参数：** 无

**返回：**`None`

---

### 📌 `close_session()`

此方法关闭内置`Session`对象及浏览器，并切换到 d 模式。

**参数：** 无

**返回：**`None`

---

### 📌 `close()`

此方法用于关闭当前标签页和 Session。

**参数：** 无

**返回：**`None`

---

### 📌 `quit()`

此方法彻底关闭内置的`Session`对象和`Driver`对象，并关闭浏览器（如已打开）。

|   参数名称    |   类型    |   默认值   | 说明          |
|:---------:|:-------:|:-------:|-------------|
| `timeout` | `float` |   `5`   | 等待浏览器关闭超时时间（秒） |
|  `force`  | `bool`  | `True`  | 关闭超时是否强制终止进程  |

**返回：**`None`
