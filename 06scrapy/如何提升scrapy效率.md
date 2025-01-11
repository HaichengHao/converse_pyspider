## 如何提升scrapy的效率  
1. 在settings配置文件中修改CONCURRENT_REQUESTS = 100  
scrapy默认开启的线程数量为32个，这样设置可以使其线程数量为100个
2. 在运行scrapy时,会有大量的日志信息输出，为了减少cpu的使用率，可以设置log输出信息为worining或者error  
3. 如果不是真的需要cookie,则在scrapy爬取数据时禁止cookie从而减少cpu的使用率，提升爬取效率，  
在配置文件中编写COOKIES_ENABLE = False
4. 禁止重试:  
对于失败的http请求(重试)会减慢爬取速度，因此可以禁止重试。在配置文件中编写:RETRY_ENABLE = False  
5. 减少下载超时:  
如果对一个非常慢的链接进行爬取，减少下载超时可以让卡住的链接快速被放弃，从而提升效率。  
在配置文件中编写:DOWNLOAD_TIMEOUT = 10 超时时间为10s