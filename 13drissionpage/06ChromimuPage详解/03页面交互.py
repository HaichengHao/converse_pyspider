"""
@File    :03页面交互.py
@Editor  : 百年
@Date    :2025/6/1 16:27 
"""
from DrissionPage import ChromiumPage,ChromiumOptions
opt1 = ChromiumOptions().set_paths(local_port=9111,user_data_path=r'D:\Chromeopts\data1')

page1 = ChromiumPage(addr_or_opts=opt1)

#tips:get() 该方法用于跳转到一个网址。当连接失败时，程序会进行重试。

# page1.get('https://www.baidu.com')

# page1.get('https://www.bilibili.com')

# page1.get('https://www.bing.com')

page1.get('https://movie.douban.com/top250')

#tips:back() 此方法用于在浏览器历史中后退若干步

# page1.back(2)

#tips: forward() 此方法用于在浏览器历史中前进若干步
# page1.forward(1)


#tips: refresh() 此方法用于刷新当前页面
# page1.refresh()

# tips: run_js()：此方法用于执行 js 脚本

# page1.run_js('alert(arguments[0]+argments[1]);','hello','drissionpage')

# tips run_js_loaded()：此方法用于运行 js 脚本，执行前等待页面加载完毕。

# page1.run_js_loaded('alert("hello")')


# tips scroll.to_bottom()：此方法用于滚动页面到底部，水平位置不变。

page1.scroll.to_bottom()