import time
from DrissionPage import WebPage
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt

# 初始化浏览器
page = WebPage()

# 登录流程
page.get('https://i-hn.meiyijia.com.cn/login.html?ReturnUrl=%2f')
logininput = page.ele('xpath:/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/input')
logininput.clear()
logininput.input('13349925309')
pwdinput = page.ele('xpath:/html/body/div[4]/div/div[2]/div[4]/div[2]/div[4]/input')
pwdinput.clear()
pwdinput.input('13477062863Czk')
verify_code = input('请输入验证码>>>')
verify_code_input = page.ele('xpath:/html/body/div[4]/div/div[2]/div[4]/div[2]/div[6]/input')
verify_code_input.clear()
verify_code_input.input(verify_code)

lg_btn = page.ele('xpath:/html/body/div[4]/div/div[2]/div[4]/div[2]/div[8]/button')
lg_btn.click()
time.sleep(4)

# 访问目标页面
page.get('https://i-hn.meiyijia.com.cn/#/StockAccount')
time.sleep(2)

# 读取商品编码
wb = open_workbook('./01.xls')
sheet = wb.sheet_by_index(0)
product_codes = [str(sheet.cell(row, 0).value).strip() for row in range(1, sheet.nrows)]

# 创建或打开结果文件
try:
    rb = open_workbook('./02.xls')
    wb = copy(rb)
    # 检查是否已有标题（读取第一行）
    sheet = rb.sheet_by_index(0)
    if sheet.nrows == 0:  # 如果是全新文件
        headers = ["商品编码", "商品名称", "规格", "单位", "库存数量", "可用数量", "锁定数量", "参考进价", "参考售价", "备注"]
        for col, header in enumerate(headers):
            wb.get_sheet(0).write(0, col, header)
except FileNotFoundError:
    # 创建新工作簿并添加标题行
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet1')
    headers = ["商品编码", "商品名称", "规格", "单位", "库存数量", "可用数量", "锁定数量", "参考进价", "参考售价", "备注"]
    for col, header in enumerate(headers):
        ws.write(0, col, header)
    wb.save('./02.xls')
    rb = open_workbook('./02.xls')
    wb = copy(rb)

result_sheet = wb.get_sheet(0)

# 批量搜索（无定期保存版）
for row, code in enumerate(product_codes, 1):
    print(f"正在处理 {row}/{len(product_codes)}: {code}")

    # 输入商品编码（增加显式等待）
    spbh = page.ele('xpath:/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[1]/form/fieldset/div[1]/div[1]/div[1]/input')
    spbh.clear()
    spbh.input(code)

    # 点击搜索（保持原样）
    search_btn = page.ele('xpath:/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[1]/form/fieldset/div[2]/div/button[1]')
    search_btn.click()
    time.sleep(1)

    # 获取结果（无结果直接跳过）
    rows = page.eles('xpath://table/tbody/tr')
    print(rows)
    if not rows:
        continue  # 直接跳过

    # 写入数据（保持原样）
    result_sheet.write(row, 0, code)
    cells = rows[0].eles('tag:td')
    for col, cell in enumerate(cells, 1):
        result_sheet.write(row, col, cell.text)

# 只在最后保存一次
wb.save('./02.xls')
print("所有商品处理完成，结果已保存")

page.close()