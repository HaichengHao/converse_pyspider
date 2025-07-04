---
id: packaging
title: '⚙️ 打包程序'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

本节介绍打包程序需要注意的事项。

## ✅️️ 使用新的虚拟环境！

养成打包的良好习惯，使用新建的虚拟环境，只安装必要的库去打包，可以使打包出来的 exe 文件体积缩小。在只安装 DrissionPage 的环境中打包出来的程序，大小大概在 14M。

如果您打包出来的程序体积巨大，请尝试这个方法。

---

## ✅️️ 解决 ini 不存在报错

:::info 说明
    从`v4.0.4.1`开始不存在这个报错，以下是此版本之前打包报错的解决方法。
:::

因为程序用到 ini 文件，而打包时不会自动带上，因此直接打包是会导致运行出错。

解决办法：

- 手动带上 ini 文件，并在程序中指定路径
- 把配置信息写在程序中，不带 ini 文件

### 📌 带上 ini 文件

在程序中用相对路径方式指定 ini 文件，把 ini 文件复制到程序文件夹。

```python
from DrissionPage import WebPage, ChromiumOptions, SessionOptions

co = ChromiumOptions(ini_path=r'.\configs.ini')
so = SessionOptions(ini_path=r'.\configs.ini')
page = WebPage(chromium_options=co, session_or_options=so)
```

可以使用`configs_to_here()`方法自动复制 ini 文件。

在项目新建一个 py 文件，输入以下内容并运行

```python
from DrissionPage.common import configs_to_here

configs_to_here()
```

之后，项目文件夹会多出一个`'dp_configs.ini'`文件。页面对象初始化时会优先读取这个文件。

把它和打包出来的可执行文件放在一起即可。

---

### 📌 不使用 ini

在程序中指定不使用 ini 文件，就不会报错。这种方法需把所有配置信息写到代码里。

以下以`WebPage`作为示例，`ChromiumPage`和`SessionPage`使用方法也一样。

```python
from DrissionPage import WebPage, ChromiumOptions, SessionOptions

co = ChromiumOptions(read_file=False)  # 不读取文件方式新建配置对象
co.set_browser_path(r'.\chrome.exe')  # 输入配置信息
so = SessionOptions(read_file=False)

page = WebPage(chromium_options=co, session_or_options=so)
```

注意，这个时候 driver 和 session 两个参数都要输入内容，如果其中一个不需要设置可以输入`False`：

```python
page = WebPage(chromium_options=co, session_or_options=False)
```

---

## ✅️️ 实用示例

通常，我会把一个绿色浏览器和打包后的 exe 文件放在一起，程序中用相对路径指向该浏览器，这样拿到别的电脑也可以正常使用。

```python
from DrissionPage import WebPage, ChromiumOptions

co = ChromiumOptions(read_file=False).set_paths(local_port='9888',
                                                browser_path=r'.\Chrome\chrome.exe',
                                                user_data_path=r'.\Chrome\userData')
page = WebPage(chromium_options=co, session_or_options=False)
# 注意：session_or_options=False

page.get('https://www.baidu.com')
```

注意以下两点，程序就会跳过读取 ini 文件：

- `ChromiumOptions()`里要设置`read_file=False`
- 如果不传入某个模式的配置（示例中为 s 模式），要在页面对象初始化时设置对应参数为`False`
