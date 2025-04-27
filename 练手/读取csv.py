"""
@File    :读取csv.py
@Editor  : 百年
@Date    :2025/4/26 16:52 
"""
import csv

with open('tianqi.csv','r',encoding='utf-8') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(row)