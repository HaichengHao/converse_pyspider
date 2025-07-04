---
id: screen
title: '🚤 截图和录像'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

## ✅️️ 页面截图

使用页面对象的`get_screenshot()`方法对页面进行截图，可对整个网页、可见网页、指定范围截图。

对可视范围外截图需要 90 以上版本浏览器支持。

下面三个参数三选一，优先级：`as_bytes`>`as_base64`>`path`。

| 参数名称           | 类型                | 默认值     | 说明                                                                                                              |
|:--------------:|:-----------------:|:-------:|-----------------------------------------------------------------------------------------------------------------|
| `path`         | `str`<br/>`Path`   | `None`  | 保存图片的路径，为`None`时保存在当前文件夹                                                                                        |
|   `name`    |      `str`      | `None`  | 完整文件名，后缀可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`，为`None`时以用 jpg 格式                                                   |
| `as_bytes`     | `str`<br/>`True`   | `None`  | 是否以字节形式返回图片，可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`、`None`、`True`<br/>不为`None`时`path`参数无效<br/>为`True`时选用 jpg 格式       |
| `as_base64`    | `str`<br/>`True`   | `None`  | 是否以 base64 形式返回图片，可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`、`None`、`True`<br/>不为`None`时`path`参数无效<br/>为`True`时选用 jpg 格式 |
| `full_page`    | `bool`            | `False` | 是否整页截图，为`True`截取整个网页，为`False`截取可视窗口                                                                             |
| `left_top`     | `Tuple[int, int]` | `None`  | 截取范围左上角坐标                                                                                                       |
| `right_bottom` | `Tuple[int, int]` | `None`  | 截取范围右下角坐标                                                                                                       |

| 返回类型    | 说明                                     |
|:-------:| -------------------------------------- |
| `bytes` | `as_bytes`生效时返回图片字节                    |
| `str`   | `as_bytes`和`as_base64`为`None`时返回图片完整路径 |
| `str`   | `as_base64`生效时返回 base64 格式的字符串         |

:::info 说明
    如`path`为包含文件名的完整路径，`name`参数无效。
:::

**示例：**

```python
# 对整页截图并保存
page.get_screenshot(path='tmp', name='pic.jpg', full_page=True)
```

## ️️ ✅️️ 元素截图

使用元素对象的`get_screenshot()`方法对元素进行截图。

若元素范围超出视口，需 90 以上版本内核支持。

下面三个参数三选一，优先级：`as_bytes`>`as_base64`>`path`。

|    参数名称     |       类型        |  默认值   | 说明                                                                                                                    |
|:-----------:|:---------------:|:------:|-----------------------------------------------------------------------------------------------------------------------|
|   `path`    | `str`<br/>`Path` | `None` | 保存图片的路径，为`None`时保存在当前文件夹                                                                                              |
|   `name`    |      `str`      | `None` | 完整文件名，后缀可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`，为`None`时以用 jpg 格式                                                         |
| `as_bytes`  | `str`<br/>`True` | `None` | 是否以字节形式返回图片，可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`、`None`、`True`<br/>不为`None`时`path`和`as_base64`参数无效<br/>为`True`时选用 jpg 格式 |
| `as_base64` | `str`<br/>`True` | `None` | 是否以 base64 形式返回图片，可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`、`None`、`True`<br/>不为`None`时`path`参数无效<br/>为`True`时选用 jpg 格式       |
| `scroll_to_center` |     `bool`      | `True` | 截图前是否滚动到视口中央 |

| 返回类型    | 说明                                     |
|:-------:| -------------------------------------- |
| `bytes` | `as_bytes`生效时返回图片字节                    |
| `str`   | `as_bytes`和`as_base64`为`None`时返回图片完整路径 |
| `str`   | `as_base64`生效时返回 base64 格式的字符串         |

:::info 说明
    如`path`为包含文件名的完整路径，`name`参数无效。
:::

**示例：**

```python
img = page('tag:img')
img.get_screenshot()
bytes_str = img.get_screenshot(as_bytes='png')  # 返回截图二进制文本
```

---

## ✅️️ 页面录像

使用页面对象的`screencast`功能，可以录取屏幕图片或视频。

### 📌 设置录制模式

录制模式一共有 5 种，通过`screencast.set_mode.xxx_mode()`设置。

| 模式                    | 说明                          |
|:---------------------:| --------------------------- |
| `video_mode()`        | 持续录制页面，停止时生成没有声音的视频         |
| `frugal_video_mode()` | 页面有变化时才录制，停止时生成没有声音的视频      |
| `js_video_mode()`   | 可生成有声音的视频，但需要手动启动 |
| `imgs_mode()`         | 持续对页面进行截图                   |
| `frugal_imgs_mode()`  | 页面有变化时才保存页面图像               |

### 📌 设置存放路径

使用`screencast.set_save_path()`设置录制结果保存路径。

| 参数名称        | 类型              | 默认值    | 说明         |
|:-----------:|:---------------:|:------:| ---------- |
| `save_path` | `str`<br/>`Path` | `None` | 保存图片或视频的路径 |

**返回：**`None`

### 📌 `screencast.start()`

此方法用于开始录制浏览器窗口。

| 参数名称        | 类型              | 默认值    | 说明         |
|:-----------:|:---------------:|:------:| ---------- |
| `save_path` | `str`<br/>`Path` | `None` | 保存图片或视频的路径 |

**返回：**`None`

:::warning 注意
    保存路径必需设置，无论是用`screencast.set()`还是`screencast.start()`都可以。
:::

### 📌 `screencast.stop()`

此方法用于停止录取屏幕。

| 参数名称         | 类型    | 默认值    | 说明                    |
|:------------:|:-----:|:------:| --------------------- |
| `video_name` | `str` | `None` | 视频文件名，为`None`时以当前时间名命 |

| 返回类型  | 说明                            |
|:-----:| ----------------------------- |
| `str` | 保存为视频时返回视频文件路径，否则返回保存图片的文件夹路径 |

### 📌 注意事项

- 使用`video_mode`和`frugal_video_mode`时，保存路径和保存文件名必需是英文。
- 使用`video_mode`和`frugal_video_mode`时，需先安装 opencv 库。`pip install opencv-python`
- 使用`js_video_mode`时，需用鼠标手动选择要录制的目标，才能开始录制
- 使用`js_video_mode`时，如要对一个窗口进行录制，需在另一个窗口开始录制，否则如窗口出现跳转，会使录制失效

### 📌 示例

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.screencast.set_save_path('video')  # 设置视频存放路径
page.screencast.set_mode.video_mode()  # 设置录制
page.screencast.start()  # 开始录制
page.wait(3)
page.screencast.stop()  # 停止录制
```
