-- 数据准备
PRAGMA foreign_keys = ON; --开启外键约束
create table class(
    cid integer primary key ,
    caption text not null
);
insert into class values
(1, '三年二班'),
(2, '三年三班'),
(3, '一年二班'),
(4, '二年九班');


create table teacher(
    tid integer primary key ,
    tname text not null
);

insert into teacher values
(1, '张磊老师'),
(2, '李平老师'),
(3, '刘海燕老师'),
(4, '朱云海老师'),
(5, '李杰老师');

create table course(
    cid integer primary key autoincrement ,
    cname text not null ,
    teacher_id integer not null ,
    foreign key (teacher_id) references teacher(tid)
);
insert into course values
(1, '生物', 1),
(2, '物理', 2),
(3, '体育', 3),
(4, '美术', 2);

create table student(
    sid integer primary key autoincrement ,
    gender text not null ,
    class_id integer not null ,
    sname text not null ,
    foreign key (class_id) references class(cid)
);
insert into student values
(1, '男', 1, '理解'),
(2, '女', 1, '钢蛋'),
(3, '男', 1, '张三'),
(4, '男', 1, '张一'),
(5, '女', 1, '张二'),
(6, '男', 1, '张四'),
(7, '女', 2, '铁锤'),
(8, '男', 2, '李三'),
(9, '男', 2, '李一'),
(10, '女', 2, '李二'),
(11, '男', 2, '李四'),
(12, '女', 3, '如花'),
(13, '男', 3, '刘三'),
(14, '男', 3, '刘一'),
(15, '女', 3, '刘二'),
(16, '男', 3, '刘四');


--
CREATE TABLE score(
  sid integer primary key autoincrement ,
  student_id integer NOT NULL,
  course_id integer NOT NULL,
  num integer NOT NULL,
  FOREIGN KEY (course_id) REFERENCES course(cid),
  FOREIGN KEY (student_id) REFERENCES student(sid)
);
INSERT INTO score VALUES
(1, 1, 1, 10),
(2, 1, 2, 9),
(5, 1, 4, 66),
(6, 2, 1, 8),
(8, 2, 3, 68),
(9, 2, 4, 99),
(10, 3, 1, 77),
(11, 3, 2, 66),
(12, 3, 3, 87),
(13, 3, 4, 99),
(14, 4, 1, 79),
(15, 4, 2, 11),
(16, 4, 3, 67),
(17, 4, 4, 100),
(18, 5, 1, 79),
(19, 5, 2, 11),
(20, 5, 3, 67),
(21, 5, 4, 100),
(22, 6, 1, 9),
(23, 6, 2, 100),
(24, 6, 3, 67),
(25, 6, 4, 100),
(26, 7, 1, 9),
(27, 7, 2, 100),
(28, 7, 3, 67),
(29, 7, 4, 88),
(30, 8, 1, 9),
(31, 8, 2, 100),
(32, 8, 3, 67),
(33, 8, 4, 88),
(34, 9, 1, 91),
(35, 9, 2, 88),
(36, 9, 3, 67),
(37, 9, 4, 22),
(38, 10, 1, 90),
(39, 10, 2, 77),
(40, 10, 3, 43),
(41, 10, 4, 87),
(42, 11, 1, 90),
(43, 11, 2, 77),
(44, 11, 3, 43),
(45, 11, 4, 87),
(46, 12, 1, 90),
(47, 12, 2, 77),
(48, 12, 3, 43),
(49, 12, 4, 87),
(52, 13, 3, 87);



--练习


-- 查询所有课程的名称以及对应任课老师的名称
select c.cname,t.tname from course as c inner join teacher as t on c.teacher_id = t.tid;

--查询学生表当中男生和女生各有几人
select gender,count(gender) from student group by gender;

-- 查询学生表中男生和女生各有几人并把名字聚合输出
select gender,count(gender),group_concat(sname) from student group by gender;

-- 查询物理成绩等于100的学生姓名
-- 先找到物理对应的cid
select cid from course where cname = '物理';

-- 先合并两张表student和score,并给出范围查询即score表中的course_id(课程id)字段要等于course表中cname(课程名称)='物理'对应字段的cid(课程id)
select * from student inner join score on student.sid = score.student_id where score.course_id = (select cid from course where cname = '物理');

-- 接下来进行精细化处理
select student.sname,student.sid from student inner join score
    on student.sid = score.student_id
where score.course_id = (select cid from course where cname = '物理') and score.num = 100;

-- 其它写法
select student.sname,student.sid from student inner join score
    on student.sid = score.student_id
inner join course on course.cid = score.course_id
where course.cname = '物理' and score.num = 100;

-- 查询平均成绩大于80分的学生的姓名和平均成绩
select * from student inner join score on student.sid = score.student_id;

-- 写法
select stu.sname,avg(sco.num) from student as stu inner join score as sco
on stu.sid = sco.student_id
    group by stu.sname
having avg(sco.num)>80;

-- 查询所有学生的姓名，选课数，总成绩
select stu.sname as '姓名',count(sco.course_id) as '选课数',sum(sco.num) as '总成绩' from student as stu inner join score as sco
on stu.sid = sco.student_id
group by stu.sid; --利用sid来分组，处理更快，如果分组条件是主键，那么查询语句可以写其它字段而不仅仅是写分组字段
-- 简单理解，利用主键做分组条件，则查询字段的限制会放宽松

-- 查询姓李的老师的个数
select * from teacher;

select count(tname) as '个数',group_concat(tname) as '姓名' from teacher where tname like '李%';

-- 查询没有报李平老师课的学生姓名
-- 查看所有学生的姓名
select * from student;
-- 查看学生的姓名和学生成绩内连接
select * from student inner join score on student.sid = score.student_id;

select * from course inner join teacher on course.teacher_id = teacher.tid;

select * from course inner join teacher on course.teacher_id = teacher.tid where tid != 2;

select teacher.tid from teacher where teacher.tname ='李平老师';


-- 查询没有报李平老师课的学生姓名写法

select student.sname from student where student.sname not in
(
select student.sname from student inner join score on student.sid = score.student_id
inner join course
on score.course_id = course.cid
where course.teacher_id = (select teacher.tid from teacher where teacher.tname ='李平老师')
group by student.sname
);
-- 简单思路，找出报李平老师课的学生的名字，然后在所有学生中没有被包含在报李平老师课程中的名单中的学生
-- 教材写法

select student.sname from student where student.sname not in
(
select student.sname from student inner join score on student.sid = score.student_id
inner join course
on score.course_id = course.cid
inner join teacher on course.teacher_id = teacher.tid
where teacher.tname = '李平老师'
group by student.sname
);

-- 查询只选择了物理课程或体育课程的学生名称
select student.sid,student.sname,count(course.cid),group_concat(course.cname) from student inner join score
on student.sid = score.student_id
inner join course
on score.course_id = course.cid
where course.cname = '体育' or course.cname = '物理'
group by student.sid
having count(course.cid) = 1;  -- 这里加限定是为了只要报物理或者只报体育的，既只能报一门

-- 查询挂科超过两门(包括两门)的学生姓名和班级id
select student.sname as '姓名',
       student.class_id as '班级号',
       class.caption as '所在班级',
       group_concat(score.course_id) as '挂科科目号',
       group_concat(course.cname) as '挂科科目名称'
       from student inner join score
    on student.sid = score.student_id
inner join course
on score.course_id = course.cid
inner join class
on student.class_id = class.cid
where score.num < 60
group by student.sid
having count(course.cname) >= 2;

-- 查询每门课程被选修的次数
select course.cname as '课程',count(score.sid) as '被选修次数'
from
score inner join course
on score.course_id = course.cid
group by course.cname;



