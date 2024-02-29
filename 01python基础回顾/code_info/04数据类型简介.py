# editor: 百年
# time: 2024/2/29 10:54
# 数字分为整数和小数类型
a=10
b=20.2
print(type(a),type(b))
# <class 'int'> <class 'float'>
print(a+b)
# 30.2

# python中的字符串可以用单引号引起来
# 可以用单引号引起来。也可以用双引号引起来
s1='life is short  you need python'
s2="life is short you need pythonyou need python"
print(s1,s2)

s3="""真的，就业很累，调剂很废
到最后满脸是泪
就业吧，不上了
"""
print(s3)
'''
真的，就业很累，调剂很废
到最后满脸是泪
就业吧，不上了
可以发现三双引号可以实现原多行打印，相当于自己换了行
'''

s4='''
三个单引号
也是可以的
'''
print(s4)
# 三个单引号
# 也是可以的


# 字符串的加法操作
# 注意，两边都得是字符串
name='哈利波特'
_preference='戴个眼镜，脸像爹，眼像妈'
print(name+_preference)
# 哈利波特戴个眼镜，脸像爹，眼像妈


# 字符串可以作乘法
print(name*3)
# 哈利波特哈利波特哈利波特


# 布尔类型
a=True
a=100<120
print(a)
# True < --以上两个结果都为True