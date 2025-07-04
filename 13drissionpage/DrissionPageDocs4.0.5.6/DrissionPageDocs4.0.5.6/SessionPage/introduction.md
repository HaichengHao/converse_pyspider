---
id: intro
title: '🚄 概述'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

`SessionPage`对象和`WebPage`对象的 s 模式，可用收发数据包的形式访问网页。

本章介绍`SessionPage`。

顾名思义，`SessionPage`是一个使用使用`Session`（requests 库）对象的页面，它使用 POM 模式封装了网络连接和 html 解析功能，使收发数据包也可以像操作页面一样便利。

并且，由于加入了本库独创的查找元素方法，使数据的采集便利性远超 requests + beautifulsoup 等组合。

`SessionPage`是本库几种页面对象中最简单的，我们先从它开始入手。

我们看个简单的例子，来了解`SessionPage`的工作方式。

---

获取 gitee 推荐项目第一页所有项目。

```python
# 导入
from DrissionPage import SessionPage
# 创建页面对象
page = SessionPage()
# 访问网页
page.get('https://gitee.com/explore/all')
# 在页面中查找元素
items = page.eles('t:h3')
# 遍历元素
for item in items[:-1]:
    # 获取当前<h3>元素下的<a>元素
    lnk = item('tag:a')
    # 打印<a>元素文本和href属性
    print(lnk.text, lnk.link)
```

**输出：**

```shell
七年觐汐/wx-calendar https://gitee.com/qq_connect-EC6BCC0B556624342/wx-calendar
ThingsPanel/thingspanel-go https://gitee.com/ThingsPanel/thingspanel-go
APITable/APITable https://gitee.com/apitable/APITable
Indexea/ideaseg https://gitee.com/indexea/ideaseg
CcSimple/vue-plugin-hiprint https://gitee.com/CcSimple/vue-plugin-hiprint
william_lzw/ExDUIR.NET https://gitee.com/william_lzw/ExDUIR.NET
anolis/ancert https://gitee.com/anolis/ancert
cozodb/cozo https://gitee.com/cozodb/cozo
后面省略...
```
