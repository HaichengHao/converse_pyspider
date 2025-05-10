"""
@File    :02文件操作规范.py
@Editor  : 百年
@Date    :2025/5/10 10:09 
"""
#看这里时可以结合基础部分的生成器看

def load_file_data():
    with open('./demo.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            yield line.strip().split(",")


def run():
    # 因为本质上load_file_data()运行结果是一个生成器对象
    generrator_obj = load_file_data()
    # 日期,星期,最低温度,最高温度,天气,风向,风力
    for day, week, min_tem, max_tem, tq, fx, fl in generrator_obj:
        print(day, week, min_tem, max_tem, tq, fx, fl)


if __name__ == '__main__':
    run()
