"""
@File    :getvv.py
@Editor  : 百年
@Date    :2025/4/8 13:21 
"""
import requests
import re


def getvv(bvid):
    url = 'https://www.bilibili.com/video/' + bvid + '/'

    session = requests.Session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'

    }
    res = session.get(url=url)
    page_source = res.text
    print(page_source)
    # obj = re.compile(r'</script><script>.*?},"aid":(?P<aid>\d+),"bvid":.*?,"cid":(?P<cid>\d+),', re.S)
    # obj = re.compile(
    #     r'''<script>.*?"timelength":(?P<duration>\d+).*?</script><script>.*?},"aid":(?P<aid>\d+),"bvid":(?P<bvid_>.*?),"cid":(?P<cid>\d+),.*?"userInteractionCount":(?P<viewcount>\d+).*?''',
    #     re.S)
    obj = re.compile(
        r'''"seek_type":"offset","dash":{"duration":(?P<duration>\d+).*?</script><script>.*?},"aid":(?P<aid>\d+),"bvid":(?P<bvid_>.*?),"cid":(?P<cid>\d+),.*?"userInteractionCount":(?P<viewcount>\d+).*?''',
        re.S)
    result = obj.finditer(page_source)
    for item in result:
        duration = item.group('duration')
        aid = item.group('aid')
        bvid_ = item.group('bvid_')
        cid = item.group('cid')
        viewcount = item.group('viewcount')
        return duration, aid, bvid_, cid, viewcount


if __name__ == '__main__':
    bvid = input('输入bvid')
    print(type(bvid))
    du, aid, bvid_, cid, vc = getvv(bvid)
    print(du, aid, bvid_, cid, vc)
