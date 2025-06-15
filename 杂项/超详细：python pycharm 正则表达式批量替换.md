 

      在使用python爬虫中，需要对复制好的网页代码进行[正则表达式](https://so.csdn.net/so/search?q=%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F&spm=1001.2101.3001.7020)批量替换，这时候需要借助EditPlus等工具进行替换，但是在pycharm中也可以使用快捷命令进行替换。

(csdn上写这个方便自己复制替换QAQ)

**目录**

[一、打开pycharm，将复制好的信息粘贴](#t0)

[二、输入替换格式](#t1)

[三、选中需要替换的部分](#t2)

[四、点击全部替换](#t3)

* * *

### 一、打开pycharm，将复制好的信息粘贴

使用快捷键Ctrl+R，打开替换界面

![](https://i-blog.csdnimg.cn/blog_migrate/d9bcf58228fe59077b9bcc0a6398f31c.png)

### 二、输入替换格式

在第一个框输入

```lisp
(.*?):(.*)
```

第二个框输入

```dart
'$1':'$2',
```

结果如下：

![](https://i-blog.csdnimg.cn/blog_migrate/22aff3e519b2c247667f21b63b4748f6.png)

### 三、选中需要替换的部分

![](https://i-blog.csdnimg.cn/blog_migrate/fe2aaa1c17d1157cd0052078f626b231.png)

### 四、点击全部替换

![](https://i-blog.csdnimg.cn/blog_migrate/52e747abe558b49f7ccb93e6f7a9d0c5.png)

