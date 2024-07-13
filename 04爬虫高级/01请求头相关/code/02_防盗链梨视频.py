# @Editor    : 百年
# @FileName  :02_防盗链梨视频.py
# @Time      :2024/7/11 12:52
# 1 拿到contid
# 2 拿到videoStatus返回的json. -> srcURL
# 3 srcURL里面的内容进行整理
# 4 下载视频
import random
import requests
import json

proxies_pool = [
    {'http': '120.79.21.48:8089'},
    {'http': '42.63.65.103:80'},
    {'http': '117.71.132.220:8089'},
    {'http': '118.31.171.218:80'},
    {'http': '123.182.58.148:8089'},
    {'http': '121.40.110.242:80'},
    {'http': '42.63.65.87:80'},
    {'http': '117.69.232.199:8089'},
    {'http': '183.164.242.146:8089'},
    {'http': '114.251.193.153:3128'},
    {'http': '117.69.233.54:8089'},
    {'http': '36.6.144.93:8089'},
    {'http': '183.164.242.203:8089'},
    {'http': '111.47.170.136:9091'},
    {'http': '221.194.147.197:80'},
    {'http': '36.6.145.68:8089'},
    {'http': '222.190.173.29:8089'},
    {'http': '120.26.93.84:80'},
    {'http': '117.71.133.196:8089'},
    {'http': '61.160.202.123:80'},
    {'http': '117.71.132.10:8089'},
    {'http': '114.231.82.133:8888'},
    {'http': '182.34.101.92:9999'},
    {'http': '183.164.243.125:8089'},
    {'http': '121.41.91.195:80'},
    {'http': '36.6.144.115:8089'},
    {'http': '117.71.155.234:8089'},
    {'http': '117.57.92.102:8089'},
    {'http': '117.71.154.28:8089'},
    {'http': '183.164.243.246:8089'},
    {'http': '117.69.233.47:8089'},
    {'http': '36.6.145.83:8089'},
    {'http': '117.71.149.109:8089'},
    {'http': '59.120.115.117:8080'},
    {'http': '113.121.23.104:9999'},
    {'http': '121.43.103.197:80'},
    {'http': '114.231.82.120:8888'},
    {'http': '36.6.145.44:8089'},
]
proxies = random.choice(proxies_pool)
User_Agent = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR "
    "2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center "
    "PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET "
    "CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR "
    "3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR "
    "2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; "
    ".NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) "
    "Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 "
    "Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 "
    "Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 "
    "TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 "
    "Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 "
    "Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; "
    "360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) "
    "Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 "
    "Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) "
    "Firefox/3.6.10 "
]
base_url = 'https://www.pearvideo.com/video_1795164'
headers = {
    'User_Agent': random.choice(User_Agent),
    #     防盗链:溯源，当前请求的上一级是谁，所以我们直接写成url即可
    # 'Referer': 'https://www.pearvideo.com/video_1795164'
    'Referer': base_url
}
base_url = 'https://www.pearvideo.com/video_1795164'
# video_status = 'https://www.pearvideo.com/videoStatus.jsp?contId=1795164&mrd=0.8094273286075608'

contid = base_url.split('_')[1]
# print(contid)
video_statusurl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contid}&mrd=0.8094273286075608'

response = requests.get(url=video_statusurl, headers=headers, proxies=proxies)
content = response.text
# print(content)
''' 出来了这样的结果，很明显并没有下线，所以我们只是被反爬了,需要在请求头添加防盗链referer，我们观察防盗链居然是视频的网页网址
{
	"resultCode":"5",
	"resultMsg":"该文章已经下线！",
	"systemTime": "1720675366915"
}
'''
'''
加了referer后再次运行，拿到了srcUrl
{
	"resultCode":"1",
	"resultMsg":"success", "reqId":"ddd687fe-4edc-4c5b-b8dd-a96636ffd855",
	"systemTime": "1720684719843",
	"videoInfo":{"playSta":"1","video_image":"https://image1.pearvideo.com/cont/20240708/cont-1795164-71076222.jpg","videos":{"hdUrl":"","hdflvUrl":"","sdUrl":"","sdflvUrl":"","srcUrl":"https://video.pearvideo.com/mp4/short/20240708/1720684719843-71107262-hd.mp4"}}
}
可以看出返回的是json数据，我们要按处理json数据的形式来进行处理
'''
# 先输出返回json数据的response的内容，再利用json索键取值法取到srcUrl的值
json_source = response.json()
# print(json_source)
'''
{'resultCode': '1', 'resultMsg': 'success', 'reqId': '1b5adff3-f722-4ead-bd97-bf102ac1eba3', 'systemTime': '1720685030202', 'videoInfo': {'playSta': '1', 'video_image': 'https://image1.pearvideo.com/cont/20240708/cont-1795164-71076222.jpg', 'videos': {'hdUrl': '', 'hdflvUrl': '', 'sdUrl': '', 'sdflvUrl': '', 'srcUrl': 'https://video.pearvideo.com/mp4/short/20240708/1720685030202-71107262-hd.mp4'}}}'''
# 发现我们要找的srcUrl在videoInfo下的videos下的srcUrl里
srcUrl = json_source.get('videoInfo')['videos'].get('srcUrl')
print(srcUrl)
# https://video.pearvideo.com/mp4/short/20240708/1720685194689-71107262-hd.mp4
# 现在我们拿到了这个srcUrl,但是它并不是最终我们要下载的视频的最终的url,所以，接下来对其进行替换
# 接下来拿到systemTime
systemTime = json_source.get('systemTime')
print(systemTime)
# 1720685194689 <--数值是随着系统时间变化的

# https://video.pearvideo.com/mp4/short/20240708/1720685194689-71107262-hd.mp4 <--无效的视频链接
# https://video.pearvideo.com/mp4/short/20240708/cont-1795164-71107262-hd.mp4 <--真实的视频链接
# 对比发现不同点就是不生效的url恶心人的那一块数字刚好就是系统时间，所以我们把它给替换掉
# 进行替换,得到最终的srcUrl，将系统时间替换为’cont-contid'的样式
srcUrl=srcUrl.replace(f'{systemTime}',f"cont-{contid}")
print(srcUrl)
# https://video.pearvideo.com/mp4/short/20240708/cont-1795164-71107262-hd.mp4 点击发现就是视频链接


# 接下来请求视频链接地址并下载视频
fp=open('../other/demovideo.mp4','wb')
newresp=requests.get(url=srcUrl,headers=headers,proxies=proxies)
newcontent=newresp.content
fp.write(newcontent)
print('程序运行结束')
fp.close()


# 本节最重要的知识点，那就是一定要确定要获取的数据的链接地址是真正的链接地址
