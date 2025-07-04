---
id: errors
title: '⚙️ 异常的使用'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

本节介绍 DrissionPage 中的自定义异常。

## ✅️️ 导入

各种异常放在`DrissionPage.errors`路径中。

```python
from DrissionPage.errors import *
```

## ✅️️ 异常介绍

### 📌 `ElementNotFoundError`

找不到元素时抛出。

---

### 📌 `AlertExistsError`

执行 JS 或调用通过 JS 实现的功能时，若存在未处理的弹出框则抛出。

--- 

### 📌 `ContextLostError`

页面被刷新后仍调用其中的元素时抛出。

---

### 📌 `ElementLostError`

元素因页面或自身被刷新而失效后，仍对其进行调用时抛出。

---

### 📌 `CDPError`

调用 cdp 方法产生异常时抛出。

---

### 📌 `PageDisconnectedError`

页面关闭或连接断开后仍调用其功能时抛出。

---

### 📌 `JavaScriptError`

JavaScript 运行错误时抛出。

---

### 📌 `NoRectError`

对没有大小和位置信息的元素获取这些信息时抛出。

---

### 📌 `BrowserConnectError`

连接浏览器出错时抛出。

---

### 📌 `NoResourceError`

浏览器元素`src()`和`save()`获取资源失败时抛出。

---

### 📌 `CanNotClickError`

---

点击元素时如元素不可点击，且设置允许抛出时抛出。

### 📌 `GetDocumentError`

获取页面文档失败时抛出

---

获取页面文档失败时抛出。

### 📌 `WaitTimeoutError`

自动等待失败，且设置允许抛出时抛出。

---

### 📌 `WrongURLError`

访问格式不正确的 url 时抛出。

---

### 📌 `StorageError`

操作数据时，如网站禁止操作则抛出。

---

### 📌 `CookieFormatError`

导入 cookie 时如格式不正确则抛出。
