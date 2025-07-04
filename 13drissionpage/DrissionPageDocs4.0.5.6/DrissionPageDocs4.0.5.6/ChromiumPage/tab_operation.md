---
id: tab
title: '🚤 标签页操作'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

本节介绍对浏览器标签页的管理及使用技巧。

一个 Tab 对象（`ChromiumTab`和`MixTab`）控制一个浏览器的标签页，是页面控制的主要单位。

一个标签页也可以被多个 Tab 对象同时控制（需禁用单例）。

`ChromiumPage`和`WebPage`是标签页的总管，也控制一个标签页，只是它们增加了一些浏览器总体控制功能。

:::info 说明
    `ChromiumPage`和`WebPage`拥有所有 tab 控制的功能。
    `ChromiumTab`和`MixTab`则只有关闭和激活自己的功能。
:::

## ✅️️ 多标签页用法

selenium 没有 tab 对象，driver 每次只能操作一个 tab。多 tab 使用时需在不同的 tab 间来回切换，且切换的时候会丢失之前获取过的元素，效率低，使用不便。

DrissionPage 支持多 tab 对象共存，对象之间互不影响，而且标签页无需激活即可操作。而且，焦点切换会增加维护的复杂性和运行的不稳定性。

因此 DrissionPage 不提供标签页切入切出功能。而使用`get_tab()`或`new_tab()`方法获取指定标签页对象进行操作。

操作逻辑与 Page 对象一致。

**示例1：新建标签页**

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
tab = page.new_tab()  # 新建标签页，获取标签页对象
tab.get('https://www.baidu.com')  # 用标签页对象对标签页进行操作
```

**示例2：获取指定标签页**

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
ele = page.ele('某个链接')
tab = ele.click.for_new_tab()  # 点击某个链接新建标签页
tab.get('https://www.baidu.com')  # 用标签页对象对标签页进行操作
```

---

## ✅️️ 标签页总览

### 📌 `tabs_count`

此属性返回标签页数量。

**类型：**`int`

```python
print(page.tabs_count)
```

**输出：**

```shell
2
```

---

### 📌 `tab_ids`

此属性以`list`方式返回所有标签页 id。

**类型：**`List[str]`

```python
print(page.tab_ids)
```

**输出：**

```shell
['0B300BEA6F1F1F4D5DE406872B79B1AD', 'B838E91F38121B32940B47E8AC59D015']
```

---

## ✅️️ 新建标签页

### 📌 `new_tab()`

该方法用于新建一个标签页，该标签页在最后面。

只有 Page 对象拥有此方法。

|     参数名称      |       类型        |   默认值   | 说明                                                 |
|:-------------:|:---------------:|:-------:|----------------------------------------------------|
|     `url`     | `str`<br/>`None` | `None`  | 新标签页访问的网址，不传入则新建空标签页                               |
| `new_window`  |     `bool`      | `False` | 是否在新窗口打开标签页                                        |
| `background`  |     `bool`      | `False` | 是否不激活新标签页，如`new_window`为`True`则无效                  |
| `new_context` |     `bool`      | `False` | 是否创建新的上下文，为`True`则打开一个无痕模式的新窗口，新窗口与其它窗口不共用 cookies |

|     返回类型      | 说明                                            |
|:-------------:|-----------------------------------------------|
| `ChromiumTab` | `ChromiumPage`对象的`new_tab()`返回`ChromiumTab`对象 |
| `MixTab`  | `WebPage`对象的`new_tab()`返回`MixTab`对象       |

**示例：**

```python
page.new_tab(url='https://www.baidu.com')
```

:::info 注意
    当传入`url`参数时，程序会根据`load_mode`设置访问页面，除了`none`模式，都将等待页面加载完毕。
    如果新建多个标签页不想等待，可批量新建不传入`url`参数的标签页，再遍历使用`get()`。
:::

---

## ✅️️ 获取标签页对象

### 📌 `get_tab()`

此方法用于获取一个标签页对象。可指定标签页序号、id、标题、url、类型等条件用于检索。

当`id_or_num`不为`None`时，其它参数无效。当所有参数都为`None`时，获取 Page 对象控制的标签页的 Tab 对象。

`title`、`url`和`tab_type`三个参数是与关系。

只有 Page 对象拥有此方法。

:::warning 注意
    如传入序号，序号与标签页视觉排序不一定一致，而是按照激活顺序排列。
:::

|    参数名称     |              类型              |   默认值   | 说明                                                |
|:-----------:|:----------------------------:|:-------:|---------------------------------------------------|
| `id_or_num` |  `str`<br/>`int`<br/>`None`  | `None`  | 要获取的标签页 id 或序号（从`1`开始，负数表示从后向前数，`0`和`1`指向同一个 tab） |
|   `title`   |  `str`  | `None`  | 要匹配的标题文本，模糊匹配，为`None`则匹配所有                        |
|    `url`    |  `str`  | `None`  | 要匹配的 url 文本，模糊匹配，为`None`则匹配所有                     |
| `tab_type`  | `str`<br/>`list`<br/>`tuple` | `'page'`  | 标签页类型，可用列表输入多个，如`'page'`,`'iframe'`等，为`None`则匹配所有 |
|   `as_id`   |            `bool`            | `False` | 是否返回标签页 id 而不是标签页对象                               |

|     返回类型      | 说明                      |
|:-------------:|-------------------------|
| `ChromiumTab` | `ChromiumPage`获取的标签页对象  |
| `MixTab`  | `WebPage`获取的标签页对象       |
|     `str`     | `as_id`为`True`时返回标签页 id |
|    `None`     | 找不到指定条件的标签页时返回`None`    |

**示例：**

```python
tab = page.get_tab()  # 获取Page对象控制的标签页的Tab对象（即Page和Tab对象同时控制一个标签页）
tab = page.get_tab(1)  # 获取列表中第1个标签页的对象
tab = page.get_tab('5399F4ADFE3A27503FFAA56390344EE5')  # 获取列表中指定id标签页的对象
tab = page.get_tab(url='baidu.com')  # 获取所有url中带 'baidu.com' 的标签页对象
```

---

### 📌 `get_tabs()`

此方法用于查找符合条件的 tab 对象。可指定标签页标题、url、类型等条件用于检索。

`title`、`url`和`tab_type`三个参数是与关系。

只有 Page 对象拥有此方法。

|    参数名称    |                 类型                  |   默认值   | 说明                               |
|:----------:|:-----------------------------------:|:-------:|----------------------------------|
|   `title`   |  `str`  | `None`  | 要匹配的标题文本，模糊匹配，为`None`则匹配所有                     |
|    `url`    |  `str`  | `None`  | 要匹配的 url 文本，模糊匹配，为`None`则匹配所有                  |
| `tab_type`  | `str`<br/>`list`<br/>`tuple` | `'page'` | 标签页类型，可用列表输入多个，如`'page'`,`'iframe'`等，为`None`则匹配所有 |
|   `as_id`   |            `bool`            | `False` | 是否返回标签页 id 而不是标签页对象                            |

|     返回类型     | 说明                           |
|:------------:|------------------------------|、
| `List[ChromiumTab]` | `ChromiumPage`获取的标签页对象列表 |
| `List[MixTab]` | `WebPage`获取的标签页对象列表 |
| `List[str]` | `as_id`为`None`时返回标签页 id 组成的列表 |

**示例：**

查找 url 包含`'baidu.com'`的 tab 并创建对象：

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')
page.new_tab('https://www.baidu.com')

tabs = page.get_tabs(url='baidu.com')
print(tabs)
```

**输出：**

```shell
[<ChromiumTab browser_id=49baaac8-5e27-4017-b1f5-cf34e453322e tab_id=43E25148146BD5E0389A8FD7F86E15C0>, 
<ChromiumTab browser_id=49baaac8-5e27-4017-b1f5-cf34e453322e tab_id=D4DECA7DFB517CCA2B742A94FF6B638F>]
```

---

### 📌 `latest_tab`

此属性返回最后激活的标签页对象。指最新出现或最新被激活的标签页。

当`Settings.singleton_tab_obj`为`True`时返回 Tab 对象，否则返回 tab id。

只有 Page 对象拥有此属性。

**类型：**`ChromiumTab`、`MixTab`、`str`

**示例：**

```python
# 打开了一个标签页
ele.click()
# 获取最新标签页对象
tab = page.latest_tab  # 与page.get_tab(0)效果一致
```

---

### 📌 `click.for_new_tab()`

在预期点击元素会出现新标签页时，可用元素的这个点击方法，点击后会返回新标签页对象。

具体参数见元素交互章节。

**示例**

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
link = page('tag:a')
tab = link.click.for_new_tab()  # 点击获取新tab对象
print(tab.title)  # 使用新tab对象操作
```

---

### 📌 `click.middle()`

用中键点击`<a>`元素，可强制在新标签页打开链接，此方法默认返回新标签页对象。

具体参数见元素交互章节。

**示例**

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
link = page('tag:a')
tab = link.click.middle()  # 点击获取新tab对象
print(tab.title)  # 使用新tab对象操作
```

---

## ✅️️ 使用多例

默认情况下，Tab 对象是单例的，即一个标签页只有一个对象，即使重复使用`get_tab()`，获取的都是同一个对象。

这主要是防止新手不理解机制，反复创建多个连接导致资源耗费。

实际上允许多个 Tab 对象同时操作一个标签页，每个负责不同的工作。比如一个执行主逻辑流程，另外的监视页面，处理各种弹窗。

要允许多例，可用`Settings`设置：

```python
from DrissionPage.common import Settings

Settings.singleton_tab_obj = False
```

**示例**

```python
from DrissionPage import ChromiumPage
from DrissionPage.common import Settings

page = ChromiumPage()
page.new_tab()
page.new_tab()

# 未启用多例：
tab1 = page.get_tab(1)
tab2 = page.get_tab(1)
print(id(tab1), id(tab2))

# 启用多例：
Settings.singleton_tab_obj = False
tab1 = page.get_tab(1)
tab2 = page.get_tab(1)
print(id(tab1), id(tab2))
```

**输出：**

可见第一次输出两个 Tab 对象是同一个，第二次输出是独立的。

```shell
2347582903056 2347582903056
2347588741840 2347588877712
```

---

## ✅️️ 关闭和重连

### 📌 `close()`

此方法用于标签页关闭自己。

Page 对象和 Tab 对象都有此方法。

值得注意的是，Page 对象关闭标签页后，仍能进行其它标签页的管理。

**参数：** 无

**返回：**`None`

---

### 📌 `disconnect()`

此方法用于页面对象断开和浏览器的连接，但不关闭标签页。断开后，对象不能对标签页进行操作。

Page 对象和 Tab 对象都有此方法。

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

### 📌 `close_tabs()`

此方法用于关闭指定的标签页，可关闭多个。默认关闭当前的。

如果被关闭的标签页包含当前页，会切换到剩下的第一个页面，但未必是视觉上第一个。

此方法只有 Page 对象拥有。

|     参数名称      |                                            类型                                             |   默认值   | 说明                                   |
|:-------------:|:-----------------------------------------------------------------------------------------:|:-------:|--------------------------------------|
| `tabs_or_ids` | `str`<br/>`None`<br/>`ChromiumTab`<br/>`List[str, ChromiumTab]`<br/>`Tuple[str, ChromiumTab]` | `None`  | 要处理的标签页对象或 id，可传入列表或元组，为`None`时处理当前页 |
|   `others`    |                                          `bool`                                           | `False` | 是否关闭指定标签页之外的                         |

**返回：**`None`

**示例：**

```python
# 关闭当前标签页
page.close_tabs()

# 关闭第1、3个标签页
tabs = page.tab_ids
page.close_tabs(tabs_or_ids=(tab_ids[0], tab_ids[2]))
```

---

## ✅️️ 激活标签页

### 📌 `set.tab_to_front()`

此方法用于激活标签页使其处于最前面。但不会把当前对象焦点跳转到该标签页。

此方法只有 Page 对象拥有。

|    参数名称     |                类型                |  默认值   | 说明                         |
|:-----------:|:--------------------------------:|:------:|----------------------------|
| `tab_or_id` | `str`<br/>`ChromiumTab`<br/>`None` | `None` | 标签页对象或 id，默认为`None`表示当前标签页 |

**返回：**`None`

---

### 📌 `set.activate()`

此方法用于 Tab 对象或 Page 对象激活自己。

**参数：** 无

**返回：**`None`

---

## ✅️️ 多标签页协同

做自动化的时候，我们经常会遇到这样一种场景：我们有一个列表页，需要逐个点开里面的链接，获取新页面的内容，每个链接会打开一个新页面。

如果用 selenium 来做，点击一个链接后必需把焦点切换到新标签页，采集信息后再回到原来的页面，点击下一个链接，但由于焦点的切换，原来的元素信息已丢失，我们只能重新获取所有链接，以计数方式点击下一个，非常不优雅。

而用`ChromiumPage`，点开标签页后焦点无需移动，可直接生成一个新标签页的页面对象，对新页面进行采集，而原来列表页的对象可以继续操作下一个链接。甚至可以用多线程控制多个标签页，实现各种黑科技。

我们用 gitee 的推荐项目页面做个演示：[最新推荐项目 - Gitee.com](https://gitee.com/explore/all)

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://gitee.com/explore/all')

links = page.eles('t:h3')
for link in links[:-1]:
    # 点击链接并获取新标签页对象
    new_tab = link.click.for_new_tab()
    # 等待新标签页加载
    new_tab.wait.load_start()
    # 打印标签页标题
    print(new_tab.title)
    # 关闭除列表页外所有标签页
    page.close_tabs(others=True)
```

**输出：**

```shell
wx-calendar: 原生小程序日历组件(可滑动，可标记，可禁用)
thingspanel-go: 开源插件化物联网平台，Go语言开发。支持MQTT、Modbus多协议、多类型设备接入与可视化、自动化、告警、规则引擎等功能。 QQ群：371794256。
APITable: vika.cn维格表社区版，地表至强的开源低代码、多维表格工具，Airtable的开源免费替代。
ideaseg: 基于 NLP 技术实现的中文分词插件，准确度比常用的分词器高太多，同时提供 ElasticSearch 和 OpenSearch 插件。
vue-plugin-hiprint: hiprint for Vue2/Vue3 ⚡打印、打印设计、可视化设计器、报表设计、元素编辑、可视化打印编辑
ExDUIR.NET: Windows平台轻量DirectUI框架

后面省略。。。
```
