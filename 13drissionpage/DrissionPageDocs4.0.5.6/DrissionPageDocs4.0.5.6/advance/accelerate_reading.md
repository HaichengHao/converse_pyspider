---
id: accelerate
title: '⚙️ 数据读取加速'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

本节演示一个能够大幅加快浏览器页面数据采集的黑科技。

## ✅️️ 示例

我们找一个比较大的页面来演示，比如网页首页：[https://www.163.com](https://www.163.com)

我们数一下这个网页内的`<a>`元素数量：

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.163.com')
print(len(page('t:body').eles('t:a')))
```

**输出：**

```shell
1613
```

嗯，数量不少，可以看出效果。

假如现在我们的任务是打印所有链接的文本，常规做法是遍历所有元素，然后打印。

这里引入本库作者写的一个计时工具，可以标记一段代码运行时间。您也可以用其它方法计时。

```python
from DrissionPage import ChromiumPage
from TimePinner import Pinner  # 导入计时工具

pinner = Pinner()  # 创建计时器对象
page = ChromiumPage()
page.get('https://www.163.com')

pinner.pin()  # 标记开始记录

# 获取所有链接对象并遍历
links = page('t:body').eles('t:a')
for lnk in links:
    print(lnk.text)

pinner.pin('用时')  # 记录并打印时间
```

**输出：**

```shell
0.0

网络大过年_网易政务_网易网
网易首页
...中间省略...
不良信息举报 Complaint Center
廉正举报
用时：4.057772700001806
```

用时 4 秒。

现在，我们稍微修改一个小小的地方。

把`page('t:body').eles('t:a')`改成`page('t:body').s_eles('t:a')`，然后再执行一次。

```python
from DrissionPage import ChromiumPage
from TimePinner import Pinner  # 导入计时工具

pinner = Pinner()  # 创建计时器对象
page = ChromiumPage()
page.get('https://www.163.com')

pinner.pin()  # 标记开始记录

# 获取所有链接对象并遍历
links = page('t:body').s_eles('t:a')
for lnk in links:
    print(lnk.text)

pinner.pin('用时')  # 记录并打印时间
```

**输出：**

```shell
0.0

网络大过年_网易政务_网易网
网易首页
...中间省略...
不良信息举报 Complaint Center
廉正举报
用时：0.2797656000002462
```

神奇不？原来 4 秒的采集时间现在只需 0.28 秒。

---

## ✅️️ 解读

`s_eles()`与`eles()`的区别在于前者会把整个页面或动态元素转变成一个静态元素，再在其中获取下级元素或信息。因为静态元素是纯文本的，没有各种属性、交互等消耗资源的部分，所以运行速度非常快。

作者曾经采集过一个非常复杂的页面，动态元素用时 30 秒，转静态元素就只要 0.X 秒，加速效果非常明显。

我们可以获取页面中内容容器（示例中的`<body>`），把它转换成静态元素，再在其中获取信息。

当然，静态元素没有交互功能，它只是副本，也不会影响原来的动态元素。
