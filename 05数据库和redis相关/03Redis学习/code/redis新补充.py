"""
@File    :redis新补充.py
@Editor  : 百年
@Date    :2025/3/11 22:03 
"""
# important:使用redis-server -raw 就可以使redis支持中文字符串存储

# QUIZ: 在python中该怎们弄呢?
# answer: redis库中的Redis[点击ctrl点击查看client.py]其初始化方法中支持对响应进行解码,默认的decode_response是False


from redis import Redis

conn = Redis(
    host='localhost',
    port=6379,
    db=3, #使用db3
    decode_responses=True #相当于 --raw 不用看字节了
    # password='your_password'  # 若没有密码，可以不填
)

# set key value

# conn.set("name","jacky")
# res1 = conn.get('name')
# print(res1)

# zadd和之前的命令行内操作不一样,是字典形式的
# 原生:  zadd name key f1 d1 f2 d2 f3 d3 #有序数据插入
# conn.zadd("phonerank", 10, "meizu", 9, "sumsung", 8, "iphone", 7, "xiaomi")
#python中，新的命令和旧的Redis版本不同
# 向名为'phonerank'的有序集合中添加成员及其分数
conn.zadd("phonerank", {"meizu": 10, "sumsung": 9, "iphone": 8, "xiaomi": 7})

# 打印出'phonerank'集合中的所有成员及其分数，验证是否添加成功
# phonerank_members = conn.zrange("phonerank", 0, -1, withscores=True)
# print(phonerank_members)

# 注意问题解决,需要更新redis, pip install --upgrade redis
# 而之前的话是redis 2.10.6