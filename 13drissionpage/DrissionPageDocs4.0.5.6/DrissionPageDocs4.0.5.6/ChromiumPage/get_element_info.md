---
id: get_ele_info
title: '🚤 获取元素信息'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

浏览器元素对应的对象是`ChromiumElement`和`ShadowRoot`，本节介绍获取到元素对象后，如何获取其信息。

`ChromiumElement`拥有`SessionElement`所有属性，并有更多浏览器专属的信息。本节重点介绍如何获取浏览器专有的元素信息。

## ✅️️ 与`SessionElement`共有信息

此处仅列出列表，具体用法请查看收发数据包部分的“获取元素信息”。

|    属性或方法     | 说明                                     |
|:------------:|----------------------------------------|
|    `html`    | 此属性返回元素的 outerHTML 文本（不包括`<iframe>`内容） |
| `inner_html` | 此属性返回元素的 innerHTML 文本                  |
|    `tag`     | 此属性返回元素的标签名                            |
|    `text`    | 此属性返回元素内所有文本组合成的字符串                    |
|  `raw_text`  | 此属性返回元素内原始文本                           |
|  `texts()`   | 此方法返回元素内所有**直接**子节点的文本，包括元素和文本节点       |
|  `comments`  | 此属性以列表形式返回元素内的注释                       |
|   `attrs`    | 此属性以字典形式返回元素所有属性及值                     |
|   `attr()`   | 此方法返回元素某个 attribute 属性值                |
|    `link`    | 此方法返回元素的 href 属性或 src 属性               |
|    `page`    | 此属性返回元素所在的总控页面对象                       |
|   `xpath`    | 此属性返回当前元素在页面中 xpath 的绝对路径              |
|  `css_path`  | 此属性返回当前元素在页面中 css selector 的绝对路径       |

---

## ✅️️ 大小和位置

### 📌 `rect.size`

此属性以元组形式返回元素的大小。

**类型：**`Tuple[float, float]`

```python
size = ele.rect.size
# 返回：(50, 50)
```

---

### 📌 `rect.location`

此属性以元组形式返回元素**左上角**在**整个页面**中的坐标。

**类型：**`Tuple[float, float]`

```python
loc = ele.rect.location
# 返回：(50, 50)
```

---

### 📌 `rect.midpoint`

此属性以元组形式返回元素**中点**在**整个页面**中的坐标。

**类型：**`Tuple[float, float]`

```python
loc = ele.rect.midpoint
# 返回：(55, 55)
```

---

### 📌 `rect.click_point`

此属性以元组形式返回元素**点击点**在**整个页面**中的坐标。

点击点是指`click()`方法点击时的位置，位于元素中上部。

**类型：**`Tuple[float, float]`

---

### 📌 `rect.viewport_location`

此属性以元组形式返回元素**左上角**在**当前视口**中的坐标。

**类型：**`Tuple[float, float]`

---

### 📌 `rect.viewport_midpoint`

此属性以元组形式返回元素**中点**在**当前视口**中的坐标。

**类型：**`Tuple[floatt, float]`

---

### 📌 `rect.viewport_click_point`

此属性以元组形式返回元素**点击点**在**当前视口**中的坐标。

**类型：**`Tuple[float, float]`

---

### 📌 `rect.screen_location`

此属性以元组形式返回元素**左上角**在**屏幕**中的坐标。

**类型：**`Tuple[float, float]`

---

### 📌 `rect.screen_midpoint`

此属性以元组形式返回元素**中点**在**屏幕**中的坐标。

**类型：**`Tuple[float, float]`

---

### 📌 `rect.screen_click_point`

此属性以元组形式返回元素**点击点**在**屏幕**中的坐标。

**类型：**`Tuple[float, float]`

---

### 📌 `rect.corners`

此属性以列表形式返回元素四个角在页面中的坐标，顺序：左上、右上、右下、左下。

**类型：**`((float, float), (float, float), (float, float), (float, float),)`

---

### 📌 `rect.viewport_corners`

此属性以列表形式返回元素四个角在视口中的坐标，顺序：左上、右上、右下、左下。

**类型：**`list[(float, float), (float, float), (float, float), (float, float)]`

---

### 📌 `rect.viewport_rect`

此属性以列表形式返回元素四个角在视口中的坐标，顺序：左上、右上、右下、左下。

**类型：**`List[(float, float), (float, float), (float, float), (float, float)]`

---

## ✅️️ 属性和内容

### 📌 `pseudo.before`

此属性以文本形式返回当前元素的`::before`伪元素内容。

**类型：**`str`

```python
before_txt = ele.pseudo.before
```

---

### 📌 `pseudo.after`

此属性以文本形式返回当前元素的`::after`伪元素内容。

**类型：**`str`

```python
after_txt = ele.pseudo.after
```

---

### 📌 `style()`

该方法返回元素 css 样式属性值，可获取伪元素的属性。它有两个参数，`style`参数输入样式属性名称，`pseudo_ele`
参数输入伪元素名称，省略则获取普通元素的 css 样式属性。

|     参数名称     |  类型   | 默认值  | 说明        |
|:------------:|:-----:|:----:|-----------|
|   `style`    | `str` |  必填  | 样式名称      |
| `pseudo_ele` | `str` | `''` | 伪元素名称（如有） |

| 返回类型  | 说明    |
|:-----:|-------|
| `str` | 样式属性值 |

**示例：**

```python
# 获取 css 属性的 color 值
prop = ele.style('color')

# 获取 after 伪元素的内容
prop = ele.style('content', 'after')
```

---

### 📌 `property()`

此方法返回`property`属性值。它接收一个字符串参数，返回该参数的属性值。

|  参数名称  |  类型   | 默认值 | 说明   |
|:------:|:-----:|:---:|------|
| `name` | `str` | 必填  | 属性名称 |

| 返回类型  | 说明  |
|:-----:|-----|
| `str` | 属性值 |

---

### 📌 `shadow_root`

此属性返回元素内的 shadow-root 对象，没有的返回`None`。

**类型：**`ShadowRoot`

---

## ✅️️ 元素列表中批量获取信息

`eles()`等返回的元素列表，自带`get`属性，可用于获取指定信息。

### 📌 示例

```python
from DrissionPage import SessionPage

page = SessionPage()
page.get('https://www.baidu.com')
eles = page('#s-top-left').eles('t:a')
print(eles.get.texts())  # 获取所有元素的文本
```

**输出：**

```shell
['新闻', 'hao123', '地图', '贴吧', '视频', '图片', '网盘', '文库', '更多', '翻译', '学术', '百科', '知道', '健康', '营销推广', '直播', '音乐', '橙篇', '查看全部百度产品 >']
```

### 📌 `get.attrs()`

此方法用于返回所有元素指定的 attribute 属性组成的列表。

|  参数名称  |  类型   | 默认值 | 说明   |
|:------:|:-----:|:---:|------|
| `name` | `str` | 必填  | 属性名称 |

|    返回类型     | 说明        |
|:-----------:|-----------|
| `List[str]` | 属性文本组成的列表 |

---

### 📌 `get.links()`

此方法用于返回所有元素的`link`属性组成的列表。

**参数：** 无

|    返回类型     | 说明        |
|:-----------:|-----------|
| `List[str]` | 链接文本组成的列表 |

---

### 📌 `get.texts()`

此方法用于返回所有元素的`text`属性组成的列表。

**参数：** 无

|    返回类型     | 说明        |
|:-----------:|-----------|
| `List[str]` | 元素文本组成的列表 |

---

## ✅️️ 状态信息

状态信息藏在`states`属性中。

### 📌`states.is_in_viewport`

此属性以布尔值方式返回元素是否在视口中，以元素可以接受点击的点为判断。

**类型：**`bool`

---

### 📌`states.is_whole_in_viewport`

此属性以布尔值方式返回元素是否整个在视口中。

**类型：**`bool`

---

### 📌`states.is_alive`

此属性以布尔值形式返回当前元素是否仍可用。用于判断 d 模式下是否因页面刷新而导致元素失效。

**类型：**`bool`

---

### 📌 `states.is_checked`

此属性以布尔值返回表单单选或多选元素是否选中。

**类型：**`bool`

---

### 📌 `states.is_selected`

此属性以布尔值返回`<select>`元素中的项是否选中。

**类型：**`bool`

---

### 📌 `states.is_enabled`

此属性以布尔值返回元素是否可用。

**类型：**`bool`

---

### 📌 `states.is_displayed`

此属性以布尔值返回元素是否可见。

**类型：**`bool`

--- 

### 📌 `states.is_covered`

此属性返回元素是否被其它元素覆盖。如被覆盖，返回覆盖元素的 id，否则返回`False`

|  返回类型   |       说明       |
|:-------:|:--------------:|
| `False` | 未被覆盖，返回`False`  |
|  `int`   | 被覆盖时返回覆盖元素的 id |

--- 

### 📌 `states.is_clickable`

此属性返回元素是否可被模拟点击，从是否有大小、是否可用、是否显示、是否响应点击判断，不判断是否被遮挡。

**类型：**`bool`

--- 

### 📌 `states.has_rect`

此属性返回元素是否拥有大小和位置信息，有则返回四个角在页面上的坐标组成的列表，没有则返回`False`。

|  返回类型   | 说明                                                        |
|:-------:|-----------------------------------------------------------|
| `list`  | 存在大小和位置信息时，以[(int, int), ...] 格式返回元素四个角的坐标，顺序：左上、右上、右下、左下 |
| `False` | 不存在时返回`False`                                             |

--- 

## ✅️️ 保存元素

保存功能是本库一个特色功能，可以直接读取浏览器缓存，无需依赖另外的 ui 库或重新下载就可以保存页面资源。

作为对比，selenium 无法自身实现图片另存，往往需要通过使用 ui 工具进行辅助，不仅效率和可靠性低，还占用键鼠资源。

### 📌 `src()`

此方法用于返回元素`src`属性所使用的资源。base64 的可转为`bytes`返回，其它的以`str`返回。无资源的返回`None`。

例如，可获取页面上图片字节数据，用于识别内容，或保存到文件。`<script>`标签也可获取 js 文本。

|       参数名称        |   类型    |  默认值   | 说明                                     |
|:-----------------:|:-------:|:------:|----------------------------------------|
|     `timeout`     | `float` | `None` | 等待资源加载超时时间，为`None`时使用元素所在页面`timeout`属性 |
| `base64_to_bytes` | `bool`  | `True` | 为`True`时，如果是 base64 数据，转换为`bytes`格式    |

|  返回类型  | 说明           |
|:------:|--------------|
| `str`  | 资源字符串        |
| `None` | 无资源的返回`None` |

**示例：**

```python
img = page('tag:img')
src = img.src()
```

---

### 📌 `save()`

此方法用于保存`src()`方法获取到的资源到文件。

|   参数名称    |        类型        |  默认值   | 说明                                     |
|:---------:|:----------------:|:------:|----------------------------------------|
|  `path`   | `str`<br/>`Path` | `None` | 文件保存路径，为`None`时保存到当前文件夹                |
|  `name`   |      `str`       | `None` | 文件名称，需包含后缀，为`None`时从资源 url 获取          |
| `timeout` |     `float`      | `None` | 等待资源加载超时时间，为`None`时使用元素所在页面`timeout`属性 |
| `rename` |      `bool`      | `True` | 遇到重名文件时是否自动重命名                         |

| 返回类型  | 说明   |
|:-----:|------|
| `str` | 保存路径 |

**示例：**

```python
img = page('tag:img')
img.save('D:\\img.png')
```

---

## ✅️️ `ShadowRoot`属性

本库把 shadow dom 的`root`看作一个元素处理，可以获取属性，也可以执行其下级的查找，使用逻辑与`ChromiumElement`
一致，但属性较之少，有如下这些：

### 📌 `tag`

此属性返回元素标签名，即`'shadow-root'`。

**类型：**`str`

---

### 📌 `html`

此属性返回`shadow_root`的 html 文本，由`<shadow_root></shadow_root>` 标签包裹。

**类型：**`str`

---

### 📌 `inner_html`

此属性返回`shadow_root`内部的 html 文本。

**类型：**`str`

---

### 📌 `page`

此属性返回元素所在页面对象。

**类型：**`ChromiumPage`、`ChromiumTab`、`ChromiumFrame`、`WebPage`

---

### 📌 `parent_ele`

此属性返回所依附的普通元素对象。

**类型：**`ChromiumElement`

---

### 📌 `states.is_enabled`

与`ChromiumElement`一致。

**类型：**`bool`

---

### 📌 `states.is_alive`

与`ChromiumElement`一致。

**类型：**`bool`


---

## ✅️️ 比较元素

两个元素对象可以用`==`来比较，以判断它们是否指向同一个元素。

**示例：**

```python
ele1 = page('t:div')
ele2 = page('t:div')
print(ele1==ele2)  # 输出True
```