from functools import partial
import subprocess
subprocess.Popen = partial(subprocess.Popen,encoding='utf-8')
import execjs
import requests
url = 'https://ctbpsp.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/1?province=&industry=&type__1017=n4%2BxnDBDgDcDy0DRDxlxGhbCo0QlAhIpPrID'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}

response = requests.get(url=url,headers=headers)
response.encoding = response.apparent_encoding
print(response.text)

ciphertext = response.text
# print(ciphertext)
with open('demojs.js','r',encoding='utf-8') as fp:
    ctx = execjs.compile(fp.read())


import base64

# 将 ciphertext 转换为 Base64 字符串
encoded_ciphertext = base64.b64encode(ciphertext.encode('utf-8')).decode('utf-8')

# 传入 JS 函数时使用 Base64 字符串
result = ctx.call('decryptByDES', encoded_ciphertext)
# result = ctx.call('decryptByDES',ciphertext.encode('utf-8'))
print(result)
