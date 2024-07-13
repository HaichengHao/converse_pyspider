# @Editor    : 百年
# @FileName  :03_代理的补充.py
# @Time      :2024/7/11 16:55
# 因为已经是第二遍过代理相关的内容
'''
之前写的代理池的样式都是这样的
import random
proxies_pool = [
    {'http': '120.79.21.48:8089'},
    {'http': '42.63.65.103:80'},
    {'http': '117.71.132.220:8089'}
    ]
proxies=random.choice(proxies_pool)
response = requests.get(url,headers,proxies=proxies)


其实也可以这样写
proxies={
    'http://120.79.21.48:8089',
    'http://42.63.65.103:80',
    'http://117.71.132.220:8089
    }
response = requests.get(url,headers,proxies=proxies)
'''