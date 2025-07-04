---
id: mode_change
title: '🛸 模式切换'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

本节介绍`WebPage`的模式切换功能。

`WebPage`的 d 模式，行为与`ChromiumPage`一致，s 模式行为与`SessionPage`一致。

使用`change_mode()`方法进行切换。模式切换的时候会同步登录信息。

## ✅️️ `mode`

**类型：**`str`

此属性返回`WebPage`当前模式。

**示例：**

```python
from DrissionPage import WebPage

page = WebPage()
print(page.mode)
```

**输出：**

```shell
d
```

---

## ✅️️ `change_mode()`

此方法用于切换`WebPage`运行模式。

| 参数名称           | 类型              | 默认值    | 说明                                               |
|:--------------:|:---------------:|:------:| ------------------------------------------------ |
| `mode`         | `str`<br/>`None` | `None` | 接收 's' 或 'd'，以切换到指定模式<br/>接收`None`则切换到与当前相对的另一个模式 |
| `go`           | `bool`          | `True` | 目标模式是否跳转到原模式的 url                                |
| `copy_cookies` | `bool`          | `True` | 切换时是否复制 cookies 到目标模式                            |

**返回：**`None`

---

## ✅️️ 跨模式使用功能

有些功能是 d 模式独有，如`click()`，有些则是 s 模式独有，如`post()`。

事实上，无论处于哪种模式，另一种模式的连接依然存在。因此，在 s 模式调用点击浏览器元素，是完全可以的，两者并不冲突。

这样的设计让使用非常灵活，如要同步登录状态，只需切换模式，或传递 cookies 即可。

### 📌 `cookies_to_session()`

此方法用于复制浏览器当前页面的 cookies 到`Session`对象。

| 参数名称              | 类型     | 默认值    | 说明                 |
|:-----------------:|:------:|:------:| ------------------ |
| `copy_user_agent` | `bool` | `True` | 是否复制 user agent 信息 |

**返回：**`None`

### 📌 `cookies_to_browser()`

此方法用于把`Session`对象的 cookies 复制到浏览器。

---

### 📌 `post()`返回值说明

`SessionPage`的`post()`方法返回网页是否连通，而用`page.html`或`page.json`获取内容。

`WebPage`在 s 模式下`post()`用法也一致。

但在 d 模式，由于`post()`是 s 模式功能，与 d 模式的`html`参数冲突。

所以，d 模式时`post()`返回获取到的`Response`对象，这与`requests`用法一致。

---

## ✅️️ 示例

### 📌 切换模式

```python
from DrissionPage import WebPage

page = WebPage()
page.get('https://www.baidu.com')
print(page.mode)
page.change_mode()
print(page.mode)
print(page.title)
```

**输出：**

```shell
d
s
百度一下，你就知道
```

本示例中，执行操作如下：

- 初始d 模式访问百度

- 切换到 s 模式，此时会同步登录信息到 s 模式，且在 s 模式访问百度

- 打印 s 模式访问到的页面标题
