"""
@File    :detail_page_rexversion.py
@Editor  : 百年
@Date    :2025/4/14 10:59 
"""
import re
import requests
from lxml import etree
import csv
data_fp = open('./data.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(data_fp)
if data_fp.tell() == 0:
    writer.writerow(['所属分类', '期刊名', '期刊名缩写', '期刊SSN', 'E-ISSN', '影响因子/分区', '学科与分区', '出版国家/地区', \
                     '出刊周期', '出刊年份', '论著文章占比', '是否OA开放时间', 'GoldOA文章占比', '官方网站', '投稿网址', '编辑部地址', '文章目录','图片路径'])
url_lst = [
    # 'https://www.iikx.com//sci/medcine/15147.html',
    # 'https://www.iikx.com//sci/medcine/15693.html',
    # 'https://www.iikx.com//sci/medcine/18770.html',
    # 'https://www.iikx.com//sci/medcine/15740.html',
    'https://www.iikx.com//sci/medcine/10047.html',
    # 'https://www.iikx.com//sci/medcine/17089.html',
    # 'https://www.iikx.com//sci/medcine/10960.html',
    # 'https://www.iikx.com//sci/medcine/9800.html',
    # 'https://www.iikx.com//sci/medcine/14526.html',
    # 'https://www.iikx.com//sci/medcine/33677.html',
    # 'https://www.iikx.com//sci/medcine/10281.html',
    # 'https://www.iikx.com//sci/medcine/18273.html',
    # 'https://www.iikx.com//sci/medcine/51935.html',
    # 'https://www.iikx.com//sci/medcine/17227.html',
    # 'https://www.iikx.com//sci/medcine/15771.html',
    # 'https://www.iikx.com//sci/medcine/10973.html',
    # 'https://www.iikx.com//sci/medcine/11518.html',
    # 'https://www.iikx.com//sci/medcine/15618.html',
    # 'https://www.iikx.com//sci/medcine/14236.html',
    # 'https://www.iikx.com//sci/medcine/12223.html',
    # 'https://www.iikx.com//sci/medcine/13521.html',
    # 'https://www.iikx.com//sci/medcine/12354.html',
    # 'https://www.iikx.com//sci/medcine/19260.html',
    # 'https://www.iikx.com//sci/medcine/10969.html',
    # 'https://www.iikx.com//sci/medcine/18045.html',
    # 'https://www.iikx.com//sci/medcine/15808.html',
    # 'https://www.iikx.com//sci/medcine/12793.html',
    # 'https://www.iikx.com//sci/medcine/16521.html',
    # 'https://www.iikx.com//sci/medcine/19558.html'
]
# url = 'https://www.iikx.com/sci/medcine/15147.html'  # tips:死数据，之后会写活，作为信息传入，这里只是Demo
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
for url in url_lst:
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    page_source = response.text
    tree = etree.HTML(page_source)
    info_lst = tree.xpath('//ul[@class="siteitem"]/li')
    the_class = tree.xpath('//ul[@class="siteitem"]/li[1]/a/text()')
    img_src = tree.xpath('//div[@class="coverbox"]/img/@src')[0]
    print(img_src)
    picname = img_src.split('/')[-1]
    with open(f'./imgs/{picname}','wb') as fp:
        response = requests.get(img_src)
        content=response.content
        fp.write(content)
        print('封面图片下载完毕')
    pic_path = r'./imgs/'+picname
    print(pic_path)

    all_content = tree.xpath(
        '//ul[@class="siteitem"]/li[1]/a[last()]/text()|//ul[@class="siteitem"]/li[2]/text()|//ul[@class="siteitem"]/li[position()>2]/text()|//ul[@class="siteitem"]/li[position()>1]/a/@href|//ul[@class="siteitem"]/li[position()>2]/a/text()')
    print(all_content)
    try:
        fenlei = all_content[0]
        title = all_content[2]
        abbtitle = all_content[3]
        IsSn = all_content[4]
        eSsn = all_content[5]
        JcR = all_content[6]
        xueke = all_content[9]
        contry_area = all_content[10]
        zhouqi = all_content[11]
        year_ = all_content[12]
        zhanbi = all_content[15]
        Oa_ = all_content[16]
        golDoa = all_content[17]
        guanwang = all_content[16]
        tougao = all_content[-4]
        bianjibu = all_content[-3]
        wenzhangmulu = all_content[-2]
        row_data = [fenlei, title, abbtitle, IsSn, eSsn, JcR, xueke, contry_area, zhouqi, year_, zhanbi, Oa_, golDoa,
                    guanwang, tougao, bianjibu, wenzhangmulu,pic_path]
        writer.writerow(row_data)
        print('写入完毕')
    except BaseException as e:
        print(e)
# row_data = [fenlei,title,abbtitle,IsSn,eSsn,JcR,xueke,contry_area,zhouqi,year_,zhanbi,Oa_,golDoa,guanwang,tougao,bianjibu,wenzhangmulu]
# writer.writerow(row_data)
# print('写入完毕')
fp.close()