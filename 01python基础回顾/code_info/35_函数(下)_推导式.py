# editor: 百年
# time: 2024/3/10 10:09
# lst=[]
# for i in range(10):
#     lst.append(i)
# print(lst)

# 简化代码，利用推导式
lst=[i for i in range(10)]
# 列表推导式[目标数据 for循环  [if判断] ]
# 例如:存放1-10中的偶数
lst2=[i for i in range(1,11) if i%2==0]
print(lst2)
# [2, 4, 6, 8, 10]
namelst=[f'张{i}' for i in range(10) ]
print(namelst)
# ['张0', '张1', '张2', '张3', '张4', '张5', '张6', '张7', '张8', '张9']

# 将英文姓名首字母转为大写
name_lst=['alon','baky','cilon','danior']
name_lst_new=[ item.capitalize() for item in name_lst]
print(name_lst_new)
# ['Alon', 'Baky', 'Cilon', 'Danior']

# 集合生成式
# 将下面的列表修改为字典，要求索引为key,数据作为value
lst_1=['孙悟空','唐僧','猪八戒','沙僧','刘能','赵四']
dic_1={i:lst_1[i] for i in range(len(lst_1))}
print(dic_1)
# {0: '孙悟空', 1: '唐僧', 2: '猪八戒', 3: '沙僧', 4: '刘能', 5: '赵四'}
'''
推导式可以简化代码
语法 :
  列表推导式
    [数据 for 循环 [if判断]]
  集合推导式
    {数据 for 循环 [if判断]}

  字典推导式
    {key : value for 循环 [if判断]}
注意，不要把推导式作为主流写法，因为推导式的可读性并不好

注意，元组没有推导式，元组不能增删改查
注意(数据 for循环 [if 判断]) 叫生成器表达式'''