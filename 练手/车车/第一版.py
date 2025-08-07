import time
from DrissionPage import ChromiumPage
from lxml import etree
import csv

# 初始化CSV文件
fp = open('./driver_data.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(fp)
if fp.tell() == 0:
    writer.writerow(['姓名', '手机号', '身份证号', '车牌号'])

# 初始化浏览器
page = ChromiumPage()

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
#点击登录
dh = page.ele('xpath:/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div[2]')
dh.click()
time.sleep(1)

# 导航到治理页面
zhili = page.ele('xpath://*[@id="w-layout-main"]/aside/div[1]/ul/li[6]')
zhili.click()
time.sleep(1)

# 点击处置任务
chuzhirenwu = page.ele('xpath://*[@id="_governance_driver-disposal_govern-manage"]')
chuzhirenwu.click()
time.sleep(3)
for i in range(1,11):
    # 点击查看详情
    ckxq = page.ele(f'xpath:/html/body/div[1]/div/section/main/div/div/div[4]/div/div/div/div/div[2]/div/div/table/tbody/tr[{i}]/td/div/button[1]',timeout=15)
    ckxq.click()
    time.sleep(3)

    tree0 = etree.HTML(page.html)
    sjid = tree0.xpath('/html/body/div[1]/div/section/main/div/div/div/div/div[2]/div[1]/div[1]/div/table/tbody/tr[1]/td/span[2]/a/text()')[0]

    # 直接访问司机详情页
    driver_url = f'https://workbench.honghusaas.com/#/driver/driver-manage/driver-detail?driverId={sjid}&companyId=1038'
    page.get(driver_url, timeout=2)
    page.wait.load_start()

    # 点击司机详情
    sjxx = page.ele('xpath://div[@data-node-key="driverDetail"]')
    sjxx.click()
    # page.wait.load_start()
    # time.sleep(4)

    # 点击复制按钮获取信息
    page.ele('xpath://*[@id="rc-tabs-0-panel-driverDetail"]//div[1]//tbody/tr[1]/td[1]/span/div/span/*[name()="svg"]').click()
    page.ele('xpath://*[@id="rc-tabs-0-panel-driverDetail"]//div[1]//tbody/tr[2]/td[2]/span/div/span/*[name()="svg"]').click()
    page.ele('xpath://*[@id="rc-tabs-0-panel-driverDetail"]//div[1]//tbody/tr[3]/td[1]/span/div/span/*[name()="svg"]').click()
    time.sleep(2)

    # 获取司机信息
    tree = etree.HTML(page.html)
    drivername = tree.xpath('//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[1]/td[1]/span/div/text()')[0]
    phonenumber = tree.xpath('//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[2]/td[2]/span/div/text()')[0]
    idcardnumber = tree.xpath('//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[3]/td[1]/span/div/text()')[0]

    # 切换到车辆详情
    clxx = page.ele('xpath://*[@id="rc-tabs-0-tab-carDetail"]')
    clxx.click()
    time.sleep(2)

    # 车牌号
    page.ele('xpath://*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/span/*[name()="svg"]').click()
    time.sleep(2)

    # 获取车牌号
    tree2 = etree.HTML(page.html)
    carDetail = tree2.xpath('//*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/text()')[0]

    # 输出并写入CSV
    print(f'司机名:{drivername},司机手机号:{phonenumber},司机身份证号:{idcardnumber},车牌号{carDetail}')
    writer.writerow([drivername, phonenumber, idcardnumber, carDetail])

    # # 返回第2页
    # page.back()  # 返回一次
    # page.wait.load_start()  # 等待页面加载
    # time.sleep(1)  # 确保完全加载
    #
    # # 再返回第1页
    # page.back()  # 返回第二次
    # page.wait.load_start()  # 等待页面加载
    # time.sleep(1)  # 确保完全加载
    # 返回列表页（直接跳转，避免 back() 问题）
    page.get('https://workbench.honghusaas.com/#/governance/driver-disposal/govern-manage')
    time.sleep(2)  #
# 关闭文件
fp.close()