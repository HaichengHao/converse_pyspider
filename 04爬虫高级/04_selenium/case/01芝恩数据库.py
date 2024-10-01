import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

# 写出chromedriver.exe的路径
chdr_path='../others/chromedriver.exe'
# 创建浏览器对象并指定可执行的路径
browser = Chrome(executable_path=chdr_path)

# 访问芝恩数据库
browser.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')
page_source = browser.page_source
print(page_source)






# 注意这是最后一步操作
browser.quit()