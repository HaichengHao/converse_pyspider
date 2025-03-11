 

**什么是Python UV？**  
[UV](https://so.csdn.net/so/search?q=UV&spm=1001.2101.3001.7020)是由Astral公司（Rust工具Ruff的开发者）推出的高性能Python包管理工具，基于Rust编写，旨在替代传统的`pip`和`pip-tools`。其核心优势在于**极快的速度**（比`pip`快10-100倍）、**轻量级设计**（仅几十MB）以及**现代化的依赖管理**（支持`pyproject.toml`和`uv.lock`文件）。UV集成了虚拟环境管理、Python版本控制、依赖解析等功能，目标是成为类似[Rust](https://so.csdn.net/so/search?q=Rust&spm=1001.2101.3001.7020) Cargo的全能工具，简化Python开发流程。

* * *

**在Windows上安装UV的3种方法**

1.  **通过PIP安装（推荐）**  
    直接使用Python自带的`pip`安装，兼容性最佳：
    
    ```bash
    pip install uv
    ```
    
    安装后，`uv`会被添加到系统环境变量，即使切换虚拟环境也能使用。
    
2.  **PowerShell脚本安装**  
    打开PowerShell，执行：
    
    ```powershell
    irm https://astral.sh/uv/install.ps1 | iex
    ```
    
3.  **使用Pipx（适合全局工具管理）**  
    若已安装`pipx`：
    
    ```bash
    pipx install uv
    ```
    

**注意**：若通过包管理器（如Chocolatey）安装，可能版本较旧，建议优先使用`pip`或官方脚本。

* * *

**UV基础用法详解**

1.  **创建虚拟环境**
    
    ```bash
    uv venv .venv  # 默认创建.venv目录
    uv venv -p 3.12  # 指定Python版本（需已安装）
    ```
    
    **激活环境**：
    
    ```cmd
    .venv\Scripts\activate  # Windows
    ```
    
2.  **安装依赖包**  
    语法与`pip`一致，但速度更快：
    
    ```bash
    uv pip install requests pandas  # 安装最新版
    uv pip install "numpy>=1.21"  # 版本约束
    ```
    
3.  **初始化项目**
    
    ```bash
    uv init  # 生成pyproject.toml和uv.lock
    ```
    
4.  **同步依赖**  
    根据`pyproject.toml`和`uv.lock`自动安装依赖：
    
    ```bash
    uv sync
    ```
    
5.  **依赖管理**
    
    *   添加/移除包：
        
        ```bash
        uv add requests  # 自动更新pyproject.toml
        uv remove pandas
        ```
        
    *   导出依赖：
        
        ```bash
        uv pip freeze > requirements.txt  # 兼容传统格式
        ```
        

* * *

**典型工作流示例**  
假设新建项目`demo`：

```bash
mkdir demo && cd demo
uv init
echo "requests" > pyproject.toml  # 手动编辑依赖
uv sync  # 自动创建.venv并安装
.venv\Scripts\activate
uv pip list  # 查看已安装包
```

* * *

**为什么选择UV？**

*   **速度碾压传统工具**：依赖解析和安装耗时仅为`pip`的1/10。
*   **一体化管理**：无需额外安装`virtualenv`或`pyenv`，直接管理Python版本和依赖。
*   **跨平台支持**：Windows/Linux/macOS命令一致，减少学习成本。
*   **现代化标准**：支持`pyproject.toml`，与Rust/Node.js生态对齐。

若你受够了`pip`的缓慢和`conda`的臃肿，UV是当前最优解。

Python虚拟环境创建方式多样，除了`uv`之外，以下是其他主流方法及对比：

* * *

#### **1\. 内置工具：venv模块**

**适用场景**：Python 3.3+原生支持，无需安装额外工具

```bash
# 创建环境
python -m venv .venv  
# 激活（Windows）
.venv\Scripts\activate
```

**特点**：  
✅ 无需安装，开箱即用  
❌ 依赖解析功能较弱，不支持跨Python版本管理

* * *

#### **2\. 第三方工具：virtualenv**

**适用场景**：兼容Python 2/3，老项目维护

```bash
# 安装
pip install virtualenv  
# 创建环境
virtualenv myenv  
# 指定Python版本（需已安装）
virtualenv -p /path/to/python myenv
```

**特点**：  
✅ 支持旧版Python  
✅ 灵活指定解释器路径  
❌ 依赖`pip`安装，功能单一

* * *

#### **3\. 集成化工具：pipenv**

**适用场景**：依赖管理+虚拟环境一体化

```bash
# 安装
pip install pipenv  
# 创建环境并安装包
pipenv install requests  
# 激活
pipenv shell
```

**特点**：  
✅ 自动生成`Pipfile`和`Pipfile.lock`  
✅ 依赖解析更严谨  
❌ 性能较慢，社区活跃度下降

* * *

#### **4\. 科学计算生态：conda**

**适用场景**：数据科学/跨语言依赖管理

```bash
# 创建环境
conda create -n myenv python=3.11  
# 激活
conda activate myenv
```

**特点**：  
✅ 支持非Python包（如C++库）  
✅ 内置Python版本管理  
❌ 安装包体积大（约500MB）

* * *

#### **5\. 现代工具链：poetry**

**适用场景**：项目打包与依赖管理深度集成

```bash
# 初始化项目（自动创建环境）
poetry new myproject  
poetry install  
# 激活
poetry shell
```

**特点**：  
✅ 自动生成`pyproject.toml`  
✅ 支持依赖分组（dev/test）  
❌ 学习成本较高

* * *

#### **横向对比**

| 工具 | 启动速度 | Python版本管理 | 依赖管理 | 适用场景 |
| --- | --- | --- | --- | --- |
| `uv` | ⚡极快 | ✅ | ✅ | 现代项目全能工具 |
| `venv` | 中等 | ❌ | ❌ | 轻量级快速隔离 |
| `pipenv` | 较慢 | ❌ | ✅ | 依赖锁定的传统项目 |
| `conda` | 慢 | ✅ | ✅ | 数据科学/跨语言项目 |
| `poetry` | 中等 | ❌ | ✅ | 需要打包的库项目 |

* * *

#### **选择建议**

*   **追求极速**：优先选`uv`
*   **简单隔离**：用内置`venv`
*   **科学计算**：选`conda`
*   **项目发布**：用`poetry`
*   **旧版兼容**：选`virtualenv`

 

![](https://i-blog.csdnimg.cn/direct/25c590ae35a446cca9db802917d87d2b.jpeg)

Agent交流群，有问题可以进群提问

![](https://g.csdnimg.cn/extension-box/1.1.6/image/qq.png) QQ群名片

![](https://g.csdnimg.cn/extension-box/1.1.6/image/ic_move.png)

本文转自 <https://blog.csdn.net/xiezhipu/article/details/145638765>，如有侵权，请联系删除。