import time
from DrissionPage import ChromiumPage
from lxml import etree
import csv

# 初始化CSV文件
fp = open('./最终数据.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(fp)
if fp.tell() == 0:
    writer.writerow(['姓名', '手机号', '身份证号', '车牌号','地址','颜色','品牌','型号'])

# 初始化浏览器
page = ChromiumPage()

# 登录流程
page.get(
    'https://page.honghusaas.com/common/pc-login/v3/index.html?appid=140300&role=3000&source=70001&redirectUrl=https%3A%2F%2Fapi.honghusaas.com%2Fbiz-api%2Fv1%2Fworkbench%2Frbac%2Fuser%2Flogin%3FredirectUrl%3D%252F%252Fworkbench.honghusaas.com%252F%2523%252F%26login_type%3D2#/')
time.sleep(1)

shoujihao = input("请输入手机号:")
mima = input("请输入密码:")

# 输入手机号
sjh = page.ele('xpath:/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div[2]/input')
sjh.clear()
sjh.input(shoujihao)
time.sleep(1)

# 输入密码
mm = page.ele('xpath:/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/input')
mm.clear()
mm.input(mima)
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
cookie = page.cookies(as_dict=True)

# print("当前Cookie:", cookie)

ticket = cookie['ticket']  # 直接获取字符串
print("提取的ticket值:", ticket)

cookies = {
    'login_type': '2',
    'ticket': f'{ticket}',
}

# 存储第一列数据的列表（不含标题）
driver_ids = []

# 读取 CSV 文件
with open('已处理司机ID.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)

    # 跳过标题行（如果不需要标题）
    next(reader)

    # 提取第一列数据
    for row in reader:
        if row:  # 确保行非空
            driver_ids.append(row[0])


i = 0

ppdh = int(input("请输入品牌代号:"))
OK = input("请手动切换品牌，切换完成点击回车按键（Enter）")



for m in driver_ids:

    i += 1
    print(f"\n--- 正在处理第 {i} 条数据 ---")

    # 跳转司机详情页
    driver_url = f'https://workbench.honghusaas.com/#/driver/driver-manage/driver-detail?driverId={m}&companyId={ppdh}'
    page.get(driver_url)
    page.wait.load_start()  # 等待页面开始加载
    page.refresh()  # 刷新页面

    # 等待司机详情标签出现（关键等待）
    page.wait.ele_displayed('xpath://div[@data-node-key="driverDetail"]', timeout=2)

    # 点击司机详情
    sjxx = page.ele('xpath://div[@data-node-key="driverDetail"]')
    sjxx.click()
    time.sleep(0.3)  # 确保 tab 切换完成

    try:
        # 等待并点击显示按钮获取信息
        page.wait.ele_displayed(
            'xpath:/html/body/div[1]/div/section/main/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[1]/td[1]/span/div/span/*[name()="svg"]')
        c1 = page.ele(
            'xpath:/html/body/div[1]/div/section/main/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[1]/td[1]/span/div/span/*[name()="svg"]',
            timeout=0.3)
        c1.click()
        c2 = page.ele(
            'xpath:/html/body/div[1]/div/section/main/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[2]/td[2]/span/div/span/*[name()="svg"]',
            timeout=0.3)
        c2.click()
        c3 = page.ele(
            'xpath:/html/body/div[1]/div/section/main/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[3]/td[1]/span/div/span/*[name()="svg"]',
            timeout=0.3)
        c3.click()
        time.sleep(0.3)

        print(page.html)
        # 获取司机信息
        tree = etree.HTML(page.html)
        drivername = \
            tree.xpath(
                f'//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[1]/td[1]/span/div/text()')[0].strip()
        phonenumber = \
            tree.xpath(
                f'//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[2]/td[2]/span/div/text()')[0].strip()
        idcardnumber = \
            tree.xpath(
                f'//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[3]/td[1]/span/div/text()')[0].strip()
        try:
            city = \
                tree.xpath(
                    f'//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/span/text()')[0].strip()
        except:
            city = "暂无"

        # 切换到车辆详情
        clxx = page.ele(f'xpath://*[@id="rc-tabs-0-tab-carDetail"]', timeout=0.3)
        clxx.click()
        time.sleep(3)  # 等待车辆详情加载
        page.wait.ele_displayed(
            f'xpath://*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/span/*[name()="svg"]')
        try:
            # 点击
            page.ele(
                f'xpath://*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/span/*[name()="svg"]',
                timeout=0.3).click()
            time.sleep(0.3)

            # 获取车牌号
            tree2 = etree.HTML(page.html)
            carDetail = \
                tree2.xpath(
                    f'//*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/text()')[0].strip()
        except:
            carDetail = "暂无"


        time.sleep(3)

        try:
            color = \
                tree.xpath(
                    f'//*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[4]/td[1]/text()')[0].strip()
            #         //tr[@class='antd5-descriptions-row'][3]/td[@class='antd5-descriptions-item-content'][2]/span
            #       //*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[4]/td[1]
        except:
            color = "暂无"
        try:
            brand = \
                tree.xpath(
                    f'//*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[3]/td[2]/text()')[0].strip()
        except:
            brand = "暂无"
        try:
            model = \
                tree.xpath(
                    f'//*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[3]/td[3]/text()')[0].strip()
        except:
            model = "暂无"

        # 输出并写入CSV
        print(
            f'司机名:{drivername}, 司机手机号:{phonenumber}, 司机身份证号:{idcardnumber}, 车牌号:{carDetail}, 运用城市:{city}, 颜色:{color}, 品牌:{brand}, 型号:{model}')
        writer.writerow([drivername, phonenumber, idcardnumber, carDetail, city, color, brand, model])

    except:
        # 输出并写入CSV
        print(f'司机ID:{m}信息获取失败')
        SJXX = "信息获取失败"
        writer.writerow([m, SJXX])

# 关闭文件
fp.close()
print("数据采集完成！")