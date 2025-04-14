# """
# @File    :正则验证.py
# @Editor  : 百年
# @Date    :2025/4/14 11:01
# """
# import re
# import requests
# url = 'https://www.iikx.com/sci/medcine/15147.html'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
# }
# response = requests.get(url=url,headers=headers)
# response.encoding = response.apparent_encoding
# page_source = response.text
# print(page_source)
#
# # important:创建正则对象准备匹配全部内容
# content = re.compile(r'.*?<div class="coverbox"><img src=(?P<imgsrc>.*?) alt=.*?',re.S)
# result = content.finditer(page_source)
# for item in result:
#     imgsrc = item.group("imgsrc")
#     print(imgsrc)


import re
import requests

# 请求网页数据
url = 'https://www.iikx.com/sci/medcine/15147.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding  # 设置正确的编码
page_source = response.text

# 创建正则对象准备匹配全部内容
# 改进正则表达式，确保更精确地匹配 <img> 标签的 src 属性
content = re.compile(
    # r'<div class="coverbox">\s*<img\s+src="(?P<imgsrc>[^"]+)"\s+alt=',
    r'<div class="coverbox">\s*<img\s+src="(?P<imgsrc>[^"]+)"\s+alt=*<ul class="siteitem"><li><strong>所属分类：</strong>*<a href="/sci/"(?P<leibie>)',
    re.S
)

# 使用 finditer 提取匹配结果
result = content.finditer(page_source)
for item in result:
    imgsrc = item.group("imgsrc")
    print(f"提取到的图片链接: {imgsrc}")

# 如果没有任何匹配结果，则提示用户
if not list(result):
    print("未找到匹配的图片链接，请检查正则表达式或网页内容是否发生变化。")