"""
@File    :model.py
@Editor  : 百年
@Date    :2025/8/4 21:56 
"""
class User():
    def __init__(self,name,pwd,phone=None):
        self.name = name
        self.pwd = pwd
        self.phone = phone

    def __str__(self):
        return self.name