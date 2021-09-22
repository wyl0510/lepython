# @Time:2021/9/14 9:12
# @Author:王袁垒
# @file:王袁垒0914.py
# 引入随机数模块
import random
# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("可以进网吧happy！")
# else:
#     print("满18再来")


# if age >= 18:
#     print("可以进网吧happy！")
# else:
#     print("满18再来")


# num1 = 通过 input 函数输入的任意数字1
# num2 = 通过 input 函数输入的任意数字
# 如果 num2 不等于 0，计算 num1 除以 num2 的结果。
# num1 = int(input("数字1："))
# num2 = int(input("数字2"))
# if num2 != 0:
#     print(num1/num2)
# elif num2 == 0:
#     print("除数不可以等于零")

# num1 = 通过 input 函数输入的任意数字
# num2 = 通过 input 函数输入的任意数字
# a = 通过 input 函数输入 + - * / 中的任意一个字符
# 如果 a 的值为+，  那么显示 num1 和 num2 相加的结果
# 如果 a 的值为-，  那么显示 num1 和 num2 相减的结果
# 如果 a 的值为*， 那么显示 num1 和 num2 相乘的结果


# num1 = int(input("数字1："))
# num2 = int(input("数字2："))
# lists = ["+", "-", "*", "/",""]
# b = random.randint(0 , 3)
# a = lists[b]
# print(a)
# if a == "+":
#     print(num1 + num2)
# elif a == "-":
#     print(num1 - num2)
# elif a == "*":
#     print(num1 * num2)
# elif a == "/":
#     print(num1 / num2)
# else:
#     print("请输入正确的运算符!")

# num1 的值为通过 input 函数输入的任意整数判断 num1 是偶数还是奇数
# 如果为偶数，print 显示"偶数"，如果为奇数 print 显示"奇数"

# num1 = int(input("请输入数字："))
# if num1 % 2 == 0:
#     print("这是一个偶数")
# else:
#     print("这是一个奇数")


# num1 的值为通过 input 函数输入的任意整数判断 num1 是正数还是负数(假设 0 为正数)
# 如果为正数，print 显示"正数"，如果为负数 print 显示"负数"
# num1 = int(input("输入数字"))
# if num1 >= 0:
#     print("正数")
# else :
#     print("负数")

# and 当两个条件都为true的时候才算通过
# name = input("请输入你的名字:")
# age = int(input("请输入你的年龄:"))
# if name == "小明" and age >= 18:
#     print("通过")
# else:
#     print("不通过")

# or 当至少满足一个条件就可以通过
# name = input("请输入你的名字:")
# age = int(input("请输入你的年龄:"))
# if name == "吴某凡" or age >= 30:
#     print("吴某凡,你可以的")
# else:
#     print("你不可以")

# not 非,当不满足条件的可以通过,
# name = input("请输入你的名字:")
# if not name == "吴某凡":
#     print("我不是吴某凡")
# else:
#     print("我是吴签")


# 通过 input 输入⼀个数 ，编写代码判断该数是否在 0 到 120 之间 。
# num1 = int(input("请输入数字:"))
# if num1 >= 0 and num1 <= 120:
#     print("在0-120之间")
# else:
#     print("我不在0-120之间")

# name 的值为通过 input 函数输入的登录账号
# passwd 的值为通过 input 函数输入的登录密码
# 只有 name 的值为"itcast",并且 passwd 的值为"123456",显示“通过登录”， 否则显示“登录失败”
# name = input("请输入账号:")
# passwd = input("请输入密码:")
# if name == "itcast" and passwd == "123456":
#     print("登录成功")
# else:
#     print("登录失败")

# 分支语句
# hday = input("请输入节日:")
# if hday == "中秋节":
#     print("放假三天好好休息")
# elif hday == "国庆节":
#     print("放假七天,去旅游")
# elif hday == "元旦":
#     print("新的一年新的开始")
# else:
#     print("打工人的苦逼生活")

# age 的值为通过 input 函数输入的任意整数
# 如果 age 小于 10，显示“小孩”
# 如果 age 在 10 到 20 之间，显示“小朋友”
# 如果 age 在 20 到 30 之间，显示“年轻人”
# 如果 age 在 30 到 50 之间，显示“中年人”
# 如果 age 大于 50，显示“老年人”
# age = int(input("请输入你的年纪:"))
# if age < 10:
#     print("小孩")
# elif 10 <= age <= 20:
#     print("小朋友")
# elif age > 20 and age <= 30:
#     print("年轻人")
# elif age > 30 and age <= 50:
#     print("中年人")
# elif age > 50:
#     print("老年人")

# num1 = int(input("输入数字:"))
# if num1 >=0 and num1 <=100:
#     if num1 % 3 ==0:
#         print("能除尽")
#     else:
#         print("不能除尽")
# else:
#     print("不在设定范围中")

# *********
# name 的值为通过 input 函数输入的字符串如果 name 的值为"tom"
# 通过 input 函数输入 age 的值，
# 如果 age 大于等于 30 显示“大叔”
# 如果 age 小于 30 显示“小弟”
# 如果 name 的值不为"tom"
# 显示“姓名错误
# name = input("请输入名字:")
# if name == "tom":
#     age = int(input("请输入年龄:"))
#     if age >= 30:
#         print("大叔")
#     else:
#         print("小弟")
# else:
#     print("姓名错误")

# num1 = int(input("请输入整数:"))
# if 500 <= num1 <= 1000:
#     if num1 % 2 ==0:
#         print("%d是偶数" % num1)
#     else:
#         print("%d是奇数" % num1)
# else:
#     print("数字不在范围")

# 列表 下标从0开始
# ru = ['石头','剪刀','布']
# 随机一个数字去取列表里面的值
# pc = ru[random.randint(0 , 2)]
# # 玩家输入一个值,去取列表里面的值
# player = ru[int(input("请输入0到2的数字:"))]
# # 玩家胜的情况
# if (player == "拳头" and pc == "剪刀") or (player == "剪刀" and pc == "布") or (player == "布" and pc == "石头"):
#     print("我赢了,我出的是"+player+",电脑出的是"+pc)
# # 玩家平局的情况
# elif pc == player:
#     print("平局,我出的是"+player+",电脑出的是"+pc)
# # 电脑胜的情况
# else:
#     print("电脑赢了,我出的是"+player+",电脑出的是"+pc)

# height = float(input("请输入身高:"))
# if height <= 150:
#     print("可以进入")
# else:
#     print("请买票")

# num1 = input("有票输入1,没票输入0:")
# if num1 == "1":
#     print("欢迎光临")
# elif num1 == "0":
#     print("请买票")
# else:
#     print("错误")

# num1 = random.randint(0,999)
# print(num1)
# if num1 >=0 and num1 <= 9:
#     print("毫米")
# elif num1 >=10 and num1 <= 99:
#     print("厘米")
# else:
#     print("分米")

# 判断语句的实例运用
# break 退出循环: 在 while 循环内部，通过 input 接收用户输入，当用户输入 exit，
# while 循环终止。
# a = 0
# while a < 10 :
#     end = input("输入exit结束循环:")
#     if end == "exit" :
#         print("结束循环!")
#         break
#     a += 1














































