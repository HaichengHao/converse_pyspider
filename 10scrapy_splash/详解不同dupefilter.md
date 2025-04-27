## 详解各个过滤器指纹（请求指纹过滤器）

### scrapy中的dupefilters.py

```python
from __future__ import annotations
import logging
import warnings
from pathlib import Path
from typing import TYPE_CHECKING

from scrapy.exceptions import ScrapyDeprecationWarning
from scrapy.utils.job import job_dir
from scrapy.utils.request import (
    RequestFingerprinter,
    RequestFingerprinterProtocol,
    referer_str,
)

if TYPE_CHECKING:
    from twisted.internet.defer import Deferred

    # typing.Self requires Python 3.11
    from typing_extensions import Self

    from scrapy.crawler import Crawler
    from scrapy.http.request import Request
    from scrapy.settings import BaseSettings
    from scrapy.spiders import Spider


class BaseDupeFilter:
    @classmethod
    def from_settings(cls, settings: BaseSettings) -> Self:
        warnings.warn(
            f"{cls.__name__}.from_settings() is deprecated, use from_crawler() instead.",
            category=ScrapyDeprecationWarning,
            stacklevel=2,
        )
        return cls()

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> Self:
        return cls()

    def request_seen(self, request: Request) -> bool:
        return False

    def open(self) -> Deferred[None] | None:
        pass

    def close(self, reason: str) -> Deferred[None] | None:
        pass

    def log(self, request: Request, spider: Spider) -> None:
        """Log that a request has been filtered"""
        pass


class RFPDupeFilter(BaseDupeFilter):
    """Request Fingerprint duplicates filter"""

    def __init__(
        self,
        path: str | None = None,
        debug: bool = False,
        *,
        fingerprinter: RequestFingerprinterProtocol | None = None,
    ) -> None:
        self.file = None
        self.fingerprinter: RequestFingerprinterProtocol = (
            fingerprinter or RequestFingerprinter()
        )
        self.fingerprints: set[str] = set()
        self.logdupes = True
        self.debug = debug
        self.logger = logging.getLogger(__name__)
        if path:
            self.file = Path(path, "requests.seen").open("a+", encoding="utf-8")
            self.file.seek(0)
            self.fingerprints.update(x.rstrip() for x in self.file)

    @classmethod
    def from_settings(
        cls,
        settings: BaseSettings,
        *,
        fingerprinter: RequestFingerprinterProtocol | None = None,
    ) -> Self:
        warnings.warn(
            f"{cls.__name__}.from_settings() is deprecated, use from_crawler() instead.",
            category=ScrapyDeprecationWarning,
            stacklevel=2,
        )
        return cls._from_settings(settings, fingerprinter=fingerprinter)

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> Self:
        assert crawler.request_fingerprinter
        return cls._from_settings(
            crawler.settings,
            fingerprinter=crawler.request_fingerprinter,
        )

    @classmethod
    def _from_settings(
        cls,
        settings: BaseSettings,
        *,
        fingerprinter: RequestFingerprinterProtocol | None = None,
    ) -> Self:
        debug = settings.getbool("DUPEFILTER_DEBUG")
        return cls(job_dir(settings), debug, fingerprinter=fingerprinter)

    def request_seen(self, request: Request) -> bool:
        fp = self.request_fingerprint(request)
        if fp in self.fingerprints:
            return True
        self.fingerprints.add(fp)
        if self.file:
            self.file.write(fp + "\n")
        return False

    def request_fingerprint(self, request: Request) -> str:  <---注意这里这是scrapy的请求指纹
        return self.fingerprinter.fingerprint(request).hex()

    def close(self, reason: str) -> None:
        if self.file:
            self.file.close()

    def log(self, request: Request, spider: Spider) -> None:
        if self.debug:
            msg = "Filtered duplicate request: %(request)s (referer: %(referer)s)"
            args = {"request": request, "referer": referer_str(request)}
            self.logger.debug(msg, args, extra={"spider": spider})
        elif self.logdupes:
            msg = (
                "Filtered duplicate request: %(request)s"
                " - no more duplicates will be shown"
                " (see DUPEFILTER_DEBUG to show all duplicates)"
            )
            self.logger.debug(msg, {"request": request}, extra={"spider": spider})
            self.logdupes = False

        assert spider.crawler.stats
        spider.crawler.stats.inc_value("dupefilter/filtered", spider=spider)


```

### splash中的dupefilter.py

```python
# -*- coding: utf-8 -*-
"""
To handle "splash" Request meta key properly a custom DupeFilter must be set.
See https://github.com/scrapy/scrapy/issues/900 for more info.
"""
from __future__ import absolute_import, annotations
from copy import deepcopy
import hashlib
from weakref import WeakKeyDictionary
from warnings import warn

from scrapy.dupefilters import RFPDupeFilter

from scrapy.utils.python import to_bytes
from scrapy.utils.url import canonicalize_url
from scrapy.utils.request import RequestFingerprinterProtocol

from .utils import dict_hash


_deprecated_fingerprint_cache = WeakKeyDictionary()


def _serialize_headers(
    headers, request
):
    for header in headers:
        if header in request.headers:
            yield header
            for value in request.headers.getlist(header):
                yield value


# From https://docs.scrapy.org/en/2.11/_modules/scrapy/utils/request.html
# Needs to be added here since it was deletedin Scrapy 2.12
def request_fingerprint(
    request,
    include_headers=None,
    keep_fragments=False,
):
    """
    Return the request fingerprint as an hexadecimal string.

    The request fingerprint is a hash that uniquely identifies the resource the
    request points to. For example, take the following two urls:

    http://www.example.com/query?id=111&cat=222
    http://www.example.com/query?cat=222&id=111

    Even though those are two different URLs both point to the same resource
    and are equivalent (i.e. they should return the same response).

    Another example are cookies used to store session ids. Suppose the
    following page is only accessible to authenticated users:

    http://www.example.com/members/offers.html

    Lots of sites use a cookie to store the session id, which adds a random
    component to the HTTP Request and thus should be ignored when calculating
    the fingerprint.

    For this reason, request headers are ignored by default when calculating
    the fingerprint. If you want to include specific headers use the
    include_headers argument, which is a list of Request headers to include.

    Also, servers usually ignore fragments in urls when handling requests,
    so they are also ignored by default when calculating the fingerprint.
    If you want to include them, set the keep_fragments argument to True
    (for instance when handling requests with a headless browser).
    """
    processed_include_headers = None
    if include_headers:
        processed_include_headers = tuple(
            to_bytes(h.lower()) for h in sorted(include_headers)
        )
    cache = _deprecated_fingerprint_cache.setdefault(request, {})
    cache_key = (processed_include_headers, keep_fragments)
    if cache_key not in cache:
        fp = hashlib.sha1()
        fp.update(to_bytes(request.method))
        fp.update(
            to_bytes(canonicalize_url(request.url, keep_fragments=keep_fragments))
        )
        fp.update(request.body or b"")
        if processed_include_headers:
            for part in _serialize_headers(processed_include_headers, request):
                fp.update(part)
        cache[cache_key] = fp.hexdigest()
    return cache[cache_key]


# 就是在这里对原来的scrapy中的request_fingerprint重写为splash_request_fingerprint

def splash_request_fingerprint(request, include_headers=None):
    """ Request fingerprint which takes 'splash' meta key into account """
    warn(
        (
            "scrapy_splash.splash_request_fingerprint is deprecated. Set "
            "the REQUEST_FINGERPRINTER_CLASS Scrapy setting to "
            "\"scrapy_splash.SplashRequestFingerprinter\" instead."
        ),
        DeprecationWarning,
        stacklevel=2,
    )
	# 就在这里对指纹进行了改写
    fp = request_fingerprint(request, include_headers=include_headers)
    if 'splash' not in request.meta:
        return fp
	#其本质上只是新增了下面的功能，因为它做了判断，如果传入的请求是原本的scrapy的fp(指纹)那就返回原来的fp
    #否则，就封装为splash的fp，非常人性化，也就是说scrapy_splash的过滤器比原本的scrapy的过滤器多加上了一个功能
    splash_options = deepcopy(request.meta['splash'])
    args = splash_options.setdefault('args', {})

    if 'url' in args:
        args['url'] = canonicalize_url(args['url'], keep_fragments=True)

    return dict_hash(splash_options, fp)


class SplashAwareDupeFilter(RFPDupeFilter): #继承了scrapy.dupefilters的RFPDupeFilter，然后对其进行重写
    """
    DupeFilter that takes 'splash' meta key in account.
    It should be used with SplashMiddleware.
    """

    def __init__(
            self,
            path: str | None = None,
            debug: bool = False,
            *,
            fingerprinter: RequestFingerprinterProtocol | None = None
    ):
        warn(
            (
                "SplashAwareDupeFilter is deprecated. Set "
                "the REQUEST_FINGERPRINTER_CLASS Scrapy setting to "
                "\"scrapy_splash.SplashRequestFingerprinter\" instead."
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(path, debug, fingerprinter=fingerprinter)

    def request_fingerprint(self, request):
        return splash_request_fingerprint(request)  #这是splash的请求指纹它调用了重写的方法，往上看，按返回结果其实就只是这里不太相同

```

### scrapy_redis的dupefilter.py  

#### 引

```python
#这里引入之前的增量式代码方便理解
import scrapy
from urllib.parse import urljoin
from redis import Redis
from ..items import Zlsdemo3Item


# abst:demo3和之前的demo1,demo2有相似之处，但是也有不同的写法，比较难理解,譬如初始化Redis对象的方法
# important: 增量式解决的就是相同内容的问题,也就是去重，有重复的数据产生就对其去除
# 方法1：使用python的集合进行去重>>但是这样效率很低，且存储起来很麻烦
# 方法2: 使用redis的集合进行去重
# tips: 放法2的两个方案
#  1存储url，作为数据指纹来判断是否该条数据已经被抓取 优点是简单，快捷方便，缺点:如果url内部进行了更新会损失数据
#  2存储数据,优点是准确性高，但是缺点是如果数据集非常庞大，那么对于reids而言是不利的(这个操作的话进入到piplines.py里进行)

# conn = Redis(
#     host="localhost",
#     port=6379,
#     db=15,
# )


class TianyaSpider(scrapy.Spider):
    name = "tianya"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://xintianya.net/"]
    model_url = 'https://xintianya.net/index-%d.htm'
    page_number = 2  # tips:定义类属性page_number,用于我们进行多页爬取的页数的初始化

    # tips:重写初始化方法，让redis实例在爬虫开始时就调用
    def __init__(self, name=None, **kwargs):
        self.redis = Redis(
            host="localhost",
            port=6379,
            db=9,
        )
        # 让父类初始化
        super(TianyaSpider, self).__init__(name, **kwargs)

    def parse(self, response):
        urls = response.xpath(
            '//div[@class="card card-threadlist"]//ul/li/div[@class="media-body"]/div/a/@href').extract()
        for url in urls:
            # print(url)
            detail_url = urljoin(self.start_urls[0], url)
            # tips:进入详情页的前提是:之前这个详情页的url没有被存储过，换句话说这是个新的才存，旧的不存
            #  1方案1:往集合里存，存进去就是新的，存不进去就是老的
            # result = self.redis.sadd("tianya:ty:detail:url",detail_url)
            # if result: #如果插入成功，说明数据是新的数据
            # #     那就插入新的数据
            #     print('get new url, the data will be add to redis')
            #     yield scrapy.Request(url=detail_url, callback=self.parse_detail)
            # else:
            #     print('this url have been saved,continue')

            # tips 其实我们只是想redis来高效的对url进行判定是否是新的
            # 但是这样有一个问题,redis并不会因为spider程序被迫停止就会停止，它仍然会进行请求
            # QUIZ:如何解决这个问题
            # answer :利用sismember来进行判断即可，不进行数据的插入,和刚才的逻辑刚好是反的
            # result = conn.sismember("tianya:ty:detail:url",detail_url)
            result = self.redis.sismember("tianya:ty:detail:url", detail_url)
            if result:  # 如果已经存在了，那就不存
                print('this url have been saved,will take no operation')
            else:  # 如果不存在那就往redis里存
                print('get new url ,the data will be add to redis')
                # 往里存
                # QUIZ:但是存的话应该写哪里合适呢?
                # answer:放到parse_detail里边，因为存在的话就不调用parse_detail
                #  或者像之前那样写到pipline里(推荐)
                yield scrapy.Request(url=detail_url, callback=self.parse_detail)

        # tips:可以继续考虑爬取下一页
        if self.page_number < 6:  # 只爬前6页当个例子看
            new_url = self.model_url % self.page_number
            self.page_number += 1
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        usrname = response.xpath('//a[@class="text-muted"]/b/text()').extract_first()
        title = response.xpath('//span[@class="break-all"]/text()').extract_first().strip()
        # print(f'username:{usrname},title:{title}')
        # tips:实例化item对象
        item = Zlsdemo3Item()
        item['usrname'] = usrname
        item['title'] = title
        self.redis.sadd("tianya:ty:detail:url", response.url)
        yield item

#         important:想验证是否成功可以运行两遍看看，第二遍就会抛出数据已经存储过

```



```python
import hashlib
import json
import logging
import time

from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.python import to_unicode
from w3lib.url import canonicalize_url

from . import defaults
from .connection import get_redis_from_settings

logger = logging.getLogger(__name__)


# TODO: Rename class to RedisDupeFilter.
class RFPDupeFilter(BaseDupeFilter):
    """Redis-based request duplicates filter.

    This class can also be used with default Scrapy's scheduler.

    """

    logger = logger

    def __init__(self, server, key, debug=False):
        """Initialize the duplicates filter.

        Parameters
        ----------
        server : redis.StrictRedis
            The redis server instance.
        key : str
            Redis key Where to store fingerprints.
        debug : bool, optional
            Whether to log filtered requests.

        """
        self.server = server
        self.key = key
        self.debug = debug
        self.logdupes = True

    @classmethod
    def from_settings(cls, settings):
        """Returns an instance from given settings.

        This uses by default the key ``dupefilter:<timestamp>``. When using the
        ``scrapy_redis.scheduler.Scheduler`` class, this method is not used as
        it needs to pass the spider name in the key.

        Parameters
        ----------
        settings : scrapy.settings.Settings

        Returns
        -------
        RFPDupeFilter
            A RFPDupeFilter instance.


        """
        server = get_redis_from_settings(settings)
        # XXX: This creates one-time key. needed to support to use this
        # class as standalone dupefilter with scrapy's default scheduler
        # if scrapy passes spider on open() method this wouldn't be needed
        # TODO: Use SCRAPY_JOB env as default and fallback to timestamp.
        key = defaults.DUPEFILTER_KEY % {"timestamp": int(time.time())}
        debug = settings.getbool("DUPEFILTER_DEBUG")
        return cls(server, key=key, debug=debug)

    @classmethod
    def from_crawler(cls, crawler):
        """Returns instance from crawler.

        Parameters
        ----------
        crawler : scrapy.crawler.Crawler

        Returns
        -------
        RFPDupeFilter
            Instance of RFPDupeFilter.

        """
        return cls.from_settings(crawler.settings)

    
    #这里也有不同之处
    def request_seen(self, request):
        """Returns True if request was already seen.

        Parameters
        ----------
        request : scrapy.http.Request

        Returns
        -------
        bool

        """
        fp = self.request_fingerprint(request)
        # This returns the number of values added, zero if already exists.
        added = self.server.sadd(self.key, fp) #这里就是ScrapyRedis的不同之处，它调用了数据库(redis数据库)进行了sadd(set add操作)，将指纹数据存储在Redis数据库当中，如果插入成功那么返回的就是1(这里就是之前增量式中插入操作的判定，如果说集合里没有这个数据，那么插入的时候就是0，如果集合中已经有了这个数据，那么返回值就是1，表示插入成功)
        return added == 0

    #这里对请求指纹方法做了重写
    def request_fingerprint(self, request):
        """Returns a fingerprint for a given request.

        Parameters
        ----------
        request : scrapy.http.Request

        Returns
        -------
        str

        """
        fingerprint_data = {
            "method": to_unicode(request.method),
            "url": canonicalize_url(request.url),
            "body": (request.body or b"").hex(),
        }
        #对请求进行了序列化操作将指纹数据加载为json字符串
        fingerprint_json = json.dumps(fingerprint_data, sort_keys=True)
        #调用散列加密的sha1（Secure Hash Alogrithm 1 安全哈希1）算法
        return hashlib.sha1(fingerprint_json.encode()).hexdigest()

    @classmethod
    def from_spider(cls, spider):
        settings = spider.settings
        server = get_redis_from_settings(settings)
        dupefilter_key = settings.get(
            "SCHEDULER_DUPEFILTER_KEY", defaults.SCHEDULER_DUPEFILTER_KEY
        )
        key = dupefilter_key % {"spider": spider.name}
        debug = settings.getbool("DUPEFILTER_DEBUG")
        return cls(server, key=key, debug=debug)

    def close(self, reason=""):
        """Delete data on close. Called by Scrapy's scheduler.

        Parameters
        ----------
        reason : str, optional

        """
        self.clear()

    def clear(self):
        """Clears fingerprints data."""
        self.server.delete(self.key)

    def log(self, request, spider):
        """Logs given request.

        Parameters
        ----------
        request : scrapy.http.Request
        spider : scrapy.spiders.Spider

        """
        if self.debug:
            msg = "Filtered duplicate request: %(request)s"
            self.logger.debug(msg, {"request": request}, extra={"spider": spider})
        elif self.logdupes:
            msg = (
                "Filtered duplicate request %(request)s"
                " - no more duplicates will be shown"
                " (see DUPEFILTER_DEBUG to show all duplicates)"
            )
            self.logger.debug(msg, {"request": request}, extra={"spider": spider})
            self.logdupes = False

```

可以看出scrapy_redis的dupefilter对scrapy原生的修改还是很多的，特别是其直接修改了RFPDupeFilterr类

### 不同配置

1. scrapy_redis的

    ```python
    ITEM_PIPELINES = {
       "dosDemo1.pipelines.Dosdemo1Pipeline": 300,
       "scrapy_redis.pipelines.RedisPipeline": 301 #important:新增了redispipline,也可以不用它随意
    }
    
    # redis相关配置
    
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB = 12
    # REDIS_PARAMS={
    #
    # }
    # scrapy-redis配置
    # 配置调度器
    # important:指定使用共享的调度器
    # tips: 使用scrapy-redis组件的过滤器去重队列
    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
    # tips :使用scrapy-redis组件自己的调度器
    SCHEDULER = "scrapy_redis.scheduler.Scheduler"
    # tips: 如果为真，在关闭时自动保存请求信息，如果为假，则不保存请求信息
    SCHEDULER_PERSIST = True #tips:设置为True可以实现断点续爬
    
    ```

3. scrapy_splash的

   ```python
   SPLASH_URL ='http://192.168.88.128:8050/'
   # 下载器中间件, 这个必须要配置
   DOWNLOADER_MIDDLEWARES = {
       'scrapy_splash.SplashCookiesMiddleware': 723,
       'scrapy_splash.SplashMiddleware': 725,
       'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
   }
   
   # 这个可有可无
   # SPIDER_MIDDLEWARES = {
   #     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
   # }
   # 去重过滤器, 这个必须要配置
   DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
   # 使用Splash的Http缓存, 这个必须要配置
   HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
   ```
   
   

3. scrapy_redis的布隆过滤器

   ```python
   ITEM_PIPELINES = {
       "scrapy_redis.pipelines.RedisPipeline": 301,
       "second.pipelines.SecondPipeline": 300,
   
   }
   
   REDIS_HOST = "127.0.0.1"
   REDIS_PORT = 6379
   REDIS_DB = 14
   
   # tips: 使用scrapy-redis组件的过滤器去重队列RequestFingerPrintDuplicatesFilter
   # DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
   # tips :使用scrapy-redis组件自己的调度器
   SCHEDULER = "scrapy_redis.scheduler.Scheduler"
   # tips: 如果为真，在关闭时自动保存请求信息，如果为假，则不保存请求信息
   SCHEDULER_PERSIST = True #tips:设置为True可以实现断点续爬
   
   # important:使用布隆过滤器
   # 在去重类中使用BloomFilter 替换 DUPEFILTER_CLASS便可使用
   DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
   # 哈希函数的个数，默认为6，可以自行修改
   BLOOMFILTER_HASH_MEMBER = 6
   # BloomFilter的bit参数，默认30，占用128M空间，去重量级1亿
   BLOOMFILTER_BIT = 30
   ```

## 接下来要实现的功能:能够进行分布式的splash(之前的学习路线-增量式->分布式->splash->最终的分布式splash)  

redis_splash中自己创建一个dupefilter.py

![image-20250422181541991](C:\Users\20201\AppData\Roaming\Typora\typora-user-images\image-20250422181541991.png)

由于scrapy_redis中的dupefilter改写的较多且scrapy_spalsh对dupefilter只是新增了一些功能，所以我们可以利用scrapy_redis的dupefilter来新增上scrapy_splash的dupefilter实现的功能

整体思路，自己定义新的过滤器，然后继承scrapy_redis的过滤器并在其中增加上splash过滤器的功能，之后配置文件的DUPEFILTER_CLASS指定自己的过滤器即可

## 踩坑 

```python

# step1:导入scrapy_redis的过滤器，然后进行继承
from scrapy_redis.dupefilter import RFPDupeFilter
from scrapy_splash.dupefilter import splash_request_fingerprint #引入,但是这样会发生问题，因为它定义文件中继承的是原始的RFPDupeFilter,而我们想让其继承自新的scrapy_redis的RFPDupeFilter
class MyDupeFilter(RFPDupeFilter):
    #step2:接下来实现splash的功能
    # pass
    def request_fingerprint(self, request):
        return splash_request_fingerprint(request) #因为改写的时候用到splash_request_fingerprint，所以这里也要引入
```

~~或者不想这样引入的话也可以粘过来splash_request_fingerprint的定义~~

### 上面想当然的写，结果错了，还是老老实实复制粘贴读逻辑

```python
"""
@File    :dupefilter.py
@Editor  : 百年
@Date    :2025/4/22 18:15 
"""

# step1:导入scrapy_redis的过滤器，然后进行继承
from scrapy_redis.dupefilter import RFPDupeFilter as BaseRFPF #起个别名
# from scrapy.dupefilters import RFPDupeFilter
import hashlib
from scrapy.utils.python import to_bytes
from scrapy.utils.url import canonicalize_url
from scrapy.utils.request import RequestFingerprinterProtocol
from copy import deepcopy
from weakref import WeakKeyDictionary
_deprecated_fingerprint_cache = WeakKeyDictionary()
# from .utils import dict_hash #注意这个utils,因为我们是直接新建的过滤器，那么需要导入的是scrapy_spalsh的dupefilter.py的同级目录下的utils
# 也就是说要这样写
from scrapy_splash.utils import dict_hash
# 还要引入deepcopy
from copy import deepcopy
from warnings import warn
def _serialize_headers(
    headers, request
):
    for header in headers:
        if header in request.headers:
            yield header
            for value in request.headers.getlist(header):
                yield value

def request_fingerprint(
    request,
    include_headers=None,
    keep_fragments=False,
):
    """
    Return the request fingerprint as an hexadecimal string.

    The request fingerprint is a hash that uniquely identifies the resource the
    request points to. For example, take the following two urls:

    http://www.example.com/query?id=111&cat=222
    http://www.example.com/query?cat=222&id=111

    Even though those are two different URLs both point to the same resource
    and are equivalent (i.e. they should return the same response).

    Another example are cookies used to store session ids. Suppose the
    following page is only accessible to authenticated users:

    http://www.example.com/members/offers.html

    Lots of sites use a cookie to store the session id, which adds a random
    component to the HTTP Request and thus should be ignored when calculating
    the fingerprint.

    For this reason, request headers are ignored by default when calculating
    the fingerprint. If you want to include specific headers use the
    include_headers argument, which is a list of Request headers to include.

    Also, servers usually ignore fragments in urls when handling requests,
    so they are also ignored by default when calculating the fingerprint.
    If you want to include them, set the keep_fragments argument to True
    (for instance when handling requests with a headless browser).
    """
    processed_include_headers = None
    if include_headers:
        processed_include_headers = tuple(
            to_bytes(h.lower()) for h in sorted(include_headers)
        )
    cache = _deprecated_fingerprint_cache.setdefault(request, {})
    cache_key = (processed_include_headers, keep_fragments)
    if cache_key not in cache:
        fp = hashlib.sha1()
        fp.update(to_bytes(request.method))
        fp.update(
            to_bytes(canonicalize_url(request.url, keep_fragments=keep_fragments))
        )
        fp.update(request.body or b"")
        if processed_include_headers:
            for part in _serialize_headers(processed_include_headers, request):
                fp.update(part)
        cache[cache_key] = fp.hexdigest()
    return cache[cache_key]

def splash_request_fingerprint(request, include_headers=None):
    """ Request fingerprint which takes 'splash' meta key into account """
    warn(
        (
            "scrapy_splash.splash_request_fingerprint is deprecated. Set "
            "the REQUEST_FINGERPRINTER_CLASS Scrapy setting to "
            "\"scrapy_splash.SplashRequestFingerprinter\" instead."
        ),
        DeprecationWarning,
        stacklevel=2,
    )

    fp = request_fingerprint(request, include_headers=include_headers)
    if 'splash' not in request.meta:
        return fp

    splash_options = deepcopy(request.meta['splash'])
    args = splash_options.setdefault('args', {})

    if 'url' in args:
        args['url'] = canonicalize_url(args['url'], keep_fragments=True)

    return dict_hash(splash_options, fp)


class MyDupeFilter(BaseRFPF):
    # step2:接下来实现splash的功能

    def request_fingerprint(self, request):
        return splash_request_fingerprint(request)  # 这里直接把splash_request_fingerprint的定义写到文件里，不走引入
```

上面这样就实现了兼容效果，即如果之后遇到scrapy_redis那样的分布式爬虫可以直接使用这个过滤器，如果遇到splash那样的也可以使用这个过滤器，就不需要记忆那么多过滤器的名称了 



### 大集合 scrapy_redis+scrapy_splash+布隆过滤器 

布隆过滤器的过滤器dupefilter.py

```python
import logging
import time
from .defaults import BLOOMFILTER_HASH_NUMBER, BLOOMFILTER_BIT, DUPEFILTER_DEBUG
from . import defaults
from scrapy_redis.connection import get_redis_from_settings
from .bloomfilter import BloomFilter
from scrapy_redis.dupefilter import RFPDupeFilter as BaseDupeFilter

logger = logging.getLogger(__name__)


class RFPDupeFilter(BaseDupeFilter):
    """Redis-based request duplicates filter.

    This class can also be used with default Scrapy's scheduler.

    """
    
    logger = logger
    
    def __init__(self, server, key, debug, bit, hash_number):
        """Initialize the duplicates filter.

        Parameters
        ----------
        server : redis.StrictRedis
            The redis server instance.
        key : str
            Redis key Where to store fingerprints.
        debug : bool, optional
            Whether to log filtered requests.

        """
        #server、key、debug、logup这些scrapy-redis都有
        self.server = server
        self.key = key
        self.debug = debug
        self.bit = bit #这个scrapy-redis没有
        self.hash_number = hash_number  #这个scrapy-redis也没有
        self.logdupes = True
        self.bf = BloomFilter(server, self.key, bit, hash_number) #这个也没有
    
    @classmethod
    def from_settings(cls, settings):
        """Returns an instance from given settings.

        This uses by default the key ``dupefilter:<timestamp>``. When using the
        ``scrapy_redis.scheduler.Scheduler`` class, this method is not used as
        it needs to pass the spider name in the key.

        Parameters
        ----------
        settings : scrapy.settings.Settings

        Returns
        -------
        RFPDupeFilter
            A RFPDupeFilter instance.


        """
        server = get_redis_from_settings(settings)
        # XXX: This creates one-time key. needed to support to use this
        # class as standalone dupefilter with scrapy's default scheduler
        # if scrapy passes spider on open() method this wouldn't be needed
        # TODO: Use SCRAPY_JOB env as default and fallback to timestamp.
        key = defaults.DUPEFILTER_KEY % {'timestamp': int(time.time())}
        debug = settings.getbool('DUPEFILTER_DEBUG', DUPEFILTER_DEBUG)
        bit = settings.getint('BLOOMFILTER_BIT', BLOOMFILTER_BIT)
        hash_number = settings.getint('BLOOMFILTER_HASH_NUMBER', BLOOMFILTER_HASH_NUMBER)
        return cls(server, key=key, debug=debug, bit=bit, hash_number=hash_number)
    
    @classmethod
    def from_crawler(cls, crawler):
        """Returns instance from crawler.

        Parameters
        ----------
        crawler : scrapy.crawler.Crawler

        Returns
        -------
        RFPDupeFilter
            Instance of RFPDupeFilter.

        """
        instance = cls.from_settings(crawler.settings)
        return instance
    #上面这部分和scrapy-redis的过滤器比较像
    @classmethod
    def from_spider(cls, spider):
        """Returns instance from crawler.

        Parameters
        ----------
        spider :

        Returns
        -------
        RFPDupeFilter
            Instance of RFPDupeFilter.

        """
        settings = spider.settings
        server = get_redis_from_settings(settings)
        dupefilter_key = settings.get("SCHEDULER_DUPEFILTER_KEY", defaults.SCHEDULER_DUPEFILTER_KEY)
        key = dupefilter_key % {'spider': spider.name}
        debug = settings.getbool('DUPEFILTER_DEBUG', DUPEFILTER_DEBUG)
        bit = settings.getint('BLOOMFILTER_BIT', BLOOMFILTER_BIT)
        hash_number = settings.getint('BLOOMFILTER_HASH_NUMBER', BLOOMFILTER_HASH_NUMBER)
        print(key, bit, hash_number)
        instance = cls(server, key=key, debug=debug, bit=bit, hash_number=hash_number)
        return instance
    
    def request_seen(self, request):
        """Returns True if request was already seen.

        Parameters
        ----------
        request : scrapy.http.Request

        Returns
        -------
        bool

        """
        fp = self.request_fingerprint(request)
        # This returns the number of values added, zero if already exists.
        if self.bf.exists(fp):
            return True
        self.bf.insert(fp)
        return False
    
    def log(self, request, spider):
        """Logs given request.

        Parameters
        ----------
        request : scrapy.http.Request
        spider : scrapy.spiders.Spider

        """
        if self.debug:
            msg = "Filtered duplicate request: %(request)s"
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
        elif self.logdupes:
            msg = ("Filtered duplicate request %(request)s"
                   " - no more duplicates will be shown"
                   " (see DUPEFILTER_DEBUG to show all duplicates)")
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
            self.logdupes = False
        spider.crawler.stats.inc_value('bloomfilter/filtered', spider=spider)

```

布隆过滤器的dupefilter.py的文件其实和本来的原生区别不算太大，既然如此那就直接将其放到之前自己写的过滤器当中





## 实现超大杯scrapy_redis+scrapy_splash+scrapy_redis_dbloomfilter 兼备的过滤器  



```python
import logging
import time
from scrapy_redis_bloomfilter.defaults import BLOOMFILTER_HASH_NUMBER, BLOOMFILTER_BIT, DUPEFILTER_DEBUG
from scrapy_redis_bloomfilter import defaults
from scrapy_redis.connection import get_redis_from_settings
from scrapy_redis_bloomfilter.bloomfilter import BloomFilter
# from scrapy_redis.dupefilter import RFPDupeFilter as BaseDupeFilter

logger = logging.getLogger(__name__)
# step1:导入scrapy_redis的过滤器，然后进行继承
from scrapy_redis.dupefilter import RFPDupeFilter as BaseRFPF  # 起个别名
# from scrapy.dupefilters import RFPDupeFilter
import hashlib
from scrapy.utils.python import to_bytes
from scrapy.utils.url import canonicalize_url
from scrapy.utils.request import RequestFingerprinterProtocol
from copy import deepcopy
from weakref import WeakKeyDictionary

_deprecated_fingerprint_cache = WeakKeyDictionary()
# from .utils import dict_hash #注意这个utils,因为我们是直接新建的过滤器，那么需要导入的是scrapy_spalsh的dupefilter.py的同级目录下的utils
# 也就是说要这样写
from scrapy_splash.utils import dict_hash
# 还要引入deepcopy
from copy import deepcopy
from warnings import warn


def _serialize_headers(
        headers, request
):
    for header in headers:
        if header in request.headers:
            yield header
            for value in request.headers.getlist(header):
                yield value


def request_fingerprint(
        request,
        include_headers=None,
        keep_fragments=False,
):
    """
    Return the request fingerprint as an hexadecimal string.

    The request fingerprint is a hash that uniquely identifies the resource the
    request points to. For example, take the following two urls:

    http://www.example.com/query?id=111&cat=222
    http://www.example.com/query?cat=222&id=111

    Even though those are two different URLs both point to the same resource
    and are equivalent (i.e. they should return the same response).

    Another example are cookies used to store session ids. Suppose the
    following page is only accessible to authenticated users:

    http://www.example.com/members/offers.html

    Lots of sites use a cookie to store the session id, which adds a random
    component to the HTTP Request and thus should be ignored when calculating
    the fingerprint.

    For this reason, request headers are ignored by default when calculating
    the fingerprint. If you want to include specific headers use the
    include_headers argument, which is a list of Request headers to include.

    Also, servers usually ignore fragments in urls when handling requests,
    so they are also ignored by default when calculating the fingerprint.
    If you want to include them, set the keep_fragments argument to True
    (for instance when handling requests with a headless browser).
    """
    processed_include_headers = None
    if include_headers:
        processed_include_headers = tuple(
            to_bytes(h.lower()) for h in sorted(include_headers)
        )
    cache = _deprecated_fingerprint_cache.setdefault(request, {})
    cache_key = (processed_include_headers, keep_fragments)
    if cache_key not in cache:
        fp = hashlib.sha1()
        fp.update(to_bytes(request.method))
        fp.update(
            to_bytes(canonicalize_url(request.url, keep_fragments=keep_fragments))
        )
        fp.update(request.body or b"")
        if processed_include_headers:
            for part in _serialize_headers(processed_include_headers, request):
                fp.update(part)
        cache[cache_key] = fp.hexdigest()
    return cache[cache_key]


def splash_request_fingerprint(request, include_headers=None):
    """ Request fingerprint which takes 'splash' meta key into account """
    warn(
        (
            "scrapy_splash.splash_request_fingerprint is deprecated. Set "
            "the REQUEST_FINGERPRINTER_CLASS Scrapy setting to "
            "\"scrapy_splash.SplashRequestFingerprinter\" instead."
        ),
        DeprecationWarning,
        stacklevel=2,
    )

    fp = request_fingerprint(request, include_headers=include_headers)
    if 'splash' not in request.meta:
        return fp

    splash_options = deepcopy(request.meta['splash'])
    args = splash_options.setdefault('args', {})

    if 'url' in args:
        args['url'] = canonicalize_url(args['url'], keep_fragments=True)

    return dict_hash(splash_options, fp)

#继承了scrapy_redis的RFPDupefilter as BaseRFPF
#把splash中改写原来的原生request_fingerprint也改写了
#把布隆过滤器的实现粘贴过来了
class MyDupeFilter(BaseRFPF):
    # step2:接下来实现splash的功能
    """Redis-based request duplicates filter.

    This class can also be used with default Scrapy's scheduler.

    """


logger = logger


def __init__(self, server, key, debug, bit, hash_number):
    """Initialize the duplicates filter.

    Parameters
    ----------
    server : redis.StrictRedis
        The redis server instance.
    key : str
        Redis key Where to store fingerprints.
    debug : bool, optional
        Whether to log filtered requests.

    """
    self.server = server
    self.key = key
    self.debug = debug
    self.bit = bit
    self.hash_number = hash_number
    self.logdupes = True
    self.bf = BloomFilter(server, self.key, bit, hash_number)


@classmethod
def from_settings(cls, settings):
    """Returns an instance from given settings.

    This uses by default the key ``dupefilter:<timestamp>``. When using the
    ``scrapy_redis.scheduler.Scheduler`` class, this method is not used as
    it needs to pass the spider name in the key.

    Parameters
    ----------
    settings : scrapy.settings.Settings

    Returns
    -------
    RFPDupeFilter
        A RFPDupeFilter instance.


    """
    server = get_redis_from_settings(settings)
    # XXX: This creates one-time key. needed to support to use this
    # class as standalone dupefilter with scrapy's default scheduler
    # if scrapy passes spider on open() method this wouldn't be needed
    # TODO: Use SCRAPY_JOB env as default and fallback to timestamp.
    key = defaults.DUPEFILTER_KEY % {'timestamp': int(time.time())}
    debug = settings.getbool('DUPEFILTER_DEBUG', DUPEFILTER_DEBUG)
    bit = settings.getint('BLOOMFILTER_BIT', BLOOMFILTER_BIT)
    hash_number = settings.getint('BLOOMFILTER_HASH_NUMBER', BLOOMFILTER_HASH_NUMBER)
    return cls(server, key=key, debug=debug, bit=bit, hash_number=hash_number)


@classmethod
def from_crawler(cls, crawler):
    """Returns instance from crawler.

    Parameters
    ----------
    crawler : scrapy.crawler.Crawler

    Returns
    -------
    RFPDupeFilter
        Instance of RFPDupeFilter.

    """
    instance = cls.from_settings(crawler.settings)
    return instance


@classmethod
def from_spider(cls, spider):
    """Returns instance from crawler.

    Parameters
    ----------
    spider :

    Returns
    -------
    RFPDupeFilter
        Instance of RFPDupeFilter.

    """
    settings = spider.settings
    server = get_redis_from_settings(settings)
    dupefilter_key = settings.get("SCHEDULER_DUPEFILTER_KEY", defaults.SCHEDULER_DUPEFILTER_KEY)
    key = dupefilter_key % {'spider': spider.name}
    debug = settings.getbool('DUPEFILTER_DEBUG', DUPEFILTER_DEBUG)
    bit = settings.getint('BLOOMFILTER_BIT', BLOOMFILTER_BIT)
    hash_number = settings.getint('BLOOMFILTER_HASH_NUMBER', BLOOMFILTER_HASH_NUMBER)
    print(key, bit, hash_number)
    instance = cls(server, key=key, debug=debug, bit=bit, hash_number=hash_number)
    return instance


def request_seen(self, request):
    """Returns True if request was already seen.

    Parameters
    ----------
    request : scrapy.http.Request

    Returns
    -------
    bool

    """
    fp = self.request_fingerprint(request)
    # This returns the number of values added, zero if already exists.
    if self.bf.exists(fp):
        return True
    self.bf.insert(fp)
    return False


def log(self, request, spider):
    """Logs given request.

    Parameters
    ----------
    request : scrapy.http.Request
    spider : scrapy.spiders.Spider

    """
    if self.debug:
        msg = "Filtered duplicate request: %(request)s"
        self.logger.debug(msg, {'request': request}, extra={'spider': spider})
    elif self.logdupes:
        msg = ("Filtered duplicate request %(request)s"
               " - no more duplicates will be shown"
               " (see DUPEFILTER_DEBUG to show all duplicates)")
        self.logger.debug(msg, {'request': request}, extra={'spider': spider})
        self.logdupes = False
    spider.crawler.stats.inc_value('bloomfilter/filtered', spider=spider)


def request_fingerprint(self, request):
    return splash_request_fingerprint(request)  # 这里直接把splash_request_fingerprint的定义写到文件里，不走引入
```

## 配置文件中的修改  

```python
#不管是分布式还是splash还是布隆过滤器,以后都只需要引入这个就行
#即在settings文件中设置
DUPEFILTER_CLASS=对应的文件.dupefilter文件名.类名
```

![image-20250422215019354](C:\Users\20201\AppData\Roaming\Typora\typora-user-images\image-20250422215019354.png)

## 然后既然是全面兼容那么所有的配置文件都要弄进来 

```python
# Scrapy settings for news project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "news"

SPIDER_MODULES = ["redis_splash.spiders"]
NEWSPIDER_MODULE = "redis_splash.spiders"


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
# ITEM_PIPELINES = {
#    "redis_splash.pipelines.NewsPipeline": 300,
# }

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


```

### 另外爬虫文件也需要进行修改

```python
import scrapy
from scrapy_splash.request import SplashRequest
from scrapy_redis.spiders import RedisSpider
from ..items import NewsItem


class WangyiSpider(RedisSpider):
    name = "news"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://news.163.com/domestic/"]
    # redis_key = 'wangyi:news:start_urls' #tips:因为要实现分布式，所以要上redis_key,但是又因为我们已经重写了start_requests，现在支持scrapy_redis,所以不需要再写
    lua_source = """
    function main(splash, args)
      assert(splash:go(args.url))
      assert(splash:wait(0.5))

      get_btn_display = splash:jsfunc([[
        function(){
        return document.getElementsByClassName('load_more_btn')[0].style.display;
      }
        ]])
      while(true)
      do
      splash:runjs("document.getElementsByClassName('load_more_btn')[0].scrollIntoView(true)")
      splash:select(".load_more_btn").click()
      splash:wait(1)
      -- 判断load_more_btn是否为none
      display = get_btn_display()
      if(display == 'none')
      then 
          break
      end
     end
     assert(splash:wait(2))
    return {
        html = splash:html(),
    }
    end

    """

    # important:重写父类
    def start_requests(self):  # tips:这里的思路和06 scrapy boss里的处理selenium的思路很相似
        yield SplashRequest(
            url=self.start_urls[0],
            callback=self.parse,
            endpoint="execute",  # important:表示要执行哪一个splash的服务
            args={
                "lua_source": self.lua_source,
            },
            dont_filter=True #tips:因为只是爬这一页的数据，所以不需要去重，那么布隆过滤器即使生效也不会在redis里有request和bloomfilter
        )

    def parse(self, response):
        # print(response.text)
        # 注意这里和之前的有所不同,scrapy_splash返回的不再是json格式的响应信息，所以这里我们可以不再进行json数据格式与python格式的转换
        # json_response = response.json()
        # responseraw = json_response['html']
        # print(responseraw)
        # response = HtmlResponse(url=self.start_urls[0],body=responseraw,encoding='utf-8')
        # titles = response.xpath('//div[contains(@class, "news_title")]//a/text()').extract()
        # hrefs = response.xpath('//div[contains(@class, "news_title")]//a/@href').extract()
        # for title in titles:
        #     print(title)
        a_s = response.xpath('//div[contains(@class, "news_title")]//a')
        for a in a_s:
            title = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            item = NewsItem()
            item['title'] = title
            item['href'] = href
            print(f'Title: {title}, Href: {href}')
            yield item

```

