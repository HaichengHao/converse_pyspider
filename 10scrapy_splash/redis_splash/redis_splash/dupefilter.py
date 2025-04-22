# """
# @File    :dupefilter.py
# @Editor  : 百年
# @Date    :2025/4/22 18:15
# """
#
# # step1:导入scrapy_redis的过滤器，然后进行继承
# # from scrapy_redis.dupefilter import RFPDupeFilter
# # from scrapy_splash.dupefilter import splash_request_fingerprint
# # class MyDupeFilter(RFPDupeFilter):
# #     #step2:接下来实现splash的功能
# #     # pass
# #     def request_fingerprint(self, request):
# #         return splash_request_fingerprint(request)
#
#
# # 或者不走引入(不推荐，很烦人)
# # step1:导入scrapy_redis的过滤器，然后进行继承
# from scrapy_redis.dupefilter import RFPDupeFilter as BaseRFPF #起个别名
# # from scrapy.dupefilters import RFPDupeFilter
# import hashlib
# from scrapy.utils.python import to_bytes
# from scrapy.utils.url import canonicalize_url
# from scrapy.utils.request import RequestFingerprinterProtocol
# from copy import deepcopy
# from weakref import WeakKeyDictionary
# _deprecated_fingerprint_cache = WeakKeyDictionary()
# # from .utils import dict_hash #注意这个utils,因为我们是直接新建的过滤器，那么需要导入的是scrapy_spalsh的dupefilter.py的同级目录下的utils
# # 也就是说要这样写
# from scrapy_splash.utils import dict_hash
# # 还要引入deepcopy
# from copy import deepcopy
# from warnings import warn
# def _serialize_headers(
#     headers, request
# ):
#     for header in headers:
#         if header in request.headers:
#             yield header
#             for value in request.headers.getlist(header):
#                 yield value
#
# def request_fingerprint(
#     request,
#     include_headers=None,
#     keep_fragments=False,
# ):
#     """
#     Return the request fingerprint as an hexadecimal string.
#
#     The request fingerprint is a hash that uniquely identifies the resource the
#     request points to. For example, take the following two urls:
#
#     http://www.example.com/query?id=111&cat=222
#     http://www.example.com/query?cat=222&id=111
#
#     Even though those are two different URLs both point to the same resource
#     and are equivalent (i.e. they should return the same response).
#
#     Another example are cookies used to store session ids. Suppose the
#     following page is only accessible to authenticated users:
#
#     http://www.example.com/members/offers.html
#
#     Lots of sites use a cookie to store the session id, which adds a random
#     component to the HTTP Request and thus should be ignored when calculating
#     the fingerprint.
#
#     For this reason, request headers are ignored by default when calculating
#     the fingerprint. If you want to include specific headers use the
#     include_headers argument, which is a list of Request headers to include.
#
#     Also, servers usually ignore fragments in urls when handling requests,
#     so they are also ignored by default when calculating the fingerprint.
#     If you want to include them, set the keep_fragments argument to True
#     (for instance when handling requests with a headless browser).
#     """
#     processed_include_headers = None
#     if include_headers:
#         processed_include_headers = tuple(
#             to_bytes(h.lower()) for h in sorted(include_headers)
#         )
#     cache = _deprecated_fingerprint_cache.setdefault(request, {})
#     cache_key = (processed_include_headers, keep_fragments)
#     if cache_key not in cache:
#         fp = hashlib.sha1()
#         fp.update(to_bytes(request.method))
#         fp.update(
#             to_bytes(canonicalize_url(request.url, keep_fragments=keep_fragments))
#         )
#         fp.update(request.body or b"")
#         if processed_include_headers:
#             for part in _serialize_headers(processed_include_headers, request):
#                 fp.update(part)
#         cache[cache_key] = fp.hexdigest()
#     return cache[cache_key]
#
# def splash_request_fingerprint(request, include_headers=None):
#     """ Request fingerprint which takes 'splash' meta key into account """
#     warn(
#         (
#             "scrapy_splash.splash_request_fingerprint is deprecated. Set "
#             "the REQUEST_FINGERPRINTER_CLASS Scrapy setting to "
#             "\"scrapy_splash.SplashRequestFingerprinter\" instead."
#         ),
#         DeprecationWarning,
#         stacklevel=2,
#     )
#
#     fp = request_fingerprint(request, include_headers=include_headers)
#     if 'splash' not in request.meta:
#         return fp
#
#     splash_options = deepcopy(request.meta['splash'])
#     args = splash_options.setdefault('args', {})
#
#     if 'url' in args:
#         args['url'] = canonicalize_url(args['url'], keep_fragments=True)
#
#     return dict_hash(splash_options, fp)
#
#
# class MyDupeFilter(BaseRFPF):
#     # step2:接下来实现splash的功能
#
#     def request_fingerprint(self, request):
#         return splash_request_fingerprint(request)  # 这里直接把splash_request_fingerprint的定义写到文件里，不走引入


"""
@File    :dupefilter.py
@Editor  : 百年
@Date    :2025/4/22 18:15
"""

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
