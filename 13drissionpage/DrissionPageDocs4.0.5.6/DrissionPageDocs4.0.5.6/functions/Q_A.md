---
id: QandA
title: '❓ 常见问题'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

本页收集一些用户使用过程中的常见问题。

欢迎各位开发者添砖加瓦，您可提交 issues、PR，也可以写成博客文章，链接发给本库作者，直接链接到文章。

## ❔ 如何在无界面 Linux 使用

CentOS 请参考这篇文章：[linux 部署说明](https://blog.csdn.net/sinat_39327967/article/details/132181129?spm=1001.2014.3001.5501)

Ubuntu 请参考这篇文章：[DrissionPage在UbuntuLinux的使用](https://zhuanlan.zhihu.com/p/674687748)

---

## ❔ 为什么浏览器不能退出无头模式？

> 为什么设置过无头后，下次运行即使不设置`headless()`，浏览器依然进入无头状态？

因为上一次打开的浏览器没有关闭，只是因为开了无头不可见，程序继续接管了它。

如果要关闭浏览器，可在程序结束时使用`page.quit()`语句。

也可以设置`co.headless(False)`，程序会自动关闭之前的无头浏览器再启动新的。

另请注意，`page.close()`的功能是关闭当前标签页，而不是关闭浏览器，除非浏览器只有一个标签页。

---

## ❔ 如何禁用保存密码、恢复页面等提示气泡？

浏览器提示气泡出现时可以手动关闭，不关闭也不影响自动操作，在代码中阻止其显示也是可以的。
加一些浏览器配置代码即可禁止相应的气泡显示，需要添加下面这样的代码：

```python
co = ChromiumOptions()

# 阻止“自动保存密码”的提示气泡
co.set_pref('credentials_enable_service', False)

# 阻止“要恢复页面吗？Chrome未正确关闭”的提示气泡
co.set_argument('--hide-crash-restore-bubble')

page = ChromiumPage(co)
```

---

## ❔ 点击报错“该元素没有位置及大小”怎么办？

没有位置及大小是正常的，很多元素都没有位置和大小。

这个时候你要检查是否页面中有同名元素，定位符没写准确拿到了另一个。

如果要点击的元素就是没有位置的，可以强制使用 js 点击，用法是 `.click(by_js=True)`，可以简写为 `.click('js')`。

---

## ❔ 如何使用启动参数、用户配置、实验项等功能？

**arguments 启动参数**
- 使用参考：https://DrissionPage.cn/ChromiumPage/browser_opt#-set_argument
- 参数详见：https://peter.sh/experiments/chromium-command-line-switches/

**prefs 用户配置**
- 使用参考：https://DrissionPage.cn/ChromiumPage/browser_opt#-set_pref
- 参数详见：https://src.chromium.org/viewvc/chrome/trunk/src/chrome/common/pref_names.cc

**flags 实验项**
- 使用参考：https://DrissionPage.cn/ChromiumPage/browser_opt#-set_flag
- 参数详见：chrome://flags

:::warning 注意
    外部链接仅供参考，请谨慎使用任何高级功能，仅在确保一切都可以掌控时才可使用，因为使用这些功能可能会导致浏览器数据丢失或安全和隐私受到威胁。
:::

## ❔ 如何匹配特殊字符（如`'&nbsp;'`）文本？

需先将特殊字符转为十六进制形式，详见《查找元素》中《语法速查表》一节。
