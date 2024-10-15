# @Editor    : 百年
# @FileName  :10_基础补充之动作链.py
# @Time      :2024/10/15 20:36


'''
动作链:
一些交互动作都是针对某个节点执行的
比如，对于输入框,我们就调用它的输入文字和清空文字方法;
对于按钮,就调用它的点击方法。其实，还有另外一些操作，它们
没有特定的执行对象,比如鼠标拖拽、键盘按键等，这些动作用另一种方式来执行-那就是动作链
'''
# 引入我们需要的包
from selenium.webdriver import ActionChains

from selenium.webdriver import Chrome
import time

# 创建浏览器对象
browser1 = Chrome(executable_path='../others/chromedriver.exe')

# 获取页面链接
browser1.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-draggable')

time.sleep(2)


# 先进入iframe中
# 首先定位
ifr = browser1.find_element_by_xpath('//*[@id="iframeResult"]')
# 然后进入
browser1.switch_to.frame(ifr)

# 执行拖动操作
div_tag = browser1.find_element_by_xpath('//*[@id="draggable"]')

# 打印一下看看我们到底有没有正确定位到
print(div_tag)

# 进行滑动,使用动作链
# 创建动作链对象,并且将其绑定给当前浏览器
actchain = ActionChains(browser1)

# 实现动作
# 先点击并长按刚才定位到的iframe里头的div标签
actchain.click_and_hold(div_tag)

# 然后进行滑动

# 实现向右滑动100px并且向下滑动100px,分五次,每次滑动20px,每次滑动完停止一秒
for i in range(5):
    # xoffset赋予的值为正数则表示向x轴正方向滑动,单位是像素,同理理解y，正为向下滑动,负为向上滑动
    actchain.move_by_offset(20,20).perform()
#   后面加上了perform表示让动作链立即执行,如果没写那就不执行
    time.sleep(1)

time.sleep(2)
# 释放动作链对象
actchain.release()
browser1.quit()

# 动作链的使用要小心,对于动作链的操作一定要使用好来解决一些简单的滑动验证码的问题
# 但是,滑动验证码的问题并不一定能够进行解决,因为部分网站的反扒手段已经将这种方式解决了

