# @Editor    : 百年
# @FileName  :41re提取分组数据.py
# @Time      :2024/4/28 10:52
'''
学习本节之前，要掌握上节的预加载的知识
两个步骤
1.写好预加载的对象
obj=re.compile(pattern)  pattern->正则语法
2.利用创建的对象调用re模块的方法
result = obj.findall(待匹配字符串)/match(待匹配字符串)/finditer(待匹配字符串)...
'''

import re

s = """
<div class='⻄游记'><span id='10010'>中国联通</span></div>
<span id='10086'>中国移动</span></div>
"""
# obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>\w+)</span>", re.S)
obj = re.compile(r"<span id='\d+'>.*?</span></div>")
result = obj.findall(s)
print(result)
# ["<span id='10010'>中国联通</span></div>", "<span id='10086'>中国移动</span></div>"]
# 我们发现，匹配是匹配了，但是全匹配到了，而我们只想要那个号码和运营商名称
# 那么查看note/39正则表达式.txt可以看到元字符里有个 ''() 匹配括号内的表达式，也表示一组''
# 说明我们可以用小括号括起来我们想要匹配的数据

# 有了上面的思路，我们再次验证
# 预加载
obj2 = re.compile(r"<span id='(\d+)'>(.*?)</span></div>")
# 利用创建的对象进行查找
result2 = obj2.findall(s)

# 查看结果
print(result2)
# [('10010', '中国联通'), ('10086', '中国移动')] <--可以看到匹配到了我们想要的结果，返回的是匹配的列表，内部元素是符合匹配规则的内容组成的元组

# 对于匹配结果我们还不是完全的满意，所以请看下面的操作

# 预加载
# 利用?P<指定的分组名称> 可以把匹配到的数据进行分组，例如我们要匹配到的是运营商的号码和运营商的名称，那么我们就利用这个方式就可对匹配到的数据进行分组
obj3 = re.compile(r"<span id='(?P<phonenumber>\d+)'>(?P<manager>.*?)</span></div>")
# 利用创建的对象进行查找,不过这次我们用的是.finditer()
result3 = obj3.finditer(s)

# 因为.finditer()返回的是一个迭代器

# 查看结果
print(result3)
# <callable_iterator object at 0x0000029EAA0E3D90>

# 所以我们要查看迭代器对象包含的元素
for item in result3:
    print(item.group("phonenumber"))
    print(item.group("manager"))