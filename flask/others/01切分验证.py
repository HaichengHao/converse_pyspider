# @Author    : 百年
# @FileName  :01切分验证.py
# @DateTime  :2024/10/28 9:42
# with open('../code/db.txt','r',encoding='utf-8') as fp:
#     for line in fp:
#         print(line.strip())
#         line = line.strip()
#         res = line.split(',') #切分行
#         print(res)

'''
224131ee-6584-4f30-bcf8-0ec6f6dfb1ca,张三
['224131ee-6584-4f30-bcf8-0ec6f6dfb1ca', '张三'] 切分返回的是一个列表对象，可以使用两个变量来接收
fc4431fc-33e3-4d36-b1e0-a8d6934ebeb3,李四
['fc4431fc-33e3-4d36-b1e0-a8d6934ebeb3', '李四']'''

with open('../00web服务/db.txt', 'r', encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        token,name= line.split(',') #切分行
        print(token)