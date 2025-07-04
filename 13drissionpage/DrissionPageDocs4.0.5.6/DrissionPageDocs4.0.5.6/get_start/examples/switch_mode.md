---
id: switch_mode
title: 🗺️ 模式切换
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

这个示例演示`WebPage`如何切换控制浏览器和收发数据包两种模式。

通常，切换模式是用来应付登录检查很严格的网站，可以用浏览器处理登录，再转换模式用收发数据包的形式来采集数据。

但是这种场景需要有对应的账号，不便于演示。演示使用浏览器在 gitee 搜索，然后转换到收发数据包的模式来读取数据。虽然此示例现实使用意义不大，但可以了解其工作模式。

## ✅️️ 页面分析

网址：[https://gitee.com/explore](https://gitee.com/explore)

打开网址，按`F12`，我们可以看到页面 html 如下：

![](imgs/change1.png)

输入框`<input>`元素`id`属性为`'q'`，搜索按钮`<button>`元素`文本`包含`'搜索'`文本，可用来作条件查找元素。

输入关键词搜索后，再查看页面 html：

![](imgs/change2.png)

通过分析 html 代码，我们可以看出，每个结果的标题都存在`id`为`'hits-list'`里面，`class`为`'item'`的元素中。因此，我们可以获取页面中所有这些元素，再遍历获取其信息。

---

## ✅️️ 示例代码

您可以直接运行以下代码：

```python
from DrissionPage import WebPage

# 创建页面对象
page = WebPage()
# 访问网址
page.get('https://gitee.com/explore/all')
# 切换到收发数据包模式
page.change_mode()
# 获取所有行元素
items = page.ele('.ui relaxed divided items explore-repo__list').eles('.item')
# 遍历获取到的元素
for item in items:
    # 打印元素文本
    print(item('t:h3').text)
    print(item('.project-desc mb-1').text)
    print()
```

**输出：**

```shell
g1879/DrissionPage
基于python的网页自动化工具。既能控制浏览器，也能收发数据包。可兼顾浏览器自动化的便利性和requests的高效率。功能强大，内置无数人性化设计和便捷功能。语法简洁而优雅，代码量少。

mirrors_g1879/DrissionPage
DrissionPage

g1879/DrissionPageDocs
DrissionPage的文档
```

---

## ✅️️ 示例详解

我们逐行解读代码：

```python
from DrissionPage import WebPage
```

↑ 首先，我们导入页面对象`WebPage`类。

```python
page = WebPage()
```

↑ 接下来，我们创建一个`WebPage`对象。

```python
page.get('https://gitee.com/explore')
```

↑ 然后控制浏览器访问 gitee。

```python
page('#q').input('DrissionPage')
page('t:button@tx():搜索').click()
page.wait.load_start()
```

↑ 再通过模拟输入的方式输入关键词，模拟点击搜索按钮。

这里查找元素的方法上两个示例已经讲过，不再细说。

`wait.load_start()`方法用于等待页面进入加载状态，避免操作过快出现异常。

```python
page.change_mode()
```

↑ `change_mode()`方法用于切换工作模式，从当前控制浏览器的模式切换到收发数据包模式。

切换的时候程序会在新模式重新访问当前 url。

```python
items = page('#hits-list').eles('.item')
```

↑ 切换后，我们可以用与控制浏览器一致的语法，获取页面元素，这获取页面中所有结果行素，它返回这些元素对象组成的列表。

```python
for item in items:
    print(item('.title').text)
    print(item('.desc').text)
    print()
```

↑ 最后，我们遍历这些元素，并逐个打印它们包含的文本。
