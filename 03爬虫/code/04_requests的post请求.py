# editor: 百年
# time: 2024/3/18 19:28
import requests
url='https://fanyi.baidu.com/sug'
headers={
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Cookie':'BIDUPSID=CA59DFBCAA61D8EFEB819A18BBC5F507; PSTM=1707878929; APPGUIDE_10_6_9=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=mJsaVAyekljQ1c3WU5aN2F3Z25PVVUyYzlEMXFzQzE5ZDBOdWlyY0hlZGNKaDVtRVFBQUFBJCQAAAAAAAAAAAEAAABM~SP2zNLPwvXobwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFyZ9mVcmfZld; BDUSS_BFESS=mJsaVAyekljQ1c3WU5aN2F3Z25PVVUyYzlEMXFzQzE5ZDBOdWlyY0hlZGNKaDVtRVFBQUFBJCQAAAAAAAAAAAEAAABM~SP2zNLPwvXobwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFyZ9mVcmfZld; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=39661_40206_40211_40079_40352_40368_40379_40402_40415_40011_40301; PSINO=1; BAIDUID=8E528E25A8C7DE301AD3427034A22190:SL=0:NR=10:FG=1; BA_HECTOR=810h84212g8h252180008l2kpg5bbr1ivg3ta1t; BAIDUID_BFESS=8E528E25A8C7DE301AD3427034A22190:SL=0:NR=10:FG=1; ZFY=5Kz2gQMC:Avj4FNaWiHkIGn10Wx9t5XELmZG6qfIzq4k:C; APPGUIDE_10_7_1=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1710761343; ab_sr=1.0.1_NDZmMGJkNDRlM2Y1MWRjYjkwZDQ2YjZmMzZkODFjNzc1OTA1MzAzZjZmMzM1YjdmYjNkYjFhZTE0ODliOWYxMzdjNGJhMGZkNGJlNDM4YTE3NTA3ZGViYzE0YmFlOGY2N2M4ZGFlN2JhOWNmZmUwMDI4MDg5ZWNmMjY1Mzg1YjQ0NTBmNjViODc0ZTJlOGQxODVkNjFlNTAwN2FmNjMzZGI5ZDNkYWM4ZmU0N2E4ZDVmZGVkYmJkYjZlNjc4NTk5; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1710766257'
}
data={
    'kw':input('请输入一个单词>>>')
}

response=requests.post(url=url,data=data,headers=headers)
response.encoding=response.apparent_encoding
content=response.text  #拿到的是文本
print(content)
print(type(content))
# {"errno":0,"data":[{"k":"spider","v":"n. \u8718\u86db; \u661f\u5f62\u8f6e\uff0c\u5341\u5b57\u53c9; \u5e26\u67c4\u4e09\u811a\u5e73\u5e95\u9505; \u4e09\u811a\u67b6"},{"k":"Spider","v":"[\u7535\u5f71]\u8718\u86db"},{"k":"SPIDER","v":"abbr. SEMATECH process induced damage effect revea"},{"k":"spiders","v":"n. \u8718\u86db( spider\u7684\u540d\u8bcd\u590d\u6570 )"},{"k":"spidery","v":"adj. \u50cf\u8718\u86db\u817f\u4e00\u822c\u7ec6\u957f\u7684; \u8c61\u8718\u86db\u7f51\u7684\uff0c\u5341\u5206\u7cbe\u81f4\u7684"}],"logid":1122094504}
# <class 'str'>
# 可见是json数据，需要转化为字符串，利用反序列化加载为字典
import json
js_content=json.loads(content)
print(js_content)
print(type(js_content))
# {'errno': 0, 'data': [{'k': 'spider', 'v': 'n. 蜘蛛; 星形轮，十字叉; 带柄三脚平底锅; 三脚架'}, {'k': 'Spider', 'v': '[电影]蜘蛛'}, {'k': 'SPIDER', 'v': 'abbr. SEMATECH process induced damage effect revea'}, {'k': 'spiders', 'v': 'n. 蜘蛛( spider的名词复数 )'}, {'k': 'spidery', 'v': 'adj. 像蜘蛛腿一般细长的; 象蜘蛛网的，十分精致的'}], 'logid': 1254957503}
# <class 'dict'>