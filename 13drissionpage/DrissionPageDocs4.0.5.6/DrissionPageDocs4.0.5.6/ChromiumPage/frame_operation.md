---
id: iframe
title: '🚤 iframe 操作'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

`<iframe>`元素是一种特殊的元素，它既是元素，也是页面，因此独立一个章节对其进行介绍。

与 selenium 不同，DrissionPage 无需切入切出即可处理`<iframe>`
元素。因此可实现跨级元素查找、元素内部单独跳转、同时操作`<iframe>`内外元素、多线程控制多个`<iframe>`等操作，功能更灵活，逻辑更清晰。

我们使用菜鸟教程在线编辑器来演示：

[菜鸟教程在线编辑器 (runoob.com)](https://www.runoob.com/try/try.php?filename=tryhtml_iframe)

源代码框内容要作一点调整，然后按“点击运行”：

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>菜鸟教程(runoob.com)</title>
</head>

<body>
<iframe id="sss" src="https://www.runoob.com">
    <p>您的浏览器不支持 iframe 标签。</p>
</iframe>
</body>
</html>
```

按`F12`，可以看到网页右侧是一个两层`<iframe>`，一个 id 是`'iframeResult'`的`<iframe>`里面有一个 id 是`'sss'`的`<iframe>`
。最里层的`<iframe>`
页面指向 https://www.runoob.com。

---

## ✅️ 获取`<iframe>`对象

获取`<iframe>`对象的方法有两种，可用获取普通元素的方式获取，或者用`get_frame()`方法获取。推荐优先使用`get_frame()`
方法，因为当作普通元素获取时，IDE 无法正确识别获取到的是`<iframe>`元素。

### 📌 `get_frame()`

此方法用于获取页面中一个`<frame>`或`<iframe>`对象。

|     参数名称      |                类型                 |  默认值   | 说明                                                                           |
|:-------------:|:---------------------------------:|:------:|------------------------------------------------------------------------------|
| `loc_ind_ele` | `str`<br/>`int`<br/>`ChromiumFrame` |   必填   | 定位符<br/>`<iframe>`元素序号（从`1`开始，负数表示倒数）<br/>`ChromiumFrame对象`<br/>`id`属性内容<br/>`name`属性内容 |
|   `timeout`   |              `float`              | `None` | 超时时间，为`None`时使用页面超时时间                                                        |

|      返回类型       | 说明                       |
|:---------------:|--------------------------|
| `ChromiumFrame` | `<frame>`或`<iframe>`元素对象 |
|  `NoneElement`  | 找不到时返回`NoneElement`      |

:::warning 注意
    需要特别注意的是，如果页面中有嵌套的`<iframe>`，用序号获取的方式会存在不准确。
    比如上面说的网站，用`get_frames()`可获取到 6 个元素，但用`get_frame(6)`却获取不到最后一个。
    这是因为有两个`<iframe>`是嵌套关系，导致获取不准确。
:::

**示例：**

```python
# 使用定位符获取
iframe = page.get_frame('#sss')

# 获取第1个iframe
iframe = page.get_frame(1)
```

---

### 📌 `get_frames()`

此方法用于获取页面中多个符合条件的`<frame>`或`<iframe>`对象。

|     参数名称      |             类型              |  默认值   | 说明                    |
|:-------------:|:---------------------------:|:------:|-----------------------|
| `locator` | `str`<br/>`Tuple[str, str]` | `None` | 定位符，为`None`时返回所有      |
|   `timeout`   |           `float`           | `None` | 超时时间，为`None`时使用页面超时时间 |

|         返回类型          | 说明                            |
|:---------------------:|-------------------------------|
| `List[ChromiumFrame]` | `<frame>`或`<iframe>`元素对象组成的列表 |

:::info 提醒
    获取所有`<iframe>`会很慢，而且浪费资源，一般使用获取需要用到的就好。
:::

---

### 📌 普通元素方式

可以用获取普通元素的方式获取`<iframe>`对象：

```python
iframe = page('#sss')
print(iframe.html)
```

**输出：**

```shell
<iframe id="sss" src="https://www.runoob.com"><html><head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>菜鸟教程 - 学的不仅是技术，更是梦想！</title>

  <meta name="robots" content="max-image-preview:large">

下面省略。。。
```

这个`ChromiumFrame`对象既是页面也是元素。由于 IDE 不会提示`<iframe>`
元素对象相关的属性和方法，因此用这种方式获取时建议再用`get_frame()`包装一下：

```python
iframe = page('#sss')
iframe = page.get_frame(iframe)
```

---

## ✅️ 查找`<iframe>`内元素

从刚才获取元素对象看出，我们并不需要先切入 id 为`'iframeResult'`的`<iframe>`
，就可以获取到里面的元素。所以我们获取元素也并不一定要先获取到`ChromiumFrame`对象。

### 📌 在`<iframe>`内查找

使用我们刚才获取到的元素，可以在里面查找元素：

```python
ele = iframe('首页')
print(ele)
```

**输出：**

```shell
<ChromiumElement a href='https://www.runoob.com/' data-id='index' title='菜鸟教程' class='current'>
```

---

### 📌 页面跨`<iframe>`查找

如果`<iframe>`元素的网址和主页面是同域的，我们可以直接用页面对象查找`<iframe>`内部元素，而无需先获取`ChromiumFrame`对象：

```python
ele = page('首页')
print(ele)
```

**输出：**

```shell
<ChromiumElement a href='https://www.runoob.com/' data-id='index' title='菜鸟教程' class='current'>
```

只要是同域名的，无论跨多少层`<iframe>`都能用页面对象直接获取。

---

### 📌 与 selenium 对比

`WebPage`：

```python
from DrissionPage import WebPage

page = WebPage()
ele = page('首页')
```

`MixPage`（基于 selenium）：

```python
from DrissionPage import MixPage

page = MixPage()
page.to_frame('#iframeResult')
page.to_frame('#sss')
ele = page('首页')
page.to_frame.main()
```

可见，原来的逻辑要切入切出，比较繁琐。

---

### 📌 重要事项

如果`<iframe>`跟当前标签页是不同域名的，不能使用页面对象直接查找其中元素，只能先获取其`ChromiumFrame`元素对象，再在这个对象中查找。

---

## ✅️ `ChromiumFrame`的元素特征

正如上面所说，`ChromiumFrame`既是元素也是页面，这里说一下其元素方面的用法。

### 📌 `tag`

此属性返回元素名称。

**类型：**`str`

---

### 📌 `html`

此属性返回整个`<iframe>`元素的 outerHTML 文本。

**类型：**`str`

---

### 📌 `inner_html`

此属性返回 innerHTML 文本。

**类型：**`str`

---

### 📌 `attrs`

此属性以`dict`形式返回元素所有 attribute 属性。

**类型：**`dict`

---

### 📌 `xpath`

此属性返回元素在其页面上的 xpath 路径。

**类型：**`str`

---

### 📌 `css_path`

此属性返回元素在其页面上的 css selector 路径。

**类型：**`str`

---

### 📌 `attr()`

此方法用于一个获取元素 attribute 属性。

|  参数名称  |  类型   | 默认值 | 说明  |
|:------:|:-----:|:---:|-----|
| `name` | `str` | 必填  | 属性名 |

|  返回类型  | 说明            |
|:------:|---------------|
| `str`  | 属性值文本         |
| `None` | 没有该属性返回`None` |

---

### 📌 `set.attr()`

此方法用于设置元素的 attribute 属性。

|  参数名称   |  类型   | 默认值 | 说明  |
|:-------:|:-----:|:---:|-----|
| `name`  | `str` | 必填  | 属性名 |
| `value` | `str` | 必填  | 属性值 |

**返回：**`None`

---

### 📌 `remove_attribute()`

此方法用于删除元素的 attribute 属性。

|  参数名称  |  类型   | 默认值 | 说明  |
|:------:|:-----:|:---:|-----|
| `name` | `str` | 必填  | 属性名 |

**返回：**`None`

---

### 📌 相对定位

相对定位方法与普通元素一致，详见获取元素章节。

- `parent()`：返回上面某一级父元素。

- `prev()`：返回前面的一个兄弟元素。

- `next()`：返回后面的一个兄弟元素。

- `before()`：返回当前元素前面的一个元素。

- `after()`：返回当前元素后面的一个元素。

- `prevs()`：返回前面全部兄弟元素或节点组成的列表。

- `nexts()`：返回后面全部兄弟元素或节点组成的列表。

- `befores()`：返回当前元素后面符合条件的全部兄弟元素或节点组成的列表。

---

## ✅️ `ChromiumFrame`的页面特征

### 📌 `url`

此属性返回页面当前 url。

**类型：**`str`

---

### 📌 `title`

此属性返回页面当前 title 文本。

**类型：**`str`

---

### 📌 `get()`

此方法用于实现`<iframe>`页面跳转，使用方法与`ChromiumPage`一致。

```python
iframe.get('https://www.runoob.com/css3/css3-tutorial.html')
```

---

### 📌 `refresh()`

此方法用于刷新页面。

**参数**： 无

**返回：**`None`

```python
iframe.refresh()
```

---

### 📌 `active_ele`

此属性返回页面中焦点所在元素。

**类型：**`ChromiumElement`

---

### 📌 `run_js()`

此方法用于在`<iframe>`内执行 js 脚本。

|    参数名称    |   类型    |   默认值   | 说明                                                |
|:----------:|:-------:|:-------:|---------------------------------------------------|
|  `script`  |  `str`  |   必填    | js 脚本文本或脚本文件路径                                           |
|  `*args`   |    -    |    无    | 传入的参数，按顺序在js文本中对应`arguments[0]`、`arguments[1]`... |
| `as_expr`  | `bool`  | `False` | 是否作为表达式运行，为`True`时`args`参数无效                      |
| `timetout` | `float` | `None`  | js 超时时间，为`None`则使用页面`timeouts.script`设置           |

| 返回类型  | 说明     |
|:-----:|--------|
| `Any` | 脚本执行结果 |

---

### 📌 `scroll`

`ChromiumFrame`的滚动方法与页面或元素是一致的。

**示例：** 使`<iframe>`元素向下滚动 300 像素

```python
iframe.scroll.down(300)
```

---

### 📌 `get_screenshot()`

此方法用于对`<iframe>`进行截图。由于技术限制，只能对视口截图。

下面三个参数三选一，优先级：`as_bytes`>`as_base64`>`path`。

| 参数名称        | 类型              | 默认值    | 说明                                                                                                                    |
|-------------|-----------------|--------|-----------------------------------------------------------------------------------------------------------------------|
| `path`      | `str`<br/>`Path` | `None` | 保存图片的路径，为`None`时保存在当前文件夹                                                                                              |
| `name`      | `str`           | `None` | 完整文件名，后缀可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`，为`None`时以用 jpg 格式                                                         |
| `as_bytes`  | `str`<br/>`True` | `None` | 是否以字节形式返回图片，可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`、`None`、`True`<br/>不为`None`时`path`和`as_base64`参数无效<br/>为`True`时选用 jpg 格式 |
| `as_base64` | `str`<br/>`True` | `None` | 是否以 base64 形式返回图片，可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`、`None`、`True`<br/>不为`None`时`path`参数无效<br/>为`True`时选用 jpg 格式       |

| 返回类型    | 说明                                     |
|---------|----------------------------------------|
| `bytes` | `as_bytes`生效时返回图片字节                    |
| `str`   | `as_bytes`和`as_base64`为`None`时返回图片完整路径 |
| `str`   | `as_base64`生效时返回 base64 格式的字符串         |

---

## ✅️ 位置与大小

### 📌 `rect.location`

此属性返回 iframe 元素左上角在页面中的坐标。格式：(x, y)，左上角为(0, 0)。

**返回类型：**`Tuple[float, float]`

---

### 📌 `rect.viewport_location`

此属性返回 iframe 元素左上角在视口中的坐标。格式：(x, y)，左上角为(0, 0)。

**返回类型：**`Tuple[float, float]`

---

### 📌 `rect.screen_location`

此属性返回 iframe 元素左上角在屏幕上的坐标。格式：(x, y)，左上角为(0, 0)。

**返回类型：**`Tuple[float, float]`

---

### 📌 `rect.size`

此属性返回 frame 内页面尺寸，格式：(宽, 高)。

**返回类型：**`Tuple[float, float]`

---

### 📌 `rect.viewport_size`

此属性返回 iframe 口宽高，格式：(宽, 高)。

**返回类型：**`Tuple[float, float]`

---

### 📌 `rect.corners`

此属性返回 iframe 元素四个角在页面中的坐标，顺序：坐上、右上、右下、左下。

**返回类型：**`((float, float), (float, float), (float, float), (float, float),)`

---

### 📌 `rect.viewport_corners`

此属性返回 iframe 元素四个角在视口中的坐标，顺序：坐上、右上、右下、左下。

**返回类型：**`((float, float), (float, float), (float, float), (float, float),)`

---

## ✅️ 对象状态

### 📌 `states.is_loading`

此属性返回页面是否在加载状态。

**返回类型：**`bool`

---

### 📌 `states.is_alive`

此属性返回frame元素是否可用，且里面仍挂载有frame。

**返回类型：**`bool`

---

### 📌 `states.is_displayed`

此属性返回 iframe 是否显示。

**返回类型：**`bool`

---

### 📌 `states.ready_state`

此属性返回加载状态，有 4 种：

- 'connecting'： 网页连接中
- `'loading'`：文档还在加载中
- `'interactive'`：DOM 已加载，但资源未加载完成
- `'complete'`：所有内容已完成加载

**返回类型：**`str`
