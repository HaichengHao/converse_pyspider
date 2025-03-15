###简单介绍  
lua是一个脚本语言，游戏后台语言有他的身影
```
    function main(splash, args)
      splash:go(args.url)   这里相当于selenium中的br0.get(url)
      splash:wait(0.5)
      return {
        html = splash:html(), 这里是加载js之后的页面源码
        png = splash:png(),  这里是页面截图
        har = splash:har(), 这是页面加载的详情
      }
    end
```            
### lua语法符号的一些细节  
对象.属性   
周瑜.血量  
args.url   

对象:方法()  
周瑜:放火()  
splash:go()  