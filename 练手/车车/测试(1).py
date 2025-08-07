import time
from DrissionPage import ChromiumPage
from lxml import etree
import csv
fp = open('./driver_data.csv','a+',encoding='utf-8',newline='')
writer = csv.writer(fp)
if fp.tell() == 0:
    writer.writerow(['姓名','手机号','身份证号','车牌号'])
page =ChromiumPage()
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

zhili = page.ele('xpath://*[@id="w-layout-main"]/aside/div[1]/ul/li[6]')
zhili.click()
time.sleep(1)

chuzhirenwu = page.ele('xpath://*[@id="_governance_driver-disposal_govern-manage"]')
chuzhirenwu.click()
time.sleep(3)
# print(page.cookies())

#查看详情
ckxq = page.ele('xpath:/html/body/div[1]/div/section/main/div/div/div[4]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/div/button[1]')
ckxq.click()
time.sleep(1)

#司机id
sjid = page.ele('xpath://span[@class="ant-descriptions-item-content"]/a')

new_tab = sjid.click.for_new_tab()
new_tab.wait.load_start()

sjxx = new_tab.ele('xpath://div[@data-node-key="driverDetail"]')
sjxx.click()



#最后的操作,点击与定位
c1 = new_tab.ele('xpath://*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[1]/td[1]/span/div/span/*[name()="svg"]').click()

c2 = new_tab.ele('xpath://*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[2]/td[2]/span/div/span/*[name()="svg"]').click()

c3 = new_tab.ele('xpath://*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[3]/td[1]/span/div/span/*[name()="svg"]').click()


time.sleep(2)
#print(new_tab.html)


# 最后的定位
tree = etree.HTML(new_tab.html)
drivername = tree.xpath('//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[1]/td[1]/span/div/text()')[0]
phonenumber = tree.xpath('//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[2]/td[2]/span/div/text()')[0]
idcardnumber = tree.xpath('//*[@id="rc-tabs-0-panel-driverDetail"]/div/div[1]/div/table/tbody/tr[3]/td[1]/span/div/text()')[0]


# print(f'司机名:{drivername},司机手机号:{phonenumber},司机身份证号:{idcardnumber}')



clxx = new_tab.ele('xpath://div[@data-node-key="carDetail"]')
#clxx.click()

tab = clxx.click.for_new_tab()
tab.wait.load_start()


#最后的操作,点击与定位
c4 = tab.ele('xpath://*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/span/*[name()="svg"]').click()


time.sleep(2)
# 最后的定位
# print(tab.html)
tree2 = etree.HTML(tab.html)
carDetail = tree2.xpath('//*[@id="rc-tabs-0-panel-carDetail"]/div/div[2]/div/table/tbody/tr[1]/td[1]/span/div/div/text()')[0]

# print('车牌号:',carDetail)
print(f'司机名:{drivername},司机手机号:{phonenumber},司机身份证号:{idcardnumber},车牌号{carDetail}')

writer.writerow([drivername,phonenumber,idcardnumber,carDetail])

fp.close()




