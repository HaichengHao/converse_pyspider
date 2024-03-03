# editor: 百年
# time: 2024/3/3 8:24
'''
s={}
print(type(s))
# <class 'dict'>  <--默认写个空的s会是一个字典类型
s1=set()
print(type(s1))
# <class 'set'>  <--这样写会是一个集合
s2=set({1, 3, 2, 5, 7})
print(s2)
# {1, 2, 3, 5, 7} <--集合是无序的！！！

s3={1,2,3,4}
print(s3)
# {1, 2, 3, 4}

s4={1,2,3,'哈哈哈'}
print(s4)
# {1, 2, 3, '哈哈哈'} <--字符串数据是可以哈希的



try:
    s6={1,3,(2,1)}
    print(s6)
except BaseException as e:
    print(e)
    # {1, 3, (2, 1)} <--元组数据也是可以哈希的

try:
    s7={1,2,True}
    print(s7)
except BaseException as e:
    print(e)
    # {1, 2} <--布尔类型也是可以哈希的

try:
    s5 = {1, 2, 3, [1, 2]}
except BaseException as e:
    print(e)
        # unhashable type: 'list'  列表数据是不可哈希的
try:
    s8={1,2,3,{1,2}}
except BaseException as e:
    print(e)
    # unhashable type: 'set' 集合类型本身也是不可以哈希的

try:
    s9={1,2,{'张三':'20'}}
except BaseException as e:
    print(e)
    # unhashable type: 'dict' <--字典类型不可哈希
'''

s=set()

# 集合元素的增加
s.add(1)
print(s)
# {1}
s.add('码云')
s.add('码农')
s.add('甲方')
print(s)
# {1, '码农', '甲方', '码云'}

# 集合元素的删除 ,注意和列表中的稍有不同，因为集合是无序的，无法通过索引删除
# 所以集合中的pop默认为随机删除一个元素
'''
s.pop()
print(s)'''
# {'码农', '甲方', '码云'}

# .remove() <--使用次数较多
s.remove('甲方')
print(s)
# {1, '码农', '码云'}

# 集合元素的修改无法通过索引位置进行修改，只能删除指定元素后再新增
# 如，修改‘码云’为‘github’
s.remove('码云')
s.add('github')
print(s)
# {1, '码农', 'github'}

for item in s:
    print(item)
    # 1
    # 码农
    # github


# 集合补充
set1={1,2,'张三',(1,2),True}
set2={1,2,'李四',(1,2),(2,5),False,True}

# 交集
print(set1&set2)
# {1, 2, (1, 2)}
print(set1.intersection(set2))
# {1, 2, (1, 2)}

# 并集
print(set1|set2)
print(set1.union(set2))
# {False, 1, 2, (1, 2), '张三', '李四', (2, 5)}
# {False, 1, 2, (1, 2), '张三', '李四', (2, 5)}

# 差集
# set1-set2 即set1|set2-set2 就是set1有的而set2没有的
print(set1-set2)
# {'张三'}
print(set2-set1)  # set2-set1即是set2有而set1没有的
# {False, '李四', (2, 5)}

# 利用集合去重
# 集合中的元素使不能重复的，利用这一特性便可去重
name_lst=['张三','张三','李四','王五','张三','赵六','陈七']
name_set=set(name_lst)
print(name_set)
# {'赵六', '李四', '王五', '陈七', '张三'} <--通过类型转换可以将其转换为字典，利用字典的特性去重

