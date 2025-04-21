 

前言
--

> 利用 **Selenium** 获取已经打开的浏览器窗口，全python操作

| 标题 | 链接 |
| --- | --- |
| [**【Selenium】控制当前已经打开的 chrome浏览器窗口**](https://blog.csdn.net/weixin_45081575/article/details/112621581) | https://blog.csdn.net/weixin\_45081575/article/details/112621581 |
| [**【Selenium】控制当前已经打开的 chrome浏览器窗口（高级篇）**](https://blog.csdn.net/weixin_45081575/article/details/126389273) | https://blog.csdn.net/weixin\_45081575/article/details/126389273 |

不同的是，本次全是用python来进行操作，省去了手动打开浏览器的操作，也相当于是节省了一点点功夫。与上一篇有异曲同工之妙。

这里使用 **chrome浏览器** 来做示例。

整个下来主要有两个步骤，

1.  手动打开浏览器，
2.  使用 **Python程序** 去获取到手动打开的 **chrome浏览器**。

应用场景(理论上)
---------

1.  登录账号并且需要输入手机验证码的网站；
2.  登录账号并且需要人机验证的网站(如图片点选、文字点选等人机验证；
3.  …

### 1\. 查看浏览器信息

在 chrome浏览器的地址栏中输入 `chrome://version`，如下图所示

![](https://i-blog.csdnimg.cn/blog_migrate/8ff615670692b1df42f520e3cc0b1b16.png)

`C:\Program Files\Google\Chrome\Application\chrome.exe` 这个是chrome 可执行路径。`mark`下来有用。

### 2\. 代码释义

在cmd命令行窗口输入以下指令

*   **start chrome**：从命令行启动 chrome 应用程序
*   释义：以调试模式打开浏览器，端口为`9527`，存放文件配置路径在`F:\selenium`(会自动创建)

```bash
start chrome --remote-debugging-port=9527 --user-data-dir="F:\selenium"
```

看以下动图  
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/f97d9a5853c6af03dbcb6e775963fe9e.gif)

### 3\. Python执行cmd命令

在Python的内置库中，os 和 [subprocess](https://so.csdn.net/so/search?q=subprocess&spm=1001.2101.3001.7020) 可以执行**cmd命令**（还有其它的，暂不表）

下面来展示他们的用法。

os模块是Python 自带的一个操作系统接口模块，详见 [OS模块介绍](https://docs.python.org/zh-cn/3.9/library/os.html)。

在这里主要用到它的 os.popen 命令，  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/9b7edad90ff796d8ca832b2d374fe800.png)

**代码如下**

*   使用`os.popen`即可执行cmd命令~（`os.popen`包装了`sunprocess.Popen`方法）

```python
import os
os.popen('start chrome --remote-debugging-port=9527 --user-data-dir="F:\selenium"')
```

看以下动图~  
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/ec6246f864954c245c41f0f451b46049.gif)

以下代码都可以调用cmd命令，效果基本上是一致的。想选用哪个就先实践一番，再做决定吧~

#### os.popen

```python
import os

# 方法一
os.popen(r'start chrome.exe --remote-debugging-port=9527 --user-data-dir="F:\selenium\"')

# 方法二
# 先切换到chrome的可执行文件路径，再执行cmd命令。注意这里没有 start
os.chdir(r"C:\Program Files\Google\Chrome\Application")
os.popen('chrome --remote-debugging-port=9527 --user-data-dir="F:\selenium"')
```

#### os.system

```python
import os

# 方法一
os.system(r'start chrome --remote-debugging-port=9527 --user-data-dir="F:\selenium"')

# 方法二
# 先切换到chrome的可执行文件路径，再执行cmd命令。注意这里没有 start
os.chdir(r"C:\Program Files\Google\Chrome\Application")
os.system(r'chrome --remote-debugging-port=9527 --user-data-dir="F:\selenium"')
```

#### subprocess.Popen

```python
import os
import subprocess

# 先切换到chrome可执行文件的路径
os.chdir(r"C:\Program Files\Google\Chrome\Application")
# 然后使用Popen执行cmd命令，这里的chrome.exe 可替换为 chrome，注意这里没有 start
subprocess.Popen('chrome.exe --remote-debugging-port=9527 --user-data-dir="F:\selenium"')
```

### 4\. Selenium的一些基础

> 这里我们来看看，怎么通过Selenium去接管已经打开的 chrome。  
> 这些都是基于 [**Chrome DevTools Protocol**](https://chromedevtools.github.io/devtools-protocol/)，感兴趣的可以深入去学习了解。

* * *

**示例代码**

```python
from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get('https://www.csdn.net/')
    # 获取远程链接的地址
    print('remote_url:', browser.caps['goog:chromeOptions']['debuggerAddress'])
    print('session_id:', browser.session_id)
    print(browser.title)

```

用调试模式执行以上代码，看到下图

*   **`{'debuggerAddress': 'localhost:64829'}`** ，，，这是关键所在，贯穿全文。

![](https://i-blog.csdnimg.cn/blog_migrate/9a3ea19470be7010eb76414baee847c8.png)

其中，需要关心的是 `debuggerAddress` 参数，将它填充到下面的`Url` 中

*   注意填充的内容需要是你当前 `Selenium 的 localhost:port`，不是我这个！！！

| 填充前 | 填充后 | 作用(表达可能有误，但大体如此) |
| --- | --- | --- |
| http://`{localhost:port}`/json | `http://localhost:64829/json` | 查看当前窗口的页面连接 |
| http://`{localhost:port}`/json/version | `http://localhost:64829/json/version` | 查看窗口远程链接 |

* * *

#### 远程调试

访问 `http://localhost:64829/json/`，如下图所示，

![](https://i-blog.csdnimg.cn/blog_migrate/5aba43549e423cd6a1597cdabd3521e8.png)  
\*\*\*\*\*  
点击 `devtoolsFrontendUrl(开发工具前端Url)`，可以到调试界面，这个可以用作于远程调试。暂不表~  
![](https://i-blog.csdnimg.cn/blog_migrate/1a340f5e5d56a3fdaaaf5a38650df4fa.gif)

* * *

#### 获取远程链接

接下来使用浏览器访问该Url： `http://localhost:64829/json/version` ，如下图所示

*   圈出来的`webSocketDebuggerUrl(调试器Url)`，是远程链接的地址，若使用 **puppeteer**的话能用到

![](https://i-blog.csdnimg.cn/blog_migrate/0fc16f1b30419ab366f0080d54491655.png)

### 5\. Python程序接管 已打开的浏览器

**代码** ：

*   这里的端口号需要修改成与上面`debuggerAddress`一致

```python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 以下代码是使用 Python 接管已经打开的浏览器
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:64829")
browser = webdriver.Chrome(options=options)

browser.get('https://www.bilibili.com/')
print(browser.title)	# 哔哩哔哩 (゜-゜)つロ 干杯~-bilibili

```

代码运行后，可以看到如下：已经将 csdn 修改成 bilibili ，且访问成功了

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/a13500fce810ca47fb959a1ac960d513.gif)  
以上，只是为了说明\*\*\*（其实不知道说明了什么）  
下面将使用 Python去进行上述的全部操作，即控制已经打开的浏览器。

#### 实例

> 譬如，我这里需要登录CSDN，然后再使用Selenium去接管chrome

**代码如下：**

*   中间加入的 `input` 乃是精髓，直到你完成登录操作后，再去手动触发后面的程序 执行。

```python
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    os.system(r'start chrome --remote-debugging-port=9527 --user-data-dir="F:\selenium"')
	
	# 此乃精髓
    input('输入空格继续程序...')
	
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    browser = webdriver.Chrome(options=options)

    print(browser.title)
    print()

	# 这里是你的其它逻辑
	"""获取粉丝数量
	   获取所有新增文章
	   获取所有文章的观看数量
	"""

```

运行之后可以看到，  
浏览器窗口请求了新的 **URL(https://www.bilibili.com)**，并且获取到了当前页面的 **title**和运行其它逻辑(`如果有的话~`)

![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/244cd951d3acad28db60d26f4d9e1e57.gif)

### 6\. 总结

调用我的代码，直接运行即可控制当前浏览器窗口。

* * *

后话
--

自己动手操作一番，岂不美哉？  
**See you🎈🎈**

本文转自 <https://blog.csdn.net/weixin_45081575/article/details/126389273>，如有侵权，请联系删除。