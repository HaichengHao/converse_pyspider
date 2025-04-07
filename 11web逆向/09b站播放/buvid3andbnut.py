"""
@File    :buvid3andbnut.py
@Editor  : 百年
@Date    :2025/4/2 10:47 
"""

# 获取buvid3和bnut
import time
import requests

session = requests.session()


# tips:将其封装成一个函数
def get_buvid3(url, headers):
    # url = 'https://www.bilibili.com/video/BV15rfTYNE7E/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=00d2dd5133ec16ea14325748b3de9d7'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    # }

    resposne = requests.get(url=url, headers=headers)
    # 将响应头的cookies转换为字典
    res = resposne.cookies.get_dict()

    print(res) #打印查看结果
    # {'buvid3': '57EA94B7-BB33-257B-E5A3-F9434A836E8873453infoc', 'b_nut': '1743662473'}
    buvid3 = res.get('buvid3') #只获取buvid3
    bnut = res.get('b_nut')
    return buvid3,bnut

if __name__ == '__main__':
    # url = 'https://www.bilibili.com/video/BV15rfTYNE7E/?spm_id_from=333.1007.tianma.1-1-1.click&'
    url = 'https://www.bilibili.com/video/BV15rfTYNE7E/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }
    res = get_buvid3(url=url,headers=headers)
    bvid3 = res[0]
    bnut = res[1]
    print(bvid3,bnut)
