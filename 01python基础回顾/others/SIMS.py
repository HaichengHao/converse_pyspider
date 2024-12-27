"""
@File    :SIMS.py
@Editor  : 百年
@Date    :2024/12/25 18:11 
"""
# editor: 百年
# time: 2024/1/26 11:39
# 定义要保存成的文件
import os.path
file_name='D:/PYWORK/python_cases/1学生信息管理系统/SIMS_ver1.0/stu_info.txt'
# 定义主函数
func_lst = [i for i in range(0,8)]
def main():
    while True:#循环执行
        menu()
        choice=int(input('请选择功能:'))
        if choice in func_lst:
            if choice==0:
                answer=input('确定退出吗？')
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
        else:
            print('请输入正确的数字')
            continue




# 定义一个函数，实现菜单界面
def menu():
    print("===============++=SIMS=++=================")
    print("==============学生信息管理系统==================\n")
    print("|-----------功能菜单---------------|")
    print("1.\t\t\t\t\t\t录入学生信息\n2.\t\t\t\t\t\t查找学生信息\n3.\t\t\t\t\t\t删除学生信息\n"
          "4.\t\t\t\t\t\t修改学生信息\n5.\t\t\t\t\t\t对学生成绩进行排序\n6.\t\t\t\t\t\t统计学生人数\n7.\t\t\t\t\t\t显示所有的学生信息\n")


# 定义一个save函数，用于存储信息
def save(lst):
    try:
        fp=open(file_name,'a',encoding='utf-8')
    except:
        # fp=open('D:/PYWORK/python_cases/1学生信息管理系统/SIMS_ver1.0/stu_info.txt','w',encoding='utf-8')
        fp=open(file_name,'w',encoding='utf-8')
    for item in lst: #遍历列表中的每个学生的信息（字典形式）并写入到文件当中并换行
        fp.write(str(item)+'\n') #将每个学生信息的字典写入到列表当中并换行，这样方便后续的查找工作
        #关闭文件
    fp.close()

# 1实现插入信息功能
def insert():
    # 创建一个空列表用于接收字典元素
    stu_lst=[]
    while True: #循环输入
        id=input('请输入学生id（如1001）:')
        # 空字符串的布尔值为False,所以if not id 即如果字符串为空则提示重新输入
        if not id:
            print('请重新输入')
            break
        name=input('请输入学生姓名:')
        if not name:
            print('请重新输入')
            break
        try:
            chinese=int(input('语文成绩:'))
            math=int(input('数学成绩:'))
            english=int(input('英语成绩:'))
        except:
            print('请重新输入正确的成绩')
            continue
        #将每个学生的信息保存为字典形式并存入列表中
        stu_info={'id':id,'姓名':name,'语文':chinese,'数学':math,'英语':english}
        stu_lst.append(stu_info) #向列表中新增元素（单个学生信息的字典）
        answer=input('是否继续添加?')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            print('学生信息录入完毕!')
            break
    # 调用save()函数
    save(stu_lst)



# 2实现查找学生信息功能
def search():
    # 创建一个空列表用于接收数据
    stu_query=[]
    # 循环执行
    while True:
        # 创建id,name
        id=''
        name=''
        # 如果文件存在
        if os.path.exists(file_name):
            # 定义查找模式mode,可按id和姓名进行自定义查询
            mode=input('按ID查找请按1，按姓名查找请按2:')
            if mode == '1':
                id=input('请输入要查找的学生的ID:')
            elif mode =='2':
                name=input('请输入学生的姓名:')
            # 如果均未查找到，则输出提示信息有误无法查询
            else:
                print('所输入的信息无法识别，请重新输入')
                search() #如果输入有误，则重新调用自己
            with open(file_name,'r',encoding='utf-8') as rfp:
                stu_info=rfp.readlines()
                for item in stu_info:
                    d=dict(eval(item))
                    if id!='': #如果输入的id不为空
                        if d['id']==id: #且查找到对应的ID
                            stu_query.append(d) #就将这一字典加入到创建的列表stu_query当中


                    elif name!='': #如果输入的姓名不为空，
                        if d['姓名']==name:#且找到对应的姓名
                            stu_query.append(d)#就将这一字典加入到创建的列表stu_query当中
        #     显示查询结果(方案1)，简单，但也简陋
        #     print(stu_query)
        #     answer=input('是否继续查找(y/n)?')
        #     if answer=='y' or answer == 'Y':
        #         stu_query.clear() #先清空列表中的数据，否则会出现多个信息
        #         continue
        #     elif answer=='n' or answer =='N':
        #         break

        # 方案2，调用自己编写的函数show_student()
            show_student(stu_query)
            stu_query.clear() #查询时防止有冗余的数据，展示完查找到的信息后对其进行清空，以免出现上次查找的结果
            answer=input('是否继续查询？(y/n)')
            if answer == 'y' or answer =='Y':
                continue
            elif answer == 'N' or answer == 'n':
                break


        else:
            print('暂未保存学员信息')
            return
#      开始定义search()模块



# 3实现删除学生信息功能
def delete():
    while True: #循环执行
        stu_id=input('请输入要删除学生的id:')
        # 如果不为空字符串
        if stu_id!='':
            # 操作文件
            # 如果存在
            if os.path.exists(file_name):
                # 则读取文件
                with open(file_name,'r',encoding='utf-8') as fp:
                    # readlines()会把读取到的每行元素保存为一个列表
                    # 将读取到的数据保存为一个列表stu_info_old
                    stu_info_old=fp.readlines()
            else: #如果没读取到则将stu_info_old置为空列表(默认值为False)
                stu_info_old=[]
            #创建一个变量名为flag的对象，默认值为False
            flag=False #用于标记信息是否删除，默认没有删除
            if stu_info_old: #相当于True，即stu_info_old里是有内容的
                # 就以写模式打开文件
                with open(file_name,'w',encoding='utf-8') as wfp:
                    # 创建空字典emp_d,用于接收读取到的内容，将其转换为字典
                    # emp_d={}
                    # 遍历列表中的元素(之前在insert()模块中知道它的元素是一个个字典)
                    for item in stu_info_old:
                        d=dict(eval(item))  #空字典
                        #将读取到的字符串转化为字典类型
                        # 这里注意，因为从文件中读取到的虽然貌似是字典，但其实在文件处理器看来就是字符串，
                        # eval()可以将 "{'id': '1020', '姓名': '柳传至', '语文': 100, '数学': 100, '英语': 20}"
                        # 消除掉外边的""
                        # 注意，eval()一定要谨慎使用，十分“危险”
                        if d['id']!=stu_id : #如果字典中的id与输入的id不相同
                            wfp.write(str(d)+'\n') #就先把这条内容写入到文件当中去
                        else: #否则（即输入的id与字典中的id相同）
                            flag=True #则标志删除(即要被删除掉了)
                    if flag==True:
                        print('id为{0}的学生信息已被成功删除'.format(stu_id))
                    else: #即flag=False
                        print('没有找到id为:{0}的学生'.format(stu_id))
            else: #如果没有读到数据
                print('无学生信息')
                break
            show()    #删除完毕后重新显示学生信息
            answer=input('是否继续删除(y/n)?')
            if answer=='y' or answer=='Y':
                continue
            elif answer=='n' or answer=='N':
                break


# 4实现修改学生功能
def modify():
    show() #先调用show()函数显示所有学生的信息以便进行修改
    if os.path.exists(file_name): #先判断文件是否存在，如果存在，
        with open(file_name,'r',encoding='utf-8') as rfp: #则以只读方式打开
            stu_old=rfp.readlines() #保存为列表形式
    else: #如果不存在
        return #则结束（不存在则谈不上修改）
# 开始定义modify模块
    stu_id=input('请输入要修改的学生的ID:')
    with open(file_name,'w',encoding='utf-8') as wfp:
        for item in stu_old:
            d=dict(eval(item))
            if d['id']==stu_id: #如果查找到要修改的id,则修改它
                print('找到学生信息，可以修改其相关信息!')
                while True:
                    try:
                        d['姓名']=input('请输入姓名:')
                        d['语文']=int(input('请输入语文成绩:'))
                        d['数学']=int(input('请输入数学成绩:'))
                        d['英语']=int(input('请输入英语成绩:'))
                    except:
                        print('请重新输入')
                    else:
                        break

                wfp.write(str(d)+'\n') #如果录入的信息无误，则写入文件当中
                print('修改成功！！')
            else:#否则写回原来的内容
                wfp.write(str(d)+'\n')
        answer=input('是否继续修改其它学生信息?')
        if answer =='y' or answer=='Y': #如果选择是，则重新调用
            modify()
        elif answer=='n' or answer=='N':
            print('修改完毕')






# 5实现对学生信息进行排序的功能
def sort():
    # show() #调用show()展示学生信息
    if os.path.exists(file_name): #如果文件存在
        with open(file_name,'r',encoding='utf-8') as rfp:#则以只读方式打开文件
            stu_info=rfp.readlines()#并将读取到的数据(列表中的元素，即每个学生的字典)
        stu_info_new=[] #创建空列表用于接收信息
        for item in stu_info:#遍历列表stu_info中的元素
            d=dict(eval(item))#并将元素的字符串类型转化为字典类型(tips:eval()“去皮”)
            stu_info_new.append(d) #并将其新增到列表当中
    else:#否则
        print('文件不存在')#输出文件不存在
        return
    asc_or_desc=input('请选择排序方式(0升序，1降序):') #定义选项
    if asc_or_desc=='0':
        asc_or_desc_bool=False #定义标志位，如果选0则表示false
    elif asc_or_desc=='1':
        asc_or_desc_bool=True #如果选1则标志True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode=input('请选择排序方式(1.语文，2.数学，3.英语，0.总成绩):')
    # 利用匿名函数获取列表中元素(字典)中的指定的键的值
    if mode=='1':
        stu_info_new.sort(key=lambda x :int(x['语文']),reverse=asc_or_desc_bool)
    elif mode=='2':
        stu_info_new.sort(key=lambda x :int(x['数学']),reverse=asc_or_desc_bool)
    elif mode=='3':
        stu_info_new.sort(key=lambda x :int(x['英语']),reverse=asc_or_desc_bool)
    elif mode=='0':
        stu_info_new.sort(key=lambda x :int(x['语文']+x['数学']+x['英语']),reverse=asc_or_desc_bool)
    else:
        print('输入有误，请重新输入，您输入的是{0}'.format(mode))
        sort() #有误后，再次调用
    show_student(stu_info_new) #调用show_student()展示学生信息

# 6实现统计学生总人数功能
def total():
    if os.path.exists(file_name):
        with open(file_name,'r',encoding='utf-8') as rfp:
            students=rfp.readlines()
            if students!='':#如果列表不为空
                print('一共有{0}名学生'.format(len(students))) #则调用len()方法获取列表长度
    #             为什么要用len()，因为列表内的元素是一个个字典，即一条字典就是一个元素，利用len()便可获取有多少个元素，即多少个学生
            else:
                print('没有学生数据')

    else:
        print('没有学生数据')


# 7实现展示学生信息的功能
def show():
    # 创建空列表用于接收数据
    stu_lst=[]
    if os.path.exists(file_name):#判断文件是否存在
        with open(file_name,'r',encoding='utf-8') as rfp:#如果文件存在
            stu_info=rfp.readlines()#则以只读方式读取文件并调用readliines()方法，返回的就是一个列表
            for item in stu_info:#对列表中的元素进行遍历，
                d=dict(eval(item)) #之后将列表中的每个元素（即字符串格式的字典）转化为字典格式
                stu_lst.append(d)#之后新增到列表stu_lst之中去
        if stu_lst!='':#如果列表不为空,
            show_student(stu_lst) #就调用show_student()函数将信息展示出来



    else:
        print('暂未保存学生数据')

# 定义一个函数显示读取到的学生信息列表
def show_student(lst):
    if len(lst)==0: #如果lst长度为0(即未读取到)
        print('没有查询到信息，无数据显示!!')
        return
    #定义标头显示格式
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^10}'
    print(format_title.format('id','姓名','语文','数学','英语','总成绩'))
    #定义内容的显示格式
    format_data='{:^6}\t{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^10}'
    for item in lst:
        print(format_data.format(item.get('id'),item.get('姓名'),item.get('语文'),item.get('数学'),item.get('英语'),
                                 int(item.get('语文')+item.get('数学')+item.get('英语'))))



# 以主程序方式运行
if __name__ == '__main__':
    main()



