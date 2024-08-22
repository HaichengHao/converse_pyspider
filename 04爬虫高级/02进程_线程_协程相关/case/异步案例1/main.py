# @Editor    : 百年
# @FileName  :main.py.py
# @Time      :2024/7/29 7:45
import requests
import time
from threading import Thread
start_time = time.time()
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/tom',
    'http://127.0.0.1:5000/jay'
]

def get_request(url):
    page_text = requests.get(url=url).text
    print(len(page_text))

ts = []
for url in urls:
    t = Thread(target=get_request,args=(url,))
    ts.append(t)
    t.start()
for t in ts:
    t.join()  # 主线程在所有线程都执行完后才结束

    # get_request(url)
print(time.time()-start_time) #程序运行的总耗时

# 非多线程写法
# 2322
# 956
# 509
# 6.048828601837158 <--非多线程写法耗时几乎为6s


# 多线程写法
# 509
# 2322
# 956
# 2.022538661956787