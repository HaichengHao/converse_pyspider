---
id: create_page_obj
title: '🛸 创建页面对象'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

本节介绍`WebPage`对象的创建。

`WebPage`对象拥有两种模式，d 模式用于操控浏览器，s 模式用于收发数据包。

## ✅️️ `WebPage`初始化参数

| 初始化参数                | 类型                                               | 默认值    | 说明                                                                                                                                        |
|:--------------------:|:------------------------------------------------:|:------:| ----------------------------------------------------------------------------------------------------------------------------------------- |
| `mode`               | `str`                                            | `'d'`  | 只能接收`'d'`或`'s'`，即初始选择操控浏览器还是收发数据包                                                                                                         |
| `timeout`            | `float`                                          | `None` | 整体超时时间，为`None`则从配置文件中读取，默认 10                                                                                                             |
| `chromium_options`  | `ChromiumOptions`<br/>`False` | `None` | 默认为`None`表示从 ini 文件读取配置进行初始化<br/>接收`ChromiumOptions`时用该配置启动或接管浏览器<br/>如不使用 d 模式功能，接收`False`，避免打包出错       |
| `session_or_options` | `Session`<br/>`SessionOptions`<br/>`False`         | `None` | 默认为`None`表示从 ini 文件读取配置进行初始化<br/>接收`Session`时直接使用一个已创建的`Session`对象<br/>接收`SessionOptions`时用该配置创建`Session`对象<br/>如不使用 s 模式功能，接收`False`，避免打包出错 |

---

## ✅️️ 直接创建

这种方式代码最简洁，程序会从默认 ini 文件中读取配置，自动生成页面对象。

创建时，可指定初始模式。

```python
from DrissionPage import WebPage

# 默认d模式创建对象
page = WebPage()

# 指定s模式创建对象
page = WebPage('s')
```

d 模式创建`WebPage`对象时会在指定端口启动浏览器，或接管该端口已有浏览器。

默认情况下，程序使用 9222 端口，浏览器可执行文件路径为`'chrome'`。如路径中没找到浏览器可执行文件，Windows 系统下程序会在注册表中查找路径。如果都没找到，则要用下一种方式手动配置。

:::warning 注意
    这种方式的程序不能直接打包，因为使用到 ini 文件。可参考“打包程序”一节的方法。
:::

:::tip Tips
    您可以修改配置文件中的配置，实现所有程序都按您的需要进行启动，详见”启动配置“章节。
:::

---

## ✅️️ 通过配置信息创建

如果需要已指定方式启动浏览器，可使用`ChromiumOptions`和`SessionOptions`。它们的使用在各自的章节已经介绍过，这里只演示如何在`WebPage`创建时使用。

### 📌 使用方法

创建两个配置对象后，传递给`WebPage`的初始化方法。

```python
from DrissionPage import WebPage, ChromiumOptions, SessionOptions

co = ChromiumOptions()
so = SessionOptions()

page = WebPage(chromium_options=co, session_or_options=so)
```

如果只需要对一个模式的配置进行修改，另一个模式使用 ini 的配置，可以只传入一种配置对象。

```python
from DrissionPage import WebPage, ChromiumOptions

co = ChromiumOptions()
page = WebPage(chromium_options=co)
```

:::info 说明
    当同时传入`ChromiumOptions`和`SessionOptions`时，两者都有的属性以`ChromiumOptions`为准。如`timeout`和`download_path`。
:::

---

### 📌 使用指定 ini 文件创建

以上方法是使用默认 ini 文件中保存的配置信息创建对象，你可以保存一个 ini 文件到别的地方，并在创建对象时指定使用它。

```python
from DrissionPage import WebPage, ChromiumOptions, SessionOptions

co = ChromiumOptions(ini_path=r'./config1.ini')
so = SessionOptions(ini_path=r'./config1.ini')

page = WebPage(chromium_options=co, session_or_options=so)
```

---