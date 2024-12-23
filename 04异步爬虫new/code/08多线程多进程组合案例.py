"""
@File    :08多线程多进程组合案例.py
@Editor  : 百年
@Date    :2024/12/23 12:24 
"""
'''
进程1 从主页面中获取详情页面的url，然后从详情页中提取到图片的下载地址
进程2 然后把拿到的下载地址进行下载'''
# //div[@class='bot-div']/a/@href <--获取详情页面的链接，注意需要进行拼接
# //div[@class='item masonry-brick']/img/@src
# IMPORTANT:一定要注意到一个问题，那就是两个进程之间是相互独立的，它们没办法传递值，
#  所以需要中间件(middleware)，这个中间件可以是mysql,redis,mongodb，知道这个就好办了
#  即第一个进程将获取到的链接存储到数据库中,然后第二个进程从数据库中读取链接来下载图片
#  但是这里不用那些，而是用队列来实现我们的需求，队列是走网卡的，内部是个sockit
#  队列可以实现进程间的通信
import requests
import random
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing import Process,Queue #important:注意我们要使用的是multiprocessing下的队列而不是python带的哪个普通的队列
from lxml import etree
from urllib import parse
# 构造headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1660.57",
}
# 构造代理池
proxies_pool = [
    {'http': '114.232.109.88:8089'},
    {'http': '114.231.42.23:8888'},
    {'http': '113.223.215.204:8089'},
    {'http': '117.69.236.23:8089'},
    {'http': '120.55.37.254:80'},
    {'http': '111.225.152.116:8089'},
    {'http': '36.6.145.4:8089'},
    {'http': '118.178.239.78:80'},
    {'http': '117.71.155.32:8089'},
    {'http': '117.57.92.25:8089'},
    {'http': '114.231.45.207:8888'},
    {'http': '113.223.214.141:8089'},
    {'http': '114.231.82.16:8089'},
    {'http': '111.225.152.64:8089'},
    {'http': '113.223.213.132:8089'},
    {'http': '117.69.233.129:8089'},
    {'http': '119.183.249.236:9000'},
    {'http': '36.6.145.95:8089'},
    {'http': '36.6.145.83:8089'},
    {'http': '117.69.233.19:8089'},
    {'http': '113.121.22.221:9999'},
    {'http': '183.164.242.59:8089'},
    {'http': '117.69.233.60:8089'},
    {'http': '121.41.79.83:80'},
    {'http': '42.63.65.99:80'},
    {'http': '36.6.144.210:8089'},
    {'http': '36.6.144.113:8089'},
    {'http': '183.164.243.43:8089'},
    {'http': '123.56.13.137:80'},
    {'http': '117.69.236.25:8089'},
    {'http': '117.71.154.141:8089'},
    {'http': '121.40.160.78:80'},
    {'http': '42.63.65.78:80'},
    {'http': '106.14.255.124:80'},
    {'http': '125.87.94.168:8089'},
    {'http': '47.94.207.215:3128'},
    {'http': '42.63.65.19:80'},
    {'http': '223.100.178.167:9091'},
    {'http': '117.70.49.102:8089'},
]


# 需要做两件事，第一件事是去获取二级页面的链接
# 第二件事是对二级页面中的图片进行下载

# 定义进程1的目标函数方便获取图片链接
def get_img_src(q):
    proxies = random.choice(proxies_pool)
    url = 'https://sc.chinaz.com/tupian/dongwutupian_2.html'
    response = requests.get(url=url, headers=headers, proxies=proxies)
    content = response.text
    # print(content)
    tree = etree.HTML(content)
    imgsrclst = tree.xpath('//div[@class="bot-div"]/a/@href')
    # for i in range(len(imgsrclst)):
    #     # newurl = 'https://sc.chinaz.com/' + imgsrclst[i].strip()
    #     # IMPORTANT:新招数
    #     newurl = parse.urljoin(url,imgsrclst[i].strip())
    #     # print(newurl) important:打印看看是否获取到正确的二级页面地址
    #     newresponse = requests.get(url=newurl, headers=headers, proxies=proxies)
    #     newcontent = newresponse.text
    #     newtree = etree.HTML(newcontent)
    #     # important:注意下面这行代码也可使用parse.urljoin，但是就不改了
    #     imgsrc = 'https:' + newtree.xpath('//div[@class="img-box"]/img/@src')[0]
    #     print(imgsrc)#IMPORTANT:打印一下看看是否获取成功
    #     # return imgsrc

    # 新写法
    for imgsrc in imgsrclst:
        # IMPORTANT:新招数
        newurl = parse.urljoin(url, imgsrc)
        newresponse = requests.get(url=newurl, headers=headers, proxies=proxies)
        newcontent = newresponse.text
        newtree = etree.HTML(newcontent)
        # important:注意下面这行代码也可使用parse.urljoin，但是就不改了
        imgsrc = 'https:' + newtree.xpath('//div[@class="img-box"]/img/@src')[0]
        print(imgsrc)  # IMPORTANT:打印一下看看是否获取成功
#       IMPORTANT:下面往队列里装入我们获取到的图片链接
        q.put(imgsrc)
        print(f'{imgsrc}被写入队列')
    q.put('队列空了') #所有的都被放入队列后就结束
# 定义进程2的目标函数用于下载图片
def download(url):
    print('开始下载')
    name = url.split('/')[-1]

    with open(f'../imgs/{name}','wb') as fp:
        response = requests.get(url)
        content = response.content #important:注意要获取二进制数据要用的是.content
        fp.write(content)
    print('下载完毕')


def download_img(q):
    # important:构造线程池
    with ThreadPoolExecutor(10) as t:
        while 1:
            src = q.get() #从队列中拿出数据，如果get不到东西会进行阻塞操作，该进程将会卡住不动，程序不停止
            # 所以我们必须加上一个判断条件，现在进程一中添加条件，如果获取到队列空了那么久终止循环
            if src == '队列空了':
                break
            else: #如果不是'队列空了'那么就从队列中获取数据
                t.submit(download,src) #将获取到的src提交给目标函数download,传入的参数是src

if __name__ == '__main__':
    # get_img_src() important:先在非多进程模式下的代码运行一次看看代码大体上有没有问题
    # 构造队列
    q = Queue()
    # IMPORTANT:一定要注意，要先构造队列并将队列作为参数传入到进程的目标函数中去
    p1 = Process(target=get_img_src,args=(q,))
    p2 = Process(target=download_img,args=(q,))

    p1.start()
    p2.start()
