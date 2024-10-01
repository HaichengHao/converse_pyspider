 

前言
--

为了帮助我们了解该文件的一些相关信息，文件的头部注释的配置还是很有必要的。  
~[同步地址](https://www.xuyifan.top/archives/pycharm-sets-python-file-header-template-information.html)~

实现方法
----

依次点击：`File -> Settings -> Editor -> File and Code Templates -> Files -> Python Script`，图教程如下：  
![进入设置](https://i-blog.csdnimg.cn/blog_migrate/3793d5cbf7a2aec654ee072742d39407.png#pic_center)  
![配置模板](https://i-blog.csdnimg.cn/blog_migrate/9d503b2cf502b2ad85dee9f2c69cc82c.png#pic_center)

编辑内容
----

> PyCharm中预设的一些模板信息，如下：

```bash
#[[$END$]]# - 创建的新文件光标的默认位置
${USER} - 当前用户的登录名。
${DATE} - 当前系统日期。
${TIME} - 当前系统时间。
${YEAR} - 今年。
${MONTH} - 当月。
${DAY} - 当天。
${HOUR} - 当前小时。
${MINUTE} - 当前分钟。
${NAME} - 在文件创建过程中在“新建文件”对话框中指定的新文件的名称。
${PRODUCT_NAME} - 将在其中创建文件的IDE的名称。
${PROJECT_NAME} - 当前项目的名称。
${MONTH_NAME_SHORT} - 月份名称的前3个字母。 示例：一月，二月等
${MONTH_NAME_FULL} - 一个月的全名。 示例：一月，二月等
```

效果展示
----

设置完之后，让我们新建一个[Python](https://so.csdn.net/so/search?q=Python&spm=1001.2101.3001.7020)文件看看效果吧。

![效果展示](https://i-blog.csdnimg.cn/blog_migrate/245268e78fa219143aab59b2f40a19d1.png#pic_center)

### 我的模板

```python
"""
 @Author: ${USER}
 @Email: xxx@xxx.com
 @FileName: ${NAME}.py
 @DateTime: ${DATE} ${TIME}
 @SoftWare: ${PRODUCT_NAME}
"""

if __name__ == '__main__':
    pass#[[$END$]]#
```

本文转自 <https://blog.csdn.net/xyf0209/article/details/119929423>，如有侵权，请联系删除。