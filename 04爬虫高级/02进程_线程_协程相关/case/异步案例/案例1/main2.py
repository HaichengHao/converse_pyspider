# @Editor    : 百年
# @FileName  :main.py.py
# @Time      :2024/7/29 7:45
import requests
# 导入线程池模块
from multiprocessing.dummy import Pool
'''按住ctrl并将鼠标移动到Pool可以查看Pool的细节
def Pool(processes=None, initializer=None, initargs=()):
    from ..pool import ThreadPool
    return ThreadPool(processes, initializer, initargs)
    
    process : 即线程任务数量，默认为None,可以自己指定
    initializer : 初始化
    '''
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

# 创建一个线程池对象
pool = Pool(processes=3) #数字3:因为我们本次请求只有3个url,所以线程池的大小设置为3就足够了，也就是设置三个线程
# 当然，如果我们不使用另外的参数，按顺序来说直接写成 pool = Pool(3) 也是完全可以的
pool.map(get_request,urls)
# map(self,func,iterable)
# 指定函数为get_request,指定的可迭代对象是urls列表，这样就可以给列表中的每个url都设置为线程

# 线程池使用完毕之后记得释放
pool.release()
'''
详细:pool.map(get_request,urls)的三次执行
第一次,拿出urls列表中的第0个元素'http://127.0.0.1:5000/bobo',并将其传入get_requests中
第一次,拿出urls列表中的第1个元素'http://127.0.0.1:5000/tom',并将其传入get_requests中
第一次,拿出urls列表中的第2个元素'http://127.0.0.1:5000/jay',并将其传入get_requests中'''
""" 这里我们用的map是这样的描述
    def map(self, func, iterable, chunksize=None):
        '''
        Apply `func` to each element in `iterable`, collecting the results
        in a list that is returned. 
        使func对可迭代对象中的每一个元素都应用上去，收集结果并返回一个列表对象
        '''
        return self._map_async(func, iterable, mapstar, chunksize).get()"""


'''我们在main.py里的写法，其实本次main2.py就是利用进程池将下面的繁琐步骤封装起来了
ts = []
for url in urls:
    # 循环遍历urls列表，为每个url都设置为线程对象
    # 那么这里你可能会问为什么都是t呢？不会乱么?
    # 请回看列表的元素的属性以及集合的元素的属性
    # 集合中是不会出现{t,t,t}这样的，集合会默认去除掉重复的数据
    # 但是列表可以[t,t,t]，所以这里并没有写错，运行试试就知道了
    t = Thread(target=get_request,args=(url,))
    ts.append(t)
    t.start()
#     循环遍历，让每个线程都加入到主程序结束之前，注意，这里还是按序加入
for t in ts:
    t.join()  # 主线程在所有线程都执行完后才结束'''
print(time.time()-start_time) #程序运行的总耗时

'''
解决大规模服务请求的终极方案——使用协程
'''

