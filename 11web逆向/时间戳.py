"""
@File    :时间戳.py
@Editor  : 百年
@Date    :2025/3/28 13:35 
"""
import time

# print(time.time())

# 1743140153.3363981 可以看到python的时间戳是10位整数加上n位小数字
# 而js的时间戳是13位整数,想要两者相互转化只需要python的时间戳乘上1000然后再取整即可

timestamp = time.time()
print(timestamp)
js_timestamp = timestamp*1000
print(int(js_timestamp))

# runtime_result:
'''
1743140958.7700226
1743140958770
'''