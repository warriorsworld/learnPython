'''
    函数返回多个值
'''

def func(age, name):
    return age, name

print(type(func(18, '小明'))) # 返回值为: <class 'tuple'>
print(func(18, '小明'))

for x in func(18, '小明'): # 遍历tuple
    print(x)

# 访问tuple元素
print(func(19, '小明')[0])

result = func(19, '小明')

# 遍历tuple的另一种方式;
for i in range(0, len(result)):
    print(result[i])

age, name = func(19, '小明')
print('----------------------------------------------')
print('名字是: ' + name)
print('年龄是: ' + str(age))