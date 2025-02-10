#!/usr/bin/env python3

class Dog:
    """ 一次模拟小狗的简单尝试 """

    def __init__(self, name, age):
        """ 初始化属性name和age """
        self.name = name
        self.age = age

    def sit(self):
        """ 模拟小狗收到命令时坐下 """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """ 模拟小狗收到命令时打滚 """
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)   # 创建实例
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

print()

my_dog = Dog('funny', 16)   # 创建实例
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
