#在Python中用[]来表示一个列表，
# 列表中的元素用','分隔
# lst=['张三','李四','王五',['列表啊我']]
# # 特性:
# # 1.也像字符串一样可以进行索引和切片
#
# print(lst[0])
# # 张三
# print(lst[1::2])
# # ['李四', ['列表啊我']]
# print(lst[::-1])
# # [['列表啊我'], '王五', '李四', '张三']
# for item in lst:
#     print(item)
'''
张三
李四
王五
['列表啊我']
'''

'''lst_1=[]'''
# .append()往列表中最后的位置追加内容
'''lst_1.append('你好')
lst_1.append('世界')
print(lst_1)'''
# ['你好', '世界']

'''lst_1.insert(0,'插队称为第一')
print(lst_1)'''
# ['插队称为第一', '你好', '世界']

# .extend()可以合并两个列表,
'''lst_1.extend(['小猫','小狗','小刺猬'])
print(lst_1)'''
# ['插队称为第一', '你好', '世界', '小猫', '小狗', '小刺猬']
'''lst_1.pop()
print(lst_1)'''
# ['插队称为第一', '你好', '世界', '小猫', '小狗']
'''
lst_1.pop(0)
print(lst_1)'''
# ['你好', '世界', '小猫', '小狗']

'''lst_1.remove('你好')
print(lst_1)'''
#['世界', '小猫', '小狗']


# 改
# 将’世界‘改为’宇宙‘
'''lst_1[0]='宇宙'
print(lst_1)'''
# ['宇宙', '小猫', '小狗']


# 小练习 ：把所有的姓张的人修改成姓章的
'''name_lst=['张三丰','章子哟','张五级','章少刚','李梓琪']
for item in name_lst:#先遍历列表中的每个元素
    if item.startswith('张'):  #如果元素以’张‘开头
        inx=name_lst.index(item) #就检索这个元素的位置
        print(inx)
        name_lst[inx]='章'+item[1:] #并把该元素的第一个位置改成’章‘并加上之后的元素
        print(item)
    #     组成的新名字放回列表

    else:
        item=item
print(name_lst)'''
# ['章三丰', '章子哟', '章五级', '章少刚', '李梓琪']

#写法2
'''name_lst=['张三丰','章子哟','张五级','章少刚','李梓琪']
for i in range(len(name_lst)):
    if name_lst[i].startswith('张'):
        name_lst[i]='章'+name_lst[i][1:]
    else:
        name_lst[i]=name_lst[i]
print(name_lst)'''
# ['章三丰', '章子哟', '章五级', '章少刚', '李梓琪']


# 列表的其它操作

# 排序操作
'''lst1=[1,2,4,5,3,7,6]
lst1.sort()
print(lst1)
# sort()默认为升序排序
# [1, 2, 3, 4, 5, 6, 7]
# 降序排序
lst1.sort(reverse=True)
print(lst1)
# [7, 6, 5, 4, 3, 2, 1]
lst2=sorted(lst1,reverse=True)
print(lst2)'''
# [7, 6, 5, 4, 3, 2, 1]

# 列表的嵌套操作
'''lst1=['abc','def',['啊','播','次','的',123],'gh',['hello',['world']]]
lst_num=lst1[2][4]
print(lst_num)
# 123
lst1[-1][-1][0]=lst1[-1][-1][0].upper()
print(lst1)
# ['abc', 'def', ['啊', '播', '次', '的', 123], 'gh', ['hello', ['WORLD']]]'''

# 列表的循环删除
'''
lst1=['张三','李四','王五','赵六','钱七','孙八','张九']
print(len(lst1))
# 7
# 需求，删除掉姓张和姓李的人
# 解决列表前移问题
# 创建临时列表,负责存储要删除的内容
# len()返回的是非索引长度，是几就是几，从1开始，而索引的下标从0开始
tmp=[]
# 注意这里的len(lst1)的值为7，但是range(7)取到的是0-6，刚好满足索引下标
for i in range(len(lst1)):
    if lst1[i].startswith('张'):
        tmp.append(lst1[i])
        # lst1.pop(i)
    elif lst1[i].startswith('李'):
        tmp.append(lst1[i])
        # lst1.remove(lst1[i])
    else:
        lst1[i]=lst1[i]
print(tmp)
# 最后再进行删除
for remove_item in tmp:
    lst1.remove(remove_item)
print(lst1)
# ['王五', '赵六', '钱七', '孙八']

# 列表的join操作
'''

lst=['a','b']
str = ''.join(lst)
print(str)
