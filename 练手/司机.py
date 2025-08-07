"""
@File    :司机.py
@Editor  : 百年
@Date    :2025/7/31 15:29 
"""
import requests

url = 'https://api.honghusaas.com/biz-api/v1/workbench/governance/detail/index'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'Cookie':'login_type=2; ticket=QYNLfstbSYdvac6ZEQ3i3jBCfUTdKKXK9jFLA7JOfHAkzDmOwzAMQNG7_JowSImyTLbTzx1mcZZGARKkMnz3wEn1urcxlKROOinCMNKEUUhzrarCqOSBk9abay29hDAaydc3wg8Jwi-5uHvvXaO1sKXMFsI_6Sqs5Mbj9rz_rWRXVduF07us4XM9yjOJtVb6HBatIlw-9ZXU_RUAAP__'
}

data={
    'case_id':'144115297787428212'
}

resp = requests.post(url=url,headers=headers,data=data)

print(resp.json())