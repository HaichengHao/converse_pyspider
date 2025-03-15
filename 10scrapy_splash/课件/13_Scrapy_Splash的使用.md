# Scrapy_splash模块使用

## 一. Splash

后续的爬虫的课程. 随便随时来听.  -- 樵夫说的. 

splash是一个可以动态渲染js的工具. 有助于我们完成复杂的js内容加载工作.  你可以理解为另一个没有界面的selenium.

### 1.1 splash安装

splash的安装过程十分复杂. 复杂到官方都不推荐你去手动安装它. 

官方建议. 用docker去安装splash. 所以. 你需要先去安装docker. 但是docker这玩意在windows上支持非常不好. 各种各样的问题. 外加上后期我们要把爬虫部署到linux. 那干脆. 我们就安装一个linux. 在linux上搞docker是非常easy的. 

有能力, 不怕苦的同学可以在windows上搞一个docker试试. 我这里就不带你们找坑踩了. 直接上Linux. 

#### 1.1.1安装VM

![17561629196138_.pic_hd](17561629196138_.pic_hd.jpg)

![17561629196138_.pic](17561629196138_.pic.jpg)

![17581629196184_.pic](17581629196184_.pic.jpg)

![17571629196155_.pic](17571629196155_.pic-9199960.jpg)

![17581629196184_.pic](17581629196184_.pic-9199973.jpg)

![17591629196208_.pic](17591629196208_.pic.jpg)

![17601629196228_.pic](17601629196228_.pic.jpg)

![17611629196237_.pic](17611629196237_.pic.jpg)

![17621629196250_.pic_hd](17621629196250_.pic_hd.jpg)

![17631629196343_.pic_hd](17631629196343_.pic_hd.jpg)

![17641629196362_.pic_hd](17641629196362_.pic_hd.jpg)

![17651629196369_.pic_hd](17651629196369_.pic_hd.jpg)

![17661629196398_.pic_hd](17661629196398_.pic_hd.jpg)

![17671629196461_.pic_hd](17671629196461_.pic_hd.jpg)

![17681629196491_.pic_hd](17681629196491_.pic_hd.jpg)

![17691629196532_.pic_hd](17691629196532_.pic_hd.jpg)

![17701629196571_.pic_hd](17701629196571_.pic_hd.jpg)

![17711629196622_.pic_hd](17711629196622_.pic_hd.jpg)

![17721629196663_.pic_hd](17721629196663_.pic_hd.jpg)

![17731629196679_.pic_hd](17731629196679_.pic_hd.jpg)



#### 1.1.2 安装Linux

<img src="image-20210817140222006.png" alt="image-20210817140222006" style="zoom:50%;" />

<img src="image-20210817140422074.png" alt="image-20210817140422074" style="zoom:40%;" />

<img src="image-20210817140631614.png" alt="image-20210817140631614" style="zoom:40%;" />

<img src="image-20210817140748141.png" alt="image-20210817140748141" style="zoom:40%;" />

<img src="image-20210817140818074.png" alt="image-20210817140818074" style="zoom:40%;" />

<img src="image-20210817140849908.png" alt="image-20210817140849908" style="zoom:40%;" />

<img src="image-20210817140925752.png" alt="image-20210817140925752" style="zoom:40%;" />

<img src="image-20210817141200195.png" alt="image-20210817141200195" style="zoom:50%;" />

<img src="image-20210817141307223.png" alt="image-20210817141307223" style="zoom:50%;" />

<img src="image-20210817141415716.png" alt="image-20210817141415716" style="zoom:40%;" />

<img src="image-20210817141552531.png" alt="image-20210817141552531" style="zoom:40%;" />

<img src="image-20210817141643259.png" alt="image-20210817141643259" style="zoom:40%;" />

<img src="image-20210817141729496.png" alt="image-20210817141729496" style="zoom:40%;" />

<img src="image-20210817141824889.png" alt="image-20210817141824889" style="zoom:40%;" />

<img src="image-20210817141850749.png" alt="image-20210817141850749" style="zoom:40%;" />

<img src="image-20210817142347367.png" alt="image-20210817142347367" style="zoom:40%;" />

<img src="image-20210817142421655.png" alt="image-20210817142421655" style="zoom:50%;" />

<img src="image-20210817142519453.png" alt="image-20210817142519453" style="zoom:40%;" />

<img src="image-20210817142634663.png" alt="image-20210817142634663" style="zoom:40%;" />

安装好的linux后,我们需要学会使用linux的一个工具. 叫yum, 我们需要用它来帮我们完成各种软件的安装. 十分的方便. 我们先用`ifconfig`来做一个测试. 

```
yum search ifconfig   // 搜索出ifconfig的包

yum install net-tools.x86_64  // 安装该软件, 安装过程中会出现很多个询问. 直接y即可
```

发现了吧, 在linux这个破黑窗口里. 属实难受+憋屈. 所以, 我们这里选择用ssh远程连接linux. 

mac版本:  打开终端. 输入

```shell
ssh root@服务器ip地址
输入密码
```

就可以顺利的链接到你的linux服务器. 接下来. 我们可以使用各种命令来操纵linux了. 

Windows: 

![17751629199547_.pic_hd](17751629199547_.pic_hd.jpg)

![17791629200276_.pic_hd](17791629200276_.pic_hd.jpg)

![17761629199585_.pic_hd](17761629199585_.pic_hd.jpg)

![17771629199596_.pic_hd](17771629199596_.pic_hd.jpg)

![17781629199688_.pic_hd](17781629199688_.pic_hd.jpg)

#### 1.1.3 安装docker

​	安装docker就一条例命令就好了

```shell
[root@sylar-centos-2 ~]# yum install docker
```

​	配置docker的源. 

```shell
[root@sylar-centos-2 ~]# vi /etc/docker/daemon.json
# 写入一下内容, 注意.先按'i', 更换为输入模式. 然后再填写内容
{
	"registry-mirrors": ["https://registry.docker-cn.com/"]
}
# 保存: 先按esc. 退出输入模式, 然后输入":wq" 表示写入, 退出. 就完事儿了
```

```shell
[root@sylar-centos-2 ~]# systemctl start docker    # 启动docker
```

```shell
[root@sylar-centos-2 ~]# docker ps      # 查看docker运行状态
```

如需关闭或者重新启动docker:

```shell
systemctl stop docker   # 停止docker服务
systemctl restart docker  # 重启docker服务
```



Vm -> cenos -> ssh -> docker -> splash 

#### 1.1.4 安装splash

1. 拉取splash镜像

    ```shell
    docker pull scrapinghub/splash
    ```

    splash比较大. 大概2个G左右. 有点儿耐心等会儿就好了

2. 运行splash

    ```shell
    docker run -p 8050:8050 scrapinghub/splash
    ```

3. 打开浏览器访问splash

    http://192.168.31.82:8050/

    ![image-20210817153337076](image-20210817153337076.png)

    

### 1.2 splash简单使用

​	我们可以在文本框内输入百度的网址. 然后点击render. 可以看到splash会对我们的网页进行动态的加载. 并返回截图. 运行状况. 以及页面代码(经过js渲染后的)

![image-20210817153704882](image-20210817153704882.png)

![image-20210817153711026](image-20210817153711026.png)

快速解释一下, script中的脚本. 这里面用的是lua的脚本语法. 所以看起来会有些难受. 

```lua
function main(splash, args)  -- 主函数
  assert(splash:go(args.url))  -- 进入xxx页面
  assert(splash:wait(0.5))   -- 等待0.5秒
  return {  -- 返回
    html = splash:html(),  -- splash:html() 页面源代码
    png = splash:png(),   -- splash:png() 页面截图
    har = splash:har(),   -- splash:har() 页面加载过程
  }
end   -- 函数结束
```

有必要说明一下. 在lua中, `.`表示的是属性(变量), `:`表示的是方法(函数)的调用. 

常见操作符都一样. 剩下的. 我们到案例里看. 

### 1.3 splash的http-api接口

splash提供了对外的http-api接口. 我们可以像访问一个普通url一样访问splash. 并由splash帮助我们渲染好页面内容. 

```python
http://192.168.31.82:8050/render.html?url=http://www.baidu.com
```

虽然看不出任何差别. 但是你心里要清楚一个事情. 此时拿到的直接是经过js渲染后的html

我们换个url你就知道了

```python
http://192.168.31.82:8050/render.html?url=https://www.endata.com.cn/BoxOffice/BO/Year/index.html&wait=5
```

endata这个网站. 它的数据是后期经过ajax请求二次加载进来的. 我们通过splash可以等待它后期加载完再拿html. 

综上, splash的工作机制:

![image-20210817155156714](image-20210817155156714.png)

整个一个代理服务器的逻辑. ~~~~



## 二. python中使用splash

### 2.1 splash在python中如何使用

既然splash提供了http-api接口. 那我们就可以像请求普通网站一样去请求到splash. 
在python中, 我们最熟悉的能发送http请求的东西就是requests了. 

接下来.我们就用requests来完成splash的对接. 

```python
import requests
"""
# splash提供的api接口
渲染html的接口
http://192.168.31.184:8050/render.html?url=你的url&wait=等待时间&time_out=超时时间

截图的接口
http://192.168.31.184:8050/render.png  参数和render.html基本一致, 可选width, height

加载过程接口
http://192.168.31.184:8050/render.har  参数和render.html基本一致

json接口
http://192.168.31.184:8050/render.json  参数和render.html基本一致

执行lua脚本的接口
http://192.168.31.184:8050/execute?lua_source=你要执行的lua脚本
"""

# 最简单的调用splash的render.html
url = "http://192.168.31.184:8050/render.html?url=https://www.baidu.com&wait=5"
resp = requests.get(url)
print(resp.text)
```



### 2.2 我们以网易新闻首页`要闻`为例. 

先搞定脚本部分.

```lua
function main(splash, args)
    assert(splash:go(args.url))
    assert(splash:wait(1))
    -- 加载一段js, 后面作为lua函数进行调用. 
    -- 在这个脚本中, 主要返回了"加载更多"按钮的状态
    get_display_style = splash:jsfunc([[
      function(){
        return document.getElementsByClassName('load_more_btn')[0].style.display;
      }
    ]])
    -- lua中的循环语句. 和python的while功能一样. 
    while (true)
    do  -- 语法规定. 相当于开始
        -- 直接运行js代码, 滚动到'加载更多'按钮
        splash:runjs("document.getElementsByClassName('load_more_btn')[0].scrollIntoView(true)")
        -- 等待
        splash:wait(1)
        -- 找到该按钮. 点击它
        splash:select(".load_more_btn").click()
        -- 调用上方预制的js脚本, 获取'正在加载按钮'的状态
        display_style = get_display_style()
        -- 如果不显示了. 也就结束了
        if(display_style== 'none')
        then
            break  -- 同python中的break. 打断循环
        end
    end
    assert(splash:wait(2)) -- 不在乎多等2秒
    return {
        html = splash:html(),
        png = splash:png(),
        har = splash:har(),
    }
end
```

到了python里面就可以使用这个脚本了

```python
# 执行lua脚本
lua = """
function main(splash, args)
    assert(splash:go(args.url))
    assert(splash:wait(0.5))
    -- 加载一段js, 后面作为lua函数进行调用. 
    -- 在这个脚本中, 主要返回了"加载更多"按钮的状态
    get_display_style = splash:jsfunc([[
      function(){
        return document.getElementsByClassName('load_more_btn')[0].style.display;
      }
    ]])
    -- lua中的循环语句. 和python的while功能一样. 
    while (true)
    do  -- 语法规定. 相当于开始
        -- 直接运行js代码, 滚动到'加载更多'按钮
        splash:runjs("document.getElementsByClassName('load_more_btn')[0].scrollIntoView(true)")
        -- 等待
        splash:wait(1)
        -- 找到该按钮. 点击它
        splash:select(".load_more_btn").click()
        -- 调用上方预制的js脚本, 获取'正在加载按钮'的状态
        display_style = get_display_style()
        -- 如果不显示了. 也就结束了
        if(display_style== 'none')
        then
            break  -- 同python中的break. 打断循环
        end
    end
    assert(splash:wait(2)) -- 不在乎多等2秒
    return {
        html = splash:html(),    -- 拿到页面源代码
        cookies = splash:get_cookies()  -- 拿到cookies
    }
end
"""


# 准备能够执行lua脚本的url  -> splash服务地址
url = "http://192.168.31.82:8050/execute"

from lxml import etree

# 远程访问splash, 执行脚本
resp = requests.get(url, params={
    "url":"https://news.163.com",
    "lua_source": lua
})

result = resp.json()

# 提取结果
tree = etree.HTML(result.get('html'))
# print(resp.text)
divs = tree.xpath("//ul[@class='newsdata_list fixed_bar_padding noloading']/li[1]/div[2]/div")

for div in divs:
    a = div.xpath("./div/div/h3/a")
    if not a:
        continue
    a = a[0]
    href = a.xpath('./@href')
    title = a.xpath('./text()')

    print(title, href)

print(result.get("cookies"))

```



##三. scrapy_splash

安装scrapy_splash模块

```python
pip install scrapy_splash
```

创建一个普通的scrapy项目, 然后把scrapy_splash配置到settings文件中

```python
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# scrapy_splash
# 渲染服务的url, 这里换成你自己的
SPLASH_URL = 'http://192.168.31.82:8050'
# 下载器中间件, 这个必须要配置
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# 这个可由可无
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }
# 去重过滤器, 这个必须要配置
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# 使用Splash的Http缓存, 这个必须要配置
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

```

最后. 整理修改一下spider

```python
import scrapy
from scrapy_splash.request import SplashRequest


# splash的lua脚本
lua_source = """
function main(splash, args)  -- 主函数
    assert(splash:go("https://news.163.com/"))  -- 访问url
    assert(splash:wait(2))  -- 等待
    -- 预存一个js函数
    get_btn_display = splash:jsfunc([[
        function(){
            return document.getElementsByClassName('load_more_btn')[0].style.display;
        }
    ]])
    -- lua的while循环
    while(true)
    do
        -- 直接执行一个js脚本
        -- 向下拉动滚动条. 
        splash:runjs("document.getElementsByClassName('load_more_btn')[0].scrollIntoView(true)")
        assert(splash:wait(1))
        -- 选择 "加载更多"
        btn = splash:select(".load_more_btn")
        -- 点它
        btn:click()
        -- 判断是否可见 调用上方预制的js函数
        ss = get_btn_display()
        -- 如果是none. 就没有数据了(网易自己设计的)
        if (ss == 'none')
        then
            break
        end
    end
    return {
        html = splash:html(),
        cookies = splash:get_cookies()
    }
    end
"""


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['163.com']
    start_urls = ['http://news.163.com/']

    def start_requests(self):
        # 发送splash请求
        yield SplashRequest(
            url=self.start_urls[0],
            callback=self.parse,
            endpoint="execute",
            args={"lua_source": lua_source, }
        )

    def parse(self, resp, **kwargs):
        divs = resp.xpath("//ul[@class='newsdata_list fixed_bar_padding noloading']/li[1]/div[2]/div")
        for div in divs:
            a = div.xpath("./div/div/h3/a")
            if not a:
                continue

            href = a.xpath('./@href').extract_first()
            title = a.xpath('./text()').extract_first()
            print(href)
            # 可以采用正常的抓取方案
            yield scrapy.Request(
                url=href,
                callback=self.details
            )

            break

    def details(self, resp):
        with open("data.txt", mode='w') as f:
            f.write("____".join(resp.xpath("//div[@class='post_body']//p/text()").extract()))

```