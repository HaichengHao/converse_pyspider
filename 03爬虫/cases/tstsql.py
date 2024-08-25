# @Editor    : 百年
# @FileName  :tstsql.py
# @Time      :2024/8/24 15:46
import sqlite3
conn = sqlite3.connect('douban.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS comments(id INTEGER PRIMARY KEY, comm TEXT)')
conn.commit()
conn.close()