"""
@File    :txtswtvoice.py
@Editor  : 百年
@Date    :2025/2/18 21:18 
"""
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '117594668'
API_KEY = 'wSZIXJ2vXBRBcagEqsVRoeBl'
SECRET_KEY = 'Uqjr9MHr2ewrZXYxaDrIGSqUVLZAuwZW'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


result  = client.synthesis('天空好像下雨我好想住你隔壁傻站在你家楼下抬起头数乌云', 'zh', 1, {
    'vol': 5,

})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('demovoice.mp3', 'wb') as f:
        f.write(result)