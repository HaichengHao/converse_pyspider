# @Author    : 百年
# @FileName  :11_selenium处理cookie.py
# @DateTime  :2024/10/20 13:32
'''
selenium可以方便的对Cookies进行操作,例如常见的获取Cookies,
示例:
.get_cookies()返回值是由字典组成的列表,叫做jsonCookies
需要将jsonCookies解析成浏览器携带的cookie形式
'''
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
# 创建浏览器对象
bro1 = Chrome(executable_path='../others/chromedriver.exe')
bro1.get('https://www.zhihu.com/explore')
json_Cookies = bro1.get_cookies() #这里拿到的是jsoncookies,我们想要的cookies其实就在jsoncookie之中

print(json_Cookies)
# 这样拿到的是jsonCookies，并不是我们真正要的cookies
'''
[{'domain': '.zhihu.com', 'httpOnly': False, 'name': 'HMACCOUNT', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'C9410B26B31BF1DB'}, {'domain': '.zhihu.com', 'httpOnly': False, 'name': 'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1729403258'}, {'domain': '.zhihu.com', 'expiry': 1763963257, 'httpOnly': False, 'name': 'd_c0', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ACDSU40xahmPTtOxezmBJa8A3nMhMTHDLnk=|1729403258'}, {'domain': '.zhihu.com', 'httpOnly': False, 'name': '_xsrf', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '89384893-1a64-4594-bea6-100ba0459284'}, {'domain': '.zhihu.com', 'expiry': 1760939257, 'httpOnly': False, 'name': 'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1729403258'}, {'domain': 'www.zhihu.com', 'expiry': 1729406857, 'httpOnly': False, 'name': 'BEC', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '32377ec81629ec05d48c98f32428ae46'}, {'domain': '.zhihu.com', 'expiry': 1763963257, 'httpOnly': False, 'name': '_zap', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '5a06cd5b-3a9e-49df-9eb3-16b8ec7c0178'}]
'''
# 解析cookie
dic={}
for cookie in json_Cookies:
    key = cookie['name']
    value = cookie['value']
    dic[key] = value
print(dic)
# 经过处理之后得到的这个就是我们想要的cookies
'''
{'HMACCOUNT': 'C9410B26B31BF1DB', 'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1729403258', 'd_c0': 'ACDSU40xahmPTtOxezmBJa8A3nMhMTHDLnk=|1729403258', '_xsrf': '89384893-1a64-4594-bea6-100ba0459284', 'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1729403258', 'BEC': '32377ec81629ec05d48c98f32428ae46', '_zap': '5a06cd5b-3a9e-49df-9eb3-16b8ec7c0178'}
'''