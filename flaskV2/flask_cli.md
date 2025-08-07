Flask CLI（Command Line Interface，命令行界面）是Flask框架提供的命令行工具，用于简化Flask应用的开发、测试和部署流程。通过它，你可以直接在终端中执行与Flask应用相关的命令，如启动开发服务器、运行测试、创建数据库等。

### Flask CLI的主要功能
1. 启动开发服务器
2. 运行Python shell（已加载Flask应用上下文）
3. 执行自定义命令（可扩展）
4. 管理应用配置和环境


### 基本使用方法

#### 1. 安装Flask
首先确保已安装Flask：
```bash
pip install flask
```


#### 2. 基本应用结构
假设你的Flask应用结构如下（以`app.py`为例）：
```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask CLI!"

if __name__ == '__main__':
    app.run()
```


#### 3. 基本命令使用

##### 查看所有可用命令
在终端中执行：
```bash
flask --help
```

##### 启动开发服务器
```bash
# 方式1：通过FLASK_APP环境变量指定应用
export FLASK_APP=app.py  # Linux/Mac
# 或
set FLASK_APP=app.py     # Windows

# 启动服务器
flask run
```

```bash
# 方式2：直接指定应用并启动（推荐）
flask --app app.py run
```

默认情况下，服务器会运行在 `http://127.0.0.1:5000/`


##### 启用调试模式
调试模式下，代码修改后服务器会自动重启，并显示详细错误信息：
```bash
export FLASK_DEBUG=1  # Linux/Mac
# 或
set FLASK_DEBUG=1     # Windows

flask run
```


##### 运行Python shell（带应用上下文）
```bash
flask shell
```
这会启动一个Python交互式环境，自动导入你的Flask应用实例，方便测试代码。


#### 4. 自定义命令
你可以通过装饰器`@app.cli.command()`定义自己的命令：

```python
# 在app.py中添加
@app.cli.command("hello")
def hello_command():
    """打印一句问候语"""
    print("Hello from custom command!")

@app.cli.command("add")
def add_numbers():
    """计算两个数的和"""
    a = 10
    b = 20
    print(f"{a} + {b} = {a + b}")
```

使用自定义命令：
```bash
flask hello   # 执行hello命令
flask add     # 执行add命令
```


#### 5. 高级用法：使用工厂函数
当使用应用工厂模式时（大型应用常用），需要稍作调整：

```python
# app.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return "Hello from factory!"
    
    return app
```

启动命令：
```bash
flask --app "app:create_app()" run
```


通过Flask CLI，你可以更高效地管理Flask应用的整个生命周期，尤其是在开发和调试阶段。对于复杂应用，自定义命令可以极大简化重复性工作。


你的写法是正确的！`flask --debug --app app.py run` 这条命令完全可行，它会以调试模式启动 `app.py` 中的Flask应用。

### 关于命令的说明：
- `--debug`：启用调试模式（等同于设置 `FLASK_DEBUG=1`）
- `--app app.py`：指定Flask应用所在的文件
- `run`：启动开发服务器


### 自定义IP地址和端口号
可以在 `run` 命令后添加参数来指定IP和端口：

```bash
# 自定义端口（默认5000）
flask --debug --app app.py run --port 8080

# 自定义IP（默认127.0.0.1）
flask --debug --app app.py run --host 0.0.0.0

# 同时自定义IP和端口
flask --debug --app app.py run --host 0.0.0.0 --port 8080
```

#### 常见参数说明：
- `--host 0.0.0.0`：允许局域网内其他设备访问你的应用（开发测试常用）
- `--port 8080`：将端口改为8080（可替换为1-65535之间的任意未占用端口）


### 补充：更简洁的写法
如果你觉得命令太长，可以通过设置环境变量简化：

```bash
# Linux/Mac
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run --host 0.0.0.0 --port 8080

# Windows
set FLASK_APP=app.py
set FLASK_DEBUG=1
flask run --host 0.0.0.0 --port 8080
```

这样后续只需执行 `flask run --host 0.0.0.0 --port 8080` 即可。

在 Flask 中，当你同时在代码中通过 `app.run()` 设置参数 **和** 在命令行通过 `flask run` 指定参数时，**命令行参数的优先级更高**。

具体来说：
- 如果你在 `app.py` 中写了 `app.run(debug=True, host='127.0.0.1', port=8090)`
- 同时在命令行执行 `flask --debug --app app.py run --host 0.0.0.0 --port 8080`

最终生效的参数是 **命令行中指定的**：
- `debug=True`（命令行 `--debug` 与代码 `debug=True` 效果一致，不冲突）
- `host=0.0.0.0`（命令行参数覆盖代码中的 `127.0.0.1`）
- `port=8080`（命令行参数覆盖代码中的 `8090`）


### 为什么会这样？
Flask 的设计逻辑是：**命令行参数是“运行时配置”，优先级高于代码中的“默认配置”**。这样可以灵活地在不修改代码的情况下，临时调整运行参数（比如开发时用不同端口测试）。


### 建议用法
为了避免混淆，通常有两种推荐方式：
1. **只在命令行指定参数**，代码中简化为 `app.run()`（不写具体参数）
2. **在代码中写默认参数**，仅在需要临时修改时通过命令行覆盖

例如，代码中保留默认值：
```python
# app.py
if __name__ == '__main__':
    # 只写默认参数，需要时通过命令行覆盖
    app.run(debug=True, host='127.0.0.1', port=8090)
```

需要修改时，用命令行覆盖：
```bash
# 临时改用8080端口，命令行参数生效
flask --app app.py run --port 8080
```