# @Editor    : 百年
# @FileName  :07_无头浏览器.py
# @Time      :2024/10/3 13:45
'''
每次打开浏览器都会占用资源且很烦人,所以我们使用无界面的浏览器
这里还是以之前的下拉列表的代码为例子进行修改
其实很简单,具体来说只有三部
1导入需要的chrome配置信息
from selenium.webdriver.chrome.ptions import Options
2新建配置信息并添加配置项
opt = Options()
opt.add_argument("配置参数")
3新建浏览器对象的时候把配置信息设置进去
browser_obj = Chrome(executable_path='',options=opt)

# 注意,既然设置成无头的了,就养成好的习惯,及时释放资源
浏览器对象.quit()
'''
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
# todo:1 导入chrome的配置信息
from selenium.webdriver.chrome.options import Options
import time
# 导入需要的处理下拉列表(在前端里就是<select>)的包
from selenium.webdriver.support.select import Select

# todo:2 创建selenium的配置信息
opts=Options() #创建一个变量接收Options
opts.add_argument("--headless") #设置为无头
opts.add_argument("--disable-gpu") #设置为禁止gpu图形渲染


# todo:3 然后在构建浏览器对象的时候指定自己设置的配置信息参数
browser1 = Chrome(executable_path='../others/chromedriver.exe',options=opts)

browser1.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

# 定位select对象
sel = browser1.find_element_by_xpath('//*[@id="OptionDate"]')
time.sleep(2)
# 调用Select()对sel对象进行封装
sel_new = Select(sel)
# 获取所有的选项<options>的标签内容
all_sel = sel_new.options  #.options是获取所有的<options>
# all_sel = sel_new.all_selected_options #还有一个是看一下当前被选中的选项，一般不使用
# for item in all_sel:
#     print(item.text)

# 其实我们主要是用长度然后根据下拉列表的特性来进行选项的访问
# print(len(all_sel))
"""
sel_new.select_by_index() #最常用,根据索引位置来切换
sel_new.select_by_value() #根据<option value='xxx'>中的xxx来进行切换,注意,如果不熟悉可以看看前端的知识
sel_new.select_by_visible_text() #根据可见文本,即<option>xxx</option>中的xxx来进行切换
"""
# 遍历所有的<options>
for i in range(len(sel_new.options)):
    # 其实时间不应该加在结尾,因为写在结尾是没有作用的
    sel_new.select_by_index(i) #根据位置进行切换,以本案例为例,获取完毕2024年的数据后它会自动跳转到2023年的数据
    time.sleep(4) #时间应该写在这里,因为上面的一行代码进行了切换,我们需要给它切换后的反应时间,所以我们应该设置在切换完之后

    # 切换完了之后进行数据的获取
    # 获取表格中的每一行，所以这时候我们要用的是elements
    trs = browser1.find_elements_by_xpath("/html/body/section/div/div[2]/div/div/div[2]/table/tbody/tr")
    for tr in trs:
        print(tr.text) #打印每一条数据
    time.sleep(1)

# 全部运行完成之后记得养成良好习惯
browser1.quit()