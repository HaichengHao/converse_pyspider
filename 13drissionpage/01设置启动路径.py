# @Author    : 百年
# @FileName  :01设置启动路径.py
# @DateTime  :2025/5/30 19:10

'''
如果00的步骤提示出错，说明程序没在系统里找到 Chrome 浏览器。
可用以下其中一种方法设置，设置会持久化记录到默认配置文件，之后程序会使用该设置启动。'''
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions

#指定浏览器的路径,可在搜索框中输入chrome://version查看
chrome_path =r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# ChromiumOptions().set_browser_path(chrome_path).save()
#上面那段代码会将浏览器路径记录到配置文件,今后启动浏览器皆以新路径为准
# 另外，如果是想临时切换浏览器路径以尝试运行和操作是否正常，可以去掉 .save()，以如下方式结合第1️⃣步的代码。
ChromiumOptions().set_browser_path(chrome_path)

#创建page对象
page = ChromiumPage()
page.get('https://www.bilibili.com')