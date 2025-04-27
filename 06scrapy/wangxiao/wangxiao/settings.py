# Scrapy settings for wangxiao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "wangxiao"

SPIDER_MODULES = ["wangxiao.spiders"]
NEWSPIDER_MODULE = "wangxiao.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "wangxiao (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'WARNING'

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
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
   "Cookie":"mantis6894=d6e03aa3756d4c338c1bfb3198ae3b42@6894; sign=jz1; Hm_lvt_fd91d2ffbfa83c234c1cee672a69326c=1745665014,1745729469; Hm_lpvt_fd91d2ffbfa83c234c1cee672a69326c=1745729469; HMACCOUNT=36598DCD2F5A4067; acw_tc=dec0bb5917457653368307749ee4f76f14470b23716502a2791be94288; autoLogin=null; userInfo=%7B%22userName%22%3A%22pc_797503255%22%2C%22token%22%3A%22922ce2d4-0823-4bf8-b0ee-e7265e2eccc5%22%2C%22headImg%22%3Anull%2C%22nickName%22%3A%22188****1568%22%2C%22sign%22%3A%22fangchan%22%2C%22isBindingMobile%22%3A%221%22%2C%22isSubPa%22%3A%220%22%2C%22userNameCookies%22%3A%22JwpdC64yHpLkkL5Yb6TEWA%3D%3D%22%2C%22passwordCookies%22%3A%22tnVB2J1UctMqkri%2FFv7osQ%3D%3D%22%7D; token=922ce2d4-0823-4bf8-b0ee-e7265e2eccc5; UserCookieName=pc_797503255; OldUsername2=JwpdC64yHpLkkL5Yb6TEWA%3D%3D; OldUsername=JwpdC64yHpLkkL5Yb6TEWA%3D%3D; OldPassword=tnVB2J1UctMqkri%2FFv7osQ%3D%3D; UserCookieName_=pc_797503255; OldUsername2_=JwpdC64yHpLkkL5Yb6TEWA%3D%3D; OldUsername_=JwpdC64yHpLkkL5Yb6TEWA%3D%3D; OldPassword_=tnVB2J1UctMqkri%2FFv7osQ%3D%3D; pc_797503255_exam=fangchan; acw_sc__v3=680e45561026ae71087ed1bf38765b57bcf65612; tfstk=gmamKfY4loobCjepH8ufxWsEOSj-lIgsKRLtBVHN4YkSkEFwkVqgLSPAGqFZIlDzYoLxBVgg_JFt3VExHfRbrJY9ktsb_F0t79BdJwFfGVgNpq2OmrJjGjvVWclwUqGOUw8EDwFbGQRDQ6EPJCqbJowZQRoq40ltUEkaQm-PZfl93h84Q75oFf92gm8aaUlIgnuZ7RPPZfMrQbVc0xaazzW7eiBxQfgLrjmmL7jB7FXoGpH3gUY95z2Kmv8iEF8arjVi3sY6-GHUAxnKL87JoVVrs8mLm9Y0I5PQb04M3seUUl2ZNu6MjvqaMka-2C-4ZPDmYrok16FUGfyZju6HJj0YqD40c19zgJH0YqN9ttFoxumIa0RM0qEL9PiUuZvIeDGgEDEcKE2F4atyYpbW5b5Tzhts0bGopvX3IrsIxKVRZ_xF1mlSGvClZhts0bGop_fkYNiqNjMd."
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "wangxiao.middlewares.WangxiaoSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "wangxiao.middlewares.WangxiaoDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "wangxiao.pipelines.WangxiaoPipeline": 300,
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
