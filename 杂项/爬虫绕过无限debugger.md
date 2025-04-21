 

一、无限debugger的原因：  
我们在实践的过程中，经常发现一些网站，刚按F12进入控制台，就会进入一个debugger状态，并且无论你怎么下一步运行，代码永远停留在这个断点的地方。这个就是反[爬虫](https://so.csdn.net/so/search?q=%E7%88%AC%E8%99%AB&spm=1001.2101.3001.7020)的一个重要手段：无限debugger。  
debugger关键字是用于浏览器调试的，这个关键字在控制台没有打开的时候是不会起到任何暂停作用，但是一旦控制台被打开了，代码将停在debugger关键字所在的地方。再配合setInterval定时器，可以一直停留在某个debugger地方，阻止调试。  
二、无限debugger解决方案：

1.  关掉全局断点：  
    我们可以在浏览器右边，把那个断点按钮，取消选中，这样所有的js代码都不会被断点了。这样就可以去分析代码了。但是这样也有一个很不好的，就是我们没法自己设置断点去破解他的逻辑，所以这种方式是在一些简单的js逻辑的时候推荐使用。
    
2.  关掉局部断点：  
    局部断点是，有时候我们会发现debugger只在某一行出现，所以我们只要把这一行去掉断点就可以了。在有debugger的代码行，在行号地方右键，点击Never pause here，这样就永远不会停留在这里了。但是这种方法在遇到动态产生debugger关键字的时候会失效。
    
3.  用条件断点：  
    条件断点是，在JS代码某一行，设置某个条件，当条件不成立的时候，就不会在这里暂停了。一般我们会设置为一个永远为false的断点，这样断点永远也不会在这个地方暂停下来了。同样，这种方法在动态生成的debugger关键字的时候会失效。
    
4.  重写断点函数：  
    我们在分析代码的时候，可以看到调用栈，在发现某个函数下有debugger的时候，可以把这个函数在调用之前进行重写，重写的时候把debugger关键字去掉。  
    (1)F12开始调试后出现debugger:![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/6025dda396f829e68aad1c01ec66a29a.png)  
    (2)从代码中可知,无限debugger产生的原因是第七行代码debuggerFunction这个函数造成的,所以我们可以重写这个函数,使无限debugger失效.在控制台中输入function debuggerFunction(){}即可,如图:  
    ![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/b3ed0e2b989aea7f3b576c5de05e123b.png)
    
5.  替换js文件：  
    如果发现无限debugger代码逻辑比较复杂，不是一两个函数能重写的。那么我们可以把js文件拿下来放到编辑器里好好阅读，理解好了后把无限debugger逻辑处理掉，再进行替换。替换的方式有多种，这里一一进行介绍。  
    5.1 用浏览器直接替换：  
    在浏览器的Sources面板中，有一个Override。  
    ![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/e2309797511c40be28d7be02c833411e.png)
    

然后选择一个本地的空文件夹。  
接着，在Page面板中，找到你需要替换的文件，然后右键->Save for overrides，再回到Override面板中，就可以看到之前加的那个文件夹中有一个同名的文件了，然后就可以在里面编辑代码，重写原网页中的代码了。重写完成后，记得在打开控制台的基础之上，重新刷新下页面。

5.2 用Reres插件替换文件(推荐使用)：  
Reres是一个Chrome插件，可以设置规则，来代理某些请求，变成你本地的文件。比如：  
找到产生无限debugger的js文件,重写这个文件,比如:(我们将产生无限debugger的代码注释掉),![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/232710fa432eb3cbedb70633645567ae.png)  
再使用Rerse插件替换掉网页上的js文件  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/960ba73671e47d28f46f14aadaed3f8b.png)  
这样就可以过掉无限debugger了.

5.3 用Fiddler软件替换：  
Fiddler是一款抓包工具，他相当于是一个浏览器和服务器的中间人。服务器返回的数据后会经过Fiddler，然后Fiddler再把这个响应返回给浏览器，在返回的过程中，可以实现修改其中的文件，来达到欺骗浏览器的目的。  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/5c1355b1b8908d3a8a6757bf88fb121a.png)

本文转自 <https://blog.csdn.net/FreeTime_9527/article/details/121198359>，如有侵权，请联系删除。