"""
@File    :03小工具.py
@Editor  : 百年
@Date    :2025/4/19 16:55 
"""
import json
def parse(src):
    # src = 'vkey=13FF1ABA78AEF5F2D2B7D9CF15CE2D83CC567FC8376079F9AB94390FA68339535553E44C2A3FC7B5547BED0FF18B9F22DD32F5FF59B304E6204A3D5899D17526C060501E06EBBF01501CF4FF54240D0BCC5BE1C71C7B6B5B56A01F5848978B7272D5350D50AB04FB5FE46C98354D9199&app_id=519748109&guid=m9nyrwv0_nf3vm13iva&ysign=df2c7e756079877e53dc61c445c3f23d&ytime=1745051813&ytype=1'
    # result = src.split('&')
    # for res in result:
    #     print(res.split('='))
    dic = {res.split('=')[0]:res.split('=')[1] for res in f"{src}".split('&')}
    # print(dic)
    final_res = json.dumps(dic,indent=2)
    # print(final_res)
    return final_res

# 3b3f2ba859047a7cc3851d36b6c63778
# if __name__ == '__main__':
if __name__ == '__main__':
    src = input('输入src>>')
    res = parse(src)
    print(res)

'''
{
  "vkey": "D2CEDC2C514F445DAC8FD00DFFAC1B3BF4AD130E60F1DA624ED6159D2AD83F192C2335998BC78B2AC5FA2C1C0C04411B0A8C581C4EE255481EC24AD481A81D9ECFBF8A47C1932DC34B99F7B13832B8334D5B0E487942D5863532FB1C9343CD14038F8ACC91AB1E4BEE33D327604E9B45",
  "app_id": "519748109",
  "guid": "m9nyrwv0_nf3vm13iva",
  "ysign": "4dc50e2ac928c649d1ee5f095abedcee",
  "ytime": "1745059166",
  "ytype": ""
}'''
'''
{
  "vkey": "EF661BC2C33E6066ACBDF2B91EC0693D1D61B3126A79BACFF287D68BA1ADE4986E6865D0B8638B623CEAA03643827602FC179838A984EF1D3B1102511389B706807AB4231EF21D4C21F1DC2990723A667665BCCA9460247D0BA3EF94222FF8CEF4FAA8DA33A710396EC08C20D1CAA914",
  "app_id": "519748109",
  "guid": "m9nyrwv0_nf3vm13iva",  <--居然没有发生任何变化
  "ysign": "7d3e38d532c4071e9a9789e8b2032528",
  "ytime": "1745060588",
  "ytype": "1"
}'''
'''
{
  "vkey": "0AAF0B5BABE0B215135B167073013B33589B040BF76069BA9DE368CC46E2E012389236C7C322A7E4A1356BF10F5019268D5D5F0CDB1802670BCB425337101A97610BD51FC8F3D2F20AD077DBCB996179B136CABD5257D19A1386D84FF41742CD4005391930094641C996257A3968B8EF",
  "app_id": "519748109",
  "guid": "m9nyrwv0_nf3vm13iva",
  "ysign": "30e9e267c5af22dd1fb3a67eff36537f",
  "ytime": "1745060855",
  "ytype": "1"
}

'''

'''
{
  "vkey": "C49FF7694A98D9CFF637F6EB51645CF04153E014CBC94BAD1735827899C68CC0BB3C5E9F11520EEAFF7EF41D910DF059DA1D298CAA20BA866E522CD57E9D6837C2510278E26FE9EADB9DF85C7F5AE37488D8911FF57374A7C5B99FA471A5F6A3A50B730DDD69B9933AD8AD6558579DDC",
  "app_id": "519748109",
  "guid": "m9p1hvbq_63q9hxqepo2", <--guid发生变化
  "ysign": "c727bafc3b746d5f57d6148c66fcff9e",
  "ytime": "1745116856",
  "ytype": "1"
}
'''