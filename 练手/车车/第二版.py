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



# 导航到治理页面并进入处置任务页
zhili = page.ele('xpath://*[@id="w-layout-main"]/aside/div[1]/ul/li[6]', timeout=15)
zhili.click()
time.sleep(1)

chuzhirenwu = page.ele('xpath://*[@id="_governance_driver-disposal_govern-manage"]', timeout=15)
chuzhirenwu.click()
time.sleep(3)

# 列表页 URL
list_url = 'https://workbench.honghusaas.com/#/governance/driver-disposal/govern-manage'

# 循环处理前10条数据
for i in range(1, 11):
    try:
        print(f"\n--- 正在处理第 {i} 条数据 ---")

        # 点击查看详情
        ckxq = page.ele(f'xpath://*[@id="w-layout-main"]/section/main/div/div/div[4]/div/div/div/div/div[2]/div/div/table/tbody/tr[{i}]/td/div/button[1]', timeout=15)
        ckxq.click()
        time.sleep(3)  # 给页面跳转和数据加载留足时间

        # 使用当前页面 HTML 获取 driverId
        tree0 = etree.HTML(page.html)
        sjid = tree0.xpath('/html/body/div[1]/div/section/main/div/div/div/div/div[2]/div[1]/div[1]/div/table/tbody/tr[1]/td/span[2]/a/text()')[0]

        # 跳转司机详情页
        driver_url = f'https://workbench.honghusaas.com/#/driver/driver-manage/driver-detail?driverId={sjid}&companyId=1038'
        page.get(driver_url)
        page.wait.load_start()  # 等待页面开始加载

        # 等待司机详情标签出现（关键等待）
        page.wait.ele_displayed('xpath://div[@data-node-key="driverDetail"]', timeout=4)

        # 点击司机详情
        sjxx = page.ele('xpath://div[@data-node-key="driverDetail"]')
        sjxx.click()
        time.sleep(1)  # 确保 tab 切换完成

        # 等待并点击显示按钮获取信息
        page.wait.ele_displayed('xpath:/html/body/div[1]/div/section/main/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[1]/td[1]/span/div/span/*[name()="svg"]')
        c1 = page.ele('xpath:/html/body/div[1]/div/section/main/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[1]/td[1]/span/div/span/*[name()="svg"]',timeout=3)
        c1.click()
        c2 = page.ele('xpath:/html/body/div[1]/div/section/main/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[2]/td[2]/span/div/span/*[name()="svg"]',timeout=3)
        c2.click()
        c3 = page.ele('xpath:/html/body/div[1]/div/section/main/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[3]/td[1]/span/div/span/*[name()="svg"]',timeout=3)
        c3.click()
        time.sleep(2)

        # 获取司机信息
        tree = etree.HTML(page.html)
        drivername = tree.xpath('//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[1]/td[1]/span/div/text()')[0].strip()
        phonenumber = tree.xpath('//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[2]/td[2]/span/div/text()')[0].strip()
        idcardnumber = tree.xpath('//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[3]/td[1]/span/div/text()')[0].strip()

        # 切换到车辆详情
        clxx = page.ele('xpath://*[@id="rc-tabs-0-tab-carDetail"]', timeout=15)
        clxx.click()
        time.sleep(3)  # 等待车辆详情加载
        page.wait.ele_displayed('xpath://*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/span/*[name()="svg"]')
        # 点击
        page.ele('xpath://*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/span/*[name()="svg"]',timeout=3).click()
        time.sleep(2)

        # 获取车牌号
        tree2 = etree.HTML(page.html)
        carDetail = tree2.xpath('//*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/text()')[0].strip()

        # 输出并写入CSV
        print(f'司机名:{drivername}, 司机手机号:{phonenumber}, 司机身份证号:{idcardnumber}, 车牌号:{carDetail}')
        writer.writerow([drivername, phonenumber, idcardnumber, carDetail])

        # 返回列表页（直接跳转）
        page.get(list_url)
        # 等待列表第一条数据出现，确保加载完成
        page.wait.ele_displayed(f'xpath:/html/body/div[1]/div/section/main/div/div/div[4]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/div/button[1]', timeout=15)
        time.sleep(2)  # 额外缓冲

    except Exception as e:
        print(f"第 {i} 条数据处理失败: {e}")
        # 出错后尝试返回列表页继续
        page.get(list_url)
        time.sleep(3)
        continue

# 关闭文件
fp.close()
print("数据采集完成！")