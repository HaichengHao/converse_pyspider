 

> 本文转自测试人社区，原文链接：[https://ceshiren.com/t/topic/30855](https://ceshiren.com/t/topic/30855)

### 一、简介

*   JavaScript是一种脚本语言，简称js。有的场景需要使用js脚本注入，辅助我们完成Selenium无法做到的事情。
*   当WebDriver遇到无法完成的操作时，可以使用JavaScript来完成，WebDriver提供了execute\_script()方法来调用js代码。
*   JavaScript是一种具有函数优先的轻量级、解释型或即时编译的编程语言。可以嵌入到HTML页面对浏览器时间做出响应，也可以基于Node.js技术进行服务器端编程。

### 二、场景应用

#### 2.1 自动化测试中的应用

*   部分场景使用Selenium原生方法无法解决：
    *   修改时间控件
    *   滚动到某个元素
    *   其他场景

#### 2.2 执行js的两种场景

*   在页面上直接执行js；
*   在某个已经定位的元素上执行js。

### 三、使用思路

#### 3.1 页面调试js脚本

*   **js脚本-调试方法**：

1.  进入console调试；
2.  js脚本如果又返回值，则会在浏览器返回。

![](https://i-blog.csdnimg.cn/blog_migrate/c021e11c23fac08aabd4ac3734f6eab9.png)

*   **js脚本-元素操作**（通过css查找）：

1.  点击元素（对应click）
2.  input标签对应的值（对应send\_keys）
3.  元素的类属性
4.  元素的文本属性

```javascript
// 百度首页：https://www.baidu.com/
// 修改属性值
document.querySelector("#kw").value = "霍格沃兹测试学院"
// 点击操作
document.querySelector("#su").click()
// 淘宝首页： https://www.taobao.com/ 
// 修改元素的类属性
document.querySelector("#J_SiteNavMytaobao").className\
="site-nav-menu site-nav-mytaobao site-nav-multi-menu J_MultiMenu site-nav-menu-hover"
// 测试人首页：https://ceshiren.com/
// 获取元素内的文本信息
document.querySelector("#ember63").innerText
```

*   **js脚本-滚动操作**

1.  页面滚动到底部
2.  指定到滚动的位置

```javascript
document.documentElement.scrollTop=1000
document.querySelector("css表达式").scrollIntoView()
```

#### 3.2 Selenium执行js

#### 3.2.1 执行js

*   Selenium可以通过execute\_script()来执行JavaScript脚本。
    *   driver.execute\_script：同步执行JavaScript在当前的窗口框架下。
    *   js脚本可以在浏览器的开发者工具->console中进行调试。

#### 3.2.2 js的返回结果

*   获取元素控件中的属性值，与Selenium结合，在代码中返回js结果。
*   Python语法：

```python
# 获取网页性能的响应时间，js脚本中使用return代表返回获取的结果
js = "return JSON.stringify(performance.timing);"
driver.execute_script(js)
```

#### 3.2.3 arguments传参

*   执行JavaScript也可以通过传参的方式传入元素信息，还可以通过下面的方法点击被遮挡的元素。

例如：某个元素在实际的操作过程中被其他元素遮挡，就可以使用js点击的方式。

*   Python语法

```python
element = driver.find_element(by,locator)
# arguments[0]代表所传值element的第一个参数
# click()代表js中的点击动作
driver.execute_script("arguments[0].click();",element)
```

### 四、实战

*   以企业微信为例，使用js点击添加图片。
*   Python语法：

```python
# 导入依赖
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWework:
        def setup(self):
                self.driver = webdriver.Chrome()
                # 隐式等待
                self.driver.implicitly_wait(10)

        def test_upload(self):
                # 元素定位
                element_add = self.driver.find_element\
                        (By.CSS_SELECTOR,".js_upload_file_selector")
                # 执行js代码
                self.driver.execute_script\
                        ("arguments[0].click();", element_add)
                self.driver.find_element(By.ID,"js_upload_input").\
                        send_keys("D:\project\demo1\demo.png")
                assert len(self.driver.find_elements(By.CSS_SELECTOR,\
                ".material_pic_list_item")) == 1

        def teardown(self):
                self.driver.quit()
```

推荐学习
----

[【霍格沃兹测试开发】7天软件测试快速入门带你从零基础/转行/小白/就业/测试用例设计实战](https://space.bilibili.com/406886660/channel/collectiondetail?sid=303135)

[【霍格沃兹测试开发】最新版！Web 自动化测试从入门到精通/ 电子商务产品实战/Selenium （上集）](https://space.bilibili.com/406886660/channel/collectiondetail?sid=371736)

[【霍格沃兹测试开发】最新版！Web 自动化测试从入门到精通/ 电子商务产品实战/Selenium （下集）](https://space.bilibili.com/406886660/channel/collectiondetail?sid=2298591)

[【霍格沃兹测试开发】明星讲师精心打造最新Python 教程软件测试开发从业者必学（上集）](https://space.bilibili.com/406886660/channel/collectiondetail?sid=2135437)

[【霍格沃兹测试开发】明星讲师精心打造最新Python 教程软件测试开发从业者必学（下集）](https://space.bilibili.com/406886660/channel/collectiondetail?sid=2294337)

[【霍格沃兹测试开发】精品课合集/ 自动化测试/ 性能测试/ 精准测试/ 测试左移/ 测试右移/ 人工智能测试](https://space.bilibili.com/406886660/channel/collectiondetail?sid=571346)

[【霍格沃兹测试开发】腾讯/ 百度/ 阿里/ 字节测试专家技术沙龙分享合集/ 精准化测试/ 流量回放/Diff](https://space.bilibili.com/406886660/channel/collectiondetail?sid=1588831)

[【霍格沃兹测试开发】Pytest 用例结构/ 编写规范 / 免费分享](https://space.bilibili.com/406886660/channel/collectiondetail?sid=1588527)

[【霍格沃兹测试开发】JMeter 实时性能监控平台/ 数据分析展示系统Grafana/Docker 安装](https://space.bilibili.com/406886660/channel/collectiondetail?sid=1588415)

[【霍格沃兹测试开发】接口自动化测试的场景有哪些？为什么要做接口自动化测试？如何一键生成测试报告？](https://space.bilibili.com/406886660/channel/collectiondetail?sid=1588490)

[【霍格沃兹测试开发】面试技巧指导/ 测试开发能力评级/1V1 模拟面试实战/ 冲刺年薪百万！](https://space.bilibili.com/406886660/channel/collectiondetail?sid=1588295)

[【霍格沃兹测试开发】腾讯软件测试能力评级标准/ 要评级表格的联系我](https://space.bilibili.com/406886660/channel/collectiondetail?sid=1538625)

[【霍格沃兹测试开发】Pytest 与Allure2 一键生成测试报告/ 测试用例断言/ 数据驱动/ 参数化](https://space.bilibili.com/406886660/channel/collectiondetail?sid=551251)

[【霍格沃兹测试开发】App 功能测试实战快速入门/adb 常用命令/adb 压力测试](https://space.bilibili.com/406886660/channel/collectiondetail?sid=536890)

[【霍格沃兹测试开发】阿里/ 百度/ 腾讯/ 滴滴/ 字节/ 一线大厂面试真题讲解，卷完拿高薪Offer ！](https://space.bilibili.com/406886660/channel/collectiondetail?sid=456475)

[【霍格沃兹测试开发】App自动化测试零基础快速入门/Appium/自动化用例录制/参数配置](https://space.bilibili.com/406886660/channel/collectiondetail?sid=374199)

[【霍格沃兹测试开发】如何用Postman 做接口测试，从入门到实战/ 接口抓包（最新最全教程）](https://space.bilibili.com/406886660/channel/collectiondetail?sid=374048)

[【霍格沃兹测试开发】6 小时轻松上手功能测试/ 软件测试工作流程/ 测试用例设计/Bug 管理](https://space.bilibili.com/406886660/channel/collectiondetail?sid=302763)

[【霍格沃兹测试开发】零基础小白如何使用Postman ，从零到一做接口自动化测试/ 从零基础到进阶到实战](https://space.bilibili.com/406886660/channel/collectiondetail?sid=301113)

[【霍格沃兹测试开发】建议收藏全国CCF 测试开发大赛Python 接口自动化测试赛前辅导 / 项目实战](https://space.bilibili.com/406886660/channel/collectiondetail?sid=2300164)

[更多软件测试开发视频教程点此](https://ceshiren.com/t/topic/30460)
----------------------------------------------------

![](https://i-blog.csdnimg.cn/blog_migrate/37c563523e37835ca5f333a823d8669b.png)  
**软件测试职业发展**  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/71fc9a924f1bcf5d2b7d6cca41ac8bd0.png)  
**零基础入门**  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/264f369cab04fc6bf5647d7bff669e5d.png)

**测试必备编程篇**  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/0928ef5a204f8803823d5509ae944927.png)  
**自动化测试**  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/60e6f2c713990bcba635ff6335576145.png)  
**性能测试**  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/5c1491d823f581e05b5d07a82fe7a635.png)  
**测试管理**  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/8af22bd84ce8bdc3a5779fda7d773875.png)  
**工程效能篇**  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/7db58d75eab3b808d30ee64d0eacf01f.png)  
**面试求职篇**

软件测试的面试宝典，内含一线互联网大厂面试真题、面试技巧、软件测试面试简历指导，免费领取！  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/1dcbf9bfbe968a52db45e76edb0499d7.png)  
![](https://i-blog.csdnimg.cn/blog_migrate/db049aad830b3cfd2b453a3c26a7a19e.png)

 

![](https://img-blog.csdnimg.cn/790dfbc6da464cc3bbefa1a6ca28f1a1.jpeg)

免费领取软件测试资料大礼包

![](https://g.csdnimg.cn/extension-box/1.1.6/image/weixin.png) 微信名片

![](https://g.csdnimg.cn/extension-box/1.1.6/image/ic_move.png)

本文转自 <https://blog.csdn.net/Ceshiren666/article/details/138161625?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522c8a05d0305256af69635a1e9d619d4c4%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=c8a05d0305256af69635a1e9d619d4c4&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-138161625-null-null.142^v102^pc_search_result_base8&utm_term=selenium%E6%89%A7%E8%A1%8Cjavascript%E8%84%9A%E6%9C%AC&spm=1018.2226.3001.4187>，如有侵权，请联系删除。