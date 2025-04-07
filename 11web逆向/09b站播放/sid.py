"""
@File    :sid.py
@Editor  : 百年
@Date    :2025/4/4 13:47 
"""
import requests
def getsid(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)

    res = response.cookies.get_dict()
    print(res)
    return res
if __name__ == '__main__':
    url = '''
        https://api.bilibili.com/x/player/wbi/v2?aid=114245610181916&cid=29196550879&isGaiaAvoided=false&web_location=1315873&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEludGVsLCBJbnRlbChSKSBVSEQgR3JhcGhpY3MgNjMwICgweDAwMDAzRTlCKSBEaXJlY3QzRDExIHZzXzVfMCBwc181XzAsIEQzRDExKUdvb2dsZSBJbmMuIChJbnRlbC&dm_img_inter=%7B%22ds%22:[],%22wh%22:[2462,1329,24],%22of%22:[376,752,376]%7D&w_rid=2abe6e7b0048cd1a594a33539097ea18&wts=1743744957
        '''
    result = getsid(url).get('sid')
    print(result)