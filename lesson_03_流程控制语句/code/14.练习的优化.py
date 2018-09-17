# 模块，通过模块可以对Python进行扩展
# 引入一个time模块，来统计程序执行的时间
from time import *
# time()函数可以用来获取当前的时间，返回的单位是秒 
begin = time()

i = 2
while i <= 100000:
    flag = True
    j = 2 
    while j <= i ** 0.5:
        if i % j == 0:
            flag = False
            # 一旦进入判断，则证明i一定不是质数，此时内层循环没有继续执行的必要
            # 使用break来退出内层的循环
            break
        j += 1
    if flag :
        # print(i)  
        pass
    i += 1

# 获取程序结束的时间
end = time()

# 计算程序执行的时间
print("程序执行花费了：",end - begin , "秒")