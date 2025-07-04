---
id: behavior
title: '🔦 行为模式'
---

## ✅️ 等待元素

由于网络、js 运行时间的不确定性，经常需要等待元素加载到 DOM 中才能使用。

浏览器所有查找元素操作都自带等待，时间默认跟随元素所在页面`timeout`属性（默认 10 秒），也可以在每次查找时单独设置，单独设置的等待时间不会改变页面原来设置。

### 📌 内置等待

```python
from DrissionPage import ChromiumPage

# 页面初始化时设置查找元素超时时间为 15 秒
tab = ChromiumPage(timeout=15)
# 设置查找元素超时时间为 5 秒
tab.set.timeouts(5)

# 使用页面超时时间来查找元素（5 秒）
ele1 = tab.ele('search text')
# 为这次查找页面独立设置等待时间（1 秒）
ele1 = tab.ele('search text', timeout=1)
# 查找后代元素，使用页面超时时间（5 秒）
ele2 = ele1.ele('search text')
# 查找后代元素，使用单独设置的超时时间（1 秒）
ele2 = ele1.ele('some text', timeout=1)  
```

### 📌 主动等待

页面对象的`wait.eles_loaded()`方法，可主动等待指定元素加载到 DOM。

用法详见等待章节。

---

## ✅️ 链式写法

因为元素对象本身又可以查找对象，所有可实现多级链式操作，可使程序更简洁。

**示例：**

```python
ele = tab.ele('#s_fm').ele('#su')
```

其中`ele()`可省略，简化写成：

```python
ele = tab('#s_fm')('#su')
```

---

## ✅️ 找不到元素时

### 📌 默认情况

默认情况下，找不到元素时不会立即抛出异常，而是返回一个`NoneElement`对象。

这个对象用`if`判断表现为`False`，调用其功能会抛出`ElementNotFoundError`异常。

这样可以用`if`判断是否找到元素，也可以用`try`去捕获异常。

查找多个元素找不到时，返回空的`list`。

**示例，用`if`判断：**

```python
ele = tab.ele('****')

# 判断是否找到元素
if ele:
    print('找到了。')

if not ele:
    print('没有找到。')
```

**示例，用`try`捕获：**

```python
try:
    ele.click()
except ElementNotFoundError:
    print('没有找到。')
```

---

### 📌 立即抛出异常

如果想在找不到元素时立刻抛出异常，可以用以下方法设置。

此设置为全局有效，在项目开始时设置一次即可。

查找多个元素找不到时，依然返回空的`list`。

设置全局变量：

```python
from DrissionPage.common import Settings

Settings.raise_when_ele_not_found = True
```

**示例：**

```python
from DrissionPage import ChromiumPage
from DrissionPage.common import Settings

Settings.raise_when_ele_not_found = True

page = ChromiumPage(timeout=1)
page.get('https://www.baidu.com')
ele = page('#abcd')  # ('#abcd')这个元素不存在
```

输出：

```console
DrissionPage.errors.ElementNotFoundError: 
没有找到元素。
method: ele()
args: {'locator': '#abcd'}
```

---

### 📌 设置默认返回值

如果查找元素后要获取一个属性，但这个元素不一定存在，或者链式查找其中一个节点找不到，可以设置查找失败时返回的值，而不是抛出异常，可以简化一些采集逻辑。

使用浏览器页面对象的`set.NoneElement_value()`方法设置该值。

|   参数名称   |   类型   |  默认值   | 说明           |
|:--------:|:------:|:------:|--------------|
| `value`  | `Any`  | `None` | 将返回的设定值      |
| `on_off` | `bool` | `True` | `bool`表示是否启用 |

**返回：**`None`

**示例**

比如说，遍历页面上一个列表中多个对象，但其中有些元素可能缺失某个子元素，可以这样写：

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.set.NoneElement_value('没找到')
for li in page.eles('t:li'):
    name = li('.name').text
    age = li('.age').text
    phone = li('.phone').text
```

这样，假如某个子元素不存在，不会抛出异常，而是返回`'没找到'`这个字符串。
