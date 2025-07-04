---
id: actions
title: '🚤 动作链'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

动作链可以在浏览器上完成一系列交互行为，如鼠标移动、鼠标点击、键盘输入等。

浏览器页面对象都支持使用动作链。

可以链式操作，也可以分开执行，每个动作执行即生效，无需`perform()`。

这些操作皆为模拟，真正的鼠标不会移动，因此可以多个标签页同时操作。

## ✅️ 使用方法

可以用上述对象内置的`actions`属性调用动作链，也可以主动创建一个动作链对象，将页面对象传入使用。

这两种方式唯一区别是，前者会等待页面加载完毕再执行，后者不会。

### 📌 使用内置`actions`属性

:::info 说明
    这种方式会等到页面框架文档（不包括 js 数据）加载完成再执行动作。
:::

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')
page.actions.move_to('#kw').click().type('DrissionPage')
page.actions.move_to('#su').click()
```

---

### 📌 使用新对象

使用`from DrissionPage.common import Actions`导入动作链。

只要把`WebPage`对象或`ChromiumPage`对象传入即可。动作链只在这个页面上生效。

| 初始化参数  |                      类型                      | 默认值 | 说明           |
|:------:|:--------------------------------------------:|:---:|--------------|
| `page` | `ChromiumPage`<br/>`WebPage`<br/>`ChromiumTab` | 必填  | 动作链要操作的浏览器页面 |

:::info 说明
    这种方式**不会**等到页面框架文档（不包括 js 数据）加载完成再执行动作。
:::

**示例：**

```python
from DrissionPage import ChromiumPage
from DrissionPage.common import Actions

page = ChromiumPage()
ac = Actions(page)
page.get('https://www.baidu.com')
ac.move_to('#kw').click().type('DrissionPage')
ac.move_to('#su').click()
```

---

### 📌 操作方式

多个动作可以用链式模式操作：

```python
tab.actions.move_to(ele).click().type('some text')
```

也可以多个操作分开执行：

```python
tab.actions.move_to(ele)
tab.actions.click()
tab.actions.type('some text')
```

这两种方式效果是一样的，每个动作总会依次执行。

---

## ✅️ 移动鼠标

### 📌 `move_to()`

此方法用于移动鼠标到元素中点，或页面上的某个绝对坐标。可设置偏移量，当带偏移量时，偏移量相对于元素左上角坐标。

|    初始化参数     |                       类型                        |  默认值  | 说明                                      |
|:------------:|:-----------------------------------------------:|:-----:|-----------------------------------------|
| `ele_or_loc` | `ChrmoiumElement`<br/>`str`<br/>`Tuple[int, int]` |  必填   | 元素对象、文本定位符或绝对坐标，坐标为`tuple`(int, int) 形式 |
|  `offset_x`  |                      `int`                      |  `0`  | x 轴偏移量，向右为正，向左为负                        |
|  `offset_y`  |                      `int`                      |  `0`  | y 轴偏移量，向下为正，向上为负                        |
|  `duration`  |                     `float`                     | `0.5` | 拖动用时，传入`0`即瞬间到达                         |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：** 使鼠标移动到 ele 元素上

```python
ele = tab('tag:a')
tab.actions.move_to(ele_or_loc=ele)
```

---

### 📌 `move()`

此方法用于使鼠标相对当前位置移动若干距离。

|    参数名称    |   类型    |  默认值  | 说明               |
|:----------:|:-------:|:-----:|------------------|
| `offset_x` |  `int`  |  `0`  | x 轴偏移量，向右为正，向左为负 |
| `offset_y` |  `int`  |  `0`  | y 轴偏移量，向下为正，向上为负 |
| `duration` | `float` | `0.5` | 拖动用时，传入`0`即瞬间到达  |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：** 鼠标向右移动 300 像素

```python
tab.actions.move(300, 0)
```

---

### 📌 `up()`

此方法用于使鼠标相对当前位置向上移动若干距离。

|  参数名称   |  类型   | 默认值 | 说明       |
|:-------:|:-----:|:---:|----------|
| `pixel` | `int` | 必填  | 鼠标移动的像素值 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：** 鼠标向上移动 50 像素

```python
tab.actions.up(50)
```

---

### 📌 `down()`

此方法用于使鼠标相对当前位置向下移动若干距离。

|  参数名称   |  类型   | 默认值 | 说明       |
|:-------:|:-----:|:---:|----------|
| `pixel` | `int` | 必填  | 鼠标移动的像素值 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：**

```python
tab.actions.down(50)
```

---

### 📌 `left()`

此方法用于使鼠标相对当前位置向左移动若干距离。

|  参数名称   |  类型   | 默认值 | 说明       |
|:-------:|:-----:|:---:|----------|
| `pixel` | `int` | 必填  | 鼠标移动的像素值 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：**

```python
tab.actions.left(50)
```

---

### 📌 `right()`

此方法用于使鼠标相对当前位置向右移动若干距离。

|  参数名称   |  类型   | 默认值 | 说明       |
|:-------:|:-----:|:---:|----------|
| `pixel` | `int` | 必填  | 鼠标移动的像素值 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：**

```python
tab.actions.right(50)
```

---

## ✅️ 鼠标按键

### 📌 `click()`

此方法用于单击鼠标左键，单击前可先移动到元素上。

|   参数名称   |             类型             |  默认值   | 说明             |
|:--------:|:--------------------------:|:------:|----------------|
| `on_ele` | `ChromiumElement`<br/>`str` | `None` | 要点击的元素对象或文本定位符 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：**

```python
tab.actions.click('#div1')
```

---

### 📌 `r_click()`

此方法用于单击鼠标右键，单击前可先移动到元素上。

|   参数名称   |             类型             |  默认值   | 说明             |
|:--------:|:--------------------------:|:------:|----------------|
| `on_ele` | `ChromiumElement`<br/>`str` | `None` | 要点击的元素对象或文本定位符 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：**

```python
tab.actions.r_click('#div1')
```

---

### 📌 `m_click()`

此方法用于单击鼠标中键，单击前可先移动到元素上。

|   参数名称   |             类型             |  默认值   | 说明             |
|:--------:|:--------------------------:|:------:|----------------|
| `on_ele` | `ChromiumElement`<br/>`str` | `None` | 要点击的元素对象或文本定位符 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：**

```python
tab.actions.m_click('#div1')
```

---

### 📌 `db_click()`

此方法用于双击鼠标左键，双击前可先移动到元素上。

|   参数名称   |             类型             |  默认值   | 说明             |
|:--------:|:--------------------------:|:------:|----------------|
| `on_ele` | `ChromiumElement`<br/>`str` | `None` | 要点击的元素对象或文本定位符 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

---

### 📌 `hold()`

此方法用于按住鼠标左键不放，按住前可先移动到元素上。

|   参数名称   |             类型             |  默认值   | 说明             |
|:--------:|:--------------------------:|:------:|----------------|
| `on_ele` | `ChromiumElement`<br/>`str` | `None` | 要按住的元素对象或文本定位符 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：**

```python
tab.actions.hold('#div1')
```

---

### 📌 `release()`

此方法用于释放鼠标左键，释放前可先移动到元素上。

|   参数名称   |             类型             |  默认值   | 说明             |
|:--------:|:--------------------------:|:------:|----------------|
| `on_ele` | `ChromiumElement`<br/>`str` | `None` | 要释放的元素对象或文本定位符 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：** 移动到某元素上然后释放鼠标左键

```python
tab.actions.release('#div1')
```

---

### 📌 `r_hold()`

此方法用于按住鼠标右键不放，按住前可先移动到元素上。

|   参数名称   |             类型             |  默认值   | 说明             |
|:--------:|:--------------------------:|:------:|----------------|
| `on_ele` | `ChromiumElement`<br/>`str` | `None` | 要按住的元素对象或文本定位符 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

---

### 📌 `r_release()`

此方法用于释放鼠标右键，释放前可先移动到元素上。

|   参数名称   |             类型             |  默认值   | 说明             |
|:--------:|:--------------------------:|:------:|----------------|
| `on_ele` | `ChromiumElement`<br/>`str` | `None` | 要释放的元素对象或文本定位符 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

---

### 📌 `m_hold()`

此方法用于按住鼠标中键不放，按住前可先移动到元素上。

|   参数名称   |             类型             |  默认值   | 说明             |
|:--------:|:--------------------------:|:------:|----------------|
| `on_ele` | `ChromiumElement`<br/>`str` | `None` | 要按住的元素对象或文本定位符 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

---

### 📌 `m_release()`

此方法用于释放鼠标中键，释放前可先移动到元素上。

|   参数名称   |             类型             |  默认值   | 说明             |
|:--------:|:--------------------------:|:------:|----------------|
| `on_ele` | `ChromiumElement`<br/>`str` | `None` | 要释放的元素对象或文本定位符 |

|       类型       | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

---

## ✅️ 滚动滚轮

### 📌 `scroll()`

此方法用于滚动鼠标滚轮，滚动前可先移动到元素上。

|   参数名称    |             类型             |  默认值   | 说明                  |
|:---------:|:--------------------------:|:------:|---------------------|
| `delta_y` |           `int`            |  `0`   | 滚轮 y 轴变化值，向下为正，向上为负 |
| `delta_x` |           `int`            |  `0`   | 滚轮 x 轴变化值，向右为正，向左为负 |
| `on_ele`  | `ChromiumElement`<br/>`str` | `None` | 要滚动的元素对象或文本定位符      |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

---

## ✅️ 键盘按键和文本输入

### 📌 `key_down()`

此方法用于按下键盘按键。非字符串按键（如 ENTER）可输入其名称，也可以用 Keys 类获取。

| 参数名称  |  类型   | 默认值 | 说明                  |
|:-----:|:-----:|:---:|---------------------|
| `key` | `str` | 必填  | 按键名称，或从`Keys`类获取的键值 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：** 按下 ENTER 键

```python
from DrissionPage.common import Keys

tab.actions.key_down('ENTER')  # 输入按键名称
tab.actions.key_down(Keys.ENTER)  # 从Keys获取按键
```

---

### 📌 `key_up()`

此方法用于提起键盘按键。非字符串按键（如 ENTER）可输入其名称，也可以用 Keys 类获取。

| 参数名称  |  类型   | 默认值 | 说明   |
|:-----:|:-----:|:---:|------|
| `key` | `str` | 必填  | 按键名称，或从`Keys`类获取的键值 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：** 提起 ENTER 键

```python
from DrissionPage.common import Keys

tab.actions.key_up('ENTER')  # 输入按键名称
tab.actions.key_up(Keys.ENTER)  # 从Keys获取按键
```

---

### 📌 `input()`

此方法用于输入一段文本或多段文本，也可输入组合键。

多段文本或组合键用列表传入。

|  参数名称  |             类型             | 默认值 | 说明                                   |
|:------:|:--------------------------:|:---:|--------------------------------------|
| `text` | `str`<br/>`list`<br/>`tuple` | 必填  | 要输入的文本或按键，多段文本或组合键可用`list`或`tuple`传入 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：**

```python
from DrissionPage import ChromiumPage

tab = ChromiumPage()
tab.get('https://www.baidu.com')
tab.actions.click('#kw').input('DrissionPage')
```

---

### 📌 `type()`

此方法用于以按键盘的方式输入一段或多段文本。也可输入组合键。

`type()`与`input()`区别在于前者模拟按键输入，逐个字符按下和提起，后者直接输入一整段文本。

|  参数名称  |             类型             | 默认值 | 说明                                   |
|:------:|:--------------------------:|:---:|--------------------------------------|
| `keys` | `str`<br/>`list`<br/>`tuple` | 必填  | 要输入的文本或按键，多段文本或组合键可用`list`或`tuple`传入 |

|      返回类型      | 说明      |
|:--------------:|---------|
| `Actions` | 动作链对象本身 |

**示例：**

```python
# 键入一段文本
tab.actions.type('text')

# 键入多段文本
tab.actions.type(('ab', 'cd'))

# 光标向左移动一位再键入文本
tab.actions.type((Keys.LEFT, 'abc'))

# 输入快捷键
tab.actions.type(Keys.CTRL_A)
```

---

## ✅️ 等待

### 📌 `wait()`

此方法用于等待若干秒。

`scope`为`None`时，效果与`time.sleep()`没有区别，等待指定秒数。

`scope`不为`None`时，获取两个参数之间的一个随机值，等待这个数值的秒数。

|   参数名称   | 类型      |  默认值  | 说明                                |
|:--------:|:-------:|:-----:|-----------------------------------|
| `second` | `float` |  必填   | 要等待的秒数，`scope`不为`None`时表示随机数范围起始值 |
| `scope` | `float` | `None` | 随机数范围结束值                          |

**返回：**`None`

---

## ✅️ 属性

### 📌 `owner`

此属性返回使用此动作链的页面对象。

**类型：**`ChromiumBase`

---

### 📌 `curr_x`

此属性返回当前光标位置的 x 坐标。

**类型：**`int`

---

### 📌 `curr_y`

此属性返回当前光标位置的 y 坐标。

**类型：**`int`

---

## ✅️ 示例

### 📌 模拟输入 ctrl+a

```python
from DrissionPage import ChromiumPage
from DrissionPage.common import Keys

# 创建页面对象
tab = ChromiumPage()

# 鼠标移动到<input>元素上
tab.actions.move_to('tag:input')
# 点击鼠标，使光标落到元素中
tab.actions.click()
# 按下 ctrl 键
tab.actions.key_down(Keys.CTRL)
# 输入 a
tab.actions.type('a')
# 提起 ctrl 键
tab.actions.key_up(Keys.CTRL)
```

链式写法：

```python
tab.actions.click('tag:input').key_down(Keys.CTRL).type('a').key_up(Keys.CTRL)
```

更简单的写法：

```python
tab.actions.click('tag:input').type(Keys.CTRL_A)
```

---

### 📌 拖拽元素

把一个元素向右拖拽 300 像素：

```python
from DrissionPage import ChromiumPage

# 创建页面
tab = ChromiumPage()

# 左键按住元素
tab.actions.hold('#div1')
# 向右移动鼠标300像素
tab.actions.right(300)
# 释放左键
tab.actions.release()
```

把一个元素拖拽到另一个元素上：

```python
tab.actions.hold('#div1').release('#div2')
```
