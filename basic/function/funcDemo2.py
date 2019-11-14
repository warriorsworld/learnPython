'''
    使用递归来实现求和
'''
def sum(lastNumber):
    if lastNumber == 0:
        return 0
    else:
        return lastNumber + sum(lastNumber - 1)

print(sum(5))
