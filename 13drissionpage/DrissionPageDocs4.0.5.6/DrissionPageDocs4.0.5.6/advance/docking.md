---
id: docking
title: ⚙️ 与其它项目对接
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

DrissionPage 提供 2 个小工具，用于与 selenium 和 playwright 项目对接。

可从旧项目对象中生成`ChromiumPage`对象。

:::info 注意
    只支持 chromium 内核的浏览器。
:::

## ✅️️ 与 selenium 对接

`from_selenium()`方法接收 selenium 的`WebDriver`对象，返回`ChromiumPage`对象。

|  参数名称  |     类型      |  默认值   | 说明                      |
|:------:|:-----------:|:------:|-------------------------|
| `driver` | `WebDriver` |   必填   | selenium 的`WebDriver`对象 |

|      返回类型      |        说明        |
|:--------------:|:----------------:|
| `ChromiumPage` | `ChromiumPage`对象 |

```python
from DrissionPage.common import from_selenium
from selenium.webdriver import Chrome

# 创建WebDriver对象
driver = Chrome()

# 从该WebDriver对象创建ChromiumPage对象
page = from_selenium(driver)

# 用ChromiumPage对象操作浏览器
page.get('http://www.DrissionPage.cn')
```

---

## ✅️️ 与 playwright 对接

`from_playwright()`方法接收 playwright 的`Page`或`Browser`对象，返回`ChromiumPage`对象。

|  参数名称  |          类型          |  默认值   | 说明                             |
|:------:|:--------------------:|:------:|--------------------------------|
| `page_or_browser` | `Page`<br/>`Browser` |   必填   | playwright 的`Page`或`Browser`对象 |

|      返回类型      |        说明        |
|:--------------:|:----------------:|
| `ChromiumPage` | `ChromiumPage`对象 |

```python
from DrissionPage.common import from_playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()  # 用playwright启动浏览器
    pw_page = browser.new_page()  # 创建一个新的页面
    
    # 从Page对象创建ChromiumPage对象
    page = from_playwright(pw_page)
    # 或 从Browser对象创建ChromiumPage对象
    page = from_playwright(browser)
    
    # 用ChromiumPage对象操作浏览器
    page.get("https://www.DrissionPage.cn")
```