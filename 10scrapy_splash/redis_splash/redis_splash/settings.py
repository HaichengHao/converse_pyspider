# Scrapy settings for news project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "news"

SPIDER_MODULES = ["news.spiders"]
NEWSPIDER_MODULE = "news.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "news (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL ='WARNING'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "news.middlewares.NewsSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "news.middlewares.NewsDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "news.pipelines.NewsPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# important:添加处理Splash要用的配置信息

# scrapy_splash
# 渲染服务的url, 这里换成你自己的
SPLASH_URL = 'http://192.168.150.133:8050/' #hero_host
# SPLASH_URL ='http://192.168.88.128:8050/'
# 下载器中间件, 这个必须要配置
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}


# important:这里修改成自己写的过滤器路径
DUPEFILTER_CLASS = 'redis_splash.dupefilter.MyDupeFilter'
# 使用Splash的Http缓存, 这个必须要配置
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


#important:scrapy_redis的配置

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 15
# tips :使用scrapy-redis组件自己的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# tips: 如果为真，在关闭时自动保存请求信息，如果为假，则不保存请求信息
SCHEDULER_PERSIST = True #tips:设置为True可以实现断点续爬

#important:布隆
ITEM_PIPELINES = {
    "scrapy_redis.pipelines.RedisPipeline": 301,
    "redis_splash.pipelines.NewsPipeline": 300,

}

# tips: 使用scrapy-redis组件的过滤器去重队列RequestFingerPrintDuplicatesFilter
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# tips :使用scrapy-redis组件自己的调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# tips: 如果为真，在关闭时自动保存请求信息，如果为假，则不保存请求信息
# SCHEDULER_PERSIST = True #tips:设置为True可以实现断点续爬

# important:使用布隆过滤器
# 在去重类中使用BloomFilter 替换 DUPEFILTER_CLASS便可使用
#DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
# 哈希函数的个数，默认为6，可以自行修改
BLOOMFILTER_HASH_MEMBER = 6
# BloomFilter的bit参数，默认30，占用128M空间，去重量级1亿
BLOOMFILTER_BIT = 30


#所有关于#DUPEFILTER_CLASS都注释掉然后改成自己的就行,只写一个
DUPEFILTER_CLASS = 'redis_splash.dupefilter.MyDupeFilter'

