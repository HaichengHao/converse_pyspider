---
id: new_browser
title: '🥦 创建全新的浏览器'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

默认设置下，DrissionPage 会在 9222 端口创建浏览器，如果该端口下浏览器已经启动，则会接管使用。

并且会重复使用用户文件夹，即该端口登录过的账号，下次启动时可能仍有效，使用的插件也一样。

这为调试和日常使用带来大量便利，无须总是要处理登录和加载插件。

但项目中往往需要创建全新的浏览器环境，不希望复用之前的用户数据，可用以下方法实现：

## ✅️️ `auto_port()`方法

使用`ChromiumOptions`对象的`atuo_port()`方法，可指定程序自动创建全新的浏览器，多个浏览器互不干扰。

```python
from DrissionPage import ChromiumOptions, ChromiumPage

co = ChromiumOptions().auto_port()
page1 = ChromiumPage(co)
page2 = ChromiumPage(co)
```

如此即可创建两个全新且独立的浏览器。

可以注意到，示例中两个`ChromiumPage`对象共用了一个`ChromiumOptions`对象，这在设置`auto_port()`时才会生效。

如果没有设置`auto_port()`，两个页面对象其实是同一个。

:::warning 注意
    如果使用`atuo_port()`后再使用`set_loacl_port()`、`set_address()`或`set_user_data_path()`，会覆盖`auto_port()`设置。
:::

---

## ✅️️ 手动配置

如果有更细致的需求，不使用`auto_port()`，可自行使用`set_loacl_port()`、`set_address()`和`set_user_data_path()`为每个浏览器指定端口和用户文件夹。

:::warning 注意
    - 务必注意的是，每个浏览器的端口和用户文件夹都必须是独立的，不能复用
    - 每个浏览器都要一个`ChromiumOptions`对象，不能复用
:::

```python
from DrissionPage import ChromiumPage, ChromiumOptions

co1 = ChromiumOptions().set_local_port(9111).set_user_data_path('data1')
co2 = ChromiumOptions().set_local_port(9222).set_user_data_path('data2')

page1 = ChromiumPage(co1)
page2 = ChromiumPage(co2)
```
