"""
@File    :05异常和重试.py
@Editor  : 百年
@Date    :2025/5/10 19:41 
"""
# import requests
# try:
#
#     phone = requests.get('......卡商的API获取手机号').json()['data']
#
#     while True: #tips:或者自己指定循环次数,即最多重试多少次 for i in range(10)
#         try:
#             v1 = requests.get()  # 异常
#             break
#         except BaseException as e:
#             pass
#
#     v2 = requests.post()
#     v3 = requests.post()
# except BaseException as e:
#     pass

import requests
try:

    phone = requests.get('......卡商的API获取手机号').json()['data']

    for i in range(10):
        try:
            v1 = requests.get()  # 异常
            break
        except BaseException as e:
            pass
    else:
        print('异常')
    v2 = requests.post()
    v3 = requests.post()
except BaseException as e:
    pass