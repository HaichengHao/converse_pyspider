---
id: ini
title: '⚙️ 配置文件的使用'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

本库使用 ini 文件记录浏览器或`Session`对象的启动配置。便于配置复用，免于在代码中加入繁琐的配置信息。  
默认情况下，页面对象启动时自动加载文件中的配置信息。  
也可以在默认配置基础上用简单的方法再次修改，再保存到 ini 文件。  
也可以保存多个 ini 文件，按不同项目需要调用。

:::warning 注意
    - ini 文件仅用于管理启动配置，页面对象创建后再修改 ini 文件是没用的。
    - 如果是接管已打开的浏览器，这些设置也没有用。
    - 每次升级本库，ini 文件都会被重置，可另存到其它路径以免重置。
:::

## ✅️️ ini 文件内容

ini 文件初始内容如下。

```ini
[paths]
download_path = 
tmp_path = 

[chromium_options]
address = 127.0.0.1:9222
browser_path = chrome
arguments = ['--no-default-browser-check', '--disable-suggestions-ui', '--no-first-run', '--disable-infobars', '--disable-popup-blocking', '--hide-crash-restore-bubble', '--disable-features=PrivacySandboxSettings4']
extensions = []
prefs = {'profile.default_content_settings.popups': 0, 'profile.default_content_setting_values': {'notifications': 2}}
flags = {}
load_mode = normal
user = Default
auto_port = False
system_user_path = False
existing_only = False

[session_options]
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'connection': 'keep-alive', 'accept-charset': 'GB2312,utf-8;q=0.7,*;q=0.7'}

[timeouts]
base = 10
page_load = 30
script = 30

[proxies]
http =
https = 

[others]
retry_times = 3
retry_interval = 2
```

---

## ✅️️ 文件位置

默认配置文件存放在 DrissionPage 库 _configs 文件夹下，文件名为 configs.ini。  
用户可另存其它配置文件，或从另存的文件读取配置，但默认文件的位置和名称不会改变。

---

## ✅️️ 使用默认配置文件启动

### 📌 使用页面对象自动加载

这是默认启动方式。

```python
from DrissionPage import WebPage

page = WebPage()
```

---

### 📌 使用配置对象加载

这种方式一般用于加载配置后需要进一步修改。

```python
from DrissionPage import ChromiumOptions, SessionOptions, WebPage

co = ChromiumOptions(ini_path=r'D:\setting.ini')
so = SessionOptions(ini_path=r'D:\setting.ini')

page = WebPage(chromium_options=co, session_or_options=so)
```

---

## ✅️️ 保存/另存 ini 文件

```python
from DrissionPage import ChromiumOptions

co = ChromiumOptions()

# 修改一些设置
co.no_imgs()

# 保存到当前打开的ini文件
co.save()
# 保存到指定位置的配置文件
co.save(r'D:\config1.ini')
# 保存到默认配置文件
co.save_to_default()
```

---

## ✅️️ 在项目路径使用 ini 文件

默认 ini 文件存放在 DrissionPage 安装目录下，修改要通过代码进行，给调试带来不便。

因此，提供了一个便捷的方法把默认 ini 文件复制到当前项目文件夹，并且程序会优先使用项目文件夹下的 ini 文件进行初始化配置。

这样开发者可方便地手动更改配置。项目打包也可以直接打包而不会造成找不到文件问题。

复制到项目下的 ini 文件名为`'dp_configs.ini'`，程序会默认读取这个文件的配置。

### 📌 `configs_to_here()`

此方法放在 `DrissionPage.common` 路径中，用于把默认 ini 文件复制到当前路径，并命名为`'dp_configs.ini'`。

| 参数名称        | 类型    | 默认值    | 说明                                  |
|:-----------:|:-----:|:------:| ----------------------------------- |
| `save_name` | `str` | `None` | 指定文件名，为`None`则命名为`'dp_configs.ini'` |

**返回：**`None`

**示例：**

在项目新建一个 py 文件，输入以下内容并运行

```python
from DrissionPage.common import configs_to_here

configs_to_here()
```

之后，项目文件夹会多出一个`'dp_configs.ini'`文件。页面对象初始化时会优先读取这个文件。

### 📌 用命令行复制

除了用`configs_to_here()`方法复制 ini 文件到项目文件夹，还可以用命令行方式复制。

在项目文件夹路径下运行以下命令即可：

```shell
dp --configs-to-here
```

效果和`configs_to_here()`一致，只是不能指定文件名。
