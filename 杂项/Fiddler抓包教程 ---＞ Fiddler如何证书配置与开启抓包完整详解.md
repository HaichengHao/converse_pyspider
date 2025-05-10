 

一、安装fiddler和配置证书
----------------

**`fiddler`**默认是只抓取**`http`**协议, 如下图

如果**`会话列表`**中的`Host`列中出现**`Tunnel to...`**字样都说明是`证书`的问题, 这种就不能抓取到我们想要的`会话`

要想抓https协议，需要配置一下

操作方法如下:

执行菜单栏中的：`Tools---->Options---->HTTPS`然后勾选`Decrypt HTTPS traffic(解密HTTPS流量)`

然后会弹出一个`对话框` 直接点击`YES`即可!

`注意`

你是第一次安装的**`Fiddler`**那么正常情况下会弹出`证书安装`的相关提示!

如果没有弹出提示，那么久勾选`Actions---> Trust Root Certificate(信任根证书)`

![](https://i-blog.csdnimg.cn/blog_migrate/0e428fe3c9872cda28a7a2dcd12b4ed8.png)

接下来弹出这个对话框 全部点击**`是`** 即可 

![](https://i-blog.csdnimg.cn/blog_migrate/5077329fe0885e730d47cdf499358ce1.png)

安装证书步骤图1

![](https://i-blog.csdnimg.cn/blog_migrate/de769ae5dd1ae406905237b81df3191c.png)

安装证书步骤图2

![](https://i-blog.csdnimg.cn/blog_migrate/2210a439e954ade0011c07210b072a5f.png)

安装证书步骤图3

![](https://i-blog.csdnimg.cn/blog_migrate/349920662eafe5b62d5b2b31c98b4b08.png)

安装证书步骤图4

![](https://i-blog.csdnimg.cn/blog_migrate/45509cd2d2f006ee5fc6d56ba7530e3e.png)

安装证书步骤图5

然后弹出`**Added Fiddler's root certificate to the Machine Root list**(将Fiddler的证书添加到机器根目录列表中)` 点击确定

最后把下面的:

`Ignore server certificate errors(unsafe)忽略服务器证书错误（不安全）`

`check for certificate revocation (证书撤销检查)`

这两个选项也**勾选上**!

`如图`

![](https://i-blog.csdnimg.cn/blog_migrate/1c89818fd8374e0447739e415ca2b170.png)

现在**`证书`**也已经安装到`Fiddler`上了, 我们可以从`Actions`中选择Open Windows Certificate Manager这一个选项, 打开`打开Windows证书管理器`去查看

如下图

按图中所示，Tools–>Options–>HTTPS–>Actions,找到证书的管理项

![](https://i-blog.csdnimg.cn/blog_migrate/326be6e90d4b8c269f713e07611dc3fb.png)

![](https://i-blog.csdnimg.cn/blog_migrate/7df2a1edfa5838be59624c2e5ae7f5bc.png)

打开**`打开Windows证书管理器`** 之后点击菜单栏上的 `操作--->查找证书`然后输入`Fiddler` 就会查找出证书了

如果没有说明没有安装成功!

![](https://i-blog.csdnimg.cn/blog_migrate/3255541e8cdbfae825b3c3ed6d71ee20.gif)

证书名为**`DO_NOT_TRUST_FiddlerRoot`**

![](https://i-blog.csdnimg.cn/blog_migrate/2dab8f3d3d1a5eef36d702663ec956b5.png)

信任证书

证书安装了之后 还要设置一下信任才行!

直接选择**`Tools--->Options---->HTTPS---->Actions--->Trust Root Certificate`**

![](https://i-blog.csdnimg.cn/blog_migrate/283da57bc9934908c531e6de37caf767.png)

在接下来弹出的对话框中直接点击`确定`或`yes`就行了!

![](https://i-blog.csdnimg.cn/blog_migrate/d6dcd66d09be68bb4e32932ca247efd8.png)

**`注意`**

如果还是不行，那么最好重置一下证书 在`Actions`中选择`Reset All Certificates(**重置所有证书**)` 然后点击确定删除`Fiddler`所配置的证书,最后重新执行之前的步骤就可以了!

`如图`

![](https://i-blog.csdnimg.cn/blog_migrate/5753aa2590dfd7e00fef26127a36c591.png)

**`小提示`**

我们在`Skip Decryption`中输入`ip地址`或者`域名`可以用来`跳过`该`主机`或`域名`的`https数据抓取`

![](https://i-blog.csdnimg.cn/blog_migrate/a3cc96b6214c477494525a2e9ee03a9e.png)

二、设置fiddler connections的值，允许fiddler远程连接
---------------------------------------

第一步：在fiddler菜单项选择Tools  ->  Options -> connections

第二步：勾选【|Allow remote computers to connect】

第三步：点击【ok】

![](https://i-blog.csdnimg.cn/blog_migrate/1e80dcb01b29abe3fc4eadd170b7c99f.png)

**然后重新启动（重要！！！！！！！！！！！！！！）**

**三、在手机上进行相应的设置，为手机[抓包](https://so.csdn.net/so/search?q=%E6%8A%93%E5%8C%85&spm=1001.2101.3001.7020 "抓包")做准备**
-------------------------------------------------------------------------------------------------------------

#### 1、查看本机ip

方法一：电脑——左下角点击Windows图标（或者同时按下Windows图标+r键）——输入cmd，打开cmd面板，输入：ipconfig ，查看本机IP地址

方法二：在fiddler主界面，将鼠标移到【online】上面，就可以查看本地的IP地址了，如果你的fiddler没有显示【online】，可以通过【fiddler菜单——View——Show Toolbar】将【Show Toolbar】勾选中，就会显示【Online】信息了。

![](https://i-blog.csdnimg.cn/blog_migrate/38b2a8adbdd98e3e8bfb0f07a5fa64f7.png)

#### 2、手机安装证书。（ios设置和Android设置基本一样）

前提条件：

手机和电脑要处于同一网络条件下（可以理解为：使用同一个WiFi）

fiddler的默认端口是：8888，根据需要进行修改，使用默认的就可以。

一个手机可以安装多个证书，但是每安装的一个证书里面都设置有IP地址，所以：安装的证书和电脑IP是一一对应的，当前的这个证书只能针对某一台电脑使用，更换电脑后，该证书将不能使用，只能重新安装与更换的电脑的IP相同的证书才能使用。

#### **第一步：**手机下载证书。打开手机的浏览器，输入：【IP:8888】下载证书。

（注：中间的冒号一定要使用英文的冒号，中文的冒号是错误的）  
 

 ![](https://i-blog.csdnimg.cn/blog_migrate/961549a252b6d4f1364cd197d0c5f97b.png)

#### 如果上面都设置了，并且ip和端口都正确，但出现无法打开下载页面，可能时防火墙的原因

**可能的解决办法**：允许应用通过防火墙中是否已勾选允许fiddler通过防火墙，如没有请将fiddler添加允许通过防火墙，若在列表中没有找到fiddler请点击更改设置再次点击允许其他应用找到fiddler的安装位置将fiddler添加进去

![](https://i-blog.csdnimg.cn/blog_migrate/9bc7fb3b737df87b384b2f4512d7df15.png)

添加fiddler安装路径下的exe文件

![](https://i-blog.csdnimg.cn/blog_migrate/9dbc3b0b41b4ed29090f11d627df416c.png) 

#### 第二步：安装证书.

 有的手机可以直接点击已下载的文件进行安装，有的手机则不行。

如果不能直接安装证书，我们可以通过以下方法来安装证书。

1.Android：安装证书。由于安装系统众多，设置的方法不尽相同，下面几个方法以供参考。

方法一：手机——设置——搜索【证书】二字——选择：安装证书或者证书管理：点击安装证书，在你的众多文件里面去选择刚刚下载的fiddler的证书，点击安装

（注：选择安装的文件后，需要输入手机的锁屏密码。Android一定要有锁屏密码才能安装证书）

![](https://i-blog.csdnimg.cn/blog_migrate/bc4335284fd76737c213373f06958191.png)

方法二**：在浏览器里面，直接打开已经下载的文件，安装即可，安装步骤是：先输入手机锁屏密码——后到上图为证书命名界面**。

证书安装好后，查看已信任证书：具体位置在【安全——更多安全设置——加密和凭据——受信任的凭据】

#### **第三步：为手机设置代理**

设置——无线网络（WLAN）——WLAN——长按已连接的WiFi 去修改网络——在高级选项里面——选择【手动代理】——出现以下界面，按图所示操作即可。

（或者长按通知栏WiFi按钮进入WiFi界面）

![](https://i-blog.csdnimg.cn/blog_migrate/c7d76b488ed32e1ec6ae8dfed847d936.png)

#### 第四步：访问手机浏览器或者任一应用就可以在fiddler里面查看到抓取的请求了

![](https://i-blog.csdnimg.cn/blog_migrate/4b93e31c257e54d3d1b9ebea8d24b332.png)

本文转自 <https://blog.csdn.net/qq_37888591/article/details/126763558>，如有侵权，请联系删除。