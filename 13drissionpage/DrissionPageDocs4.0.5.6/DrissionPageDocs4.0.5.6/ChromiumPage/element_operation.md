---
id: ele_operation
title: '🚤 元素交互'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

本节介绍与浏览器元素的交互。浏览器元素对象为`ChromiumElement`。

## ✅️️ 点击元素

### 📌 `click()`和`click.left()`

这两个方法作用是一样的，用于左键点击元素。可选择模拟点击或 js 点击。

|    参数名称     |   类型    |   默认值   | 说明                                                                                             |
|:-----------:|:-------:|:-------:|------------------------------------------------------------------------------------------------|
|   `by_js`   | `bool`  | `False` | 指定点击行为方式。<br/>为`None`时，如不被遮挡，用模拟点击，否则用 js 点击<br/>为`True`时直接用 js 点击；<br/>为`False`时强制模拟点击，被遮挡也会进行点击 |
|  `timeout`  | `float` |  `1.5`  | 模拟点击的超时时间，等待元素可见、可用、进入视口                                                                       |
| `wait_stop` | `bool`  | `True`  | 点击前是否等待元素停止运动                                                                                  |

|   返回值   | 说明                                    |
|:-------:|---------------------------------------|
| `False` | `by_js`为`False`，且元素不可用、不可见时，返回`False` |
| `True`  | 除以上情况，其余情况都返回`True`                   |

**示例：**

```python
# 对ele元素进行模拟点击，如判断被遮挡也会点击
ele.click()

# 用js方式点击ele元素，无视遮罩层
ele.click(by_js=True)

# 如元素不被遮挡，用模拟点击，否则用js点击
ele.click(by_js=None)
```

默认情况下，`by_js`为`None`，优先用模拟方式点击，如遇遮挡、元素不可用、不可见、无法自动进入视口，等待直到超时后自动改用 js
方式点击。

`by_js`为`False`，程序会强制使用模拟点击，即使被遮挡也会点击元素位置。如果元素不可见、不可用，会返回`False`。如元素无法自动滚动到视口，会改用
js 点击。

`by_js`为`True`时，则可无视任何遮挡，只要元素在 DOM 内，就能点击得到，但元素是否响应点击视网页所用架构而定。

可以根据需要灵活地对元素进行操作。

在模拟点击前，程序会先尝试把元素滚动到视口中。

默认情况下，如无法进行模拟点击（元素无法进入视口、不可用、隐藏）时，左键单击会返回`False`。但也可以通过全局设置使其抛出异常：

```python
from DrissionPage.common import Settings

Settings.raise_click_failed = True
ele.click()  # 如无法点击则抛出异常
```

---

### 📌 `click.right()`

此方法实现右键单击元素。

**参数：** 无

**返回：**`None`

**示例：**

```python
ele.click.right()
```

---

### 📌 `click.middle()`

此方法实现中键单击元素。

|   参数名称    |   类型    |  默认值   | 说明              |
|:---------:|:-------:|:------:|-----------------|
| `get_tab` | `bool`  | `True` | 是否返回新出现的 Tab 对象 |

|     返回类型      |                      说明                      |
|:-------------:|:--------------------------------------------:|
| `ChromiumTab` | `get_tab`参数为`True`时，`ChromiumPage`返回的 Tab 对象 |
| `MixTab`  |             `get_tab`参数为`True`时，`WebPage`返回的 Tab 对象              |
|     `None`     |             `get_tab`参数为`False`时             |

**示例：**

```python
tab = ele.click.middle()
print(tab.title)
```

---

### 📌 `click.multi()`

此方法实现左键多次点击元素。

|  参数名称   |  类型   | 默认值 | 说明   |
|:-------:|:-----:|:---:|------|
| `times` | `int` | `2` | 点击次数 |

**返回：**`None`

---

### 📌 `click.at()`

此方法用于带偏移量点击元素，偏移量相对于元素左上角坐标。不传入`offset_x`和`offset_y`时点击元素中间点。   
点击的目标不一定在元素上，可以传入负值，或大于元素大小的值，点击元素附近的区域。向右和向下为正值，向左和向上为负值。

|    参数名称    |   类型    |   默认值    | 说明                                                         |
|:----------:|:-------:|:--------:|------------------------------------------------------------|
| `offset_x` | `float` |  `None`  | 相对元素左上角坐标的 x 轴偏移量，向下向右为正                                   |
| `offset_y` | `float` |  `None`  | 相对元素左上角坐标的 y 轴偏移量，向下向右为正                                   |
|  `button`  |  `str`  | `'left'` | 要点击的键，传入`'left'`、`'right'`、`'middle'`、`'back'`、`'forward'` |
|  `count`   |  `int`  |   `1`    | 点击次数                                                       |

**返回：**`None`

**示例：**

```python
# 点击元素右上方 50*50 的位置
ele.click.at(50, -50)

# 点击元素上中部，x相对左上角向右偏移50，y保持在元素中点
ele.click.at(offset_x=50)

# 和click()一致，但没有重试功能
ele.click.at()
```

---

### 📌 `click.to_upload()`

此方法用于点击元素，触发文件选择框并把指定的文件路径添加到网页，详见“文件上传”章节。

|     参数名称     |                   类型                    |   默认值   | 说明                                        |
|:------------:|:---------------------------------------:|:-------:|-------------------------------------------|
| `file_paths` | `str`<br/>`Path`<br/>`list`<br/>`tuple` |   必填    | 文件路径，如果上传框支持多文件，可传入列表或字符串，字符串时多个文件用`\n`分隔 |
|  `by_js`  |                 `bool`                  | `False` | 是否用 js 方式点击，逻辑与`click()`一致                 |

**返回：**`None`

---

### 📌 `click.to_download()`

此方法用于点击元素触发下载，并返回下载任务对象。用法详见“文件下载”章节。

|    参数名称    |        类型        |   默认值    | 说明                               |
|:----------:|:----------------:|:--------:|----------------------------------|
| `save_path` | `str`<br/>`Path` |    必填    | 保存路径，为`None`保存在原来设置的，如未设置保存到当前路径 |
| `rename` |      `str`       |  `None`  | 重命名文件名，为`None`则不修改               |
|  `suffix`  |      `str`       | `'left'` | 指定文件后缀，为`None`则不修改               |
|  `new_tab`   |      `bool`      |   `1`    | 该下载是否在新 tab 中触发                  |
|  `by_js`   |      `bool`      | `False`  | 是否用 js 方式点击，逻辑与`click()`一致       |
|  `timeout`  |     `float`      | `None`  | 超时时间，为`None`时使用页面对象默认超时时间        |

|       返回类型        |   说明   |
|:-----------------:|:------:|
| `DownloadMission` | 下载任务对象 |

---

### 📌 `click.for_new_tab()`

在预期点击后会出现新 tab 的时候，可用此方法点击，会等待并返回新 tab 对象。

|    参数名称    |        类型        |   默认值    | 说明                               |
|:----------:|:----------------:|:--------:|----------------------------------|
|  `by_js`   |      `bool`      | `False`  | 是否用 js 方式点击，逻辑与`click()`一致       |

|     返回类型      |         说明          |
|:-------------:|:-------------------:|
| `ChromiumTab` | 使用`ChromiumPage`时返回 |
| `MixTab`  |   使用`WebPage`时返回    |

---

## ✅️️ 输入内容

### 📌 `clear()`

此方法用于清空元素文本，可选择模拟按键或 js 方式。

模拟按键方式会自动输入`ctrl-a-del`组合键来清除文本框，js 方式则直接把元素`value`属性设置为`''`。

|  参数名称   |   类型   |   默认值   | 说明          |
|:-------:|:------:|:-------:|-------------|
| `by_js` | `bool` | `False` | 是否用 js 方式清空 |

**返回：**`None`

**示例：**

```python
ele.clear() 
```

---

### 📌 `input()`

此方法用于向元素输入文本或组合键，也可用于输入文件路径到上传控件。可选择输入前是否清空元素。

|  参数名称   |   类型   |   默认值   | 说明                                 |
|:-------:|:------:|:-------:|------------------------------------|
| `vals`  | `Any`  | `False` | 文本值或按键组合<br/>对文件上传控件时输入路径字符串或其组成的列表 |
| `clear` | `bool` | `False` | 输入前是否清空文本框                         |
| `by_js` | `bool` | `False` | 是否用 js 方式输入，为`True`时不能输入组合键        |

**返回：**`None`

:::tip Tips
    - 有些文本框可以接收回车代替点击按钮，可以直接在文本末尾加上`'\n'`。
    - 会自动把非`str`数据转换为`str`。
:::

**示例：**

```python
# 输入文本
ele.input('Hello world!')

# 输入文本并回车
ele.input('Hello world!\n')
```

---

### 📌 输入组合键

使用组合键或要传入特殊按键前，先要导入按键类`Keys`。

```python
from DrissionPage.common import Keys
```

然后将组合键放在一个`tuple`中传入`input()`即可。

```python
ele.input((Keys.CTRL, 'a', Keys.DEL))  # ctrl+a+del
```

`Keys`内置了 5 个常用组合键，分别为`CTRL_A`、`CTRL_C`、`CTRL_X`、`CTRL_V`、`CTRL_Z`、`CTRL_Y`。

```python
ele.input(Keys.CTRL_A)  # 全选
```

---

### 📌 `focus()`

此方法用于使元素获取焦点。

**参数：** 无

**返回：** `None`

---

## ✅️️ 拖拽和悬停

:::tip Tips
    除了以下方法，本库还提供更灵活的动作链功能，详见后面章节。
:::

### 📌 `drag()`

此方法用于拖拽元素到相对于当前的一个新位置，可以设置速度。

|    参数名称    |   类型    |  默认值  | 说明                |
|:----------:|:-------:|:-----:|-------------------|
| `offset_x` |  `int`  |  `0`  | x 轴偏移量，向下向右为正     |
| `offset_y` |  `int`  |  `0`  | y 轴偏移量，向下向右为正     |
| `duration` | `float` | `0.5` | 用时，单位秒，传入`0`即瞬间到达 |

**返回：**`None`

**示例：**

```python
# 拖动当前元素到距离50*50的位置，用时1秒
ele.drag(50, 50, 1)
```

---

### 📌 `drag_to()`

此方法用于拖拽元素到另一个元素上或一个坐标上。

|     参数名称     |                   类型                   |  默认值  | 说明                |
|:------------:|:--------------------------------------:|:-----:|-------------------|
| `ele_or_loc` | `ChromiumElement`<br/>`Tuple[int, int]` |  必填   | 另一个元素对象或坐标元组      |
|  `duration`  |                `float`                 | `0.5` | 用时，单位秒，传入`0`即瞬间到达 |

**返回：**`None`

**示例：**

```python
# 把 ele1 拖拽到 ele2 上
ele1 = page.ele('#div1')
ele2 = page.ele('#div2')
ele1.drag_to(ele2)

# 把 ele1 拖拽到网页 50, 50 的位置
ele1.drag_to((50, 50))
```

---

### 📌 `hover()`

此方法用于模拟鼠标悬停在元素上，可接受偏移量，偏移量相对于元素左上角坐标。不传入`offset_x`和`offset_y`值时悬停在元素中点。

|    参数名称    |  类型   |  默认值   | 说明                       |
|:----------:|:-----:|:------:|--------------------------|
| `offset_x` | `int` | `None` | 相对元素左上角坐标的 x 轴偏移量，向下向右为正 |
| `offset_y` | `int` | `None` | 相对元素左上角坐标的 y 轴偏移量，向下向右为正 |

**返回：**`None`

**示例：**

```python
# 悬停在元素右上方 50*50 的位置
ele.hover(50, -50)

# 悬停在元素上中部，x 相对左上角向右偏移50，y 保持在元素中点
ele.hover(offset_x=50)

# 悬停在元素中点
ele.hover()
```

---

## ✅️️ 修改元素

### 📌 `set.innerHTML()`

此方法用于设置元素的 innerHTML 内容。

|  参数名称  |  类型   | 默认值 | 说明     |
|:------:|:-----:|:---:|--------|
| `html` | `str` | 必填  | html文本 |

**返回：**`None`

---

### 📌 `set.property()`

此方法用于设置元素`property`属性。

|  参数名称   |  类型   | 默认值 | 说明  |
|:-------:|:-----:|:---:|-----|
| `name`  | `str` | 必填  | 属性名 |
| `value` | `str` | 必填  | 属性值 |

**返回：**`None`

**示例：**

```python
ele.set.property('value', 'Hello world!')
```

---

### 📌 `set.style()`

此方法用于设置元素样式。

|  参数名称   |  类型   | 默认值 | 说明  |
|:-------:|:-----:|:---:|-----|
| `name`  | `str` | 必填  | 属性名 |
| `value` | `str` | 必填  | 属性值 |

**返回：**`None`

---

### 📌 `set.attr()`

此方法用于设置元素 attribute 属性。

|  参数名称   |  类型   | 默认值 | 说明  |
|:-------:|:-----:|:---:|-----|
| `name`  | `str` | 必填  | 属性名 |
| `value` | `str` | 必填  | 属性值 |

**返回：**`None`

**示例：**

```python
ele.set.attr('href', 'http://www.gitee.com')
```

---

### 📌 `remove_attr()`

此方法用于删除元素 attribute 属性。

|  参数名称  |  类型   | 默认值 | 说明  |
|:------:|:-----:|:---:|-----|
| `name` | `str` | 必填  | 属性名 |

**返回：**`None`

**示例：**

```python
ele.remove_attr('href')
```

---

### 📌 `set.value()`

此方法用于设置元素`value`值。

|  参数名称   |  类型   | 默认值 | 说明  |
|:-------:|:-----:|:---:|-----|
| `value` | `str` | 必填  | 属性值 |

**返回：**`None`

---

### 📌 `check()`

此方法用于选中或取消选中元素。

| 参数名称 | 类型 | 默认值 | 说明 |
|:---------:|:------:|:-------:|---|
| `uncheck` | `bool` | `False` | 是否取消选中 |
| `by_js` | `bool` | `False` | 是否用 js 方式选择 |

**返回：**`None`

---

## ✅️️ 执行 js 脚本

### 📌 `run_js()`

此方法用于对元素执行 js 代码，代码中用`this`表示元素自己。

|    参数名称    |   类型    |   默认值   | 说明                                                |
|:----------:|:-------:|:-------:|---------------------------------------------------|
|  `script`  |  `str`  |   必填    | js 脚本文本或脚本文件路径                                           |
|  `*args`   |    -    |    无    | 传入的参数，按顺序在js文本中对应`arguments[0]`、`arguments[1]`... |
| `as_expr`  | `bool`  | `False` | 是否作为表达式运行，为`True`时`args`参数无效                      |
| `timetout` | `float` | `None`  | js 超时时间，为`None`则使用页面`timeouts.script`设置           |

| 返回类型  | 说明     |
|:-----:|--------|
| `Any` | 脚本执行结果 |

:::warning 注意
    要获取 js 结果记得写上`return`。
:::

**示例：**

```python
# 用执行 js 的方式点击元素
ele.run_js('this.click();')

# 用 js 获取元素高度
height = ele.run_js('return this.offsetHeight;')
```

---

### 📌 `run_async_js()`

此方法用于以异步方式执行 js 代码，代码中用`this`表示元素自己。

|    参数名称    |   类型    |   默认值   | 说明                                                |
|:----------:|:-------:|:-------:|---------------------------------------------------|
|  `script`  |  `str`  |   必填    | js 脚本文本                                           |
|  `*args`   |    -    |    无    | 传入的参数，按顺序在js文本中对应`arguments[0]`、`arguments[1]`... |
| `as_expr`  | `bool`  | `False` | 是否作为表达式运行，为`True`时`args`参数无效                      |

**返回：**`None`

---

### 📌 `add_init_js()`

此方法用于添加初始化脚本，在页面加载任何脚本前执行。

|    参数名称    |   类型    |   默认值   | 说明                                                |
|:----------:|:-------:|:-------:|---------------------------------------------------|
|  `script`  |  `str`  |   必填    | js 脚本文本                                           |

| 返回类型  | 说明        |
|:-----:|-----------|
| `str` | 添加的脚本的 id |


---

### 📌 `remove_init_js()`

此方法用于删除初始化脚本，`script_id`传入`None`时删除所有。

|    参数名称    |   类型    |   默认值   | 说明     |
|:----------:|:-------:|:-------:|--------|
|  `script_id`  |  `str`  |   `None`    | 脚本的id，传入`None`时删除所有 |

**返回：**`None`

---

## ✅️️ 元素滚动

元素滚动功能藏在`scroll`属性中。用于使可滚动的容器元素内部进行滚动，或使元素本身滚动到可见。

```python
# 滚动到底部
ele.scroll.to_bottom()

# 滚动到最右边
ele.scroll.to_rightmost()

# 向下滚动 200 像素
ele.scroll.down(200)

# 滚动到指定位置
ele.scroll.to_location(100, 300)

# 滚动页面使自己可见
ele.scroll.to_see()
```

---

### 📌 `scroll.to_top()`

此方法用于滚动到元素顶部，水平位置不变。

**参数：** 无

**返回：**`None`

**示例：**

```python
page.scroll.to_top()
```

---

### 📌 `scroll.to_bottom()`

此方法用于滚动到元素底部，水平位置不变。

**参数：** 无

**返回：**`None`

---

### 📌 `scroll.to_half()`

此方法用于滚动到元素垂直中间位置，水平位置不变。

**参数：** 无

**返回：**`None`

---

### 📌 `scroll.to_rightmost()`

此方法用于滚动到元素最右边，垂直位置不变。

**参数：** 无

**返回：**`None`

---

### 📌 `scroll.to_leftmost()`

此方法用于滚动到元素最左边，垂直位置不变。

**参数：** 无

**返回：**`None`

---

### 📌 `scroll.to_location()`

此方法用于滚动到元素滚动到指定位置。

| 参数名称 |  类型   | 默认值 | 说明   |
|:----:|:-----:|:---:|------|
| `x`  | `int` | 必填  | 水平位置 |
| `y`  | `int` | 必填  | 垂直位置 |

**返回：**`None`

**示例：**

```python
page.scroll.to_location(300, 50)
```

---

### 📌 `scroll.up()`

此方法用于使元素向上滚动若干像素，水平位置不变。

|  参数名称   |  类型   | 默认值 | 说明    |
|:-------:|:-----:|:---:|-------|
| `pixel` | `int` | 必填  | 滚动的像素 |

**返回：**`None`

**示例：**

```python
page.scroll.up(30)
```

---

### 📌 `scroll.down()`

此方法用于使元素向下滚动若干像素，水平位置不变。

|  参数名称   |  类型   | 默认值 | 说明    |
|:-------:|:-----:|:---:|-------|
| `pixel` | `int` | 必填  | 滚动的像素 |

**返回：**`None`

---

### 📌 `scroll.right()`

此方法用于使元素内滚动条向右滚动若干像素，垂直位置不变。

|  参数名称   |  类型   | 默认值 | 说明    |
|:-------:|:-----:|:---:|-------|
| `pixel` | `int` | 必填  | 滚动的像素 |

**返回：**`None`

---

### 📌 `scroll.left()`

此方法用于使元素内滚动条向左滚动若干像素，垂直位置不变。

|  参数名称   |  类型   | 默认值 | 说明    |
|:-------:|:-----:|:---:|-------|
| `pixel` | `int` | 必填  | 滚动的像素 |

**返回：**`None`

---

### 📌 `scroll.to_see()`

此方法用于滚动页面直到元素可见。

|   参数名称   |        类型        |  默认值   | 说明                                 |
|:--------:|:----------------:|:------:|------------------------------------|
| `center` | `bool`<br/>`None` | `None` | 是否尽量滚动到页面正中，为`None`时如果被遮挡，则滚动到页面正中 |

**返回：**`None`

---

### 📌 `scroll.to_center()`

此方法用于尽量把元素滚动到视口正中。

**参数：** 无

**返回：**`None`

---

## ✅️️ 列表选择

`<select>`下拉列表元素功能在`select`属性中。可自动等待列表项出现再实施选择。

此属性用于对`<select>`元素的操作。非`<select>`元素此属性为`None`。

假设有以下`<select>`元素，下面示例以此为基础：

```html
<select id='s' multiple>
    <option value='value1'>text1</option>
    <option value='value2'>text2</option>
    <option value='value3'>text3</option>
</select>
```

### 📌 点击列表项元素进行选取

可以获取`<option>`元素，进行选取或取消选择。

**示例：**

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
ele = page('t:select')('t:option')
ele.click()
```

---

### 📌 `select()`和`select.by_text()`

这两个方法功能一样，用于按文本选择列表项。如为多选列表，可多选。

|   参数名称    |             类型             |  默认值   | 说明                              |
|:---------:|:--------------------------:|:------:|---------------------------------|
|  `text`   | `str`<br/>`list`<br/>`tuple` |   必填   | 作为选择条件的文本，传入`list`或`tuple`可选择多项 |
| `timeout` |          `float`           | `None` | 超时时间，为`None`默认使用页面超时时间          |

|  返回类型  | 说明     |
|:------:|--------|
| `bool` | 是否选择成功 |

---

### 📌 `select.by_value()`

此方法用于按`value`属性选择列表项。如为多选列表，可多选。

|   参数名称    |             类型             |  默认值   | 说明                                    |
|:---------:|:--------------------------:|:------:|---------------------------------------|
|  `value`  | `str`<br/>`list`<br/>`tuple` |   必填   | 作为选择条件的`value`值，传入`list`或`tuple`可选择多项 |
| `timeout` |          `float`           | `None` | 超时时间，为`None`默认使用页面超时时间                |

|  返回类型  | 说明     |
|:------:|--------|
| `bool` | 是否选择成功 |

---

### 📌 `select.by_index()`

此方法用于按序号选择列表项，从`1`开始。如为多选列表，可多选。

|   参数名称    |             类型             |  默认值   | 说明                          |
|:---------:|:--------------------------:|:------:|-----------------------------|
|  `index`  | `int`<br/>`list`<br/>`tuple` |   必填   | 选择第几项，传入`list`或`tuple`可选择多项 |
| `timeout` |          `float`           | `None` | 超时时间，为`None`默认使用页面超时时间      |

|  返回类型  | 说明     |
|:------:|--------|
| `bool` | 是否选择成功 |

---

### 📌 `select.by_locator()`

此方法可用定位符筛选选项元素。如为多选列表，可多选。

|   参数名称    |             类型             |  默认值   | 说明                        |
|:---------:|:--------------------------:|:------:|---------------------------|
|   `locator`   | `str`<br/>`list`<br/>`tuple` |   必填   | 定位符，传入`list`或`tuple`可选择多项 |
| `timeout` |          `float`           | `None` | 超时时间，为`None`默认使用页面超时时间    |

|  返回类型  | 说明     |
|:------:|--------|
| `bool` | 是否选择成功 |

---

### 📌 `select.by_option()`

此方法用于选中单个或多个列表项元素。如为多选列表，可多选。

|   参数名称   |                      类型                      | 默认值 | 说明                   |
|:--------:|:--------------------------------------------:|:---:|----------------------|
| `option` | `ChromiumElement`<br/>`List[ChromiumElement]` | 必填  | `<option>`元素或它们组成的列表 |

**返回：**`None`

**示例：**

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
select = page('t:select')
option = select('t:option')
select.select.by_option(option)
```

---

### 📌 `select.cancel_by_text()`

此方法用于按文本取消选择列表项。如为多选列表，可取消多项。

|   参数名称    |             类型             |  默认值   | 说明                              |
|:---------:|:--------------------------:|:------:|---------------------------------|
|  `text`   | `str`<br/>`list`<br/>`tuple` |   必填   | 作为选择条件的文本，传入`list`或`tuple`可选择多项 |
| `timeout` |          `float`           | `None` | 超时时间，为`None`默认使用页面超时时间          |

|  返回类型  | 说明     |
|:------:|--------|
| `bool` | 是否选择成功 |

---

### 📌 `select.cancel_by_value()`

此方法用于按`value`属性取消选择列表项。如为多选列表，可取消多项。

|   参数名称    |             类型             |  默认值   | 说明                                    |
|:---------:|:--------------------------:|:------:|---------------------------------------|
|  `value`  | `str`<br/>`list`<br/>`tuple` |   必填   | 作为选择条件的`value`值，传入`list`或`tuple`可选择多项 |
| `timeout` |          `float`           | `None` | 超时时间，为`None`默认使用页面超时时间                |

|  返回类型  | 说明     |
|:------:|--------|
| `bool` | 是否选择成功 |

---

### 📌 `select.cancel_by_index()`

此方法用于按序号取消选择列表项，从`1`开始。如为多选列表，可取消多项。

|   参数名称    |             类型             |  默认值   | 说明                          |
|:---------:|:--------------------------:|:------:|-----------------------------|
|  `index`  | `int`<br/>`list`<br/>`tuple` |   必填   | 选择第几项，传入`list`或`tuple`可选择多项 |
| `timeout` |          `float`           | `None` | 超时时间，为`None`默认使用页面超时时间      |

|  返回类型  | 说明     |
|:------:|--------|
| `bool` | 是否选择成功 |

---

### 📌 `select.cancel_by_locator()`

此方法可用定位符筛选选项元素。如为多选列表，可取消多项。

|   参数名称    |             类型             |  默认值   | 说明                        |
|:---------:|:--------------------------:|:------:|---------------------------|
|   `locator`   | `str`<br/>`list`<br/>`tuple` |   必填   | 定位符，传入`list`或`tuple`可选择多项 |
| `timeout` |          `float`           | `None` | 超时时间，为`None`默认使用页面超时时间    |

|  返回类型  | 说明     |
|:------:|--------|
| `bool` | 是否选择成功 |

---

### 📌 `select.cancel_by_option()`

此方法用于取消选中单个或多个列表项元素。如为多选列表，可多选。

|   参数名称   |                      类型                      | 默认值 | 说明                   |
|:--------:|:--------------------------------------------:|:---:|----------------------|
| `option` | `ChromiumElement`<br/>`List[ChromiumElement]` | 必填  | `<option>`元素或它们组成的列表 |

**返回：**`None`

---

### 📌 `select.all()`

此方法用于全选所有项。多选列表才有效。

**参数：** 无

**返回：**`None`

---

### 📌 `select.clear()`

此方法用于取消所有项选中状态。多选列表才有效。

**参数：** 无

**返回：**`None`

---

### 📌 `select.invert()`

此方法用于反选。多选列表才有效。

**参数：** 无

**返回：**`None`

---

### 📌 `select.is_multi`

此属性返回当前元素是否多选列表。

**返回类型：**`bool`

---

### 📌 `select.options`

此属性返回当前列表元素所有选项元素对象。

**返回类型：**`ChromiumElement`

---

### 📌 `select.selected_option`

此属性返回当前元素选中的选项（单选列表）。

**返回类型：**`bool`

---

### 📌 `select.selected_options`

此属性返回当前元素所有选中的选项（多选列表）。

**返回类型：**`List[ChromiumElement]`