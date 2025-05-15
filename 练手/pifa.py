import requests
import time
from urllib.parse import quote

# 替换为你自己的 Cookie（从浏览器复制）
cookie = 'BAIDUID_BFESS=B4EDC01785C427276A44CF99A1D85583:FG=1; BAIDU_WISE_UID=wapp_1734689414778_990; ZFY=CBe9JsPTqwNyZVuNFnDahBXJYE5tty:AA5ZVG1:ANsWF0:C; MCITY=-218%3A; BIDUPSID=B4EDC01785C427276A44CF99A1D85583; PSTM=1735734885; H_PS_PSSID=61027_61391_61445_60853_61491_61524_61521_61497_61561_61607_61633; __bid_n=1951819a9871328f98f0db; BDUSS=ktVUFpMjg5Sm5-TzEzSE13b09oS05uQngwOWItVXlSMmYxdjJlN1FTUGJGTnhuSVFBQUFBJCQAAAAAAAAAAAEAAABM~SP2zNLPwvXobwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANuHtGfbh7RndX; BDUSS_BFESS=ktVUFpMjg5Sm5-TzEzSE13b09oS05uQngwOWItVXlSMmYxdjJlN1FTUGJGTnhuSVFBQUFBJCQAAAAAAAAAAAEAAABM~SP2zNLPwvXobwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANuHtGfbh7RndX; jsdk-uuid=a5ac097c-e652-4c9a-8c82-ab8621133d70; BDB2BID=B4EDC01785C427276A44CF99A1D85583:FG=1; B2B_AB_FCT2=46580207; Hm_lvt_77fe88a330b395c39e37e1ea1cea9a8c=1747313256; HMACCOUNT=36598DCD2F5A4067; B2B_AB_SID=258_278_344_357_370_382_389_505_521_531_545_582_586_588_597_600_612_621_724_736_740_766_789_780_783_792_796_799_800_802_817_892_895_903_908_910_918_923; B2B_SE_HISTORY_WL=%5B%7B%22_w%22%3A%22%E5%B9%BF%E5%91%8A%22%2C%22_t%22%3A1747315233%7D%2C%7B%22_w%22%3A%22%E6%89%B9%E5%8F%91%E4%BB%B7%E6%A0%BC%22%2C%22_t%22%3A1747315080%7D%5D; Hm_lpvt_77fe88a330b395c39e37e1ea1cea9a8c=1747315234; ab_sr=1.0.1_ZGRiNmYxZTYxNjQwMDAzNzlmNDNkZTdjYmYwNmMzNzg4ZDM2YmU4YmJkMTAxNGYzZTA1MzE5YzgxNjk4YWY0YTI3OTUwMWFhOWNlZDJhOThiY2ZhMThiYjI1MWU2Y2EwODIzODdjNWZkMWUxNzRkZDFhOTE0YjhmOWZkYTM4NTE2OWViZjRlM2Y2Njg1NzEyOGE5YmExZGY3MzQyODQ1ZTY1NDQ1N2M2ZTZlYjEzOGIzMzJmZDE5ZDY0MjE3M2E1; RT="z=1&dm=baidu.com&si=858fcdb5-f37e-495c-8ad0-f1f11a38f4c4&ss=mapd73eq&sl=17&tt=khbg&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=19w0l"'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://b2b.baidu.com/s?q=%E5%B9%BF%E5%91%8A&from=search&fid=0%2C1747313254529&pi=b2b.s.search...9616176037079317",
    "Cookie": cookie
}

# 构造参数
params = {
    "ajax": 1,
    "csrf_token": "2a56fc40ee3c967bd71955011dabd222",
    "logid": "3979741574858822707",
    "fid": "0,1747313254529",
    "_": int(time.time() * 1000),
    "q": "广告",  # 搜索词
    "from": "search",
    "pi": "b2b.s.search...9616176037079317",
    "o": 0,
    "p": 2,   # 第一页
    "mk": "全部结果",
    "f": "[]",
    "s": 30,  # 每页30条
    "adn": 0,
    "resType": "product",
    "fn": '{"brand_name":"品牌","select_param1":"制作类型","select_param2":"展示方式"}'
}

url = "https://b2b.baidu.com/s/a?"

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()

    # 提取总结果数（用于确认）
    total = len(data.get("data", {}).get("productList", []))
    print(f"共找到 {total} 条商品结果：")

    # 遍历 productList
    for item in data.get("data", {}).get("productList", []):
        title = item.get("fullName")  # 商品标题
        price = item.get("price")  # 价格
        unit = item.get("unit")  # 单位
        supplier = item.get("fullProviderName")  # 供应商名称
        link = item.get("jumpUrl")  # 跳转链接
        location = item.get("location")  # 所在地

        print("-" * 60)
        print(f"标题: {title}")
        print(f"价格: {price} {unit}")
        print(f"商家: {supplier}")
        print(f"所在地: {location}")
        print(f"链接: {link}")
else:
    print("请求失败，状态码：", response.status_code)
    print(response.text)