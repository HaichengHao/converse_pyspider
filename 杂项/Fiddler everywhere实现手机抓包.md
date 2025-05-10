 

推荐一款[抓包工具](https://so.csdn.net/so/search?q=%E6%8A%93%E5%8C%85%E5%B7%A5%E5%85%B7&spm=1001.2101.3001.7020)Fiddler everywhere，这是我用过的抓包工具中感觉界面最简洁，功能也全面(有postman功能)，用起来最舒服的抓包工具。

##### 下载地址 [https://www.telerik.com/download/fiddler-everywhere](https://www.telerik.com/download/fiddler-everywhere)![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/d2b64fbfb0148d880f5620526f43e83d.png)

安装，注册账号，登录后界面如下  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/035d42a7dddec9409bda67b609ce0304.png)

##### 安卓手机抓包

1.打开设置，勾选这两个，点击Trust root certificate按钮，弹出的对话框点击允许  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3b3c9353e0e8d87806e40272c029b755.png)

2.选择connections，勾选这两个，记住上面的端口号  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/11ae9efc8c63c94340142b68fc3cae05.png)  
保存设置

3.查看电脑所处的网络，手机和电脑需同处于一个网络，可以把鼠标移到右下角的Connected查看  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/4deae0405035c779cd332908fe925c8f.png)  
4.手机连接和电脑同一网络的wifi，打开wifi设置，选择手动代理，把ip设置为上一步查看的ip和端口设置为客户端设置的端口  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/253c41c569c53913b9fefeb3af643053.png)  
5.手机浏览器输入上一步ip和端口组成的地址如192.168.3.8::8877，打开后页面如下，如果无法打开，请关闭电脑防火墙重试  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/82498f0bc3e7721ad2ccdff1bb01f8cc.png)  
6.点击FiddlerRoot certificate，下载证书，然后安装证书，安装完成之后就能正常抓包了

##### IOS抓包

由于没有设备就不写步骤了，需要的可以参考官方文档[https://docs.telerik.com/fiddler-everywhere/get-started/mobile-traffic/configure-ios](https://docs.telerik.com/fiddler-everywhere/get-started/mobile-traffic/configure-ios)

##### Post Man功能

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3cd78c5b03bd0b5a18de9e19970c35e6.png)  
右键某个请求，点击Eidt in Composer就可以对某个请求进行修改了  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/bd879a2e5c587a8e4cd8dac2ac937523.png)

##### 修改返回数据

1.点击 Add new rule  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/2161f7c0bfc7e0f473fc567ad539c06f.png)  
选择匹配规则和返回数据  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/58df4504a647f34091f1dcd6f1ebd933.png)  
上图是请求地址包含returnGeometry字符串的，返回结果就是用本地的http://127.0.0.1:8081/test/tb返回的数据

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/e621b14d5a7a91127bc883474a076f27.png)  
上图EXACT:地址 就是完全匹配这个地址的返回404

更多匹配规则请参考官方文档[https://docs.telerik.com/fiddler-everywhere/user-guide/live-traffic/autoresponder](https://docs.telerik.com/fiddler-everywhere/user-guide/live-traffic/autoresponder)

本文转自 <https://blog.csdn.net/qq_34023088/article/details/117256262>，如有侵权，请联系删除。