 

转自公众号  ： Hacking黑白红

0x00  常用[抓包工具](https://so.csdn.net/so/search?q=%E6%8A%93%E5%8C%85%E5%B7%A5%E5%85%B7&spm=1001.2101.3001.7020)特点

     常用的抓包工具有fiddler、[wireshark](https://so.csdn.net/so/search?q=wireshark&spm=1001.2101.3001.7020)、httpwatch、 firebug、F12/等。抓包抓的是协议，fiddler抓的是HTTP、HTTPS协议，wireshark抓的是其他协议。fiddler、wireshark可以修改接口的参数和返回值，常用的F12调试工具只可以查看接口的参数和响应值。

*   fiddler最适合，在APP测试的时候抓包；
    
*   wireshare适合对整个流量进行抓取；
    
*   burpsuite最大的特点是抓包改包
    

0x01  Fiddler原理

     Fiddler是以代理WEB服务器的形式工作的,浏览器与服务器之间通过建立TCP连接以HTTP协议进行通信，浏览器默认通过自己发送HTTP请求到服务器，它使用代理地址:127.0.0.1, 端口:8888. 当Fiddler开启会自动设置代理， 退出的时候它会自动注销代理，这样就不会影响别的程序。不过如果Fiddler非正常退出，这时候因为Fiddler没有自动注销，会造成网页无法访问。解决的办法是重新启动下Fiddler.

![图片](https://i-blog.csdnimg.cn/blog_migrate/62effc5f053e6f2d94b80fd1b4a619e5.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/70b646261fcd04a93b089902ed410760.png)

0X02 安装应用

**1.下载最新版Fiddler,强烈建议在官网下载：**https://www.telerik.com/download/fiddler

![图片](https://i-blog.csdnimg.cn/blog_migrate/a9a55de435133c19b2522f4472b278c2.png)

**2\. 正常傻瓜式安装，**

下一步，下一步，安装完毕后，先不用急于打开软件。

**3.下载并安装Fiddler证书生成器：**

http://www.telerik.com/docs/default-source/fiddler/addons/fiddlercertmaker.exe?sfvrsn=2

**4.打开Fiddler进行设置**

点击工具栏中的Tools—>Options

![图片](https://i-blog.csdnimg.cn/blog_migrate/679693b3327339308d25e9a52724483d.png)

 **5、点击HTTPS，**勾选Decrypt HTTPS traffic和Ignore server certificate(unsafe)

![图片](https://i-blog.csdnimg.cn/blog_migrate/0467c77db5829a5de025c49a7022786e.png)

 **6、点击Actions**，点击Export Root Certificate to Desktop 

![图片](https://i-blog.csdnimg.cn/blog_migrate/9d3ea6f77047b5e316914a87834b8b53.png)

 【注】此时电脑上会生成 一个证书

![图片](https://i-blog.csdnimg.cn/blog_migrate/af6dc65ada13f403338aced10b7800a3.png)

**7、https设置及connections设置，勾选选择项**

![图片](https://i-blog.csdnimg.cn/blog_migrate/36c67abbe918ad54f2076b499f89ec05.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/5f12c83431b3824b08384aa5549e156d.png)

 **8、安装雷电模拟器  https://www.ldmnq.com/**

![图片](https://i-blog.csdnimg.cn/blog_migrate/7e8a387355a1fe85cdb0ab845f329f5a.png)

**9、安装好后，桌面双击打开雷电模拟器，点击设置**

![图片](https://i-blog.csdnimg.cn/blog_migrate/3b6727cc8f287bcfbf6509351f8e1d0f.png)

 **10、安装好后，桌面双击打开雷电模拟器，点击设置**

![图片](https://i-blog.csdnimg.cn/blog_migrate/c58917a066cd44a92a68cc30c1508eb0.png)

 **11、选择网络设置，勾选桥接模式，点击安装驱动，点击确定，点击保存设置**

![图片](https://i-blog.csdnimg.cn/blog_migrate/2239dd096b31e3371820b9e6418638c3.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/09a5d4fb93108ae546582342f95c3a98.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/633f3eb08aa3b4b9447f3e5751637ef4.png)

 12、打开模拟器，设置代理。找到系统应用，点击设置，点击无线网络WLAN—>左键常按点击已连接网络—>修改网络

![图片](https://i-blog.csdnimg.cn/blog_migrate/4c7a0352364581cffe1557ad30dca8ae.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/d9bba2f2198f04b5241187d0edd5c5c7.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/36a0d0446d95047fccd5b5b1f9d48fc6.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/a9dddc7e0ad621e553c5d3bc0ed5fbca.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/e15fca23c19dafa058920b991a52fced.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/50e44c5225667daf299b19afd6f55f4b.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/da5bb6be5217145725ed265d3793a374.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/a1892980100170783e769c0902c75fae.png)

**13、将步骤6导出的证书FiddlerRoot.cer文件导入至模拟器**

![图片](https://i-blog.csdnimg.cn/blog_migrate/15822c5179403fe1089a1c256618179f.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/3a066576e197712ec34e4191ce13bff8.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/4f9c2ff51dc010f9e05e99c4e288fc39.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/76749dc2e2c08160d05d291dd7a0bd22.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/9b529bc84ef12bddc329733421533d9c.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/f00594078e5be2e2653c46c1bbe0fdaa.png)

 点击完成导入

![图片](https://i-blog.csdnimg.cn/blog_migrate/fab3148dbc2211b3e34b0f3ff68a32b5.png)

14、在模拟器中打开系统应用—>设置—>安全—>从SD卡安装。找到FiddlerRoot.cer文件，按提示导入即可，注意在此过程需要名称和解锁图案等，自行即可

设置-安全-为证书命名

![图片](https://i-blog.csdnimg.cn/blog_migrate/3620685b6b713d733ea62685e3eba4d3.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/5acafb19ad71167a343690a8c914c4e3.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/3796ad971cf77fb8e75a615ffb465996.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/a115ccb1b636b08abedda72c78b72fdb.png)

![图片](https://i-blog.csdnimg.cn/blog_migrate/4396ace0171076ff1387294270e6d5ae.png)

或者另一种方法安装证书：

在雷电模拟器里打开浏览器，访问刚才设置的本机IP加端口，便可自动下载证书进行安装

流程如下

手机端(客户端)设置

保证Fiddler和手机在同一局域网下，设置手机代理服务器地址为Fiddler服务器地址即可。

![图片](https://i-blog.csdnimg.cn/blog_migrate/70f101c7020c3fa080710b97fee35699.png)

设置代理服务器

当使用https协议时，需要下载证书(根据需要)

在手机浏览器访问Fiddler服务器---下载证书---安装证书（设置→安全→凭据存储→从sd卡安装）

![图片](https://i-blog.csdnimg.cn/blog_migrate/9ce9bdb5c628039a31ea82dde7757f1b.png)

下载证书

15、打开fiddler，重启模拟器，输入设置的密码，按回车键，打开需要抓包的APP，就可以在电脑上进行APP抓包了

![图片](https://i-blog.csdnimg.cn/blog_migrate/d9b6fb1a7c47533052eccb80c33fa43e.png)

常用图标含义 

![图片](https://i-blog.csdnimg.cn/blog_migrate/d6fcdcae74db1621f983b6fadf455285.png)

本文转自 <https://blog.csdn.net/Fiverya/article/details/120325676>，如有侵权，请联系删除。