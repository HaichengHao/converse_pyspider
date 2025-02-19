"""
@File    :baidu.py
@Editor  : 百年
@Date    :2025/2/18 16:36 
"""
'''

{
    "log_id": 4457308639853058292,
    "items": [
        {
            "score": 0.997762,
            "tag": "iphone"
        },
        {
            "score": 0.861775,
            "tag": "手机"
        },
        {
            "score": 0.845657,
            "tag": "苹果"
        },
        {
            "score": 0.83649,
            "tag": "苹果公司"
        },
        {
            "score": 0.797243,
            "tag": "数码"
        }
    ]
}'''

#百度api自然语言处理之提取置信度高的文本标签
from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '117587424'
API_KEY = 'Zwi5fEC9nH3P32v70SVooMJ8'
SECRET_KEY = 'LoWxISDCgkTkAeX6PDCMep7768gMUiXr'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


title = "iphone手机出现“白苹果”原因及解决办法，用苹果手机的可以看下"

content = "如果下面的方法还是没有解决你的问题建议来我们门店看下成都市锦江区红星路三段99号银石广场24层01室。"

""" 调用文章标签 """
result = client.keyword(title, content)

for dic in result['items']:
    # tips:可以做一个限定来输出得分高（置信度高）的标签
    score = dic['score']
    if score>0.8:
        keyword_tag = dic['tag']
        print(keyword_tag)
