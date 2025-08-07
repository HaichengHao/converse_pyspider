import json
import time
import DrissionPage
from DrissionPage import WebPage
from lxml import etree
import requests
import csv

# 初始化CSV文件
fp = open('./driver_data.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(fp)
if fp.tell() == 0:
    writer.writerow(['姓名', '手机号', '身份证号', '车牌号'])

# 初始化浏览器
page = WebPage()

# 登录流程
page.get('https://page.honghusaas.com/common/pc-login/v3/index.html?appid=140300&role=3000&source=70001&redirectUrl=https%3A%2F%2Fapi.honghusaas.com%2Fbiz-api%2Fv1%2Fworkbench%2Frbac%2Fuser%2Flogin%3FredirectUrl%3D%252F%252Fworkbench.honghusaas.com%252F%2523%252F%26login_type%3D2#/')
time.sleep(1)

# 输入手机号
sjh = page.ele('xpath:/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div[2]/input')
sjh.clear()
sjh.input('15527691953')
time.sleep(1)

# 输入密码
mm = page.ele('xpath:/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/input')
mm.clear()
mm.input('960000ZW')
time.sleep(1)

# 点击登录
dh = page.ele('xpath:/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div[2]')
dh.click()
time.sleep(3)  # 等待登录完成

# 导航到治理页面并进入处置任务页
zhili = page.ele('xpath://*[@id="w-layout-main"]/aside/div[1]/ul/li[6]', timeout=15)
zhili.click()
time.sleep(1)

chuzhirenwu = page.ele('xpath://*[@id="_governance_driver-disposal_govern-manage"]', timeout=15)
chuzhirenwu.click()
time.sleep(3)

# 获取当前页面所有cookie（返回CookieJar对象）
cookies = page.cookies(as_dict=True)




# # 设置请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
}
# #
data = {
    'page_index': '1',
    'page_size': '100',
    'table_status': '0',
}

page.change_mode()
# # # 使用从浏览器获取的cookies发送请求
page.post(
    url='https://api.honghusaas.com/biz-api/v1/workbench/governance/list/index',
    cookies=cookies,
    headers=headers,
    data=data,
)

# print(page.html)
driverids = page.html
print(type(driverids))
driverids_format = json.loads(driverids)
mylst = driverids_format['data']['list']
print(mylst)

# print()

# # 创建一个空列表用于存储司机ID
driver_ids = [dics['driver_id'] for dics in mylst]
print(driver_ids)

page.change_mode()
for did in driver_ids:
    driver_url = f'https://workbench.honghusaas.com/#/driver/driver-manage/driver-detail?driverId={did}&companyId=1038'
    page.get(driver_url)
    page.wait.load_start()  # 等待页面开始加载
    #等待司机详情标签出现（关键等待）
    page.wait.ele_displayed('xpath://div[@data-node-key="driverDetail"]', timeout=4)

    # 点击司机详情
    sjxx = page.ele('xpath://div[@data-node-key="driverDetail"]')
    sjxx.click()
    time.sleep(1)  # 确保 tab 切换完成

    # 等待并点击显示按钮获取信息
    try:
        page.wait.ele_displayed(
            'xpath:/html/body/div[1]/div/section/main/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[1]/td[1]/span/div/span/*[name()="svg"]',timeout=15)
    except DrissionPage.errors.ElementNotFoundError as e:
        continue
    c1 = page.ele(
        'xpath:/html/body/div[1]/div/section/main/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[1]/td[1]/span/div/span/*[name()="svg"]',
        timeout=3)
    c1.click()
    c2 = page.ele(
        'xpath:/html/body/div[1]/div/section/main/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[2]/td[2]/span/div/span/*[name()="svg"]',
        timeout=3)
    c2.click()
    c3 = page.ele(
        'xpath:/html/body/div[1]/div/section/main/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[3]/td[1]/span/div/span/*[name()="svg"]',
        timeout=3)
    c3.click()
    time.sleep(2)


    # 获取司机信息
    tree = etree.HTML(page.html)
    drivername = \
        tree.xpath(f'//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[1]/td[1]/span/div/text()')[0]
    phonenumber = \
        tree.xpath(f'//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[2]/td[2]/span/div/text()')[0]
    idcardnumber = \
        tree.xpath(f'//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[3]/td[1]/span/div/text()')[0]
    try:
        city = \
            tree.xpath(f'//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/span/text()')[0]
    except:
        city = "暂无"
#
    # 切换到车辆详情
    clxx = page.ele(f'xpath://*[@id="rc-tabs-0-tab-carDetail"]', timeout=2)
    clxx.click()
    time.sleep(3)  # 等待车辆详情加载
    page.wait.ele_displayed(f'xpath://*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/span/*[name()="svg"]')
    try:
        # 点击
        page.ele(
            f'xpath://*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/span/*[name()="svg"]',
            timeout=3).click()
        time.sleep(2)

        # 获取车牌号
        tree2 = etree.HTML(page.html)
        carDetail = \
            tree2.xpath(
                f'//*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/text()')[0]
    except:
        carDetail = "暂无"


    # 输出并写入CSV
    print(f'司机名:{drivername}, 司机手机号:{phonenumber}, 司机身份证号:{idcardnumber}, 车牌号:{carDetail}, 运用城市:{city}')
    writer.writerow([drivername, phonenumber, idcardnumber, carDetail,city])


# 关闭文件
fp.close()
print("数据采集完成！")

