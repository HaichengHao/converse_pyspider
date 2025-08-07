"""
@File    :all_id.py
@Editor  : 百年
@Date    :2025/7/31 16:02 
"""
from DrissionPage import WebPage
import requests
import csv



#先展开登录逻辑
# page =


fp = open('./driverdata.csv','a+',encoding='utf-8',newline='')
writer = csv.writer(fp)
if fp.tell() == 0:
    writer.writerow(['姓名','ID'])

url = 'https://api.honghusaas.com/biz-api/v1/workbench/governance/list/index'

headers={
    'Cookie':'login_type=2; ticket=zt4zOQgA1gHm1a2DeofK0X5rSqk2KCx2hPvfmO-n6kQkzDtOxUAMQNG93Np6ssfjmdgtPXvgEz7NIIGoouwdhVed7hwspfCb3hRhGWXCapR1dVVhOXXRKZvR1YePJqygeHhEeKJAeKa23vucUzMibWvDUnilwoWdOvj5-v1-2ampqnYKb_-lZ8-8yncKi2hzpGU4wse9_qT0_AsAAP__',
    # 'Cookie':'login_type=2; ticket=dA-gZI2kOPMesQ19w4sW9_wBg6naWxHk_gwTBJKpkEokzDmOwzAMQNG7_JowSEk0JbbTzx1m8SyNAiRIZfjugZPqdW9nKklddFGEaaQJs5DWtKoKs5InjbTwptVLhDCd5O0d4YME4ZPsrbWI0OE-rJfVhvBNugkbuXO73K9fGxmqaofw8yzraL2f5S-JuZdYhw2vCH-v-p_U4xEAAP__',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

data={
    'page_index':1,
    'page_size':20,
    'table_status':0
}

resp = requests.post(url=url,headers=headers,data=data)
json_data = resp.json()
print(
    resp.json()
)

all_ls = json_data['data']['list']
print(all_ls)

for item in all_ls:
    name = item['driver_name']
    driver_id = item['driver_id']
    writer.writerow([name,driver_id])

# fp.close()