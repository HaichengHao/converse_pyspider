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