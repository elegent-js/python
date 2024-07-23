# 演示python中类的创建，注意构造方法是__init__，类中的方法第一个参数是self
# 类中的属性通过self.xxx来访问，类中的方法通过self.method()来调用
# 类中的方法第一个参数是self，表示实例本身，类似java中的this
# 类中的方法调用时，不需要传递self参数，python会自动传递

class Dog:
    """一次模拟小狗的简单尝试"""

    # 特殊方法，类似构造函数
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")


    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")