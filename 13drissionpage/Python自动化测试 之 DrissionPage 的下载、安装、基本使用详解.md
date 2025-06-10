 

#### [Python自动化测试](https://so.csdn.net/so/search?q=Python%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&spm=1001.2101.3001.7020) 之 DrissionPage 使用详解

*   *   [🏡前言：](#_2)
    *   [一、☀️DrissionPage的基本概述](#DrissionPage_4)
    *   [二、 🗺️环境安装](#__39)
    *   *   [2.1 ✅️️运行环境](#21__40)
        *   [2.2 ✅️️一键安装](#22__48)
    *   [三、🗺️快速入门](#_63)
    *   *   [3.1 页面类](#31__65)
        *   *   [🛰️ChromiumPage](#ChromiumPage_69)
            *   [🛫 SessionPage](#_SessionPage_77)
            *   [🔎WebPage](#WebPage_85)
        *   [3.2 🌏 准备工作](#32___93)
        *   *   [3.2.1 尝试启动浏览器](#321__101)
            *   [3.2.2 设置浏览器驱动路径](#322__113)
            *   [3.2.3 🌏️控制浏览器](#323__162)
        *   [3.3 收发数据包](#33__188)
        *   [3.4 模式切换](#34__212)
    *   [四、🗺️ChromiumPage详解](#ChromiumPage_249)
    *   *   [4.1 启动和接管浏览器](#41__255)
        *   *   [4.1.1 启动浏览器](#411__259)
            *   [4.1.2 接管浏览器](#412__276)
            *   [4.1.3 多浏览器共存](#413__297)
        *   [4.2 页面交互](#42__317)
        *   [4.3 查找元素](#43__363)
        *   [4.4 获取元素信息的常用属性或方法](#44__467)
    *   [五、🗺️SessionPage详解](#SessionPage_497)
    *   *   [5.1 get请求](#51_get_522)
        *   [5.2 post请求](#52_post_546)
        *   [5.3 page对象常用属性](#53_page_586)
    *   [六、🗺️WebPage详解](#WebPage_597)
    *   [扩展](#_640)
    *   *   [⭐下载文件](#_641)
        *   [🥬设置 cookies](#_cookies_653)
        *   [❓ 常见问题](#__673)

### 🏡前言：

> 之前分享过一篇关于 [自动化测试框架 Selenium](https://so.csdn.net/so/search?q=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E6%A1%86%E6%9E%B6%20Selenium&spm=1001.2101.3001.7020) 使用的文章： [Python自动化测试 环境搭建 Selenium、WebDriver下载、安装、配置、基本使用详解](https://blog.csdn.net/muguli2008/article/details/130189085)，虽然 [Selenium](https://so.csdn.net/so/search?q=Selenium&spm=1001.2101.3001.7020)也很强大，但在使用下来后，感觉DrissionPage操作更简单、功能更强大一些（不像Selenium 会担心WebDriver版本对不上无法运行等情况），尤其是对新手入门来讲，DrissionPage是非常值得推荐学习的。

### 一、☀️DrissionPage的基本概述

> DrissionPage 是一个基于 python 的网页自动化工具。它既能控制浏览器，也能像requests一样收发数据包，更重要的是还能把两者合二为一。因此，简单来说DrissionPage可兼顾浏览器自动化的便利性和 requests 的高效率。  
> DrissionPage功能强大，内置无数人性化设计和便捷功能。并且它的语法简洁而优雅，代码量少，对新手友好。

![drissionpage](https://i-blog.csdnimg.cn/direct/ebeb001d0a0b4866be2dd08b4ffe1c7d.png#pic_center)

**🚀官网：[https://drissionpage.cn/](https://drissionpage.cn/)**

**📚文档：[https://drissionpage.cn/browser\_control/intro](https://drissionpage.cn/browser_control/intro)**

**💖 特性：**  
✅️️ 强大的自研内核

*   不依赖 webdriver
*   无需为不同版本的浏览器下载不同的驱动
*   运行速度更快
*   可以跨 iframe 查找元素，无需切入切出
*   可同时操作多个标签页，无需切换
*   方便好用的数据包监听功能
*   可处理非open状态的 shadow-root

✅️️ 极简的定位语法

*   制定了一套简洁高效的查找元素语法，支持链式操作，支持相对定位。
*   每次查找内置等待，可以独立设置每次查找超时时间。

✅️️ 更多便捷的功能

*   可对整个网页截图，包括视口外的部分
*   每次运行程序可以反复使用已经打开的浏览器，无需每次从头运行
*   s 模式访问网页时会自动纠正编码，无需手动设置
*   s 模式在连接时会自动根据当前域名自动填写Host和Referer属性
*   下载工具支持多种方式处理文件名冲突、自动创建目标路径、断链重试等
*   支持直接获取after和before伪元素的内容
*   上传文件可直接拦截文件选择框并输入路径，无需依靠 GUI 或查找元素输入

### 二、 🗺️环境安装

#### 2.1 ✅️️运行环境

操作系统：Windows、Linux 或 Mac。

python 版本：3.6 及以上

支持浏览器：Chromium 内核（如 Chrome 和 Edge）

#### 2.2 ✅️️一键安装

使用 pip 安装 DrissionPage：

```python
# 安装最新版本
pip install DrissionPage

# 如果已安装，可以在命令后面加上 --upgrade 参数 升级到最新版本
pip install DrissionPage --upgrade

# 指定版本升级
pip install DrissionPage==4.0.0b17
```

### 三、🗺️快速入门

#### 3.1 页面类

> 在DrissionPage框架中，有一个非常重要的工具叫做“**页面类**”，主要用于控制浏览器 和 收发数据包。DrissionPage 包含三种主要页面类。我们可以根据自己的需要选择使用。

##### 🛰️ChromiumPage

如果只要控制浏览器，导入`ChromiumPage`。

```python
from DrissionPage import ChromiumPage
```

##### 🛫 SessionPage

如果只要收发数据包，导入`SessionPage`。

```python
from DrissionPage import SessionPage
```

##### 🔎WebPage

`WebPage`是功能最全面的页面类，既可控制浏览器，也可收发数据包。

```python
from DrissionPage import WebPage
```

#### 3.2 🌏 准备工作

> 如果只使用收发数据包功能，无需任何准备工作。  
> 如果要控制浏览器，需设置浏览器路径。程序默认设置控制 Chrome，所以下面用 Chrome 演示。

> 开始前，我们先设置一下浏览器路径。  
> 程序默认控制 Chrome，所以下面用 Chrome 演示。 如果要使用 Edge 或其它 Chromium 内核浏览器，设置方法是一样的。

##### 3.2.1 尝试启动浏览器

> 默认状态下，程序会自动在系统内查找 Chrome 路径。  
> 执行以下代码，浏览器启动并且访问了相关网站，如果访问执行成功说明可直接使用，跳过后面的步骤即可。

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')
```

##### 3.2.2 设置浏览器驱动路径

> 如果上面的步骤提示出错，说明程序没在系统里找到 Chrome 浏览器。  
> 可用以下其中一种方法设置，设置会持久化记录到默认配置文件，之后程序会使用该设置启动。  
> ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8d94bc4e53b14a01811d19c74a68a7d2.png#pic_center)

*   **📌方法1**：
    
    *   新建一个临时 py 文件，并输入以下代码，填入您电脑里的 Chrome 浏览器可执行文件路径，然后运行。
        
        ```python
        from DrissionPage import ChromiumOptions
        
        path = r'D:\Chrome\Chrome.exe'  # 请改为你电脑内Chrome可执行文件路径
        ChromiumOptions().set_browser_path(path).save()
        ```
        
        > 这段代码会把浏览器路径记录到配置文件，今后启动浏览器皆以新路径为准。  
        > 另外，如果是想临时切换浏览器路径以尝试运行和操作是否正常，可以去掉 `.save()`，以如下方式结合第1️⃣步的代码。
        
        ```python
        from DrissionPage import ChromiumPage, ChromiumOptions
        
        path = r'C:\Users\Administrator\AppData\Local\Google\Chrome SxS\Application\chrome.exe'  # 请改为你电脑内Chrome可执行文件路径
        co = ChromiumOptions().set_browser_path(path)
        page = ChromiumPage(co)
        page.get('http://DrissionPage.cn')
        ```
    
*   **📌方法2**：
    
    *   在命令行输入以下命令（路径改成自己电脑里的）：
        
        ```shell
        dp -p C:\Users\Administrator\AppData\Local\Google\Chrome SxS\Application\chrome.exe
        ```
        
        > ⚠️注意命令行的 python 环境与项目应是同一个  
        > ⚠️注意要先使用 cd 命令定位到项目路径
        

现在，请重新执行第1️⃣步的代码，如果正确访问了目标网址，说明已经设置完成。

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')
```

**✅️️ OK，当您完成以上准备工作以后，无需关闭浏览器，后面的上手示例可继续接管当前浏览器。**

##### 3.2.3 🌏️控制浏览器

现在，我们通过一些例子，来直观感受一下 DrissionPage 的工作方式。

本示例演示使用`ChromiumPage`控制浏览器登录 gitee 网站。

```python
from DrissionPage import ChromiumPage

# 创建页面对象，并启动浏览器
page = ChromiumPage()
# 跳转到登录页面
page.get('https://gitee.com/login')

# 定位到账号文本框，获取文本框元素
ele = page.ele('#user_login')
# 输入对文本框输入账号  
ele.input('你的账号')
# 定位到密码文本框并输入密码
page.ele('#user_password').input('你的密码')
# 点击登录按钮:@attrName=value,这是根据属性和属性值进行标签定位的方式
page.ele('@value=登 录').click()
```

> 注意：`ele()`方法用于查找元素，它返回一个`ChromiumElement`对象，用于操作元素。值得一提的是，`ele()`内置了等待，如果元素未加载，它会执行等待，直到元素出现或到达时限。默认超时时间 10 秒。

#### 3.3 收发数据包

> 本示例演示用`SessionPage`已收发数据包的方式采集 gitee 网站数据。这个示例的目标，要获取所有库的名称和链接，为避免对网站造成压力，我们只采集 3 页。网址：https://gitee.com/explore/all

```python
from DrissionPage import SessionPage

# 创建页面/请求对象
page = SessionPage()

# 爬取3页
for i in range(1, 4):
    # 访问某一页的网页
    page.get(f'https://gitee.com/explore/all?page={i}')
    # 获取所有开源库<a>元素列表(所有库的链接的a标签的class属性值都是一样的)
    links = page.eles('.title project-namespace-path')
    # 遍历所有<a>元素
    for link in links:
        # 打印链接信息：
        print(link.text, link.link)
```

`.text`获取元素的文本，`.link`获取元素的`href`或`src`属性。

#### 3.4 模式切换

> 这个示例演示`WebPage`如何切换控制浏览器和收发数据包两种模式。  
> 通常，切换模式是用来应付登录检查很严格的网站，可以用控制浏览器的形式处理登录，再转换模式用收发数据包的形式来采集数据。

> 实例：基于浏览器控制模式进行gitee的登陆，登录成功后切换模式基于收发数据包的性质访问该账户的个人主页，获取该账户主页左下角所有的组织名称。

```python
from DrissionPage import ChromiumOptions
from DrissionPage import WebPage

# 创建页面对象
page = WebPage()
# 访问网址,进行登录
page.get('https://gitee.com/login?redirect_to_url=%2F')
# 定位到账号文本框，获取文本框元素
ele = page.ele('#user_login')
# 输入对文本框输入账号
ele.input('你的账号')
# 定位到密码文本框并输入密码
page.ele('#user_password').input('你的密码')
# 点击登录按钮:@attrName=value,这是根据属性和属性值进行标签定位的方式
page.ele('@value=登 录').click()

# 切换到收发数据包模式
page.change_mode() #切换的时候程序会在新模式重新访问当前 url。
#切换模式后，重新访问基于登录状态后新的url（个人主页）
page.get('https://gitee.com/muguilin')

# 根据class属性值获取div标签，然后将该div下面class为item的元素标签批量获取
items = page.ele('.ui middle aligned list').eles('.item')
# 遍历获取到的元素
for item in items:
    # 打印元素文本
    print(item('.content').text)
```

### 四、🗺️ChromiumPage详解

> 顾名思义，`ChromiumPage`是 Chromium 内核浏览器的页面，使用它，我们可与网页进行交互，如调整窗口大小、滚动页面、操作弹出框等等。还可以跟页面中的元素进行交互，如输入文字、点击按钮、选择下拉菜单、在页面或元素上运行 JavaScript 代码等等。

> 可以说，操控浏览器的绝大部分操作，都可以由`ChromiumPage`及其衍生的对象完成，而它们的功能，还在不断增加。除了与页面和元素的交互，`ChromiumPage`还扮演着浏览器控制器的角色，可以说，一个`ChromiumPage`对象，就是一个浏览器。

#### 4.1 启动和接管浏览器

> 用`ChromiumPage()`创建页面对象。根据不同的配置，可以接管已打开的浏览器，也可以启动新的浏览器。程序结束时，被打开的浏览器不会主动关闭，以便下次运行程序时使用（由 VSCode 启动的会被关闭）。

##### 4.1.1 启动浏览器

> 这种方式代码最简洁，程序会使用默认配置，自动生成页面对象。创建`ChromiumPage`对象时会在指定端口启动浏览器。默认情况下，程序使用 9222 端口。

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
```

指定端口启动浏览器：

```python
# 启动9333端口的浏览器，如该端口空闲，启动一个浏览器
page = ChromiumPage(9333)
```

##### 4.1.2 接管浏览器

> 当页面对象创建时，只要指定的端口port已有浏览器在运行，就会直接接管。无论浏览器是哪种方式启动的。比如：先通过如下代码启动一个端口为8888的浏览器

```python
from DrissionPage import ChromiumPage

page = ChromiumPage(666)

```

在启动的端口为8888的浏览器中，手动访问百度页面，然后使用如下程序测试是否可以接管该浏览器：

```python
from DrissionPage import ChromiumPage

page = ChromiumPage(666)
#打印接管浏览器的page标题和访问的url
print(page.title,page.url)
```

##### 4.1.3 多浏览器共存

> 如果想要同时操作多个浏览器，或者自己在使用其中一个上网，同时控制另外几个浏览器跑自动化，就需要给这些被程序控制的浏览器设置单独的**端口**和**用户文件夹**，否则会造成冲突。

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

#### 4.2 页面交互

*   get()：该方法用于跳转到一个网址。当连接失败时，程序会进行重试。
    
    ```python
    page.get('https://www.baidu.com')
    ```
    
*   back()：此方法用于在浏览历史中后退若干步。
    
    ```python
    page.back(2)  # 后退两个网页
    ```
    
*   forward()：此方法用于在浏览历史中前进若干步。
    
    ```python
    page.forward(2)  # 前进两步
    ```
    
*   refresh()：此方法用于刷新当前页面。
    
    ```python
    page.refresh()  # 刷新页面
    ```
    
*   run\_js()：此方法用于执行 js 脚本。
    
    ```python
    # 用传入参数的方式执行 js 脚本显示弹出框显示 Hello world!
    #参数1：执行的js脚本。参数2：*args表示给js脚本传递的参数
    page.run_js('alert(arguments[0]+arguments[1]);', 'Hello', ' world!')
    ```
    
*   run\_js\_loaded()：此方法用于运行 js 脚本，执行前等待页面加载完毕。
    
    ```python
    page.run_js_loaded('alert(arguments[0]+arguments[1]);', 'Hello', ' world!')
    ```
    
*   scroll.to\_bottom()：此方法用于滚动页面到底部，水平位置不变。
    
    ```python
    page.scroll.to_bottom()
    ```
    

#### 4.3 查找元素

> 本节介绍 DrissionPage 自创的查找元素语法。  
> 查找语法能用于指明以哪种方式去查找指定元素，定位语法简洁明了，熟练使用可大幅提高程序可读性。

**🔦 更多页面或元素内查找：[https://drissionpage.cn/browser\_control/get\_elements/find\_in\_object](https://drissionpage.cn/browser_control/get_elements/find_in_object)**

以下使用这个页面进行讲解test.html(可以在pycharm中使用chrome打开该页面获取页面链接)：

```html
<html>
<body>
<div id="one">
    <p class="p_cls" id="row1" data="a">第一行</p>
    <p class="p_cls" id="row2" data="b">第二行</p>
    <p class="p_cls">第三行</p>
</div>
<div id="two">
    第二个div
</div>
</body>
</html>
```

**基本定位语法：注意下面的ele和eles**

page.ele：只能定位满足要求第一次出现的标签

page.eles：定位到满足要求所有的标签

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('http://localhost:63342/Code/test.html?_ijt=chuqtur5cikh95asobefg123mf')
#id属性定位
tag1 = page.ele('@id=one')  # 获取第一个id为one的元素

#文本定位
tag2 = page.ele('@text()=第一行')  # 获取第一个文本为“第一行”的元素

#当需要多个条件同时确定一个元素时，每个属性用'@@'开头。
tag3 = page.ele('@@class=p_cls@@text()=第三行')  # 查找class为p_cls且文本为“第三行”的元素

#当需要以或关系条件查找元素时，每个属性用'@|'开头。
tag4 = page.eles('@|id=row1@|id=row2')  # 查找所有id为row1或id为row2的元素

#表示模糊匹配，匹配含有指定字符串的文本或属性。
tag5 = page.eles('@id:ow')  # 获取id属性包含'ow'的元素

#表示匹配开头，匹配开头为指定字符串的文本或属性。
tag6 = page.eles('@id^row')  # 获取id属性以'row'开头的元素

#表示匹配结尾，匹配结尾为指定字符串的文本或属性。
tag7 = page.ele('@id$w1')  # 获取id属性以'w1'结尾的元素

print(tag7)
```

**选择器定位语法**

id选择器定位：

```python
ele1 = page.ele('#one')  # 查找id为one的元素
ele2 = page.ele('#=one')  # 和上面一行一致
ele3 = page.ele('#:ne')  # 查找id属性包含ne的元素
ele4 = page.ele('#^on')  # 查找id属性以on开头的元素
ele5 = page.ele('#$ne')  # 查找id属性以ne结尾的元素
```

class选择器定位：

```python
e1 = page.ele('.p_cls')  # 查找class属性为p_cls的元素
e2 = page.ele('.=p_cls')  # 与上一行一致
e3 = page.ele('.:_cls')  # 查找class属性包含_cls的元素
e4 = page.ele('.^p_')  # 查找class属性以p_开头的元素
e5 = page.ele('.$_cls')  # 查找class属性以_cls结尾的元素
```

文本选择器定位：

```python
element1 = page.ele('text=第二行')  # 查找文本为“第二行”的元素
element2 = page.ele('text:第二')  # 查找文本包含“第二”的元素
element3 = page.ele('第二')  # 与上一行一致
```

标签选择器定位：

```python
ele1 = page.ele('tag:div')  # 查找第一个div元素
ele2 = page.ele('tag:p@class=p_cls')  # 与单属性查找配合使用
ele3 = page.ele('tag:p@@class=p_cls@@text()=第二行')  # 与多属性查找配合使用
```

xpath定位：

```python
eles = page.eles('xpath://div/p[@id="row1"]')
```

**🚀查看更多语法：[https://drissionpage.cn/browser\_control/get\_elements/sheet](https://drissionpage.cn/browser_control/get_elements/sheet)**

#### 4.4 获取元素信息的常用属性或方法

| 属性或方法 | 说明 |
| :-: | --- |
| `html` | 此属性返回元素的 HTML 文本（不包括`<iframe>`内容） |
| `inner_html` | 此属性返回元素内部的 HTML 文本 |
| `tag` | 此属性返回元素的标签名 |
| `text` | 此属性返回元素内所有文本组合成的字符串 |
| `texts()` | 此方法返回元素内所有**直接**子节点的文本（列表） |
| `attrs` | 此属性以字典形式返回元素所有属性及值 |
| `attr('attrName')` | 此方法返回元素某个 attribute 属性值 |
| `link` | 此方法返回元素的 href 属性或 src 属性 |
| `xpath` | 此属性返回当前元素在页面中 xpath 的绝对路径 |

<table><thead><tr><th style="text-align:center">原写法</th><th style="text-align:center">简化写法</th><th style="text-align:center">精确匹配</th><th style="text-align:center">模糊匹配</th><th style="text-align:center">匹配开头</th><th style="text-align:center">匹配结尾</th><th style="text-align:center">备注</th></tr></thead><tbody><tr><td style="text-align:center"><code>@id</code></td><td style="text-align:center"><code>#</code></td><td style="text-align:center"><code>#</code>或<code>#=</code></td><td style="text-align:center"><code>#:</code></td><td style="text-align:center"><code>#^</code></td><td style="text-align:center"><code>#$</code></td><td style="text-align:center">简化写法只能单独使用</td></tr><tr><td style="text-align:center"><code>@class</code></td><td style="text-align:center"><code>.</code></td><td style="text-align:center"><code>.</code>或<code>.=</code></td><td style="text-align:center"><code>.:</code></td><td style="text-align:center"><code>.^</code></td><td style="text-align:center"><code>.$</code></td><td style="text-align:center">简化写法只能单独使用</td></tr><tr><td style="text-align:center"><code>tag</code></td><td style="text-align:center"><code>t</code></td><td style="text-align:center"><code>t:</code>或<code>t=</code></td><td style="text-align:center">无</td><td style="text-align:center">无</td><td style="text-align:center">无</td><td style="text-align:center">只能用在句首</td></tr><tr><td style="text-align:center"><code>@tag()</code></td><td style="text-align:center"><code>@t()</code></td><td style="text-align:center"><code>@t():</code>或<code>@t()=</code></td><td style="text-align:center">无</td><td style="text-align:center">无</td><td style="text-align:center">无</td><td style="text-align:center">可作为属性组合使用</td></tr><tr><td style="text-align:center"><code>text</code></td><td style="text-align:center"><code>tx</code></td><td style="text-align:center"><code>tx=</code></td><td style="text-align:center"><code>tx:</code>或不写</td><td style="text-align:center"><code>tx^</code></td><td style="text-align:center"><code>tx$</code></td><td style="text-align:center">无标签时使用模糊匹配文本</td></tr><tr><td style="text-align:center"><code>@text()</code></td><td style="text-align:center"><code>@tx()</code></td><td style="text-align:center"><code>@tx()=</code></td><td style="text-align:center"><code>@tx():</code></td><td style="text-align:center"><code>@tx()^</code></td><td style="text-align:center"><code>@tx()$</code></td><td style="text-align:center">可作为属性组合使用</td></tr><tr><td style="text-align:center"><code>xpath</code></td><td style="text-align:center"><code>x</code></td><td style="text-align:center"><code>x:</code>或<code>x=</code></td><td style="text-align:center">无</td><td style="text-align:center">无</td><td style="text-align:center">无</td><td style="text-align:center">只能单独使用</td></tr><tr><td style="text-align:center"><code>css</code></td><td style="text-align:center"><code>c</code></td><td style="text-align:center"><code>c:</code>或<code>c=</code></td><td style="text-align:center">无</td><td style="text-align:center">无</td><td style="text-align:center">无</td><td style="text-align:center">只能单独使用</td></tr></tbody></table>



**元素列表中批量获取信息**

`eles()`等返回的元素列表，自带`get`属性，可用于获取指定信息。

```python
from DrissionPage import SessionPage

page = SessionPage()
page.get('https://www.baidu.com')
eles = page.ele('#s-top-left').eles('t:a')
print(eles.get.texts())  # 获取所有元素的文本
print(eles.get.links())  # 获取所有元素的链接
print(eles.get.attrs("class"))  # 获取所有元素的指定属性值

```

### 五、🗺️SessionPage详解

> 顾名思义，`SessionPage`是一个使用`Session`（requests 库）对象的页面，且它还封装了网络连接和 html 解析功能，使收发数据包也可以像操作页面一样便利。  
> 并且，由于加入了本库独创的查找元素方法，使数据的采集便利性远超 requests + beautifulsoup 等组合。

**🚀了解更多：[https://drissionpage.cn/SessionPage/intro](https://drissionpage.cn/SessionPage/intro)**  
获取 gitee 推荐项目第一页所有项目。

```python
# 导入
from DrissionPage import SessionPage
# 创建页面对象
page = SessionPage()
# 访问网页
page.get('https://gitee.com/explore/all')
# 在页面中查找元素
items = page.eles('tag:h3')
# 遍历元素
for item in items[:-1]:
    # 获取当前<h3>元素下的<a>元素
    lnk = item('tag:a')
    # 打印<a>元素文本和href属性
    print(lnk.text, lnk.link)
```

#### 5.1 get请求

> `get()`方法语法与 requests 的`get()`方法一致，在此基础上增加了连接失败重试功能。与 requests 不一样的是，它不返回`Response`对象，而是返回一个bool值，表示请求是否成功。

示例：请求51游戏指定关键字对应的搜索结果页面

```python
from DrissionPage import SessionPage

page = SessionPage()
url = 'https://game.51.com/search/action/game/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
cookies = {'name': 'value'}
# proxies = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
param = {"q":'传奇'}
page.get(url, headers=headers, cookies=cookies,params=param,proxies=None)
print(page.html,page.title)
```

其他参数：

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/1bdf12361ba74cb08e6d524ad2017081.png#pic_center)

#### 5.2 post请求

请求：中国人事考试网—站内搜索：http://www.cpta.com.cn/category/search.html

```python
from DrissionPage import SessionPage

page = SessionPage()
url = 'http://www.cpta.com.cn/category/search'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
cookies = {'name': 'value'}
# proxies = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}
data = {"keywords":'财务','搜索':'搜索'}
page.post(url, headers=headers, cookies=cookies,data=data,proxies=None)
print(page.html,page.title)
```

> 注意：在get和post请求中，headers中的User-Agent可以不写，因为SessionPage和WebPage在创建页面对象时会自动加载一个ini的配置文件，该配置文件中已经存在了User-Agent。

ini 文件初始内容如下:

```python
......
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

#### 5.3 page对象常用属性

```
url:此属性返回当前访问的 url。
title:此属性返回当前页面title文本。
raw_data:此属性返回访问到的二进制数据，即Response对象的content属性。
html：此属性返回当前页面 html 文本。
json：此属性把返回内容解析成 json。比如请求接口时，若返回内容是 json 格式，用html属性获取的话会得到一个字符串，用此属性获取可将其解析成dict。

```

### 六、🗺️WebPage详解

> WebPage覆盖了ChromiumPage所有功能，并且增加了切换模式功能，创建的标签页对象为MixTab。

```python
from DrissionPage import WebPage

page = WebPage()

page.get('https://gitee.com/login')

# 定位到账号文本框，获取文本框元素
ele = page.ele('#user_login')

# 输入对文本框输入账号
ele.input('你的账号')

# 定位到密码文本框并输入密码
page.ele('#user_password').input('你的密码')

# 点击登录按钮
page.ele('@value=登 录').click()

"""
登录成功后，就可以进行相应的请求发送了
"""
# 模式切换 https://drissionpage.cn/get_start/examples/switch_mode
page.change_mode()

# 获取个人主页的推荐项目
self_page = 'https://gitee.com/muguilin'
page.get(self_page)

# 获取所有行元素
items = page.ele('#popular-pinned-projects').eles('.ui card fluid')
# 遍历获取到的元素
for item in items:
    # 打印元素文本
    # print(item('t:h3').text)
    print(item('.content').text)
    print()
```

### 扩展

#### ⭐下载文件

> DrissionPage 带一个简便易用的下载器，一行即可实现下载功能。

```python
from DrissionPage import SessionPage

url = 'https://www.baidu.com/img/flexible/logo/pc/result.png'
save_path = r'C:\download'

page = SessionPage()
page.download(url, save_path)
```

#### 🥬设置 cookies

[🥦 设置 cookieshttps://drissionpage.cn/tutorials/functions/set\_cookies](https://drissionpage.cn/tutorials/functions/set_cookies)  
**页面对象中设置**

> 任意页面对象都有set.cookies()方法，用于设置 cookies。  
> 该方法接收多种格式的 cookies 信息，可设置一个或多个 cookies。  
> 使用浏览器时，任意页面对象设置的 cookies 是所有标签页共用的（由new\_tab(new\_context=True)创建的标签页除外）。

示例：

```python
from DrissionPage import Chromium

tab = Chromium().latest_tab
cookies = 'name1=value1; name2=value2; path=/; domain=.example.com;'

tab.set.cookies(cookies)
```

**删除 cookies**  
页面对象用set.cookies.remove()和set.cookies.clear()删除和清空 cookies。  
SessionOptions对象用set\_cookies(None)清空 cookies。  
具体用法详见使用文档有关章节。

#### ❓ 常见问题

❔ 如何禁用保存密码、恢复页面等提示气泡？  
浏览器提示气泡出现时可以手动关闭，不关闭也不影响自动操作，在代码中阻止其显示也是可以的。 加一些浏览器配置代码即可禁止相应的气泡显示，需要添加下面这样的代码：

```python
co = ChromiumOptions()

# 阻止“自动保存密码”的提示气泡
co.set_pref('credentials_enable_service', False)

# 阻止“要恢复页面吗？Chrome未正确关闭”的提示气泡
co.set_argument('--hide-crash-restore-bubble')
```

❔ 如何使用启动参数、用户配置、实验项等功能？  
**arguments 启动参数**

*   使用参考：http://DrissionPage.cn/ChromiumPage/browser\_opt#-set\_argument
    
*   参数详见：https://peter.sh/experiments/chromium-command-line-switches/  
    **prefs 用户配置**
    
*   使用参考：http://DrissionPage.cn/ChromiumPage/browser\_opt#-set\_pref
    
*   参数详见：https://src.chromium.org/viewvc/chrome/trunk/src/chrome/common/pref\_names.cc  
    **flags 实验项**
    
*   使用参考：http://DrissionPage.cn/ChromiumPage/browser\_opt#-set\_flag
    
*   参数详见：chrome://flags
    

**🚀更多常见问题[https://drissionpage.cn/tutorials/QandA](https://drissionpage.cn/tutorials/QandA)**

本文转自 <https://blog.csdn.net/muguli2008/article/details/146488116>，如有侵权，请联系删除。