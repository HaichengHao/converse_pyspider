---
id: intro
title: '🚤 概述'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

`ChromiumPage`对象和`WebPage`对象的 d 模式，可操控浏览器。本章介绍`ChromiumPage`。

顾名思义，`ChromiumPage`是 Chromium 内核浏览器的页面，它用 POM 方式封装了操控网页所需的属性和方法。

使用它，我们可与网页进行交互，如调整窗口大小、滚动页面、操作弹出框等等。

通过从中获取的元素对象，我们还可以跟页面中的元素进行交互，如输入文字、点击按钮、选择下拉菜单等等。

甚至，我们可以在页面或元素上运行 JavaScript 代码、修改元素属性、增删元素等。

可以说，操控浏览器的绝大部分操作，都可以由`ChromiumPage`及其衍生的对象完成，而它们的功能，还在不断增加。

除了与页面和元素的交互，`ChromiumPage`还扮演着浏览器控制器的角色，可以说，一个`ChromiumPage`对象，就是一个浏览器。

它可以对标签页进行管理，可以对下载任务进行控制。可以为每个标签页生成独立的页面对象（`ChromiumTab`），以实现多标签页同时操作，而无需切入切出。

随着 3.0 版本脱离对 WebDriver 的依赖，作者终于可以放飞自我，为`ChromiumPage`添加各种各样有意思的功能，我们以后会越做越好。

我们看个简单的例子，来了解`CromiumPage`的工作方式。

---

在百度搜搜“Drissionpage”，并打印结果。

```python
# 导入
from DrissionPage import ChromiumPage

# 创建对象
page = ChromiumPage()
# 访问网页
page.get('https://www.baidu.com')
# 输入文本
page('#kw').input('DrissionPage')
# 点击按钮
page('#su').click()
# 等待页面跳转
page.wait.load_start()
# 获取所有结果
links = page.eles('tag:h3')
# 遍历并打印结果
for link in links:
    print(link.text)
```
