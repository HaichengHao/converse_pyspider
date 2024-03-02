# editor: 百年
# time: 2024/3/2 14:22
t=(1.2,3,5,[1,3])
print(t[1:])
# (3, 5, [1, 3]) <--可以进行索引

try:
    t[1]='6'
except BaseException as e:
    print(e)
    # 'tuple' object does not support item assignment
    # 可以知道，元组类型不支持修改元素
# 元组如果只有一个元素，那么
t1=('1')
print(t1,type(t1))
# 1 <class 'str'> <--如果元组中只有一个元素，那么默认会认为是这一个元素的类型
t2=(1)
print(type(t2))
# <class 'int'> <--同上的结论