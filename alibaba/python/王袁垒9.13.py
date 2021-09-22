# @Time:2021/9/13 11:49
# @Author:王袁垒
# @file:test_002.py
# import keyword
# print(keyword.kwlist)
"""
python解释器 解读代码 代码电脑解读不了
"""



'''
print('hello,world')
name=input('请输入你的名字：')
print('你的名字是'+name)
num=int(input('你多大了'))
if num>18:
    print('成年了')
elif num<18:
    print('你还未成年')
'''

'''
多行注释
可以注释
'''
'''print(1+1)
print(2-1)
print(2*2)
print(2/2)
print(5%2)
print(5**2)
print(5//2)'''


# #运算 +
# a = 10
# b = 15
# he = '和是：'
# print(he,a+b)
# sum = a+b
# print('和是：',sum)
# print('差是：',b-a)
#
# #运算 *
# a = 5
# b = 6
# print('积是：',a*b)
# # /
# a = 20
# b = 5
# print('商是：',a/b)
# # //
# a = 20
# b = 3
# print('取整：',a//b)
# # %
# a = 20
# b = 3
# print('取余：',a%b)
# # ** 次方 幂
# a = 2
# b = 3
# print('幂：',a**b)


'''
price = 8.5
weight = 7.5
money = price * weight
print(money)

price = 8.5
weight = 10
money = price * weight
money = money - 5
print(money)
'''
#交换值
# a = 10
# b = 20
# 交换
# a,b = b,a
# print(a,b)
'''
print('交换前a,b：',a,b)
temp = a
a = b
b = temp
print('交换后a,b：',a,b)
'''
# # 数字类型 整型  浮点型  布尔型
# a = 10
# b = 10.1
# c = b<a
# print(type(a))
# print(type(b))
# print(type(c))
# print(c)
# # 非数字类型
# str1 = "111"
# str2 = "2asa"
# print(type(str1))
# list1 = [1,2,3,4,5,6]
# print(type(list1))
# for int1 in list1:
#     print(int1)
# a = "12"
# print(type(int(a)))

# i = 10 整数类型
# f = 10.5 浮点类型
# b = True True代表1
# ff = False False代表0
# print(i * b)
# print(i * f)
# print(int(i * f))强转为int类型
# print(b + ff) 布尔类型 true,false 在运算是代表的是数字1,0


# 字符串计算会拼接起来
# str1 = "王"
# str2 = "袁垒"
# str3 = str1 + str2
# print(str3)

# 字符串和整型 相乘时会进行复制类型的操作
# str1 = "王"
# str2 = str1 * 3
# print(str2)

# 不同类型变量的计算结果
# a = True
# b = False
# c = "你好"
# d = 3.14
# e = 5
# # 计算 a + b = ?
# print(a + b)
# # 计算 c + d = ?
# print(c + str(d))
# # 计算 c * e = ?
# print(c * e)
# # 计算 d * b = ?
# print(d * b)

# # int 转 str
# a = 1
# print(type(str(a)))
# # str 转 int
# a = "3"
# print(type(int(a)))
# # str 转 float
# a = "3.14"
# print(type(float(a)))
# # float 转 int
# a = 3.99
# print(type(int(a)))

# a = "123"
# b = 456
# 把b 转化为字符串，与a 拼接成一个字符串"123456"，并用print 显示结果
# print(a+str(b))
# 把a 转化为数字，结果与b 相加，并用print 显示结果
# print(int(a)+b)

# a = 任意数字
# b = 任意数字
# 求a / b 的结果，要求结果只保留整数，并且四舍五入 round()
# a = 18
# b = 5
# print(round(a / b))

# QQ = input("请输入你的QQ号：")
# password = input("请输入你的密码：")
# print("你的QQ号是："+QQ+"\n"+"你的密码是："+password)

# a = int(input("请输入任意数字："))
# b = int(input("请输入任意数字："))
# print(a + b)
# # 检查a + b 的结果是什么？

# 字符串格式化
# name = '小明'
# print("我的名字叫%s请多多关照" % name)
# gongsi = "艾腾科技"
# name = "王袁垒"
# tel = "13461317955"
# email = "1822394957@qq.com"

# print("********************")
# print("公司名称:%s" % gongsi)
# print("姓名:%s" % name)
# print("电话：%s" % tel)
# print("邮箱：%s" % email)
# print("********************")


# # 1.定义字符串变量 name = “小明”，输出:  我的名字叫小明，请多多关照！
# name = "小明"
# print("我的名字叫%s，请多多关照！" % name)
# # 2.定义整数变量 num = 1，输出: 我的学号是  000001
# num = 1
# print("我的学号是  %.6d" % num )
# # 3.定义⼩数 price = 8.5、 weight = 5 ，输出：苹果单价 8.5 元／⽄，购买了5.00 ⽄，需要支付  42.50 元
# price = 8.5
# weight = 5
# print("苹果单价 %.1f 元／⽄，购买了%.2f ⽄，需要支付  %.2f 元" % (price,weight,(price * weight)))
# # 4.定义⼀个⼩数 scale = 10.01 ，输出: 数据是  10.01%
# scale = 10.01
# print("数据是  %.2f%%" % scale)

# 多个print 函数会输出结果打印到一行
# print("hello world", end="")
# print("hello python")
# 使用end=""  能实现一个不换行的操作
'''
print("你好你好",end = " ")
print("hihi")
'''

# 3.转义字符
# \t 制表符，用在输出字符上，类似一个tab键的实现
# \n 换行
# \\ 会有一个\输出出来
# \' 单引号 打印单引号时可使用
#  \" 双引号 打印双引号时使用
# print("1\t2\t3\t")
# print("这中间有一个空格我用\t代替")
# print("这换行我用(\+n\n)代替")
# print("这是一个单引号\'\'")
# print("这是一个双引号\"\"")
# print(r"这是一个反斜杠\\\\")

# 禁止转义 在打印引号前面写r 就禁止转义，里面的转义字符不会执行，有啥打印啥
# print("hello\tworld\nhello\\world")
# print(r"hello\tworld\nhello\\world")

# num1 = "123"
# num1 = int(num1)
# print(type(num1))

# a=input("输入数字:")
# b=input("输入数字:")
# print(int(a)+int(b))

# print("我是转义字符\\n,你是转义字符\\t")
# idcard = "我的名片"
# name = "itheima"
# qq = 213123
# tel = 18523123
# address = "北京市昌平区"
# print("==========%s==========" % idcard)
# print("\t姓名:%s" % name)
# print("\tQQ:%.6d" % qq)
# print("\t手机号:%.8d" % tel)
# print("\t公司地址:%s" % address)
# print("===========================")
# print("我是转义字符\\n,你是转义字符\\t")
# print(r"我是转义字符\n,你是转义字符\t")

