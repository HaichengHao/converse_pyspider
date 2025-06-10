"""
@File    :00老版本.py
@Editor  : 百年
@Date    :2025/6/8 10:14 
"""
import requests
import json
import base64
# 抠图
from PIL import Image

session = requests.session()
inital_url = 'https://beijing.tuitui99.com/denglu.html'

session.headers[
    'User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"

session.get(url=inital_url)

# 接下来访问图片的url
img_url = 'https://beijing.tuitui99.com/tncode.html?t=0.8900648516397043'

img_rsp = session.get(img_url)
with open('./demo.png', 'wb') as f:
    f.write(img_rsp.content)

img = Image.open('./demo.png')
newimg = img.crop((0, 0, 240, 150))  # 左,上,右,下的坐标值,矩形区域
newimg.save("./new.png")


# 计算缺口位置:可以写算法,也可以第三方
def base64_api(img, typeid):
    with open(img, 'rb') as f2:
        base64_data = base64.b64encode(f2.read())
        b64 = base64_data.decode()
    data = {"username": 'ninkofox', "password": 'HHCzio20', "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""


result = base64_api('./new.png', 33)
print(result)


#拿到识别的结果之后便可构造请求
params = {
    'tn_r':result
}
final_res = session.get('https://beijing.tuitui99.com/checkcode.html',params=params)
print(final_res.text)  #产生error可能是距离的问题,第三方平台并不是特别理想

