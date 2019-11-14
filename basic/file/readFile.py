# 创建的目录
# path = "./"
# list1 = ['Google', 'Runoob', '1997', '2000']
# for item in list1:
#     os.rmdir(item)

# print ("目录已创建")

import os, sys
# 打开文件
fd = os.open("./test.txt",os.O_RDWR)
print(fd)
   
# 读取文本
ret = os.read(fd)
print (ret)

# 关闭文件
os.close(fd)
print ("关闭文件成功!!")