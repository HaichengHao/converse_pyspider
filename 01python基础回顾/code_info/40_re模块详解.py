# editor: 百年
# time: 2024/3/17 16:17
import re

str='我叫张大炮，今年30岁，年薪800000块'
ptn='\d+'

#
# 1. re.findall(pattern, string,flags)
#         pattern 匹配规则
#         string 待匹配字符串
#         flags 标志位表示匹配多少次
target=re.findall(pattern=ptn,string=str)
# 也可直接写明匹配规则
# 但是要注意"\"反斜杠在python中表示的是转义字符，所以为了避免出现错误，需要用规则的原义,即加上r
target_2=re.findall(r"\d+",str)
print(target)
print(target_2)
# ['30', '800000']
# ['30', '800000']


# 2. re.finditer(pattern, string, flags)
# target_new=re.finditer(pattern=ptn,string=str)
# print(target_new)
# <callable_iterator object at 0x0000015080493E20>
# 注意 iterator <--迭代器对象，回顾之前学的内容
# print(list(target_new))
# [<re.Match object; span=(8, 10), match='30'>, <re.Match object; span=(14, 20), match='800000'>]

# for i in target_new:
#     print(i)
# <re.Match object; span=(8, 10), match='30'>
# <re.Match object; span=(14, 20), match='800000'>

# 我们想拿到re.Match对象中的内容即匹配的结果match,注意先把上面的注释掉，不然迭代器进行一次迭代后就会停止迭代了，如果不注释就写下面的代码，那么下面的代码也是不会运行的
# for i in target_new:
#     print(i.group())
    # 30
    # 800000
# tg_1=re.search(pattern=ptn,string=str)
# print(tg_1)
# print(tg_1.group())
# <re.Match object; span=(8, 10), match='30'>
# 30
# 可见其返回的和re.finditer一样都是re.Match对象，
# 不同的是search只返回第一个符合匹配规则的，而finditer返回的是全部符合匹配规则的

# 4 re.match(pattern,string,flags)
tg_2=re.match(pattern=ptn,string=str)
print(tg_2)
# None <--返回的是None
# 注意，match在匹配的时候，是从字符串的开头匹配的
# 例如我们写的匹配规则是 \d+ 而经过match之后就变成了 ^\d+
# 即匹配规则变成了字符串开头，可我们的字符串开头并不是数字

# 我们再写一个以数字开头的字符串
str2='1,你就是个光棍,11就是双光棍，筷子罢了'
# 再次尝试match
tg_3=re.match(pattern=ptn,string=str2)
# print(tg_3)
# <re.Match object; span=(0, 1), match='1'>
# match和search一样，也是只匹配一次，但是match相当于给匹配规则加上了必须以数字开头
#数据获取方式也是.group()
# 注意，记得注释上面的print(tg_3)，别忘了这是迭代器，迭代完就关闭
print(tg_3.group())
# 1


# 预加载re.compile()
str3="一个2，一个250，没救了"
ptn_3="\d+"
# 预加载，提前把正则对象加载完毕
obj=re.compile(pattern=ptn_3)
# 直接把加载好的正则进行使用
result=obj.findall(str3)
# result=obj.findall(str3,re.S)
# 补充，re.S可以让正则中的元字符的 . 匹配换行符
print(result)
# ['2', '250']