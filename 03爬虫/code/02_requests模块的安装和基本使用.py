# editor: 百年
# time: 2024/3/18 17:17
import requests
url='http://www.baidu.com/'
response=requests.get(url)
response.encoding = response.apparent_encoding
content=response.text
print(content)
with open('../others/demohtml.html', 'a+',encoding='utf-8') as wfp:
    wfp.write(content)