---
id: tools
title: '⚙️ 实用工具'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

`DrissionPage.common`路径可导入几个小工具。

## ✅️️ `make_session_ele()`

此方法用于把页面对象、元素对象或 html 文本转换为`SessionElement`对象，或以其为基准搜索元素，获取其静态版本。

|  参数名称  |                                                                类型                                                                |  默认值   | 说明             |
|:------:|:--------------------------------------------------------------------------------------------------------------------------------:|:------:|----------------|
| `html_or_ele` | `str`<br/>`ChromiumElement`<br/>`ChromiumPage`<br/>`ChromiumTab`<br/>`WebPage`<br/>`MixTab`<br/>`ChromiumFrame`<br/>`ShdownRoot` |   必填   | html文本、元素或页面对象 |
| `loc` |                                                   `str`<br/>`Tuple[str, str]`                                                    | `None` | 定位元组或字符串，为`None`时不在下级查找，返回根元素   |
| `index` |                                                              `int`                                                               |  `1`   | 获取第几个元素，从`1`开始，可传入负数获取倒数第几个，`None`获取所有   |

|          返回类型          |              说明              |
|:----------------------:|:----------------------------:|
|    `SessionElement`    |     `index`为数字时返回静态元素对象      |
| `List[SessionElement]` | `index`为`None`时返回静态元素对象组成的列表 |

**示例：**

```python
from DrissionPage.common import make_session_ele

html = '''
<html><body><div>abc</div></body></html>
'''
ele = make_session_ele(html)
print(ele.text)
```

**输出：**

```shell
abc
```

---

## ✅️️ `get_blob()`

此方法用于获取指定 blob 资源内容。

:::warning 注意
    - 如果资源在异域`<iframe>`元素内，必须获取该`<iframe>`元素对象，再把该对象传入才能获取到
    - 本方法只能用于获取静态的资源，流媒体不可以
:::

|    参数名称    |                                         类型                                          |  默认值   | 说明             |
|:----------:|:-----------------------------------------------------------------------------------:|:------:|----------------|
|   `page`   | `ChromiumPage`<br/>`ChromiumTab`<br/>`WebPage`<br/>`MixTab`<br/>`ChromiumFrame` |   必填   | 该资源所在的页面对象     |
|   `url`    |                                        `str`                                        |   必填   | blob 资源 url    |
| `as_bytes` |                                       `bool`                                        | `True` | 是否以`bytes`类型返回 |

|  返回类型   |                 说明                 |
|:-------:|:----------------------------------:|
|  `str`  | `as_bytes`参数为`False`时以 base64 格式返回 |
| `bytes` |    `as_bytes`参数为`True`时以字节数据返回     |

---

## ✅️️ `configs_to_here()`

此方法用于把 ini 文件复制到当前路径。

|    参数名称    |  类型   | 默认值 | 说明             |
|:----------:|:-----:|:---:|----------------|
|   `save_name`   | `str` |  `None`   | 指定文件名，为`None`则命名为`'dp_configs.ini'`   |

**返回：** `None`

---

## ✅️️ `wait_until()`

此方法用于等待传入的方法返回值不为假。超时则抛出`TimeoutError`。

|    参数名称    |     类型     |  默认值   | 说明      |
|:----------:|:----------:|:------:|---------|
| `function` | `callable` |   必填   | 要执行的方法  |
|  `kwargs`  |   `dict`   | `None` | 方法参数    |
| `timeout`  |   `float`   |  `10`  | 超时时间（秒） |

**返回：** `Any`

---

## ✅️️ `tree()`

此方法用于打印页面或元素结构。

|     参数名称      |    类型     |   默认值   | 说明                      |
|:-------------:|:---------:|:-------:|-------------------------|
| `ele_or_page` | 所有页面和元素对象 |   必填    | 页面或元素对象                 |
| `text` |  `bool`   | `False` | 是否打印元素文本                |
| `show_js` | `bool` |    `False`     | 打印文本时是否打印`<script>`标签内容 |
| `show_css` | `bool` |   `False`    | 打印文本时是否打印`<style>`标签内容  |

**返回：** `None`

---

## ✅️️ `Keys`

这是快速获取特殊按键和组合键的类。

---

## ✅️️ `By`

与 selenium 的`By`类一致，方便项目迁移。
