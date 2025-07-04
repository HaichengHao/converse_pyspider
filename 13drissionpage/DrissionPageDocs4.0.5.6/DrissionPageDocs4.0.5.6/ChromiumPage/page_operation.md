---
id: page_operation
title: '🚤 页面交互'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

本节介绍浏览器页面交互功能，元素的交互在下一节。

一个 Tab 对象（`ChromiumTab`和`MixTab`）控制一个浏览器的标签页，是页面控制的主要单位。

`ChromiumPage`和`WebPage`也控制一个标签页，只是它们增加了一些浏览器总体控制功能。

下面介绍的功能，除了关闭浏览器，Tab 对象都可使用。

## ✅️️ 页面跳转

### 📌 `get()`

该方法用于跳转到一个网址。当连接失败时，程序会进行重试。

|     参数名称      |   类型    |   默认值   | 说明                          |
|:-------------:|:-------:|:-------:|-----------------------------|
|     `url`     |  `str`  |   必填    | 目标 url                      |
| `show_errmsg` | `bool`  | `False` | 连接出错时是否显示和抛出异常              |
|    `retry`    |  `int`  | `None`  | 重试次数，为`None`时使用页面参数，默认 3    |
|  `interval`   | `float` | `None`  | 重试间隔（秒），为`None`时使用页面参数，默认 2 |
|   `timeout`   | `float` | `None`  | 加载超时时间（秒）                   |

|  返回类型  | 说明     |
|:------:|--------|
| `bool` | 是否连接成功 |

**示例：**

```python
page.get('https://www.baidu.com')
```

---

### 📌 `back()`

此方法用于在浏览历史中后退若干步。

|  参数名称   |  类型   | 默认值 | 说明   |
|:-------:|:-----:|:---:|------|
| `steps` | `int` | `1` | 后退步数 |

**返回：**`None`

**示例：**

```python
page.back(2)  # 后退两个网页
```

---

### 📌 `forward()`

此方法用于在浏览历史中前进若干步。

|  参数名称   |  类型   | 默认值 | 说明   |
|:-------:|:-----:|:---:|------|
| `steps` | `int` | `1` | 前进步数 |

**返回：**`None`

```python
page.forward(2)  # 前进两步
```

---

### 📌 `refresh()`

此方法用于刷新当前页面。

|      参数名称      |   类型   |   默认值   | 说明        |
|:--------------:|:------:|:-------:|-----------|
| `ignore_cache` | `bool` | `False` | 刷新时是否忽略缓存 |

**返回：**`None`

**示例：**

```python
page.refresh()  # 刷新页面
```

---

### 📌 `stop_loading()`

此方法用于强制停止当前页面加载。

**参数：** 无

**返回：**`None`

---

### 📌 `set.blocked_urls()`

此方法用于设置忽略的连接。

|      参数名称      |                  类型                  | 默认值 | 说明                                         |
|:--------------:|:------------------------------------:|:---:|--------------------------------------------|
| `urls` | `str`<br/>`list`<br/>`tuple`<br/>`None` | 必填  | 要忽略的 url，可传入多个，可用`'*'`通配符，传入`None`时清空已设置的项 |

**返回：**`None`

**示例：**

```python
page.set.blocked_urls('*.css*')  # 设置不加载css文件
```

---

## ✅️️ 元素管理

### 📌 `add_ele()`

此方法用于创建一个元素。可选择是否插入到 DOM。

`html_or_info`传入元素完整 html 文本时，会插入到 DOM。如`insert_to`参数为`None`，插入到`body`元素。

传入元素信息（格式：`(tag, {name: value})`）时，如`insert_to`参数为`None`，不插入到 DOM。此时返回的元素需用 js 方式点击。

|      参数名称      |                        类型                         |  默认值  | 说明                                                |
|:--------------:|:-------------------------------------------------:|:-----:|---------------------------------------------------|
| `html_or_info` |           `str`<br/>`Tuple[str, dict]`            |  必填   | 新元素的 html 文本或信息；为`tuple`可新建不加入到 DOM 的元素           |
|  `insert_to`   | `str`<br/>`ChromiumElement`<br/>`Tuple[str, str]` |  `None`   | 插入到哪个元素中，可接收元素对象和定位符；如为`None`，`html_or_info`是`str`时添加到 body，否则不添加到 DOM |
|    `before`    | `str`<br/>`ChromiumElement`<br/>`Tuple[str, str]` | `None` | 在哪个子节点前面插入，可接收对象和定位符，为`None`插入到父元素末尾              |

|       返回类型        | 说明    |
|:-----------------:|:---:|
| `ChromiumElement` |  新建的元素对象   |

**添加一个可见的元素：**

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')
html = '<a href="https://DrissionPage.cn" target="blank">DrissionPage </a> '
ele = page.add_ele(html, '#s-top-left', '新闻')  # 插入到导航栏
ele.click()
```

**添加一个不可见的元素：**

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
info = ('a', {'innerText': 'DrissionPage', 'href': 'https://DrissionPage.cn', 'target': 'blank'})
ele = page.add_ele(info)
ele.click('js')  # 需用js点击
```

---

### 📌 `remove_ele()`

此方法用于从页面上删除一个元素。

|     参数名称     |                       类型                        | 默认值 | 说明               |
|:------------:|:-----------------------------------------------:|:---:|------------------|
| `loc_or_ele` | `str`<br/>`Tuple[str, str]`<br/>`ChromiumElement` | 必填  | 要删除的元素，可以是元素或定位符 |

**返回：**`None`

**示例：**

```python
# 删除一个已获得的元素
ele = page('tag:a')
page.remove_ele(ele)

# 删除用定位符找到的元素
page.remove_ele('tag:a')
```

--- 

## ✅️️ 执行脚本或命令

### 📌 `run_js()`

此方法用于执行 js 脚本。

|    参数名称    |   类型    |   默认值   | 说明                                                |
|:----------:|:-------:|:-------:|---------------------------------------------------|
|  `script`  |  `str`  |   必填    | js 脚本文本或脚本文件路径                                    |
|  `*args`   |    -    |    无    | 传入的参数，按顺序在js文本中对应`arguments[0]`、`arguments[1]`... |
| `as_expr`  | `bool`  | `False` | 是否作为表达式运行，为`True`时`args`参数无效                      |
| `timetout` | `float` | `None`  | js 超时时间，为`None`则使用页面`timeouts.script`设置           |

| 返回类型  | 说明     |
|:-----:|--------|
| `Any` | 脚本执行结果 |

**示例：**

```python
# 用传入参数的方式执行 js 脚本显示弹出框显示 Hello world!
page.run_js('alert(arguments[0]+arguments[1]);', 'Hello', ' world!')
```

:::warning 注意
    - 如果`as_expr`为`True`，脚本应是返回一个结果的形式，并且不能有`return`
    - 如果`as_expr`不为`True'，脚本应尽量写成一个方法。
:::

---

### 📌 `run_js_loaded()`

此方法用于运行 js 脚本，执行前等待页面加载完毕。

|    参数名称    |   类型    |   默认值   | 说明                                                |
|:----------:|:-------:|:-------:|---------------------------------------------------|
|  `script`  |  `str`  |   必填    | js 脚本文本                                           |
|  `*args`   |    -    |    无    | 传入的参数，按顺序在js文本中对应`arguments[0]`、`arguments[1]`... |
| `as_expr`  | `bool`  | `False` | 是否作为表达式运行，为`True`时`args`参数无效                      |
| `timetout` | `float` | `None`  | js 超时时间，为`None`则使用页面`timeouts.script`设置           |

| 返回类型  | 说明     |
|:-----:|--------|
| `Any` | 脚本执行结果 |

---

### 📌 `run_async_js()`

此方法用于以异步方式执行 js 代码。

**参数：**

|    参数名称    |   类型    |   默认值   | 说明                                                |
|:----------:|:-------:|:-------:|---------------------------------------------------|
|  `script`  |  `str`  |   必填    | js 脚本文本                                           |
|  `*args`   |    -    |    无    | 传入的参数，按顺序在js文本中对应`arguments[0]`、`arguments[1]`... |
| `as_expr`  | `bool`  | `False` | 是否作为表达式运行，为`True`时`args`参数无效                      |

**返回：**`None`

---

### 📌 `run_cdp()`

此方法用于执行 Chrome DevTools Protocol 语句。

cdp 用法详见 [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)。

|     参数名称     |  类型   | 默认值 | 说明   |
|:------------:|:-----:|:---:|------|
|    `cmd`     | `str` | 必填  | 协议项目 |
| `**cmd_args` |   -   |  无  | 项目参数 |

|  返回类型  | 说明      |
|:------:|---------|
| `dict` | 执行返回的结果 |

**示例：**

```python
# 停止页面加载
page.run_cdp('Page.stopLoading')
```

---

### 📌 `run_cdp_loaded()`

此方法用于执行 Chrome DevTools Protocol 语句，执行前先确保页面加载完毕。

|     参数名称     |  类型   | 默认值 | 说明   |
|:------------:|:-----:|:---:|------|
|    `cmd`     | `str` | 必填  | 协议项目 |
| `**cmd_args` |   -   |  无  | 项目参数 |

|  返回类型  | 说明      |
|:------:|---------|
| `dict` | 执行返回的结果 |

---

## ✅️️ cookies 及缓存

### 📌 `set.cookies()`

此方法用于设置 cookie。可设置一个或多个。

设置一个 cookie 支持的格式：

- `Cookie`：单个`Cookie`对象
- `str`：`'name=value; domain=****; ...'`或`'name=****; value=****; domain=****; ...'`格式，只支持用`';'`分隔
- `dict`：`{'name': '****', 'value': '****', 'domain': '****', ...}`或`{name: value, 'domain': '****', ...}`格式

设置多个 cookie 支持的格式：

- `list`或`tuple`：上面几种形式的单个 cookie 放到列表中传入即可
- `dict`：`{name1: value1, name2: value2, ..., 'domain': '****', ...}`格式
- `str`：`'name1=value1; name2=value2; ... domain=****; ...'`格式，多个 cookie 之间只能用`';'`分隔
- `CookieJar`：单个`CookieJar`对象

| 参数名称      | 类型                                                          | 默认值 | 说明         |
|:---------:|:-----------------------------------------------------------:|:---:|------------|
| `cookies` | `Cookie`<br/>`CookieJar`<br/>`list`<br/>`tuple`<br/>`str`<br/>`dict` | 必填  | cookies 信息 |

**返回：**`None`

**示例：**

```python
# 可以接受多种类型的参数
cookies1 = ['name1=value1', 'name2=value2']
cookies2 = 'name1=value1; name2=value2; path=/; domain=.example.com;'
cookies3 = {'name1': 'value1', 'name2': 'value2', 'domain': '.example.com'}
page.set.cookies(cookies1)
```

---

### 📌 `set.cookies.clear()`

此方法用于清除所有 cookie。

**参数：** 无

**返回：**`None`

---

### 📌 `set.cookies.remove()`

此方法用于删除一个 cookie。

|   参数名称   |  类型   |    默认值     | 说明                 |
|:--------:|:-----:|:----------:|--------------------|
|  `name`  | `str` |     必填     | cookie 的 name 字段   |
|  `url`   | `str` |   `None`   | cookie 的 url 字段    |
| `domain` | `str` |   `None`   | cookie 的 domain 字段 |
|  `path`  | `str` |      `None`      | cookie 的 path 字段   |

**返回：**`None`

---

### 📌 `set.session_storage()`

此方法用于设置或删除某项 sessionStorage 信息。

|  参数名称   |        类型        | 默认值 | 说明             |
|:-------:|:----------------:|:---:|----------------|
| `item`  |      `str`       | 必填  | 要设置的项          |
| `value` | `str`<br/>`False` | 必填  | 为`False`时，删除该项 |

**返回：**`None`

**示例：**

```python
page.set.session_storage(item='abc', value='123')
```

---

### 📌 `set.local_storage()`

此方法用于设置或删除某项 localStorage 信息。

|  参数名称   |        类型        | 默认值 | 说明             |
|:-------:|:----------------:|:---:|----------------|
| `item`  |      `str`       | 必填  | 要设置的项          |
| `value` | `str`<br/>`False` | 必填  | 为`False`时，删除该项 |

**返回：**`None`

---

### 📌 `clear_cache()`

此方法用于清除缓存，可选择要清除的项。

|       参数名称        |   类型   |  默认值   | 说明                  |
|:-----------------:|:------:|:------:|---------------------|
| `session_storage` | `bool` | `True` | 是否清除 sessionstorage |
|  `local_storage`  | `bool` | `True` | 是否清除 localStorage   |
|      `cache`      | `bool` | `True` | 是否清除 cache          |
|     `cookies`     | `bool` | `True` | 是否清除 cookies        |

**返回：**`None`

**示例：**

```python
page.clear_cache(cookies=False)  # 除了 cookies，其它都清除
```

---

## ✅️️ 运行参数设置

各种设置功能藏在`set`属性中。

### 📌 `set.retry_times()`

此方法用于设置连接失败时重连次数。

| 参数名称    | 类型    | 默认值 | 说明 |
|---------|-------|-----|----|
| `times` | `int` | 必填  | 次数 |

**返回：**`None`

### 📌 `set.retry_interval()`

此方法用于设置连接失败时重连间隔。

| 参数名称       | 类型      | 默认值 | 说明 |
|------------|---------|-----|----|
| `interval` | `float` | 必填  | 秒数 |

**返回：**`None`

### 📌 `set.timeouts()`

此方法用于设置三种超时时间，单位为秒。可单独设置，为`None`表示不改变原来设置。

|    参数名称     |   类型    |  默认值   | 说明       |
|:-----------:|:-------:|:------:|----------|
|   `base`    | `float` | `None` | 整体超时时间   |
| `page_load` | `float` | `None` | 页面加载超时时间 |
|  `script`   | `float` | `None` | 脚本运行超时时间 |

**返回：**`None`

**示例：**

```python
page.set.timeouts(base=10, page_load=30)
```

---

### 📌 `set.load_mode`

此属性用于设置页面加载策略，调用其方法选择某种策略。

|    方法名称    | 参数 | 说明                  |
|:----------:|:--:|---------------------|
| `normal()` | 无  | 等待页面完全加载完成，为默认状态    |
| `eager()`  | 无  | 等待文档加载完成就结束，不等待资源加载 |
|  `none()`  | 无  | 页面连接完成就结束           |

**示例：**

```python
page.set.load_mode.normal()
page.set.load_mode.eager()
page.set.load_mode.none()
```

---

### 📌 `set.user_agent()`

此方法用于为浏览器当前标签页设置 user agent。

|    参数名称    |  类型   |  默认值   | 说明                |
|:----------:|:-----:|:------:|-------------------|
|    `ua`    | `str` |   必填   | user agent 字符串    |
| `platform` | `str` | `None` | 平台类型，如`'android'` |

**返回：**`None`

---

### 📌 `set.headers()`

此方法用于设置额外添加到当前页面请求 headers 的参数。

headers 可以是`dict`格式的，也可以是文本格式。

文本格式不同字段用`\n`分隔，字段 key 和 value 用`': '`分隔，即从浏览器直接复制的格式。

|   参数名称    |        类型        | 默认值 | 说明         |
|:---------:|:----------------:|:---:|------------|
| `headers` | `dict`<br/>`str` | 必填  | headers 信息 |

**返回：**`None`

**示例：**

```python
# dict格式
h = {'connection': 'keep-alive', 'accept-charset': 'GB2312,utf-8;q=0.7,*;q=0.7'}
page.set.headers(headers=h)

# 文本格式
h = '''
connection: keep-alive
accept-charset: GB2312,utf-8;q=0.7,*;q=0.7
'''
page.set.headers(headers=h)
```

--- 

## ✅️️ 窗口管理

窗口管理功能藏在`set.window`属性中。

### 📌 `set.window.max()`

此方法用于使窗口最大化。

**参数：** 无

**返回：**`None`

**示例：**

```python
page.set.window.max()
```

---

### 📌 `set.window.mini()`

此方法用于使窗口最小化。

**参数：** 无

**返回：**`None`

---

### 📌 `set.window.full()`

此方法用于使窗口切换到全屏模式。

**参数：** 无

**返回：**`None`

---

### 📌 `set.window.normal()`

此方法用于使窗口切换到普通模式。

**参数：** 无

**返回：**`None`

---

### 📌 `set.window.size()`

此方法用于设置窗口大小。只传入一个参数时另一个参数不会变化。

|   参数名称   |  类型   |  默认值   | 说明   |
|:--------:|:-----:|:------:|------|
| `width`  | `int` | `None` | 窗口宽度 |
| `height` | `int` | `None` | 窗口高度 |

**返回：**`None`

**示例：**

```python
page.set.window.size(500, 500)
```

---

### 📌 `set.window.location()`

此方法用于设置窗口位置。只传入一个参数时另一个参数不会变化。

| 参数名称 |  类型   |  默认值   | 说明     |
|:----:|:-----:|:------:|--------|
| `x`  | `int` | `None` | 距离顶部距离 |
| `y`  | `int` | `None` | 距离左边距离 |

**返回：**`None`

**示例：**

```python
page.set.window.location(500, 500)
```

---

### 📌 `set.window.hide()`

此方法用于隐藏浏览器窗口。

与 headless 模式不一样，这个方法是直接隐藏浏览器进程。在任务栏上也会消失。只支持 Windows 系统，并且必需已安装 pypiwin32 库才可使用。

不过，窗口隐藏后，如果有新窗口出现，整个浏览器又会显现出来。

**参数：** 无

**返回：**`None`

**示例：**

```python
page.set.window.hide()
```

:::warning 注意
    - 浏览器隐藏后并没有关闭，下次运行程序还会接管已隐藏的浏览器
    - 浏览器隐藏后，如果有新建标签页，会自行显示出来
:::

---

### 📌 `set.window.show()`

此方法用于显示当前浏览器窗口。

**参数：** 无

**返回：**`None`

---

## ✅️️ 页面滚动

页面滚动的功能藏在`scroll`属性中。

### 📌 `scroll.to_top()`

此方法用于滚动页面到顶部，水平位置不变。

**参数：** 无

**返回：**`None`

**示例：**

```python
page.scroll.to_top()
```

---

### 📌 `scroll.to_bottom()`

此方法用于滚动页面到底部，水平位置不变。

**参数：** 无

**返回：**`None`

---

### 📌 `scroll.to_half()`

此方法用于滚动页面到垂直中间位置，水平位置不变。

**参数：** 无

**返回：**`None`

---

### 📌 `scroll.to_rightmost()`

此方法用于滚动页面到最右边，垂直位置不变。

**参数：** 无

**返回：**`None`

---

### 📌 `scroll.to_leftmost()`

此方法用于滚动页面到最左边，垂直位置不变。

**参数：** 无

**返回：**`None`

---

### 📌 `scroll.to_location()`

此方法用于滚动页面到滚动到指定位置。

| 参数名称 |  类型   |  默认值   | 说明     |
|:----:|:-----:|:------:|--------|
| `x` | `int` | 必填 | 水平位置，单位是像素 |
| `y` | `int` | 必填 | 垂直位置，单位是像素 |

**返回：**`None`

**示例：**

```python
page.scroll.to_location(300, 50)
```

---

### 📌 `scroll.up()`

此方法用于使页面向上滚动若干像素，水平位置不变。

| 参数名称 |  类型   |  默认值   | 说明     |
|:----:|:-----:|:------:|--------|
| `pixel` | `int` | 必填 | 滚动的像素 |

**返回：**`None`

**示例：**

```python
page.scroll.up(30)
```

---

### 📌 `scroll.down()`

此方法用于使页面向下滚动若干像素，水平位置不变。

| 参数名称 |  类型   |  默认值   | 说明     |
|:----:|:-----:|:------:|--------|
| `pixel` | `int` | 必填 | 滚动的像素 |

**返回：**`None`

---

### 📌 `scroll.right()`

此方法用于使页面向右滚动若干像素，垂直位置不变。

| 参数名称 |  类型   |  默认值   | 说明     |
|:----:|:-----:|:------:|--------|
| `pixel` | `int` | 必填 | 滚动的像素 |

**返回：**`None`

---

### 📌 `scroll.left()`

此方法用于使页面向左滚动若干像素，垂直位置不变。

| 参数名称 |  类型   |  默认值   | 说明     |
|:----:|:-----:|:------:|--------|
| `pixel` | `int` | 必填 | 滚动的像素 |

**返回：**`None`

---

### 📌 `scroll.to_see()`

此方法用于滚动页面直到元素可见。

|     参数名称     |                  类型                   |  默认值   | 说明                                 |
|:------------:|:-------------------------------------:|:------:|------------------------------------|
| `loc_or_ele` | `str`<br/>`tuple`<br/>`ChromiumElement` |   必填   | 元素的定位信息，可以是元素、定位符                  |
|   `center`   |           `bool`<br/>`None`            | `None` | 是否尽量滚动到页面正中，为`None`时如果被遮挡，则滚动到页面正中 |

**返回：**`None`

**示例：**

```python
# 滚动到某个已获取到的元素
ele = page.ele('tag:div')
page.scroll.to_see(ele)

# 滚动到按定位符查找到的元素
page.scroll.to_see('tag:div')
```

---

## ✅️️ 滚动设置

页面滚动有两种方式，一种是滚动时直接跳到目标位置，第二种是平滑滚动，需要一定时间。后者滚动时间难以确定，容易导致程序不稳定，点击不准确的问题。

一些网站会在 css 设置中指定网站使用平滑滚动，这是我们不希望的，但本着让开发者拥有充分选择权利的原则，本库没有强制修改，而是提供两项设置供开发者选择。

### 📌 `set.scroll.smooth()`

此方法设置网站是否开启平滑滚动。建议用此方法为网页关闭平滑滚动。

|   参数名称   |   类型   |  默认值   | 说明          |
|:--------:|:------:|:------:|-------------|
| `on_off` | `bool` | `True` | `bool`表示开或关 |

**返回：**`None`

**示例：**

```python
page.set.scroll.smooth(on_off=False)
```

---

### 📌 `set.scroll.wait_complete()`

此方法用于设置滚动后是否等待滚动结束。在不想关闭网页平滑滚动功能时，可开启此设置以保障滚动结束后才执行后面的步骤

| 参数名称     | 类型     | 默认值    | 说明          |
|----------|--------|--------|-------------|
| `on_off` | `bool` | `True` | `bool`表示开或关 |

**返回：**`None`

**示例：**

```python
page.set.scroll.wait_complete(on_off=True)
```

---

## ✅️️ 弹出消息处理

### 📌 `handle_alert()`

此方法用于处理提示框。  
它能够设置等待时间，等待提示框出现才进行处理，若超时没等到提示框，返回`False`。  
也可只获取提示框文本而不处理提示框。
还可以处理下一个出现的提示框，这在处理离开页面时触发的弹窗非常有用。

:::warning 注意
    程序无法接管一个已经弹出了提示框的浏览器或标签页。
:::

|    参数名称    |        类型        |   默认值   | 说明                                         |
|:----------:|:----------------:|:-------:|--------------------------------------------|
|  `accept`  | `bool`<br/>`None` | `True`  | `True`表示确认，`False`表示取消，`None`不会按按钮但依然返回文本值 |
|   `send`   |      `str`       | `None`  | 处理 prompt 提示框时可输入文本                        |
| `timeout`  |     `float`      | `None`  | 等待提示框出现的超时时间，为`None`时使用页面整体超时时间            |
| `next_one` |      `bool`      | `False` | 是否处理下一个出现的弹窗，为`True`时`timeout`参数无效         |

|  返回类型   | 说明               |
|:-------:|------------------|
|  `str`  | 提示框内容文本          |
| `False` | 未等到提示框则返回`False` |

**示例：**

```python
# 确认提示框并获取提示框文本
txt = page.handle_alert()

# 点击取消
page.handle_alert(accept=False)

# 给 prompt 提示框输入文本并点击确定
page.handle_alert(accept=True, send='some text')

# 不处理提示框，只获取提示框文本
txt = page.handle_alert(accept=None)
```

---

### 📌 自动处理

标签页对象可使用`set.auto_handle_alert()`方法设置自动处理该 tab 的提示框，使提示框不会弹窗而直接被处理掉。

|   参数名称   |   类型   |  默认值   | 说明             |
|:--------:|:------:|:------:|----------------|
| `on_off` | `bool` | `True` | 开或关    |
| `accept` | `bool` | `True` | 确定还是取消 |

**返回：**`None`

**示例：**

```python
from DrissionPage import ChromiumPage

p = ChromiumPage()
p.set.auto_handle_alert()  # 这之后出现的弹窗都会自动确认
```

---

### 📌 全局自动处理

Page 对象的`set.auto_handle_alert()`方法比 Tab 对象的多一个`all_tabs`参数，可用于指定是否全局设置自动处理。

设置后，所有 tab 的弹窗都会根据设置自动处理。

|    参数名称    |   类型   |   默认值   | 说明      |
|:----------:|:------:|:-------:|---------|
|  `on_off`  | `bool` | `True`  | 开或关     |
|  `accept`  | `bool` | `True`  | 确定还是取消  |
| `all_tabs` | `bool` | `False` | 是否为全局设置 |

**返回：**`None`

**示例：**

```python
from DrissionPage import ChromiumPage

p = ChromiumPage()
p.set.auto_handle_alert(all_tabs=True)  # 这之后出现的弹窗都会自动确认
```

---

## ✅️️ 关闭及重连

### 📌 `disconnect()`

此方法用于页面对象断开与页面的连接，但不关闭标签页。断开后，对象不能对标签页进行操作。

Page、Tab 和`ChromiumFrame`对象都有此方法。

值得注意的是，Page 对象断开和浏览器的连接后，仍能进行标签页的管理。

**参数：** 无

**返回：**`None`

---

### 📌 `reconnect()`

此方法用于关闭与页面连接，然后重建一个新连接。

这主要用于应付长期运行导致内存占用过高，断开连接可释放内存，然后重连继续控制浏览器。

Page、Tab 和`ChromiumFrame`对象都有此方法。

|  参数名称  |   类型    | 默认值 | 说明          |
|:------:|:-------:|:---:|-------------|
| `wait` | `float` | `0` | 关闭后等待多少秒再连接 |

**返回：**`None`

---

### 📌 `quit()`

此方法用于关闭浏览器。

|   参数名称    |   类型    |   默认值   | 说明                                         |
|:---------:|:-------:|:-------:|--------------------------------------------|
| `timeout` | `float` |   `5`   | 等待浏览器关闭超时时间（秒）  |
|  `force`  | `bool`  | `True`  | 关闭超时是否强制终止进程      |

**返回：**`None`
