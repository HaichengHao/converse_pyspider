# editor: 百年
# time: 2024/3/12 10:54
# 注意，想直接导入自己写的模块是不行的
# 需要先将文件夹标记为源文件，即Mark Directory as Sources Root
import cal
from logger import get_logger

print(dir(cal))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'div', 'floordiv', 'mod', 'mul', 'pow', 'sub']
# 可以看到我们自定义的模块

# 直接使用cal模块中的add函数
print(cal.add(1,5))
# 6

# 使用logger模块中的getlogger方法
get_logger()
# 打印日志
# 尝试使用另一个函数
try:
    tool()
except BaseException as e:
    print(e)
    # name 'tool' is not defined
    # 为何会这样，因为我们利用的是from 模块名 impo 成员变量 的方式，这样只能使用导入的成员变量而不能使用所有成员变量
# 所以要使用就得导入
from logger import tool  #这样就导入了tool
# 使用tool
tool()
# 工具
if __name__ == '__main__':
    print('当前处于执行文件中')

# 导入自己的包里的模块
from mypkg import cal
print(cal.mul(2,7))
# 14


