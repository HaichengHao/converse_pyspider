 

系列文章目录
------

Python 中 pip 常见命令

* * *

#### 文章目录

*   [系列文章目录](#_0)
*   [前言](#_10)
*   [一、python pip 命令](#python_pip__18)
*   [二、命令总结](#_25)
*   *   [1.显示列表pip list](#1pip_list_26)
    *   [2.安装命令pip install](#2pip_install_31)
    *   [3.安装完查看安装路径pip show](#3pip_show_46)
    *   [4.卸载安装包pip uninstall](#4pip_uninstall_51)
    *   [5.查看可以升级的包pip list -o](#5pip_list_o_56)
    *   [6.升级包pip install -U](#6pip_install_U_61)
    *   [7.搜索包pip search](#7pip_search_66)
    *   [8.查看已经安装的包及版本信息pip freeze](#8pip_freeze_69)
    *   [9.安装本地安装包](#9_72)
    *   [10.升级pip命令](#10pip_77)
    *   [10.导出命令pip freeze > 文件名](#10pip_freeze___89)
*   [总结](#_101)

* * *

前言
--

Python 中 pip 常见命令

* * *

提示：以下是本篇文章正文内容，下面命令可供参考

一、[python](https://so.csdn.net/so/search?q=python&spm=1001.2101.3001.7020) pip 命令
---------------------------------------------------------------------------------

主要用于“查询列表”和“安装”“更新”列表。

二、命令总结
------

### 1.显示列表pip list

pip list

代码如下（示例）：  
![pip list 显示列表如上图，为已经安装的](https://i-blog.csdnimg.cn/blog_migrate/7a65678be0a51c0f10e3490f0755e750.png)

### 2.安装命令pip install

1、pip install <包名>  
或  
2、pip install -r requirements.txt  
使用==,>=,<=,>,<来指定版本  
3、这里安装django：  
pip install Django==2.2  
代码如下（示例）：  
1、pip install bs4  
![pip install <包名>或pip install -r requirements.txt](https://i-blog.csdnimg.cn/blog_migrate/0b89ac869950dd3040e34cc598fe74ca.png)  
2、不演示

3、pip install Django==2.2  
![正在下载中](https://i-blog.csdnimg.cn/blog_migrate/aec31112439ca842809b1d46ca7c538a.png)  
![提示安装成功](https://i-blog.csdnimg.cn/blog_migrate/e428242b6913379088197a7c7e197daa.png)

### 3.安装完查看安装路径pip show

pip show

代码如下（示例）：  
![展示刚才安装的Django包的详细信息](https://i-blog.csdnimg.cn/blog_migrate/da10cd3c674129202a7160d448894bee.png)

### 4.卸载安装包pip uninstall

pip uninstall <包名>

代码如下（示例）：  
![输入“Y”开始卸载没输入“n”取消卸载，这里演示的是卸载成功](https://i-blog.csdnimg.cn/blog_migrate/bf1285c5ae88addaf51c5825e6820c40.png)

### 5.查看可以升级的包pip list -o

pip list -o

代码如下（示例）：  
![pip list -o](https://i-blog.csdnimg.cn/blog_migrate/a65deb5051588cf68c58118aa95a89c6.png)

### 6.升级包pip install -U

升级:pip install -U <包名>

代码如下（示例）：  
![例如升级包setuotools，安装成功](https://i-blog.csdnimg.cn/blog_migrate/8fea085784424fdd548802cff9154c45.png)

### 7.搜索包pip search

pip search <搜索关键字>

### 8.查看已经安装的包及版本信息pip freeze

代码如下（示例）：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/da81063b08fd1d82388c02ed29e18787.png)

### 9.安装本地安装包

pip install <目录>/<文件名>  
或  
pip install --use-wheel --no-index --find-links=wheelhouse/ <包名>

### 10.升级pip命令

pip install -U pip  
或

使用pip安装插件的时候报错时：

You are using pip version 8.1.1, however version 9.0.1 is available.

You should consider upgrading via the ‘python -m pip install --upgrade pip’ command.

升级命令： python -m pip install --upgrade pip

### 10.导出命令pip freeze > 文件名

导出到指定文件中，如图，注意 “ > ”，文件名称随意。常见按第二种写法。

代码如下（示例）：

![pip freeze > 文件名](https://i-blog.csdnimg.cn/blog_migrate/4206602ca3937c9d815a11c6aacd7564.png)  
![pip.txt打开可看到所有信息](https://i-blog.csdnimg.cn/blog_migrate/de835a0d4144a3fcff247b5247e2ce69.png)  

* * *

总结
--

pip常用的命令就这么多，还会持续在评论区更新。

本文转自 <https://blog.csdn.net/weixin_55018452/article/details/121989078>，如有侵权，请联系删除。