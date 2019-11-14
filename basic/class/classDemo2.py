'''
    this file is a pratice for learning class extend
'''

class Animal(object):
    # 可变参数前与关键字参数;
    def __init__(self, *args, **kw):
        pass

    def run(self):
        print('Animal is running')


class Dog(Animal):
    def __init__(self, *args, **kw):
        super(Dog, self).__init__()

    def run1(self):
        print('Dog is runnnig')

dog1 = Dog()
dog1.run1()

# 使用isinstance判断一个实例是不是某一个类型的数据;
# print(isinstance(dog1, Animal))
# print(isinstance(dog1, Dog))

def a():
    pass

print(dir(dog1))