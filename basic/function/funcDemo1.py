'''
    使用for循环来求和
'''

def sum(lastNumber):
    sumResult = 0
    for i in range(0, lastNumber):
        sumResult += i
    return sumResult
    
print(sum(5)) # 10
print(type(sum(5))) # <class 'int'>