"""
@File    :sims_cmq.py
@Editor  : breaze
"""
# 定义要保存成的文件
import os.path
file_name = '../stu_info.txt'

# 定义主函数
func_lst = [i for i in range(0, 10)]  # 增加成绩判断功能

def main():
    while True:  # 循环执行
        menu()
        choice = int(input('请选择功能:'))
        if choice in func_lst:
            if choice == 0:
                answer = input('确定退出吗？(y/n)')
                if answer == 'y' or answer == 'Y':
                    print('感谢使用')
                    break
                elif answer == 'N' or answer == 'n':
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
            elif choice == 8:
                search_by_score_range()  # 查询成绩范围内的学生
            elif choice == 9:
                score_evaluation()  # 新增成绩评定功能
        else:
            print('请输入正确的数字')
            continue


# 定义一个函数，实现菜单界面
def menu():
    print("===============++=SIMS=++=================")
    print("==============学生信息管理系统==================\n")
    print("|-----------功能菜单---------------|")
    print("0.\t\t\t\t\t\t退出系统\n1.\t\t\t\t\t\t录入学生信息\n2.\t\t\t\t\t\t查找学生信息\n3.\t\t\t\t\t\t删除学生信息\n"
          "4.\t\t\t\t\t\t修改学生信息\n5.\t\t\t\t\t\t对学生成绩进行排序\n6.\t\t\t\t\t\t统计学生人数\n7.\t\t\t\t\t\t显示所有的学生信息\n"
          "8.\t\t\t\t\t\t查询成绩范围内的学生信息\n9.\t\t\t\t\t\t成绩评定统计")  # 新增成绩评定统计


# 定义一个save函数，用于存储信息
def save(lst):
    try:
        fp = open(file_name, 'a', encoding='utf-8')
    except:
        fp = open(file_name, 'w', encoding='utf-8')
    for item in lst:
        fp.write(str(item) + '\n')
    fp.close()


# 1实现插入信息功能
def insert():
    stu_lst = []
    while True:  # 循环输入
        id = input('请输入学生id（如1001）:')
        if not id:
            print('请重新输入')
            break
        name = input('请输入学生姓名:')
        if not name:
            print('请重新输入')
            break
        try:
            chinese = int(input('语文成绩:'))
            math = int(input('数学成绩:'))
            english = int(input('英语成绩:'))
        except:
            print('请重新输入正确的成绩')
            continue
        stu_info = {'id': id, '姓名': name, '语文': chinese, '数学': math, '英语': english}
        stu_lst.append(stu_info)
        answer = input('是否继续添加?')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            print('学生信息录入完毕!')
            break
    save(stu_lst)


# 2实现查找学生信息功能
def search():
    stu_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(file_name):
            mode = input('按ID查找请按1，按姓名查找请按2:')
            if mode == '1':
                id = input('请输入要查找的学生的ID:')
            elif mode == '2':
                name = input('请输入学生的姓名:')
            else:
                print('所输入的信息无法识别，请重新输入')
                search()
            with open(file_name, 'r', encoding='utf-8') as rfp:
                stu_info = rfp.readlines()
                for item in stu_info:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            stu_query.append(d)
                    elif name != '':
                        if d['姓名'] == name:
                            stu_query.append(d)
            show_student(stu_query)
            stu_query.clear()
            answer = input('是否继续查询？(y/n)')
            if answer == 'y' or answer == 'Y':
                continue
            elif answer == 'N' or answer == 'n':
                break
        else:
            print('暂未保存学员信息')
            return


# 3实现删除学生信息功能
def delete():
    while True:
        stu_id = input('请输入要删除学生的id:')
        if stu_id != '':
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as fp:
                    stu_info_old = fp.readlines()
            else:
                stu_info_old = []
            flag = False
            if stu_info_old:
                with open(file_name, 'w', encoding='utf-8') as wfp:
                    for item in stu_info_old:
                        d = dict(eval(item))
                        if d['id'] != stu_id:
                            wfp.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag == True:
                        print(f'id为{stu_id}的学生信息已被成功删除')
                    else:
                        print(f'没有找到id为:{stu_id}的学生')
            else:
                print('无学生信息')
                break
            show()
            answer = input('是否继续删除(y/n)?')
            if answer == 'y' or answer == 'Y':
                continue
            elif answer == 'n' or answer == 'N':
                break


# 4实现修改学生功能
def modify():
    show()
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rfp:
            stu_old = rfp.readlines()
    else:
        return
    stu_id = input('请输入要修改的学生的ID:')
    with open(file_name, 'w', encoding='utf-8') as wfp:
        for item in stu_old:
            d = dict(eval(item))
            if d['id'] == stu_id:
                print('找到学生信息，可以修改其相关信息!')
                while True:
                    try:
                        d['姓名'] = input('请输入姓名:')
                        d['语文'] = int(input('请输入语文成绩:'))
                        d['数学'] = int(input('请输入数学成绩:'))
                        d['英语'] = int(input('请输入英语成绩:'))
                    except:
                        print('请重新输入')
                    else:
                        break
                wfp.write(str(d) + '\n')
                print('修改成功！！')
            else:
                wfp.write(str(d) + '\n')
        answer = input('是否继续修改其它学生信息?')
        if answer == 'y' or answer == 'Y':
            modify()
        elif answer == 'n' or answer == 'N':
            print('修改完毕')


# 5实现对学生信息进行排序的功能
def sort():
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rfp:
            stu_info = rfp.readlines()
        stu_info_new = []
        for item in stu_info:
            d = dict(eval(item))
            stu_info_new.append(d)
    else:
        print('文件不存在')
        return
    asc_or_desc = input('请选择排序方式(0升序，1降序):')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode = input('请选择排序方式(1.语文，2.数学，3.英语，0.总成绩):')
    if mode == '1':
        stu_info_new.sort(key=lambda x: int(x['语文']), reverse=asc_or_desc_bool)
    elif mode == '2':
        stu_info_new.sort(key=lambda x: int(x['数学']), reverse=asc_or_desc_bool)
    elif mode == '3':
        stu_info_new.sort(key=lambda x: int(x['英语']), reverse=asc_or_desc_bool)
    elif mode == '0':
        stu_info_new.sort(key=lambda x: int(x['语文'] + x['数学'] + x['英语']), reverse=asc_or_desc_bool)
    else:
        print('输入有误，请重新输入，您输入的是{0}'.format(mode))
        sort()
    show_student(stu_info_new)


# 6实现统计学生总人数功能
def total():
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rfp:
            students = rfp.readlines()
            if students != '':
                print('一共有{0}名学生'.format(len(students)))
            else:
                print('没有学生数据')
    else:
        print('没有学生信息数据')


# 7实现显示学生信息功能
def show():
    if os.path.exists(file_name):
        stu_lst = []
        with open(file_name, 'r', encoding='utf-8') as rfp:
            stu_info = rfp.readlines()
            for item in stu_info:
                d = dict(eval(item))
                stu_lst.append(d)
        show_student(stu_lst)
    else:
        print('没有学生信息数据')


def show_student(stu_lst):
    print('学生信息如下:')
    print('学号\t姓名\t语文\t数学\t英语')
    for d in stu_lst:
        print(f"{d['id']}\t{d['姓名']}\t{d['语文']}\t{d['数学']}\t{d['英语']}")


# 8 实现查询成绩范围内的学生信息(可以实现自由查询符合条件的分数范围)
def search_by_score_range():
    stu_query = []
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rfp:
            stu_info = rfp.readlines()
            try:
                min_score = int(input("请输入最低成绩: "))
                max_score = int(input("请输入最高成绩: "))
            except ValueError:
                print("输入无效，请输入整数成绩")
                return
            for item in stu_info:
                d = dict(eval(item))  # 将每行的字符串转化为字典
                total_score = d['语文'] + d['数学'] + d['英语']
                if min_score <= total_score <= max_score:
                    stu_query.append(d)

        if stu_query:
            show_student(stu_query)  # 显示符合条件的学生信息
        else:
            print("没有找到符合条件的学生信息")
    else:
        print("没有学生信息数据")


# 9 成绩评定统计功能(就是你说的分段吧应该，记得把这条注释掉)
def score_evaluation():
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rfp:
            stu_info = rfp.readlines()
            subject = input("请输入想要判定的科目（语文，数学，英语）:")
            level = input("请输入要查询的成绩等级（不及格，良好，中等，优秀）:")

            level_map = {
                "不及格": (0, 60), #0-60分是不及格
                "良好": (61, 70), #61-70分良好
                "中等": (71, 85), #71-85分中等
                "优秀": (86, 100) #86-100优秀
            }

            if level not in level_map:
                print("无效的成绩等级")
                return

            min_score, max_score = level_map[level]
            filtered_students = []

            for item in stu_info:
                d = dict(eval(item))
                score = d.get(subject)
                if score is not None and min_score <= score <= max_score:
                    filtered_students.append(d)

            print(f"科目{subject}成绩为'{level}'的学生信息如下：")
            show_student(filtered_students)
            print(f"符合条件的学生人数为：{len(filtered_students)}")
    else:
        print("没有学生信息数据")

if __name__ == '__main__':
    main()