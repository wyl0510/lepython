# @Time:2021/9/18 9:36
# @Author:王袁垒
# @file:王袁垒0918.py
# def my_sum(a, b,c,d,e,m):#定义函数 def   变量名(行参,行参)
#     sum1 = a+b+c+d+e+m
#     return sum1
# print(my_sum(10,30,5,10,50,63))

# def my_found(a, b, c):
#     num1 = a * b * c
#     return num1
# my_found(5 , 10 , 20)# 直接调用函数,执行里面的值
# print(my_found(5 , 10 , 20))
#
# def my_found1():
#     num1 = "无参"
#     return num1
# my_found1()# 直接调用函数,执行里面的值
# print(my_found1())

# def hello():# 定义函数
#     print("hello")
#     print("python")
#     print("world")
# hello()   #调用函数


# #定义函数 my_func1()
# def my_func1():
#     #for函数打印20个*
#     for a in range(20):
#         print("*",end="")
#     print("\n")
# #定义函数 my_func2()
# def my_func2():
#     b = 0
#     # while函数打印20个*
#     while b < 20:
#         print("*",end="")
#         b += 1
#     print("\n")
# #定义函数 my_func3()
# def my_func3():
#     #打印20个*
#    print("*" * 20)
#    print("\n")
# my_func1()
# my_func2()
# my_func3()
# def def_func1(a,b):
#     num = a // b
#     return num
# print(def_func1(20,10))

# def my_func2(num1):
#     for i in range(num1):
#         print("*",end="")
#
# my_func2(3)
#
# def my_sum2(num1, num2):
#     result = num1 + num2
#     return result
# # return 后面的代码，将不会被执行
#     print("test")
#
# print(my_sum2(2,10))


"""
# 定义一个函数计算开始数字到结束数字间的整数和
def def_sum(start,stop):
    sum1 = 0
    # for 循环遍历
    for x in range(start,stop):
        # 计算和
        sum1 += x
    return sum1
# 调方法 传参  打印返回值
print(def_sum(0,101))
"""
# #定义函数计算面积
# def def_mm(height,weight):
#     sum = height * weight
#     return  sum
# # 调方法 传参  打印返回值
# print(def_mm(10,20))

"""
# 定义函数计算长方体的体积
def def_tiji(length,weigth,height):
    # 计算体积
    sum1 = length* weigth* height
    return sum1
# 调方法 传参  打印返回值
print(def_tiji(10,10,10))
"""

"""
def my_squar(height, width):
    sum1 = height * width
    return sum1
print(my_squar(5,6))


def my_func(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
print(my_func(10,3))
"""

"""
def test1_case1():
    print("test1")


def test_case2():
    test1_case1()
    print("test2")


test_case2()
"""

"""
def Test_001(a, b):
    sum1 = a + b
    return sum1


def Test_002(c, d):
    s = Test_001(3, 4)
    sum2 = c * d
    return s + sum2
"""

# 2   #7  #9
# ww = Test_002(1, 2)
# print(ww)


"""
全局变量:函数外部定义的变量

局部变量:函数内部定义的变量

变量的生命周期:变量从被创建到被系统回收的过程

部变量在函数执⾏时才会被创建 ；
函数执⾏结束后局部变量被系统回收 ；
"""
"""
def my_func1():
    a = 10


def my_func2():
    a = 20
    # 调用 my_func2 函数，不会影响 a 的值
    my_func1()
    print("a = %d" % a)


my_func2()
"""
# a = 9
#
#
# def test_n():
#     b = 10
#     print(b)
#
#
# def test_m():
#     b = 11
#     print(b)
# 局部变量名字可以重复,局部变量只作用于自己的函数里面
# 全局变量名字不可以重复,作用于所用函数,都可以调用
#
# test_n()
# test_m()

"""
# 定义一个全局变量num
num = 100
def my_func1():
#函数内部使用global 关键字声明全局变量num
    global num
    num = 1

# 全局变量num 的值被my_func1 函数改变
my_func1()
print(num)
"""

# 定义一个全局变量
# name=”张三”,
# 定义一个函数 my_test1,
# 在函数 my_test1 内部修改全局变量 name 的值为”李四”
# name = "张三"
#
#
# def my_test1():
#     global name
#     name = "李四"
#
#
# my_test1()
# print(name)


"""
参数进阶: 非数字类型在函数内部进行的修改,外部的数据也会修改
数字类型在函数内部进行修改,外部不会受到影响
非数字类型:列表 集合 字典 元组 str
"""

# def my_test(list1):
#     list1[0] = "刘备"
#     return list1
#
#
# a = ["曹操", 35, 178]
# print(my_test(a))
# print(a)

"""
def myfunc(list_1):
    list_1.clear()


list1 = [2, 5, 3]
myfunc(list1)
print(list1)
"""

"""
缺省参数,设置缺省参数,可以不添加该参数时使用缺省值

设置缺省值要放在行参的末尾设置
def my_num_test(a, b=10):
    return a + b


def my_num_test1(a=20, b=10):
    return a + b


print(my_num_test(5))
print(my_num_test1())
"""

# 匿名函数


# my_num = lambda a, b: a + b
# print(my_num(10, 20))

# 简化版的lambda 函数，求最大值
# num = (lambda a, b: a if a > b else b)(9, 5)
# print(num)

#  使用匿名函数 做一个简单的比较大小的函数
# num1 = (lambda a, b: a if a > b else b)(10, 10)
# print(num1)

# 1.定义一个函数my_func(),函数执行结果为输出10行”hello world”
# def my_func():
#     print("hello,world\n" * 10)


# my_func()


# def my_sub(a, b):
#     num = a - b
#     print(num)
#
#
# my_sub(5, 9)


# 2.定义一个函数my_sub(a, b), a和b为整数, 调用函数, 执行结果为显示a - b的差
# def my_sub(a, b):
#     num = a - b
#     return num
#
#
# print(my_sub(9, 5))

# 4.


# def my_num(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False


# print(my_num(8))
# # 5.
#
#
num1 = 0


def my_num():
    global num1
    num1 = 10
    return num1
def my_num1():
    print(num1)

my_num1()
print(my_num())


# def my_sum1(a, b, c, d):
#     num = a + b + c + d
#     return num
#
#
# print(my_sum1(1, 2, 3, 4))

# sum1 = lambda a: a*10
#
# print(sum1(2))











