# editor: 百年
# time: 2024/3/4 15:24

# 读
'''
fp=open('../text/19文件操作.txt','r',encoding='utf-8')
# print(fp.read())
# print(fp.readline())
# 加上.strip()
print(fp.readline().strip())
# print(fp.readlines())
# fp.close()
print('哈哈哈') #print内部存在一个换行
print('呼呼呼')
# 1 文件的操作需要利用open()打开文件
#
# 哈哈哈
# 呼呼呼
# 从文件读取到的内容会换行，不过可以利用.strip()去掉字符串左右两端的空白，即空格，换行，制表符等

# 加上.strip()后
# 1 文件的操作需要利用open()打开文件
# 哈哈哈
# 呼呼呼

for line in fp:
    print(line.strip())

fp.close()'''

# 写
# 写入读取的文件
# rfp=open('../text/19文件操作.txt','r',encoding='utf-8')
# wfp=open('../others/19文件操作.txt','a+',encoding='utf-8')
# # for line in rfp:
# #     content=line.strip()
# #     wfp.write(content)
# content=rfp.read()
# wfp.write(content)
#
# rfp.close()
# wfp.close()
# 非上下文管理器进行的文件操作每次都需要进行文件的关闭，否则会造成严重后果
# 小案例
#     准备一个列表，把列表中的每一项内容都写入到文件中
# lst=[1,2,3,4,5,8]
# lst2=['cat','dog','spider','squirrel']
# with open('../others/19_demo.txt','w+',encoding='utf-8') as wfp:
#     wfp.write(str(lst)) #注意格式转换，写入的数据必须是字符串类型
#     for item in lst2:
#         wfp.write(str(item)+'\n')


# 读取图片
# 非文本文件不能指定字符集

# 图片复制
# with open('../others/img.png','rb') as rfp, \
#      open('../others/myscst.png','wb') as wfp:
#         # wfp.write(rfp.read())
#         for line in rfp:
#             wfp.write(line)


# 3文件修改
# 先准备一个文件
# lst=['张三','李四','王五','赵六','赵七','张八']
# with open('../others/19_name.txt','w+',encoding='utf-8') as wfp:
#     for item in lst:
#         wfp.write(str(item)+'\n')
# 把姓张的改为姓章的
# 思路，读取并修改，但是要写到新的文件当中去
import os
import time
with open('../others/19_name.txt','r',encoding='utf-8') as fp,\
    open('../others/19_name_副本.txt','w',encoding='utf-8') as wfp:
    for line in fp:
        line=line.strip()   #去掉换行
        if line.startswith('张'):
            line=line.replace('张','章')  #修改,注意字符串不可变，因此产生了一个新的字符串，所以要利用新的对象来接收修改后的字符串
        wfp.write(line+'\n')

#         删除源文件，保留副本文件,需要利用os模块
time.sleep(3)
os.remove('../others/19_name.txt')
time.sleep(3)
# 把副本文件重命名为源文件
os.rename('../others/19_name_副本.txt','../others/19_name.txt')


# 如果想看到变化过程，那么可以导入time模块





