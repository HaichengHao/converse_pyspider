---
id: intro
title: '⤵️ 概述'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

DrissionPage 提供了强大的文件下载管理功能。

能够主动发起下载任务，也能够对浏览器触发的下载任务进行管理。

## ✅️️ `download()`方法

该方法可以主动发起下载任务，提供任务管理、多线程、大文件分块、自动重连、文件名冲突处理等功能。

页面对象、标签页对象、`<iframe>`元素对象均支持此方法。

:::tip Tips
    使用时，程序会自动同步调用方法的对象的 cookies 信息。
:::

**示例：**

```python
from DrissionPage import SessionPage

page = SessionPage()
page.download('https://dldir1.qq.com/qqfile/qq/TIM3.4.8/TIM3.4.8.22092.exe')
```

---

## ✅️️ 浏览器的下载任务

浏览器页面对象、标签页对象、`<iframe>`对象可对浏览器下载任务进行控制。

包含以下功能：

- 每个标签页对象可独立指定下载地址
- 可在下载前指定重命名文件名
- 可拦截下载任务，获取任务信息

**示例：**

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
mission = page('t:a').click.to_download('tmp', 'file_name')  # 点击一个会触发下载的链接，同时设置下载路径和文件名
mission.wait()  # 等待下载结束
```

功能分解写法，效果和上面的一样：

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.set.download_path('save_path')  # 设置文件保存路径
page.set.download_file_name('file_name')  # 设置重命名文件名
page('t:a').click()  # 点击一个会触发下载的链接
page.wait.download_begin()  # 等待下载开始
page.wait.downloads_done()  # 等待下载结束
```