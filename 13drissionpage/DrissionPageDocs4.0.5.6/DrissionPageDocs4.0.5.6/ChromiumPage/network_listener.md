---
id: listener
title: '🚤 监听网络数据'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

许多网页的数据来自接口，在网站使用过程中动态加载，如使用 JS 加载内容的翻页列表。

这些数据通常以 json 形式发送，浏览器接收后，对其进行解析，再加载到 DOM 相应位置。

做数据采集的时候，我们往往从 DOM 中去获取解析后数据的，可能存在数据不全、加载响应不及时、难以判断加载完成等问题。

如果我们可以拿到浏览器收发的数据包，根据数据包状态判断下一步操作，甚至直接获取数据，岂不是爽爆了？

DrissionPage 每个页面对象（包括 Tab 和 Frame 对象）内置了一个监听器，专门用于抓取浏览器数据包。

可以提供等待和捕获指定数据包，实时返回指定数据包功能。

## ✅️ 示例

先看两个示例了解监听器工作方式。

:::warning 注意
    要先启动监听，再执行动作，`listen.start()`之前的数据包是获取不到的。
:::

### 📌 等待并获取

点击下一页，等待数据包，再点击下一页，循环。

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://gitee.com/explore/all')  # 访问网址，这行产生的数据包不监听

page.listen.start('gitee.com/explore')  # 开始监听，指定获取包含该文本的数据包
for _ in range(5):
    page('@rel=next').click()  # 点击下一页
    res = page.listen.wait()  # 等待并获取一个数据包
    print(res.url)  # 打印数据包url
```

**输出：**

```shell
https://gitee.com/explore/all?page=2
https://gitee.com/explore/all?page=3
https://gitee.com/explore/all?page=4
https://gitee.com/explore/all?page=5
https://gitee.com/explore/all?page=6
```

---

### 📌 实时获取

跟上一个示例做同样的事情，不过换一种方式。

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.listen.start('gitee.com/explore')  # 开始监听，指定获取包含该文本的数据包
page.get('https://gitee.com/explore/all')  # 访问网址

i = 0
for packet in page.listen.steps():
    print(packet.url)  # 打印数据包url
    page('@rel=next').click()  # 点击下一页
    i += 1
    if i == 5:
        break
```

---

## ✅️ 设置目标和启动监听

### 📌 `listen.start()`

此方法用于启动监听器，启动同时可设置获取的目标特征。

可设置多个特征，符合条件的数据包会被获取。

如果监听未停止时调用这个方法，可清除已抓取的队列。

|    参数名称    |                 类型                  |   默认值   | 说明                                                              |
|:----------:|:-----------------------------------:|:-------:|-----------------------------------------------------------------|
| `targets`  | `str`<br/>`list`<br/>`tuple`<br/>`set` | `None`  | 要匹配的数据包 url 特征，可用列表指定多个，为`True`时获取所有                            |
| `is_regex` |               `bool`                | `None` | 设置的 target 是否正则表达式，为`None`时保持原来设置                               |
|  `method`  | `str`<br/>`list`<br/>`tuple`<br/>`set` | `None`  | 设置监听的请求类型，可指定多个，默认`('GET', 'POST')`，为`True`时监听所有，为`None`时保持原来设置 |
| `res_type` | `str`<br/>`list`<br/>`tuple`<br/>`set` | `None`  | 设置监听的 ResourceType 类型，可指定多个，为`True`时监听所有，为`None`时保持原来设置         |

**返回：** `None`

:::warning 注意
    当`targets`不为`None`，`is_regex`会自动设为`False`。  
    即如要使用正则，每次设置`targets`时需显式指定`is_regex=True`。  
:::

--- 

### 📌 `listen.set_targets()`

此方法可在监听过程中修改监听目标，也可在监听开始前设置。

如监听未启动，不会启动监听。

|    参数名称    |                 类型                  |        默认值        | 说明                                               |
|:----------:|:-----------------------------------:|:-----------------:|--------------------------------------------------|
| `targets`  | `str`<br/>`list`<br/>`tuple`<br/>`set` |      `True`       | 要匹配的数据包 url 特征，可用列表指定多个，为`True`时获取所有             |
| `is_regex` |               `bool`                |      `False`      | 设置的 target 是否正则表达式                               |
|  `method`  | `str`<br/>`list`<br/>`tuple`<br/>`set` | `('GET', 'POST')` | 设置监听的请求类型，可指定多个，默认`('GET', 'POST')`，为`True`时监听所有 |
| `res_type` | `str`<br/>`list`<br/>`tuple`<br/>`set` |      `True`       | 设置监听的 ResourceType 类型，可指定多个，为`True`时监听所有         |

**返回：** `None`

--- 

## ✅️ 等待和获取数据包

### 📌 `listen.wait()`

此方法用于等待符合要求的数据包到达指定数量。

所有符合条件的数据包都会存储到队列，`wait()`实际上是逐个从队列中取结果，不用担心页面已刷走而丢包。

|    参数名称     |        类型         |  默认值   | 说明                                                 |
|:-----------:|:-----------------:|:------:|----------------------------------------------------|
|   `count`   |       `int`       |  `1`   | 需要捕捉的数据包数量                                         |
|  `timeout`  | `float`<br/>`None` | `None` | 超时时间，为`None`无限等待                                   |
| `fit_count` |      `bool`       | `True` | 是否必需满足总数要求，如超时，为`True`返回`False`，为`False`返回已捕捉到的数据包 |
| `raise_err` |      `bool`       | `None` | 超时时是否抛出错误，为`None`时根据`Settings`设置，如不抛出，超时返回`False`  |

|        返回类型        | 说明                                                |
|:------------------:|---------------------------------------------------|
|    `DataPacket`    | `count`为`1`且未超时，返回一个数据包对象                         |
| `List[DataPacket]` | `count`大于`1`，未超时或`fit_count`为`False`，返回数据包对象组成的列表 |
|      `False`       | 超时且`fit_count`为`True`时                            |

---

### 📌 `listen.steps()`

此方法返回一个可迭代对象，用于`for`循环，每次循环可从中获取到的数据包。

可实现实时获取并返回数据包。

如果`timeout`超时，会中断循环。

|   参数名称    |        类型         |  默认值   | 说明                      |
|:---------:|:-----------------:|:------:|-------------------------|
|  `count`  |       `int`       | `None` | 需捕获的数据包总数，为`None`表示无限   |
| `timeout` | `float`<br/>`None` | `None` | 每个数据包等待时间，为`None`表示无限等待 |
|   `gap`   |       `int`       |  `1`   | 每接收到多少个数据包返回一次数据        |

|        返回类型        | 说明                      |
|:------------------:|-------------------------|
|    `DataPacket`    | `gap`为`1`时，返回一个数据包对象    |
| `List[DataPacket]` | `gap`大于`1`，返回数据包对象组成的列表 |

---

### 📌 `listen.wait_silent()`

此方法用于等待所有指定的请求完成。

|      参数名称      |         类型         |   默认值   | 说明                    |
|:--------------:|:------------------:|:-------:|-----------------------|
|   `timeout`    | `float`<br/>`None` | `None`  | 等待时间，为`None`表示无限等待    |
| `targets_only` |       `bool`       | `False` | 是否只等待`targets`指定的请求结束 |
|    `limit`     |       `int`        |   `0`   | 剩下多少个连接时视为结束          |

|  返回类型  | 说明     |
|:------:|--------|
| `bool` | 是否等待成功 |

---

## ✅️ 暂停和恢复

### 📌 `listen.pause()`

此方法用于暂停监听。

|  参数名称   |   类型   |  默认值   | 说明        |
|:-------:|:------:|:------:|-----------|
| `clear` | `bool` | `True` | 是否清空已获取队列 |

**返回：** `None`

---

### 📌 `listen.resume()`

此方法用于继续暂停的监听。

**参数：** 无

**返回：**`None`

---

### 📌 `listen.stop()`

此方法用于终止监听器的运行，会清空已获取的队列，不清空 targets。

**参数：** 无

**返回：**`None`

---

## ✅️ `DataPacket`对象

`DataPacket`对象是获取到的数据包结果对象，包含了数据包各种信息。

### 📌 `对象属性`

|      属性名称      |    数据类型    | 说明             |
|:--------------:|:----------:|----------------|
|    `tab_id`    |   `str`    | 产生这个请求的标签页的 id |
|   `frameId`    |   `str`    | 产生这个请求的框架 id   |
|    `target`    |   `str`    | 产生这个请求的监听目标    |
|     `url`      |   `str`    | 数据包请求网址        |
|    `method`    |   `str`    | 请求类型           |
|  `is_failed`   |   `bool`   | 是否连接失败         |
| `resourceType` |   `str`    | 资源类型           |
|   `request`    | `Request`  | 保存请求信息的对象      |
|   `response`   | `Response` | 保存响应信息的对象      |
|  `fail_info`   | `FailInof` | 保存连接失败信息的对象    |

### 📌 `wait_extra_info()`

有些数据包有`extra_info`数据，但这些数据可能会迟于数据包返回，用这个方法可以等待这些数据加载到数据包对象。

|   参数名称    |        类型         |  默认值   | 说明               |
|:---------:|:-----------------:|:------:|------------------|
| `timeout` | `float`<br/>`None` | `None` | 超时时间，`None`为无限等待 |

|  返回类型  | 说明     |
|:------:|--------|
| `bool` | 是否等待成功 |

### 📌 `Request`对象

`Request`对象是`DataPacket`对象内用于保存请求信息的对象，有以下属性：

|    属性名称    |         数据类型          | 说明                                |
|:----------:|:---------------------:|-----------------------------------|
|   `url`    |         `str`         | 请求的网址                             |
|  `method`  |         `str`         | 请求类型                              |
| `headers`  | `CaseInsensitiveDict` | 以大小写不敏感字典返回 headers 数据            |
| `cookies`  |     `List[dict]`      | 返回发送的 cookies                     |
| `postData` |   `str`<br/>`dict`    | post 类型的请求所提交的数据，json 以`dict`格式返回 |

除以上常用属性，还有以下属性，自行体会：

urlFragment、hasPostData、postDataEntries、mixedContentType、initialPriority、referrerPolicy、isLinkPreload、trustTokenParams、isSameSite

---

### 📌 `Response`对象

`Response`对象是`DataPacket`对象内用于保存响应信息的对象，有以下属性：

|    属性名称    |             数据类型             | 说明                                                       |
|:----------:|:----------------------------:|----------------------------------------------------------|
|   `url`    |            `str`             | 请求的网址                                                    |
| `headers`  |    `CaseInsensitiveDict`     | 以大小写不敏感字典返回 headers 数据                                   |
|   `body`   | `str`<br/>`bytes`<br/>`dict` | 如果是 json 格式，转换为`dict`；如果是 base64 格式，转换为`bytes`，其它格式直接返回文本 |
| `raw_body` |            `str`             | 未被处理的 body 文本                                            |
| `status` |            `int`             | 请求状态                                                     |
| `statusText` |            `str`             | 请求状态文本                                                   |

除以上属性，还有以下属性，自行体会：

headersText、mimeType、requestHeaders、requestHeadersText、connectionReused、connectionId、remoteIPAddress、remotePort、fromDiskCache、fromServiceWorker、fromPrefetchCache、encodedDataLength、timing、serviceWorkerResponseSource、responseTime、cacheStorageCacheName、protocol、alternateProtocolUsage、securityState、securityDetails

--- 

### 📌 `FailInfo`对象

`FailInfo`对象是`DataPacket`对象内用于保存连接失败信息的对象，有以下属性：

|       属性名称        |  数据类型  | 说明        |
|:-----------------:|:------:|-----------|
|    `errorText`    | `str`  | 错误信息文本    |
|    `canceled`     | `bool` | 是否取消      |
|  `blockedReason`  | `str`  | 拦截原因      |
| `corsErrorStatus` | `str`  | cors 错误状态 |
