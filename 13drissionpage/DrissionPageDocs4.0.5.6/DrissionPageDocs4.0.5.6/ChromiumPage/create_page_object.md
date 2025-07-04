---
id: create_page_obj
title: '🚤 启动或接管浏览器'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

`ChromiumPage`对象和`WebPage`对象的 d 模式都能控制浏览器，本节只介绍`ChromiumPage`的创建，在`WebPage`的章节再对其进行介绍。

用`ChromiumPage()`创建页面对象。根据不同的配置，可以接管已打开的浏览器，也可以启动新的浏览器。

程序结束时，被打开的浏览器不会主动关闭，以便下次运行程序时使用（由 VSCode 启动的会被关闭）。

新手在使用无头模式时需注意，程序关闭后其实浏览器进程还在，只是看不见。

`ChromiumPage`和`WebPage`对象为单例，每个浏览器只能有一个该对象。对同一个浏览器重复使用`ChromiumPage`获取的都是同一个对象。

## ✅️ `ChromiumPage`初始化参数

|     初始化参数      | 类型                                                           | 默认值    | 说明                                                                                                  |
|:--------------:|:------------------------------------------------------------:|:------:|-----------------------------------------------------------------------------------------------------|
| `addr_or_opts` | `str`<br/>`int`<br/>`ChromiumOptions`<br/> | `None` | 浏览器启动配置或接管信息。<br/>传入 'ip: port' 字符串、端口数字或`ChromiumOptions`对象时按配置启动或接管浏览器；<br/>为`None`时使用配置文件配置启动浏览器 |
|    `tab_id`    | `str`                                                        | `None` | 要控制的标签页 id，为`None`则控制激活的标签页                                                                         |
|   `timeout`    | `float`                                                      | `None` | 整体超时时间，为`None`则从配置文件中读取，默认`10`                                                                       |

---

## ✅️ 直接创建

### 📌 默认方式

这种方式代码最简洁，程序会使用默认配置，自动生成页面对象。

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
```

创建`ChromiumPage`对象时会在指定端口启动浏览器，或接管该端口已有浏览器。

默认情况下，程序使用 9222 端口，浏览器可执行文件路径为`'chrome'`。

如路径中没找到浏览器可执行文件，Windows 系统下程序会在注册表中查找路径。

如果都没找到，则要用下文介绍的手动配置方法。

直接创建时，程序默认读取 ini 文件配置，如 ini 文件不存在，会使用内置配置。

默认 ini 和内置配置信息详见“进阶使用->配置文件的使用”章节。

:::tip Tips
    您可以修改配置文件中的配置，实现所有程序都按您的需要进行启动，详见”启动配置“章节。
:::

---

### 📌 指定端口或地址

创建`ChromiumPage`对象时向`addr_or_opts`参数传入端口号或地址，可接管指定端口浏览器，若端口空闲，使用默认配置在该端口启动一个浏览器。

传入端口时用`int`类型，传入地址时用`'address:port'`格式。

```python
# 接管9333端口的浏览器，如该端口空闲，启动一个浏览器
page = ChromiumPage(9333)
page = ChromiumPage('127.0.0.1:9333')
```

---

## ✅️ 通过配置信息创建

如果需要已指定方式启动浏览器，可使用`ChromiumOptions`。它是专门用于设置浏览器初始状态的类，内置了常用的配置。详细使用方法见“浏览器启动配置”一节。

### 📌 使用方法

`ChromiumOptions`用于管理创建浏览器时的配置，内置了常用的配置，并能实现链式操作。详细使用方法见“启动配置”一节。

| 初始化参数       | 类型     | 默认值    | 说明                                   |
| ----------- | ------ | ------ | ------------------------------------ |
| `read_file` | `bool` | `True` | 是否从 ini 文件中读取配置信息，如果为`False`则用默认配置创建 |
| `ini_path`  | `str`  | `None` | 文件路径，为`None`则读取默认 ini 文件             |

:::warning 注意
    - 配置对象只有在启动浏览器时生效。
    - 浏览器创建后再修改这个配置是没有效果的。
    - 接管已打开的浏览器配置也不会生效。
:::

```python
# 导入 ChromiumOptions
from DrissionPage import ChromiumPage, ChromiumOptions

# 创建浏览器配置对象，指定浏览器路径
co = ChromiumOptions().set_browser_path(r'D:\chrome.exe')
# 用该配置创建页面对象
page = ChromiumPage(addr_or_opts=co)
```

---

### 📌 直接指定地址创建

`ChromiumPage`可以直接接收浏览器地址来创建，格式为 'ip:port'。

使用这种方式时，如果浏览器已存在，程序会直接接管；如不存在，程序会读取默认配置文件配置，在指定端口启动浏览器。

```python
page = ChromiumPage(addr_or_opts='127.0.0.1:9333')
```

---

### 📌 使用指定 ini 文件创建

以上方法是使用默认 ini 文件中保存的配置信息创建对象，你可以保存一个 ini 文件到别的地方，并在创建对象时指定使用它。

```python
from DrissionPage import ChromiumPage, ChromiumOptions

# 创建配置对象时指定要读取的ini文件路径
co = ChromiumOptions(ini_path=r'./config1.ini')
# 使用该配置对象创建页面
page = ChromiumPage(addr_or_opts=co)
```

---

## ✅️ 接管已打开的浏览器

页面对象创建时，只要指定的地址（ip: port）已有浏览器在运行，就会直接接管。无论浏览器是下面哪种方式启动的。

### 📌 用程序启动的浏览器

默认情况下，创建浏览器页面对象时会自动启动一个浏览器。只要这个浏览器不关闭，下次运行程序时会接管同一个浏览器继续操作（配置的 ip: port 信息不变）。

这种方式极大地方便了程序的调试，使程序不必每次重新开始，可以单独调试某个功能。

```python
from DrissionPage import ChromiumPage

# 创建对象同时启动浏览器，如果浏览器已经存在，则接管它
page = ChromiumPage()  
```

---

### 📌 手动打开的浏览器

如果需要手动打开浏览器再接管，可以这样做：

1. 右键点击浏览器图标，选择属性
2. 在“目标”路径后面加上` --remote-debugging-port=端口号`（注意最前面有个空格）
3. 点击确定
4. 在程序中的浏览器配置中指定接管该端口浏览器

文件快捷方式的目标路径设置：

```
D:\chrome.exe --remote-debugging-port=9222
```

程序代码：

```python
from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions().set_local_port(9222)
page = ChromiumPage(addr_or_opts=co)
```

:::warning 注意
    接管浏览器时只有`local_port`、`address`参数是有效的。
:::

---

### 📌 bat 文件启动的浏览器

可以把上一种方式的目标路径设置写进 bat 文件（Windows系统），运行 bat 文件来启动浏览器，再用程序接管。

新建一个文本文件，在里面输入以下内容（路径改为自己电脑的）：

```shell
"D:\chrome.exe" --remote-debugging-port=9222
```

保存后把后缀改成 bat，然后双击运行就能在 9222 端口启动一个浏览器。程序代码则和上一个方法一致。

---

## ✅️ 多浏览器共存

如果想要同时操作多个浏览器，或者自己在使用其中一个上网，同时控制另外几个跑自动化，就需要给这些被程序控制的浏览器设置单独的**端口**和**用户文件夹**，否则会造成冲突。

### 📌 指定独立端口和数据文件夹

每个要启动的浏览器使用一个独立的`ChromiumOptions`对象进行设置：

```python
from DrissionPage import ChromiumPage, ChromiumOptions

# 创建多个配置对象，每个指定不同的端口号和用户文件夹路径
do1 = ChromiumOptions().set_paths(local_port=9111, user_data_path=r'D:\data1')
do2 = ChromiumOptions().set_paths(local_port=9222, user_data_path=r'D:\data2')

# 创建多个页面对象
page1 = ChromiumPage(addr_or_opts=do1)
page2 = ChromiumPage(addr_or_opts=do2)

# 每个页面对象控制一个浏览器
page1.get('https://www.baidu.com')
page2.get('http://www.163.com')
```

:::warning 注意
    每个浏览器都要设置独立的端口号和用户文件夹，二者缺一不可。
:::

---

### 📌 `auto_port()`方法

`ChromiumOptions`对象的`auto_port()`方法，可以指定程序每次使用空闲的端口和临时用户文件夹创建浏览器。也是每个浏览器要使用独立的`ChromiumOptions`对象。

但这种方法创建的浏览器不能重复使用。

:::tip Tips
    `auto_port()`支持多线程，但不支持多进程。  
    多进程使用时，可用`scope`参数指定每个进程使用的端口范围，以免发生冲突。
:::

```python
from DrissionPage import ChromiumPage, ChromiumOptions

co1 = ChromiumOptions().auto_port()
co2 = ChromiumOptions().auto_port()

page1 = ChromiumPage(addr_or_opts=co1)
page2 = ChromiumPage(addr_or_opts=co2)

page1.get('https://www.baidu.com')
page2.get('http://www.163.com')
```

---

### 📌 在 ini 文件设置自动分配

可以把自动分配的配置记录到 ini 文件，这样无需创建`ChromiumOptions`，每次启动的浏览器都是独立的，不会冲突。但和`auto_port()`一样，这些浏览器也不能复用。

```python
from DrissionPage import ChromiumOptions

ChromiumOptions().auto_port(True).save()
```

这段代码把该配置记录到 ini 文件，只需运行一次，要关闭的话把参数换成`False`再执行一次即可。

```python
from DrissionPage import ChromiumPage

page1 = ChromiumPage()
page2 = ChromiumPage()

page1.get('https://www.baidu.com')
page2.get('http://www.163.com')
```

## ✅️ 使用系统浏览器用户目录

初始默认配置下，程序会为每个使用的端口创建空的用户目录，并且每次接管都使用，这样可以有效避免浏览器冲突。

有些时候我们希望使用系统安装的浏览器的默认用户文件夹。以便复用用户信息和插件等。

我们可以这样设置：

### 📌 使用`ChromiumOptions`

用`ChromiumOptions`在每次启动时配置。

```python
from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions().use_system_user_path()
page = ChromiumPage(co)
```

### 📌 使用 ini 文件

把这个配置记录到 ini 文件，就不用每次使用都配置。

```python
from DrissionPage import ChromiumOptions

ChromiumOptions().use_system_user_path().save()
```

### 📌 冲突的处理

假如和已打开的浏览器发生冲突，会弹出异常并提醒用户关闭浏览器。

```shell
DrissionPage.errors.BrowserConnectError: 
127.0.0.1:9222浏览器无法链接。
请确认：
1、该端口为浏览器
2、已添加'--remote-debugging-port=9222'启动项
3、用户文件夹没有和已打开的浏览器冲突
4、如为无界面系统，请添加'--headless=new'参数
5、如果是Linux系统，可能还要添加'--no-sandbox'启动参数
可使用ChromiumOptions设置端口和用户文件夹路径。
```

---

## ✅️ 创建全新的浏览器

默认情况下，程序会复用之前用过的浏览器用户数据，因此可能带有登录数据、历史记录等。

如果想打开全新的浏览器，可用以下方法：

### 📌 使用`auto_port()`

上文提过的`auto_port()`方法，设置后每次打开的浏览器都是全新的。

示例见上文。

---

### 📌 手动指定端口和路径

给浏览器用户文件夹路径指定空的路径，以及指定一个空闲的端口，即可打开全新浏览器。

```python
from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions().set_local_port(9333).set_user_data_path(r'C:\tmp')
page = ChromiumPage(co)
```
