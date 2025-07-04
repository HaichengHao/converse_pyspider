---
id: import
title: 🌏 导入
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

## ✅️ 页面类

页面类是最主要的工具，用于控制浏览器或收发数据包。

DrissionPage 包含三种主要页面类。根据需要在其中选择使用。

### 📌 `ChromiumPage`

如果只要控制浏览器，导入`ChromiumPage`。

```python
from DrissionPage import ChromiumPage
```

---

### 📌 `SessionPage`

如果只要收发数据包，导入`SessionPage`。

```python
from DrissionPage import SessionPage
```

---

### 📌 `WebPage`

`WebPage`是功能最全面的页面类，既可控制浏览器，也可收发数据包。

```python
from DrissionPage import WebPage
```

---

## ✅️ 配置工具

### 📌 `ChromiumOptions`

`ChromiumOptions`类用于设置浏览器启动参数。

这些参数只有在启动浏览器时有用，接管已存在的浏览器时是不生效的。

```python
from DrissionPage import ChromiumOptions
```

---

### 📌 `SessionOptions`

`SessionOptions`类用于设置`Session`对象启动参数。

用于配置`SessionPage`或`WebPage`s 模式的连接参数。

```python
from DrissionPage import SessionOptions
```

---

### 📌 `Settings`

`Settings`用于设置全局运行配置，如找不到元素时是否抛出异常等。

```python
from DrissionPage.common import Settings
```

---

## ✅️ 其它工具

其它可能用到的工具，放在`DrissionPage.common`路径。

### 📌 `Keys`

键盘按键类，用于键入 ctrl、alt 等按键。

```python
from DrissionPage.common import Keys
```

---

### 📌 `Actions`

动作链，用于执行一系列动作。

在浏览器页面对象中已有内置，无如特殊需要无需主动导入。

```python
from DrissionPage.common import Actions
```

---

### 📌 `By`

与 selenium 一致的`By`类，便于项目迁移。

```python
from DrissionPage.common import By
```

---

### 📌 其它工具

- `wait_until`：可等待传入的方法结果为真
- `make_session_ele`：从 html 文本生成`ChromiumElement`对象
- `configs_to_here`：把配置文件复制到当前路径
- `get_blob`：获取指定的 blob 资源
- `tree`：用于打印页面对象或元素对象结构
- `from_selenium`：用于对接 selenium 代码
- `from_playwright`：用于对接 playwright 代码

```python
from DrissionPage.common import wait_until
from DrissionPage.common import make_session_ele
from DrissionPage.common import configs_to_here
```

---

## ✅️ 异常

异常放在`DrissionPage.errors`路径。

全部异常详见进阶使用章节。

```python
from DrissionPage.errors import ElementNotFoundError
```

---

## ✅️ 衍生对象类型

Tab、Element 等对象是由 Page 对象生成，开发过程中需要类型判断时需要导入这些类型。

可在`DrissionPage.items`路径导入。

```python
from DrissionPage.items import SessionElement
from DrissionPage.items import ChromiumElement
from DrissionPage.items import ShadowRoot
from DrissionPage.items import NoneElement
from DrissionPage.items import ChromiumTab
from DrissionPage.items import MixTab
from DrissionPage.items import ChromiumFrame
```