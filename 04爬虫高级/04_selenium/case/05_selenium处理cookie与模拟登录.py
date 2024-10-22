# # @Author    : 百年
# # @FileName  :05_selenium处理cookie与模拟登录.py
# # @DateTime  :2024/10/20 13:54
# '''
# 由于17k小说网禁止调试所以换一个网站
# '''
# import time
# import json
# import requests
# from selenium.webdriver import Chrome
# import requests
# # 创建浏览器对象
# bro1 = Chrome(executable_path='../others/chromedriver.exe')
# bro1.get('https://www.mgshu.cc/user/login.html?jumpurl=undefined')
#
# usr_name = bro1.find_element_by_xpath('/html/body/div[5]/div/p[2]/input')
# pass_word = bro1.find_element_by_xpath('/html/body/div[5]/div/p[4]/input')
# lg_btn = bro1.find_element_by_xpath('/html/body/div[5]/div/p[6]/input')
# # usr_id = int(input('请输入您的账号>>'))
# # passwd = input('输入密码>>')
# usr_name.send_keys('18864771568')
# pass_word.send_keys('HHCzio20.')
#
# time.sleep(2)
# # 点击登录
# lg_btn.click()
#
# # 获取到json_cookie
# json_Cookies = bro1.get_cookies()
# print(json_Cookies)
#
# # 创建一个字典用于接收cookie
# dic = {}
# for item in json_Cookies:
#         key = item['name']
#         value = item['value']
#         dic[key] = value
# print(dic)
# # {'HMACCOUNT': 'AF4C2D07FDB7F6E7', 'Hm_lpvt_0f20b8c5b0d2f108de80ac8128e0c587': '1729407004', 'Hm_lvt_0f20b8c5b0d2f108de80ac8128e0c587': '1729407004'}
# #拿到的是字典,但是放在请求的headers里不能是这个样子的，要对其进行便利,拿出其中的键和值
# '''或者不写在headers里头,直接指定在cookies里头,cookies是可以字典赋值的
# requests.get(url=url,headers=headers,proxies=proxies,cookies=cookies)'''
# # 然后无登录访问书架
# headers = {
#         'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36',
#         # 'Cookie':dic
# }
#
# # id_ = dic[1].values()
# # print(id_)
# # 书架的地址
# book_case_url = 'https://www.mgshu.cc/user/bookcase.html'
# # print(book_case_url)
# # 书架保存书籍的格式是json格式,所有对其进行加载为json数据
# response = requests.get(url=book_case_url,headers=headers,cookies=dic)
# response.encoding = response.apparent_encoding
# content = response.text
# time.sleep(2)
# print(content)
#
# time.sleep(2)
# # 关闭浏览器对象
# # bro1.quit()
# '''
# 1729408371178
# 1729408314
# 1729408223
# '''
# # {
# # 'HMACCOUNT': '06F92273EB881875',
# # 'Hm_lpvt_0f20b8c5b0d2f108de80ac8128e0c587': '1729484252',
# # 'Hm_lvt_0f20b8c5b0d2f108de80ac8128e0c587': '1729484252'}
#
#
#
from selenium.webdriver import Chrome
import time
import json

web = Chrome(executable_path='../others/chromedriver')
web.get('https://www.17k.com/')
time.sleep(3)
# 登录
web.find_element_by_xpath('//*[@id="header_login_user"]/a[1]').click()

# 切换iframe
iframe = web.find_element_by_xpath('/html/body/div[20]/div/div[1]/iframe')
web.switch_to.frame(iframe)

web.find_element_by_xpath('/html/body/form/dl/dd[2]/input').send_keys("18864771568")
web.find_element_by_xpath('/html/body/form/dl/dd[3]/input').send_keys("HHCzio20.")
web.find_element_by_xpath('/html/body/form/dl/dd[5]/input').click()

time.sleep(3)
cookies = web.get_cookies()

# 存文件里
with open("../others/cookies.txt", mode="w", encoding='utf-8') as f:
    f.write(json.dumps(cookies))


# 组装cookie字典, 直接给requests用
dic = {}
for cook in cookies:
    dic[cook['name']] = cook['value']
# 衔接. 把cookie直接怼进去
import requests
#访问的书架（获取书架内容）
url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
headers = {
    'cookie':dic
}
resp = requests.get(url,cookies=dic)
print(resp.text)

web.close()
