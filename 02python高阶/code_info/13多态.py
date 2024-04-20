# @Editor    : 百年
# @FileName  :13多态.py
# @Time      :2024/4/20 9:11
class Animal(object):
    def eat(self):
        print('动物吃')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Human(Animal):
    def eat(self):
        print('人吃五谷杂粮')

def func(obj):
    obj.eat()

func(Dog())
# 狗吃骨头
