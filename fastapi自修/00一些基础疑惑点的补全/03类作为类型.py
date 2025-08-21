# @Author    : 百年
# @FileName  :03类作为类型.py
# @DateTime  :2025/8/20 22:41

class Person:
    def __init__(self,name:str):
        self.name = name

def get_person_name(one_person:Person):
    return one_person.name

