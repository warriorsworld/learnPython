'''
    闭包实现求和
'''

def sum():
    sumResult = 0
    def wrapper():
        # 如果在闭包的内部函数中直接使用外部函数的变量时，不需要任何操作，直接使用就可以了。
        # 但是如果要修改外部变量的值，需要将变量声明为 nonlocal
        # nonlocal 声明变量为非本地变量，如果确定在程序要修改外部变量，那么建议将 nonlocal 写在内部函数的第一行
        nonlocal sumResult
        sumResult += 1
        return sumResult
    return wrapper

sumfunc = sum()
# python的闭包跟js中不一样的一点是，python高阶函数必须要引用其外部函数的变量
print(sumfunc())
print(sumfunc())
print(sumfunc())

# 每个函数都只有自己的名字;
print(sumfunc.__name__)