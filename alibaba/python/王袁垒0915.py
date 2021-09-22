# @Time:2021/9/14 20:30
# @Author:王袁垒
# @file:王袁垒0915.py
"""
顺序  分支  循环
"""
# a = 0
# while a < 5:
#     print("大哥你来了\t%d" % a)
#     a += 1
# a = 1
# while a < 101:
#     print("王袁垒")
#     print(a)
#     a+=1
# a = 0
# 死循环 因为a没变一直是对的
# while a < 5:
#     print("擦,大哥")

# 从 0 开始，截止到 5 的 6 个数字
# a=0
# while a < 6:
#     print(a)
#     a += 1

# 1.	课堂练习---输出连续数字	从 5 开始，截止到 0 的 6 个数字
# i = 5
# while i >= 0:
#     print(i)
#     i -= 1
#
# print(i)


# 1.	需求----计算 0 ~ 100 之间所有数字的累计求和结果
# count = 0
# num = 0
# while num <= 100:
#     count += num
#     num += 1
#
# print(count)

# 计算 300到415累计相加的和
# a = 300
# sum = 0
# while a <= 415:
#     sum += a
#     a += 1
# print(sum)+

# a = 0
# while a <10:
#     a+=1
#     if a == 5:
#         break
#     print(a)
#
# print(a)

# break 退出循环: 在 while 循环内部，通过 input 接收用户输入，当用户输入 exit，
# while 循环终止。
#
# while True:
#     end = input("退出请输入exit:")
#     if end == "exit":
#         break
#     print("你输入的是%s" % end)
# a = 0
# while a < 1:
#     end = input("退出请输入exit:")
#     if end == "exit":
#         break
# continue 执行continue的时候,跳过本次循环,不执行下面的程序,再次进入循环执行程序
# a = 0
# while a < 10:
#     a += 1
#     if a == 6:
#         continue
#     print(a)
# 通过 input 输入任意一个整数
# 如果输入的是 5，那么就打印 5 行*号，如果输入 10，就打印 10 行*号如果输入大于 20，最多只打印 20 行*号
# num = int(input("请输入打印行数:"))
# n = 0
# 方法一
# while n < num:
#     print("*%d" % n)
#     n += 1
#     if n == 20:
#         break
# 方法二
# if num < 20:
#     while n <= num:
#         print("*%d" % n)
#         n += 1
# elif num >= 20:
#     while n < num:
#         if n == 21:
#             break
#         print("*%d" % n)
#         n += 1

# while嵌套
# end=""  实现不换行
# print("") 与print()
#
# a = 0
# while a < 5:
#     a += 1
#     b = 0
#     while b < 5:
#         print("*",end="")
#         b += 1
#     print("")
# 打印三角形
# a = 0
# while a < 5:
#     b = 0
#     while b <= a:
#         print("*",end="")
#         b+=1
#     print("")
#     a+=1
# 打印数字三角形
# a = 0
# while a < 5:
#     b = 0
#     while b <= a:
#         b += 1
#         print(b,end="")
#     print("")
#     a += 1
# 输出两行* 每行三个
# a = 0
# while a < 2:
#     a += 1
#     b = 0
#     while b < 3:
#         print("*",end="")
#         b+=1
#     print("")
# 实现的代码
# *
# **
# ***
# a = 0
# while a < 3:
#     b = 0
#     while b <= a:
#         print("*",end="")
#         b += 1
#     a += 1
#     print()

# 99乘法表
# i=0
# while i < 9:
#     i += 1
#     j = 0
#     while j < i:
#         j += 1
#         print("%d * %d = %d" % (j,i,i*j),end=" ")
#     print()
# str1 = "ABCDEFG"
# # n 分别代表str1 字符串里每一个字符
# for n in str1:
#     print(n)

# 4.	课堂练习----循环遍历计算字符串"hello itcast", 计算字符串中有多少字符
# hello = "hello itcast"
# num = 0
# for hi in hello:
#     print(hi)
#     num += 1
# print(num)
"""
range(start,stop,int)
start:数字起始值
stop:数字停止位置--不包含
int:默认为1,代表遍历范围内的每一个值,int为2代表遍历范围里面的全部偶数,
    小于0代表降序遍历每一个值并降序打印,但start,stop要倒着写range(20,10,-1)
    -2代表降序遍历每一个偶数值并降序打印range(20,10,-2)
"""
# for a in range(20,10,-2):
#     print(a)
#
# for a in range(0,101):
#     print(a)
#
# for a in range(0,5):
#     for b in range(0,5):
#         print("*",end="")
#     print("")


































































































































































