# @Author    : 百年
# @FileName  :00_梗概.py
# @DateTime  :2024/10/23 20:16
'''
对于mysql的学习，之前已经学过，不在这里整合，直接开始使用，且不想污染工作电脑，故使用sqllite替代
要用到的包
import sqllite3
之后将会按照菜鸟教程完整地学习一遍sqllite，也是对于之前学的mysql的巩固和补充
'''
import sqlite3
conn = sqlite3.connect('spider3.db')
cursor = conn.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTS comments(id INTEGER PRIMARY KEY, comm TEXT)')
conn.commit()
conn.close()

'''
sqllite默认是关闭外键约束的,所以要用PRAGMA foreign_keys = ON 写到要开启外键约束的sql表语句之前,
注意外键所在的也要输入激活，也就是俩console里都要写
PRAGMA foreign_keys = ON;
create table if not exists emp(
    id integer primary key autoincrement ,
    name text unique not null ,
    age integer not null ,
    score real,
    overschool text,
    gender text check ( gender in ('male','female')), /*虽然sqllite没有枚举类型，但是可以用这个代替*/
    hobby text check ( hobby in ('eat','sleep','study')),/*同样可以使用它实现多选*/
    dep_id integer not null ,
    foreign key(dep_id) references dep(id) /*将dep_id字段指定一个外键约束，外键是dep表中的id字段*/
);

insert into emp values (6,'lisa','female',1);
'''

'''
-- alter table SPIDER rename to stu; /*修改表的名称*/

-- sqllite利用SQL来实现列类型的修改是困难的,只能创建新表,制定好名称再将旧表的数据插入进去

alter table stu rename to old_table;

create table stu(
    id integer primary key autoincrement ,
    name text not null ,
    score real,
    overschool text,
    gender check ( gender in ('male','female')),
    hobby check ( hobby in ('sleep','study','eat'))
);

insert into stu(id,name,score,overschool,gender,hobby) select id,name,score,overschool,gender,hobby from old_table;

drop table old_table;'''

'''
'''