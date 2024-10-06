# @Editor    : 百年
# @FileName  :03猎聘获取招聘信息.py
# @Time      :2024/10/1 10:29
import time #如果有时候操作叠加过快,那就手动设置timesleep来控制时间,直接进行sleep操作
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
chdr_path='../others/chromedriver.exe'
# 创建一个Chrome对象
web = Chrome(executable_path=chdr_path)
# 访问猎聘
web.get(url='https://www.liepin.com/')


# 搜索岗位
jobs = web.find_element_by_xpath("/html/body/section[4]/div/div/div/div/div/div/div[1]/div/div/div/input")
jobs.send_keys('Python')
time.sleep(3) # 等待三秒, 让操作生效
jobs.send_keys(Keys.ENTER)
time.sleep(4)

# 注意,已经跳转到新的页面了,但是在selenium看来我们依然在以前的页面中,它这时候已经傻眼了
# 我们必须调整selenium的视角
# 切换窗口
# 相对于跳转的窗口加上父级窗口,我们现在是打开了两个窗口,所以我们需要将其转换为最后一个窗口,
# 那么这个窗口的索引值就是-1
time.sleep(2)
web.switch_to.window(web.window_handles[-1])
# 然后我们就从转换的视角,也就是新的窗口来获取我们真正想要的内容
# 注意,要获得多个目标内容的话就写成find_elements_by_xpath，把element写成复数形式elements,并且返回值是一个列表,所以不能够直接使用.text属性来获取文字内容,而是遍历每一个列表中的单个element元素来获得.text内容
job_lst=web.find_elements_by_xpath("//div[@class='job-list-box']//div[@class='jsx-2387891236 job-title-box']/div[1]")
for item in job_lst:
    print(item.text)

# 完毕后关闭当前的窗口并将视角调整回去
web.close()
web.switch_to.window(web.window_handles[0])
# 然后可以进行其它操作
web.quit()
