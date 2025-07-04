---
id: get_ele_intro
title: '🔦 概述'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

本章介绍如何获取元素对象。

定位元素是自动化重中之重的技能，虽然可在开发者工具直接复制绝对路径，但这样做有几个缺点：

- 代码冗长，可读性低
- 动态页面容易导致元素失效
- 无法使用相对定位
- 网页稍有改动或者出现临时元素就不能用，容错性低
- 无法跨`<iframe>`查找元素

因此作者极不建议使用右键复制的元素路径。

本库提供一套简洁易用的语法，用于快速定位元素，并且内置等待功能、支持链式查找，减少了代码的复杂性。  
同时也兼容 css selector、xpath 和 selenium 原生的 loc 元组。

## ✅️️ 基本用法

所有页面对象和元素对象（包括`<iframe>`和 shadow-root），都可以在自己内部查找元素。

元素对象还能以自己为基准，相对定位其它元素。

定位元素大致有以下几种方法，将在后续小节中详细说明。

- 在页面或元素内查找子元素
- 根据 DOM 结构相对定位
- 根据视觉位置相对定位

所有的查找元素方法，都可以使用本库自创的查找语法、xpath、css selector和 selenium 的定位符元组，去查找元素。

---

## ✅️️ 示例

先看一些示例，后面再详细讲解用法。

### 📌 简单示例

假设有这样一个页面，本章示例皆使用此页面：

```html
<html>
<body>
<div id="one">
    <p class="p_cls" name="row1">第一行</p>
    <p class="p_cls" name="row2">第二行</p>
    <p class="p_cls">第三行</p>
</div>
<div id="two">
    第二个div
</div>
</body>
</html>
```

我们可以用页面对象去获取其中的元素：

```python
div1 = tab.ele('#one')  # 获取 id 为 one 的元素
p1 = tab.ele('@name=row1')  # 获取 name 属性为 row1 的元素
div2 = tab.ele('第二个div')  # 获取包含“第二个div”文本的元素
div_list = tab.eles('tag:div')  # 获取所有div元素
```

也可以获取到一个元素，然后在它里面或周围查找元素：

```python
div1 = tab.ele('#one')  # 获取到一个元素div1
p_list = div1.eles('tag:p')  # 在div1内查找所有p元素
div2 = div1.next()  # 获取div1后面一个元素
```

---

### 📌 实际示例

复制此代码可直接运行查看结果。

```python
from DrissionPage import SessionPage

page = SessionPage()
page.get('https://gitee.com/explore')

# 获取包含“全部推荐项目”文本的 ul 元素
ul_ele = page.ele('tag:ul@text():全部推荐项目')  

# 获取该 ul 元素下所有 a 元素
titles = ul_ele.eles('tag:a')  

# 遍历列表，打印每个 a 元素的文本
for i in titles:  
    print(i.text)
```

**输出：**

```shell
全部推荐项目
前沿技术
智能硬件
IOT/物联网/边缘计算
车载应用
...
```
