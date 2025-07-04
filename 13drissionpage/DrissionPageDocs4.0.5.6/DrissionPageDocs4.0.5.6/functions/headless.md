---
id: headless
title: '🥦 无头模式'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

要使用无头模式很简单，在`ChromiumOptions`设置`headless()`即可。

```python
from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions().headless()
page = ChromiumPage(co)
```

需要注意的是，程序结束时浏览器不会自动关闭，下次运行会继续接管该浏览器。

无头浏览器因为看不见很容易被忽视。可在程序结尾用`page.quit()`将其关闭。