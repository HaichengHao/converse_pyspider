![](https://ask.qcloudimg.com/http-save/yehe-3043884/dw2c9xy33p.png)

摄影：产品经理

产品经理在七夕做的牛排

FastApi 自带的接口文档，让我们在开发后端接口的时候省了不少的工作量。它能自动根据你的代码识别接口的参数，还能根据你的注释生成接口的说明，如下图所示：

![](https://ask.qcloudimg.com/http-save/yehe-3043884/kw4jsj1srh.png)

但问题来了，难道你上线的时候也把这个接口开放给外界？如下图所示：

![](https://ask.qcloudimg.com/http-save/yehe-3043884/6fq60efui1.png)

重要接口的加密算法，就这么大摇大摆直接公开了，任何人只要在你的网址后面加上`/docs`就能看到。如果老板知道了，可能你就得当场滚蛋了吧。

为了保住饭碗，我们必须在上线的时候，把文档接口关了。只有在开发测试的时候才能打开。

### **关闭部分接口**

如何关闭部分接口？例如我做的这个服务，本身就是公共 API，就是拿给大家用的，只有几个核心接口隐藏一下，其他接口直接公开。

要隐藏部分接口，我们可以在路由装饰器上面添加一个参数`include_in_schema=False`，如下图所示：

代码语言：javascript

代码运行次数：0

运行

AI代码解释

复制

```javascript
@app.post('/login', include_in_schema=False)
def login(params: LoginInfo):
    """
    请求参数校验方案：
    token = md5(username + password + 'kingnameisyourfather' + ts[3] + ts[8] + ts[15])
    如果用户上传的 token 无法通过校验，则鉴权失败

    """
    user_token = params.token
    username = params.username
    password = params.password
    ts = params.ts
    correct_token = hashlib.md5((username + password + 'kingnameisyourfather' + ts[3] + ts[8] + ts[15]).encode()).hexdigest()
    if user_token != correct_token:
        return {'success': False, 'msg': '反爬虫成功！'}
    print('认证通过，开始进行后续处理')
    ...
    return {'success': True, 'data': 'xxx'}

```

运行效果如下图所示：

![](https://ask.qcloudimg.com/http-save/yehe-3043884/tnsguoy0s7.png)

可以看到，其他接口依然可以在文档中看到。但增加了这个排除参数的接口，已经从文档里面消失了。

关于`include_in_schema`参数，可以参阅官方文档：Path Operation Advanced Configuration - FastAPI\[1\]

### **隐藏所有接口**

如果你想把所有的接口全部关了怎么办呢？实际上也很简单，在初始化 FastApi 对象的时候，增加一个参数就可以了。

代码语言：javascript

代码运行次数：0

运行

AI代码解释

复制

```javascript
app = FastAPI(docs_url=None)
```

运行效果如下图所示：

![](https://ask.qcloudimg.com/http-save/yehe-3043884/aqvk13bccu.png)

好了，可以安心回家睡觉了——才怪。

FastAPI 实际上有两套文档系统，默认是同时开启的，我们刚刚只是关闭了其中一套。你试一试把`/docs`改成`/redoc`看看：

![](https://ask.qcloudimg.com/http-save/yehe-3043884/h8k0aa6vel.png)

要关闭 redoc也可以使用相同的方法：

代码语言：javascript

代码运行次数：0

运行

AI代码解释

复制

```javascript
app = FastAPI(docs_url=None, redoc_url=None)
```

运行效果如下图所示：

![](https://ask.qcloudimg.com/http-save/yehe-3043884/v7yn5p3wi7.png)

关于这两个参数的更多详情，比如说保留文档，但是把网址改名，可以参阅官方文档：Metadata and Docs URLs - FastAPI\[2\]

### **如何自动切换**

在开发阶段，我想要文档，在部署的时候，我不想要文档。难道每次都手动去改这几个参数？实际上不用，我们可以使用环境变量来自动控制，实现只有显式添加环境变量`env=develop`的时候才显示文档，其他情况下都不显示。部分代码如下：

代码语言：javascript

代码运行次数：0

运行

AI代码解释

复制

```javascript
import os
from fastapi import FastAPI

env = os.getenv('env')
if env != 'develop':
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    app = FastAPI()
```

当我们在自己电脑上开发的时候，我们在环境变量中添加一项`env`，它的值为`develop`，于是文档自动打开。当我们部署到线上环境的时候，把`env`的值设置成`prod`或者不设置，那么文档自动关闭。

* * *

#### **参考资料**

\[1\]

Path Operation Advanced Configuration - FastAPI: _https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/#exclude-from-openapi_

\[2\]

Metadata and Docs URLs - FastAPI: _https://fastapi.tiangolo.com/tutorial/metadata/#docs-urls_

本文转自 <https://cloud.tencent.com/developer/article/1697199>，如有侵权，请联系删除。