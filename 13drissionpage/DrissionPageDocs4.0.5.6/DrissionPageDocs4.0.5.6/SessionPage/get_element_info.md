---
id: get_ele_info
title: '🚄 获取元素信息'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

`SessionPage`对象和`WebPage` 对象s 模式获取的元素是`SessionElement`，本节介绍其属性。

假设`ele`为以下`div`元素的对象，本节示例均使用该元素：

```html
<div id="div1" class="divs">Hello World!
    <p>行元素</p>
    <!--这是注释-->
</div>
```

## ✅️️ `html`

此属性返回元素的`outerHTML`文本。

**返回类型：**`str`

```python
print(ele.html)
```

**输出：**

```shell
<div id="div1" class="divs">Hello World!
    <p>行元素</p>
    <!--这是注释-->
</div>
```

---

## ✅️️ `inner_html`

此属性返回元素的`innerHTML`文本。

**返回类型：**`str`

```python
print(ele.inner_html)
```

**输出：**

```shell
Hello World!
    <p>行元素</p>
    <!--这是注释-->
```

---

## ✅️️ `tag`

此属性返回元素的标签名。

**返回类型：**`str`

```python
print(ele.tag)
```

**输出：**

```shell
div
```

---

## ✅️️ `text`

此属性返回元素内所有文本组合成的字符串。  
该字符串已格式化，即已转码，已去除多余换行符，符合人读取习惯，便于直接使用。

**返回类型：**`str`

```python
print(ele.text)
```

**输出：**

```shell
Hello World!
行元素
```

---

## ✅️️ `raw_text`

此属性返回元素内原始文本。

**返回类型：**`str`

```python
print(ele.raw_text)
```

输出（注意保留了元素间的空格和换行）：

```shell
Hello World!
    行元素
　    
　
```

---

## ✅️️ `texts()`

此方法返回元素内所有**直接**子节点的文本，包括元素和文本节点。 它有一个参数`text_node_only`，为`True`时则只获取只返回不被包裹的文本节点。这个方法适用于获取文本节点和元素节点混排的情况。

| 参数名称             | 类型     | 默认值     | 说明        |
|:----------------:|:------:|:-------:| --------- |
| `text_node_only` | `bool` | `False` | 是否只返回文本节点 |

| 返回类型        | 说明   |
|:-----------:| ---- |
| `List[str]` | 文本列表 |

**示例：**

```python
print(e.texts())  
print(e.texts(text_node_only=True))  
```

**输出：**

```shell
['Hello World!', '行元素']
['Hello World!']
```

---

## ✅️️ `comments`

此属性以列表形式返回元素内的注释。

**返回类型：**`List[str]`

```python
print(ele.comments)
```

**输出：**

```shell
[<!--这是注释-->]
```

---

## ✅️️ `attrs`

此属性以字典形式返回元素所有属性及值。

**返回类型：**`dict`

```python
print(ele.attrs)
```

**输出：**

```shell
{'id': 'div1', 'class': 'divs'}
```

---

## ✅️️ `attr()`

此方法返回元素某个 attribute 属性值。它接收一个字符串参数，返回该属性值文本，无该属性时返回`None`。  
此属性返回的`src`、`href`属性为已补充完整的路径。`text`属性为已格式化文本。

|  参数名称  | 类型    | 默认值 | 说明   |
|:------:|:-----:|:---:| ---- |
| `name` | `str` | 必填  | 属性名称 |

| 返回类型   | 说明            |
|:------:| ------------- |
| `str`  | 属性值文本         |
| `None` | 没有该属性返回`None` |

**示例：**

```python
print(ele.attr('id'))
```

**输出：**

```shell
div1
```

---

## ✅️️ `value`

此方法返回元素的`value`值。

**返回类型：**`str`

---

## ✅️️ `link`

此方法返回元素的 href 属性或 src 属性，没有这两个属性则返回`None`。

**返回类型：**`str`

```html
<a href='http://www.baidu.com'>百度</a>
```

假设`a_ele`为以上元素的对象：

```python
print(a_ele.link)
```

**输出：**

```shell
http://www.baidu.com
```

---

## ✅️️ `page`

此属性返回元素所在的页面对象。由 html 文本直接生成的`SessionElement`的`page`属性为`None`。

**返回类型：**`SessionPage`、`WebPage`

```python
page = ele.page
```

---

## ✅️️ `xpath`

此属性返回当前元素在页面中 xpath 的绝对路径。

**返回类型：**`str`

```python
print(ele.xpath)
```

**输出：**

```shell
/html/body/div
```

---

## ✅️️ `css_path`

此属性返回当前元素在页面中 css selector 的绝对路径。

**返回类型：**`str`

```python
print(ele.css_path)
```

**输出：**

```shell
:nth-child(1)>:nth-child(1)>:nth-child(1)
```

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

## ✅️️ 实际示例

以下示例可直接运行查看结果：

```python
from DrissionPage import SessionPage

page = SessionPage()
page.get('https://gitee.com/explore')

# 获取推荐目录下所有 a 元素
li_eles = page('tag:ul@text():全部推荐项目').eles('t:a')

# 遍历列表
for i in li_eles:  
    # 获取并打印标签名、文本、href 属性
    print(i.tag, i.text, i.attribute('href'))
```

**输出：**

```shell
a 全部推荐项目 https://gitee.com/explore/all
a 前沿技术 https://gitee.com/explore/new-tech
a 智能硬件 https://gitee.com/explore/hardware
a IOT/物联网/边缘计算 https://gitee.com/explore/iot
a 车载应用 https://gitee.com/explore/vehicle
以下省略……
```
