---
id: upload
title: '🚤 文件上传'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

上传文件有两种方式：

- 拦截文件输入框，自动填入路径
- 找到`<input>`元素，填入文件路径

## ✅️️ 自然的交互

传统自动化工具的文件上传，需要开发者在 DOM 里找到文件上传控件，然后用元素对象的`input()`方法填入路径。

有些上传控件是临时加载的，有些藏得很深，找起来费时费力。

本库提供一种自然的文件上传方式，无需在 DOM 里找控件，只要自然地点击触发文件选择框，程序就能主动截获，并填写设定好的路径，开发更省事。

### 📌 `click.to_upload()`

浏览器元素对象拥有此方法，用于上传文件到网页。

|     参数名称     |                        类型                         |   默认值   | 说明                                        |
|:------------:|:-------------------------------------------------:|:-------:|-------------------------------------------|
| `file_paths` |            `str`<br/>`Path`<br/>`list`<br/>`tuple`            |   必填    | 文件路径，如果上传框支持多文件，可传入列表或字符串，字符串时多个文件用`\n`分隔 |
|  `by_js`  |                      `bool`                       | `False` | 是否用 js 方式点击，逻辑与`click()`一致                 |

**返回：**`None`

**示例**

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
ele = page('#uploadButton')
ele.click.to_upload(r'C:\text.txt')
```

---

### 📌 手动方式

上面的方法使用默认点击方式触发上传，假如页面要求其它触发方式，可自行手动写上传逻辑。

**步骤：**

- 设置要上传的文件路径，多路径传入`list`、`tuple`或以`\n`分隔的字符串
- 点击会触发文件选择框的按钮
- 调用等待录入语句，确保输入完整

**示例：**

```python
# 设置要上传的文件路径
page.set.upload_files('demo.txt')
# 点击触发文件选择框按钮
btn_ele.click()
# 等待路径填入
page.wait.upload_paths_inputted()
```

点击按钮后，文本选择框被拦截不会弹出，但可以看到文件路径已经传入其中。

由于此动作是异步输入，需显式等待输入完成才进行下一步操作。

---

### 📌 注意事项

如果您要操作的上传控件在一个异域的`<iframe>`，那必需用这个`<iframe>`对象来设置上传路径，而不能用页面对象设置。

❌ 错误做法：

```python
page.set.upload_paths('demo.txt')
page.get_frame(1).ele('@type=file').click()
page.wait.upload_paths_inputted()
```

⭕ 正确做法：

```python
iframe = page.get_frame(1)
iframe.set.upload_paths('demo.txt')
iframe.ele('@type=file').click()
iframe.wait.upload_paths_inputted()
```

如果`<iframe>`和主页面是同域的，则用域名对象和`<iframe>`对象设置均可。

---

## ✅️️ 传统方式

传统方式，需要开发者在 DOM 里找到文件上传控件，然后用元素对象的`input()`方法填入路径。

文件上传控件是`type`属性为`'file'`的`<input>`元素进行输入，把文件路径输入到元素即可，用法与输入文本一致。

稍有不同的是，无论`clear`参数是什么，都会清空原控件内容。

如果控件支持多文件上传，多个路径用`list`、`tuple`或以`\n`分隔的字符串传入。

```python
upload = page('tag:input@type=file')

# 传入一个路径
upload.input('D:\\test1.txt')

# 传入多个路径，方式 1
paths = 'D:\\test1.txt\nD:\\test2.txt'
upload.input(paths)

# 传入多个路径，方式 2
paths = ['D:\\test1.txt', 'D:\\test2.txt']
upload.input(paths)
```

如果`<input>`元素很好找，这种方式是很简便的。

有些`<input>`是临时加载的，或者经过修饰隐藏很深，找起来很费劲。

万一有些上传是用 js 控制的，这种方式未必能奏效。