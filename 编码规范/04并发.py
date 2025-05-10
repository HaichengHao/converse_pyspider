"""
@File    :04并发.py
@Editor  : 百年
@Date    :2025/5/10 16:39 
"""
import requests
from concurrent.futures import ThreadPoolExecutor
import threading
import os

RLOCK = threading.RLock()


def task(password):
    # 1.requests发请求，给你一个手机（卡商 ）
    res = requests.get(".......")
    phone = res.json()['data']['phone']

    # 2.注册
    requests.post(
        url="...",
        data={
            'phone': phone,
            'password': password,
        }
    )

    # 3.文件名
    file_name = "xxxx-{}.txt".format(threading.current_thread().ident) #threading.current_thread().ident获取的是线程id
    with open(file_name, mode='a+', encoding='utf-8') as f:
        f.write(".....")


def run():
    password = "qwe123"
    pool = ThreadPoolExecutor(40)
    for i in range(100000):
        pool.submit(task, password)


        pool.shutdown()# 等待，等待40个线程吧100000个任务全部执行完毕（等待线程池中的任务执行完毕）并非字面意思上的关闭线程池

    # 获取目录下的所有文件合并
    for name in os.listdir("xxx/xxx/xx/dist"):
        pass


if __name__ == '__main__':
    run()