"""
@File    :tst1.py
@Editor  : 百年
@Date    :2024/12/21 16:18 
"""
#IMPORTANT: 注意，这个文件是用来实验selenium登录b站要用的超级鹰验证码的切分的坐标的返回值的形式
str1 = '214,209|133,170|254,89|60,234'
codelst = str1.split('|')
print(codelst)
'''
['214,209', '133,170', '254,89', '60,234']
切分的返回值是个列表'''
for code in codelst:
    code = code.split(',')
    print(code[0])
    print(code[1])