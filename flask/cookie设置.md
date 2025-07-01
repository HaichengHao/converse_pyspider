在Flask框架中设置Cookie可以通过`make_response`函数或者直接在返回`Response`对象时进行。以下是两种设置Cookie的方法：

### 方法一：使用 `make_response`

```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response('设置cookie')
    resp.set_cookie('username', 'admin')
    return resp
```

### 方法二：直接在视图函数返回`Response`对象时设置

如果你的视图函数返回的是一个模板，你也可以通过如下方式设置：

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 假设index.html是你的模板文件
    response = render_template('index.html')
    # 注意这种方法需要将render_template的结果转换为一个响应对象
    # 通常我们推荐使用第一种方法来设置cookie
```

不过，上面第二种方法中的说明可能存在误导。实际上，`render_template`返回的是一个字符串，而不是一个`Response`对象。正确的方式应该还是先用`make_response`包装一下：

```python
from flask import Flask, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    template = render_template('index.html')
    resp = make_response(template)
    resp.set_cookie('username', 'admin')
    return resp
```

### 设置更多选项

设置Cookie时还可以指定更多的参数，如过期时间、路径等：

```python
resp.set_cookie('username', 'admin', max_age=3600, path='/')
```

- `max_age`: Cookie的生存周期，以秒为单位。
- `path`: 设置此Cookie的有效路径。

通过这些步骤，你就可以在Flask应用中轻松地设置和管理Cookies了。