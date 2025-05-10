"""
@File    :03代理ip生成器.py
@Editor  : 百年
@Date    :2025/5/10 10:24 
"""


# 关键思想:解耦,各项功能各司其职
import requests


def register(proxy_object):
    proxy_dict = next(proxy_object)

    session = requests.Session()
    session.proxies = {
        "http": "{ip}:{port}".format(**proxy_dict),  # "59.63.107.231:19025"
        "https": "{ip}:{port}".format(**proxy_dict),  # "59.63.107.231:19025"
    }
    session.get(".......")
    session.post("......")


def get_proxy_object():
    while True:
        res = requests.get("....?count=100")
        for item in res.json()['obj']:  # 100
            # item = {"port":"19025","ip":"59.63.107.231"}
            yield item


def run():
    proxy_object = get_proxy_object() #tips:先拿到生成器对象
    # while True:
    #     v1 = next(proxy_object)  #拿到生成器中的每一个对象
    #     print(v1)
    for i in range(1000000):
        register()


if __name__ == '__main__':
    run()
