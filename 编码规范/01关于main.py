"""
@File    :01关于main.py
@Editor  : 百年
@Date    :2025/5/10 9:56 
"""


#全局变量大写
DATA_LST =[]


#业务逻辑写在函数内

def run():
    for i in range(10):
        DATA_LST.append(i)
    print(DATA_LST)

if __name__ == '__main__':
    run() #主函数只保留接口