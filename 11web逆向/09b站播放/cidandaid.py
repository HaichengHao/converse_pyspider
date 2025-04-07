"""
@File    :cidandaid.py
@Editor  : 百年
@Date    :2025/4/4 21:19 
"""
import requests
import re
# url ='https://www.bilibili.com/video/BV13oZUYGE7d/?spm_id_from=333.337.search-card.all.click'
# url ='https://www.bilibili.com/video/BV13oZUYGE7d'
url='https://www.bilibili.com/video/BV165RBYJEGT/'
# url ='https://www.bilibili.com/x/player/pagelist?'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

response = requests.get(url=url,headers=headers)
pagesource = response.text
# print(pagesource)

obj = re.compile(r'</script><script>.*?},"aid":(?P<aid>\d+),"bvid":.*?,"cid":(?P<cid>\d+),',re.S)
result = obj.finditer(pagesource)
for item in result:
    aid = item.group('aid')
    cid = item.group('cid')
    print(f"aid:{aid}\ncid:{cid}")

# obj = re.compile(r'')


# 上面的代码用于解决aid和cid的问腿,就是没有cid和aid每次复制链接来获取sid会很麻烦
# import requests
# def getsid(url):
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
#     }
#
#     response = requests.get(url=url, headers=headers)
#
#     res = response.cookies.get_dict()
#     print(res)
#     return res
# if __name__ == '__main__':
#     url = '''
#         https://api.bilibili.com/x/player/wbi/v2?aid=114245610181916&cid=29196550879
#         '''
#     result = getsid(url).get('sid')
#     print(result)