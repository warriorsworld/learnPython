'''
    this file is a pratice for lerning class instance methond
'''

class Student(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
    
    def go_school(self):
        print(self.name + '去上学')

    def sum_number(self, lastNumber):
        num = 0
        sum = 0
        while num <= lastNumber:
            sum += num
            num += 1
        return sum
    
    def analysis_score(self, score):
        if (score >= 85):
            print('优秀')
        elif score >=60:
            print('及格')
        else:
            print('不及格，等着补考吧')


# this part is class method call;
student1 = Student('小明', '男', 18)
student1.analysis_score(78)
student1.analysis_score(58)
student1.analysis_score(88)

# 打印该文件的文档注释;
print(__doc__);
# student1.go_school()
# print('the number is : %s' % (student1.sum_number(100)))