# @Author    : 百年
# @FileName  :lj.py
# @DateTime  :2025/3/17 14:37


import requests
from lxml import etree
from fake_useragent import UserAgent

url = 'https://sy.lianjia.com/ershoufang/'
ua = UserAgent().random
print(ua)
cookie_string ='SECKEY_ABVK=Iqm1vhnygbjpblU09CMZInHX+sYNuYjB/O1csA3KLgc%3D; BMAP_SECKEY=YxM_L4k9wp0RFzTeX-3NbtflX97Gt09mF4b92qjE6QzLPFWXag0kDOyPSbsLLBTGjpdW58EB1jNwUmobm7Sh_IpVHosk7IigL7Hp1t7rGQ1kUr4Y3B-7c8CTkaSyy0eohH0XaYPjl5XW3mEp54JdHAmiCMHu2RhoM8xwinkhcvxA2iEwG-nwvj2AEFNUjWBh; lianjia_uuid=e89eb85e-c5c6-4d23-95d6-d649a40bf152; _ga=GA1.2.838267245.1741587641; lianjia_ssid=89607fa2-dc94-4d89-bd2b-9fbd2fd314da; select_city=210100; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221957eb63914166-0075f0adf84d41-26011a51-1474560-1957eb63915176%22%2C%22%24device_id%22%3A%221957eb63914166-0075f0adf84d41-26011a51-1474560-1957eb63915176%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _gid=GA1.2.794042625.1742192515; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1741587626,1742192503,1742192647,1742193090; HMACCOUNT=5419259C604846BC; login_ucid=2000000472000451; lianjia_token=2.001260f74844d9bd6703cdde794431b0e6; lianjia_token_secure=2.001260f74844d9bd6703cdde794431b0e6; security_ticket=b/0tnr/Yv6QxPOWv9HuXm1T8BypMsVF0RdVu1FNcnwBhzuLNYIrisSd1Wz02chLH6qEuFeFi02/1rewNv5JSIhkA60rY+QglHEm4A24IPV8XPRlmrKPoYlNpsX0pQlFwKMQd4Jvj5BuvO4iV49YZ3/dE2LG8yxETM4NSRQW0D4M=; ftkrc_=0ddf42a3-57c3-453c-ac69-4114a8c4ecb7; lfrc_=af85d3ff-410d-4c7d-ae0d-bf517869c5b8; Hm_lvt_efa595b768cc9dc7d7f9823368e795f1=1742193328; Hm_lpvt_efa595b768cc9dc7d7f9823368e795f1=1742193333; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1742194462; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYmU2NDlkODdkNDBlZjg1MDIyNzhhZjFjMmU4YmI0NGUwODkzZjNkYTU4NjQyODljMTBkMGViOWU0OWUyZDZjZDI1MjM4NzBjOGJiZDJlYTkwODVhOWQ4OTVmMmQ3ZDk2ZDc5M2NjZGUzNjE5NzBjZjdiNWE5NTM2OWRmYzU1OThiM2ZiYTM1NTgwZTZlYmIxMmE0Y2I0ZGI4MzdjZDQ1MDVlNDQ0MWUyODQxOTg4N2EwOWE1NWE0ZjUwZDUzNGZmYzIzOTI0ZTVlN2ZhOWNiZmFhYmRmNWQzYTI2MWZlNTMwZjE1MDU5ZWY4ZDc4MTBiZTkyNTk4OTVlNzVmOTA1ZVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJhNWYyMTE2ZFwifSIsInIiOiJodHRwczovL3N5LmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1'
cookies = {item.split("=")[0]: item.split("=")[1] for item in cookie_string.split("; ")}
headers={
    'User_Agent':ua,
}
response = requests.get(url=url,headers=headers)
print(response.text)
tree = etree.HTML(response.text)
hrefs = tree.xpath('//div[@class="title"]/a/@href')
for href in hrefs:
    print(href)
    new_resp = requests.get(url=href, headers=ua, cookies=cookies)
    newtree = etree.HTML(new_resp.text)
    try:
        infodemo = newtree.xpath('//div[1]/div[@class="content"][1]/ul/li[1]/text()').strip()
        print(infodemo)
    except IndexError:
        print('未获取')
