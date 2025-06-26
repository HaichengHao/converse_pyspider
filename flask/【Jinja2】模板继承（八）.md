 

一、模板继承
------

通过关键字_**extends**_来实现

语法格式：_**{% extends "父模板.html" %}**_

例如：

定义一个访问父模板和一个访问字模板的路由：

```python
@app.route('/base')def my_base():    return render_template("base.html") @app.route('/child1')def my_child():    return render_template("child1.html")
```

编写名为base.html的父模板中代码：

![](https://i-blog.csdnimg.cn/blog_migrate/138d58c44f3d36fc5da66e99b9440c4c.png)

浏览器访问路由可以看见：

![](https://i-blog.csdnimg.cn/blog_migrate/167404927815c9c1e35e4bf59f911c0f.png)

如果想要继承base.html模板，在子模板child1.html中利用关键字extends导入父模板即可：

![](https://i-blog.csdnimg.cn/blog_migrate/454f69c518a7993e4c8210d0f4a4a7c0.png)

访问子模板的路由，可以看见显示出了父模板的标题和内容：

![](https://i-blog.csdnimg.cn/blog_migrate/564a4d892a3fa10dced9266d18a7ef7c.png)

   
二、子模板中内容改写
--------------

        使用子模板继承父模板时，希望改写部分代码块，可以在父模板和子模板中利用block语法结构来实现。具体使用方法是，父模板和子模板中引入同样的语法结构_**{% block content  %} ...{% endblock %}**_，content表示这段代码块的名字，可以由我们自己命名，保持父和子模板名字一致即可，比如将他命名为title、body之类的都可以，子模板中，[省略号](https://so.csdn.net/so/search?q=%E7%9C%81%E7%95%A5%E5%8F%B7&spm=1001.2101.3001.7020)位置可以写入我们希望改写的代码。

示例：

![](https://i-blog.csdnimg.cn/blog_migrate/3e5d90c4d508e1c287e7d60003a3693d.png)

![](https://i-blog.csdnimg.cn/blog_migrate/f5439db018c1fda83ca7324ed9662409.png)

此时，访问子模板路由：

![](https://i-blog.csdnimg.cn/blog_migrate/8e26facc82b7fe03676128f6128df975.png)

如图所示，已经继承了父模板，并且将标题和内容代码改写了。

三、项目演示
------

1、入口程序

模板继承.py

```python
from flask import Flask,render_template app = Flask(__name__) @app.route('/child1')def child1():    return render_template('child1.html') @app.route('/child2')def child2():    return render_template('child2.html') if __name__ == '__main__':    app.run()
```

 2、父模板

parent.html

```html
<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>{% block title  %}{% endblock %}</title></head><body><ul>    <li><a href="#">首页</a></li>    <li><a href="#">新闻</a></li></ul>{% block body %}{% endblock %}<footer>这是底部的标签</footer></body></html>
```

3、子模板

child1.html

```html
{#通过extends参数实现#}{% extends "base.html" %} {% block title %}我是child1的标题{% endblock %} {% block body %}我是child1的body{% endblock %}
```

child2.html

```html
{% extends "base.html" %} {% block title %}我是child2的标题{% endblock %} {% block body %}我是child2的body{% endblock %}
```

4、启动入口程序，地址栏输入地址

![](https://i-blog.csdnimg.cn/blog_migrate/06538cc80cbb84d28a8b379042a7e02b.png)

本文转自 <https://blog.csdn.net/hold_on_qlc/article/details/128179468>，如有侵权，请联系删除。