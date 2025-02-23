 

从网上抓了一些字节流，想打印出来结果发生了一下错误：

UnicodeEncodeError: 'gbk' codec can't encode character '\\xbb' in position 8530: illegal multibyte sequence

代码

```python
import urllib.requestres=urllib.request.urlopen('http://www.baidu.com')htmlBytes=res.read()print(htmlBytes.decode('utf-8'))
```

  
错误信息让人很困惑，为什么用的是'utf-8'解码，错误信息却提示'gbk'错误呢？

不仅如此，从百度首页的html中发现以下代码：

```html
<meta http-equiv="content-type" content="text/html;charset=utf-8">
```

  
这说明网页的确用的是utf-8，为什么会出现Error呢？

在python3里，有几点关于编码的常识

1.字符就是[unicode](https://so.csdn.net/so/search?q=unicode&spm=1001.2101.3001.7020)字符，字符串就是unicode字符数组

如果用以下代码测试，

```python
print('a'=='\u0061')
```

  
会发现结果为True，足以说明两者的等价关系。

2.str转bytes叫encode，bytes转str叫decode，如上面的代码就是将抓到的字节流给decode成unicode数组

我根据上面的错误信息分析了字节流中出现\\xbb的地方，发现有个\\xc2\\xbb的特殊字符»，我怀疑是它无法被解码。

用以下代码测试后

```python
print(b'\xc2\xbb'.decode('utf-8'))
```

它果然报错了: UnicodeEncodeError: 'gbk' codec can't encode character '\\xbb' in position 0: illegal multibyte sequence

上网找了下utf-8编码表，发现的确特殊字符»的utf-8形式就是c2bb,unicode是'\\u00bb'，为什么无法解码呢。。。

仔细看看错误信息，它提示'gbk'无法encode，但是我的代码是utf-8无法decode，压根牛头不对马嘴，终于让我怀疑是print函数出错了。。于是立即有了以下的测试

```python
print('\u00bb')
```

结果报错了： UnicodeEncodeError: 'gbk' codec can't encode character '\\xbb' in position 0: illegal multibyte sequence

原来是print()函数自身有限制，不能完全打印所有的unicode字符。

知道原因后，google了一下解决方法，其实print()函数的局限就是Python默认编码的局限，因为系统是win7的，python的默认编码不是'utf-8',改一下python的默认编码成'utf-8'就行了

```python
import ioimport sysimport urllib.requestsys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码res=urllib.request.urlopen('http://www.baidu.com')htmlBytes=res.read()print(htmlBytes.decode('utf-8'))
```

  

运行后不报错了，但是居然有好多乱码（英文显示正常，中文则显示乱码）！！又一阵折腾后发现是控制台的问题，具体来说就是我在cmd下运行该脚本会有乱码，而在IDLE下运行却很正常。

由此我推测是cmd不能很好地兼容utf8，而IDLE就可以，甚至在IDLE下运行，连“改变标准输出的默认编码”都不用，因为它默认就是utf8。如果一定要在cmd下运行，那就改一下编码，比如我换成“gb18030”，就能正常显示了：

```python
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')         #改变标准输出的默认编码
```


最后，附上一些常用的和中文有关的编码的名称，分别赋值给encoding，就可以看到不同的效果了：

<table border="1" width="200" cellspacing="1" cellpadding="1"><tbody><tr><td>编码名称</td><td>用途</td></tr><tr><td>utf8</td><td>所有语言</td></tr><tr><td>gbk</td><td>简体中文</td></tr><tr><td>gb2312</td><td>简体中文</td></tr><tr><td>gb18030</td><td>简体中文</td></tr><tr><td>big5</td><td>繁体中文</td></tr><tr><td>big5hkscs</td><td>繁体中文</td></tr></tbody></table>

本文转自 <https://blog.csdn.net/jim7424994/article/details/22675759>，如有侵权，请联系删除。