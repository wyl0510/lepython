# @Time:2021/9/17 9:42
# @Author:王袁垒
# @file:王袁垒0917.py
# 集合 set{}
# 列表 list[]
# 元组 tuple()

# 定义一个空集合
# set1 = set()
#  列表是有序的对象集合 ；
#  集合是⽆序的对象集合 ；
#  同一个集合内值不允许重复。
# list1 = ["1",2,6]
# set1 ={"1",2,6,2}
# print(list1)
# print(set1)


# 增加 add(值)
# set1 = {"莽撞人","烟云兽","锁子连环甲"}
# set1.add("豹头环眼")
# print(set1)
# 删除
# 删除集合最后一个
# set1.pop()
# print(set1)
# 删除指定的数据
# set1.remove("莽撞人")
# print(set1)
# 清空集合
# set1.clear()
# print(set1)

# set1 = set()
# for循环
# for a in range(0,5):
#     b = int(input("请输入整数:"))
#     set1.add(b)
# while循环
# i = 0
# while i < 5:
#     set1.add(int(input("输入整数:")))
#     i+=1
# print(min(set1))
# for循环遍历,顺序随机
# set1 = {"妲己",35,30}
# for i in set1:
#     print(i)
# 定义一个空集合变量，通过input函数，向集合里输入任意3个字符串 # 遍历集合,显示集合中所有的字符串
# set1  = set()
# for a in range(0,3):
#    set1.add(input("输入字符串:"))
# for b in set1:
#     print(b)

#定义一个空的集合
# set1 = set()
#往空集合里添加五个元素
# for a in range(5):
#     set1.add(a)
# print(set1)
#删除几个最后的一个元素
# set1.pop()
# print(set1)
# set1.pop()
# print(set1)
# set1.pop()
# print(set1)
#删除集合里指定的元素（自己指定元素删除）
# set1.remove(0)
# print(set1)
#清空集合
# set1.clear()
# print(set1)


#定义一个集合，里边有五个元素
# set2 = {1,2,3,4,5}
#求集合里的元素个数
# print(len(set2))
#求集合里元素的最大值
# print(max(set2))
#求集合里元素的最小值
# print(min(set2))
#判断5在不在集合，在的话打印，不在添加进去
# for i in set2:
#     if i == 5 :
#         print(i)
#     else:
#         set2.add(5)
# print(set2)
# if 5 in set2:
#     print(set2)
# else:
#     set2.add(5)
# dict1 = {}
# dict2 = {"key1":"value1"}
# print(len(dict2))
# for i in dict2:
#     print(dict2[i])

# 字典的增和改
# dict1 = {"刘备":"哭","张飞":"莽"}
# dict1["关羽"] = "勇"
# dict1["刘备"] = "聪明"
# # 删除指定键 pop("键")
# dict1.pop("刘备")
# # clear() 清空字典
# dict1.clear()
# print(dict1)

dict1 = {"name":"周瑜","age":32,"id":"001"}
#字典中增加一个键值对’sex’:’男’；
# 删除键’id’；
# 将键’age’的值修改为26。
# dict1["sex"] = "男"
# print(dict1)
# dict1.pop("id")
# print(dict1)
# dict1["age"] = 26
# for n in dict1:
#     print(n,dict1[n])
# print(dict1)
"""items 返回包含键值对的元组"""
# dict1 = {"name":"周瑜","age":32,"id":"001"}
# print(dict1.items())
'''拆包'''
# for n,m in dict1.items():
#     print(n,m)
# 课堂练习
# 循环遍历字典, 显示字典每个键和键对应的值
# dict1 = {"a": 23, "b": 4, "c": 9, "d": 3, "e": 12}
# for i, j in dict1.items():
#     print("%s:%s" % (i, j))
# for i in dict1:
#     print("\t%s:%s" % (i, dict1[i]))

'''
字符串索引
字符串[索引]
'''
'''
str1 = "123456"
print(str1.index("6"))
'''
'''
isalpha()  判断字符串是否全部都为文字构成
isdigit()  判断字符串是否全为数字构成
'''
# zh_CN = "字符串是否全部都为文字构成"
# if zh_CN.isalpha():
#     print("全文字")
# else:
#     print("非全文字")

# num = '123456'
# if num.isdigit():
#     print("全数字")
# else:
#     print("非全数字")

'''
islower() 判断字符串中所有字母是否都为小写
isupper() 判断字符串中所有字母是否都为大写
'''
# lower = "AAAA"
# if lower.islower():
#     print("全是小写")
# else:
#     print("非全是小写")
# if lower.isupper():
#     print("全是大写")
# else:
#     print("非全是大写")

'''
find("字符串") 查找子串在字符串中出现的位置，找不到返回 -1
replace(“子串”, ”新子串”) 查找子串，并用新的子串替代
count(“子串”) 返回子串在字符串中出现的次数
'''
# str1 = "hello,python"
# print(str1.find("th"))
# print(str1.replace("python","world"))
# print(str1.count("l"))

'''
upper() 将小写字母转化为大写
lower() 将大写字母转化为小写
swapcase() 将大小写字母反转
'''
# str1 = "hello,WORLD"
# # 小写转大写
# print(str1.upper())
# # 大写转小写
# print(str1.lower())
# # 大小写反转
# print(str1.swapcase())
'''
lstrip() 去除左侧空格
rstrip() 去除右侧空格
strip()  去除左右两侧空格
'''
# str1 = " hello"
# str2 = "hello "
# str3 = " hello "
# print(str1)
# print(str1.lstrip())
# print(str2.rstrip())
# print(str3.strip())
#
'''
split("子串")
'''
# str1 = "hello,world,and,python"
# list1 = str1.split(",")
# print(list1)

# str1 = "123 98 234 23 345"
# list1 = str1.split(" ")
# j = 0
# for i in list1:
#     j += int(i)
# print(j)


# 通过 input 函数，输入一个字符串，判断字符串是否可以转化为整数，
# 如果不可以转化, 显示"请输入数字"
# str1 = input("输入一个字符串:")
# if str1.isdigit():
#     print("你输入的是%s" % str1)
# else:
#     print("请输入数字")


# "明日复明日 明日何其多 我生待明日 万事成蹉跎"
# 去掉字符串中，中间的空格
# str1 = "明日复明日 明日何其多 我生待明日 万事成蹉跎"
# print(str1.replace(" ",""))

# id = 1
# name = "刘备"
# weight = 80.2
# tel = "13912345678"
# # 以上变量，输出结果如下
# print("*********************")
# print("编号:%.6d" % id)
# print("姓名:%s" % name)
# print("体重:%.3f" % weight)
# print("电话:%s" % tel)
# print("*********************")
'''
切片器
'''
# 定义一个字符串str1
# str1 = "我爱 python"
# s = str1[-1]
# print(s)
# 定义一个字符串
# str1 = "我爱 python"
# s = str1[0::3]
# print(s)

# 截取从 2 ~ 末尾的字符串
# 定义一个字符串str1
# str1 = "我爱 python"
# print(str1[2:])


# 截取从开始 ~ 5 位置的字符串
# 定义一个字符串str1
# str1 = "我爱 python"
# print(str1[:5])

# 截取完整的字符串
# 定义一个字符串str1
# str1 = "我爱 python"
# print(str1[:])

# 从开始位置，每隔⼀个字符截取字符串
# 定义一个字符串str1
# str1 = "我爱 python"
# print(str1[::2])

# 从索引 1 开始，每隔⼀个取⼀个
# str1 = "我爱 python"
# print(str1[1::2])

# 截取从 2 到末尾 - 1 的字符串
# 定义一个字符串str1
# str1 = "我爱 pythno"
# print(str1[2:-1:])

# 截取字符串末尾两个字符
# str1 = "我爱 pythno"
# print(str1[-2:])

# 字符串的逆序（⾯试题）
# str1 = "我爱 python"
# print(str1[::-1])

# set1={"曹操",  "刘备", 100}
# set1.add("诸葛亮")
# set1.remove("刘备")
# for i in set1:
#     print(i)

# dict1 = {"id": 10, "name": "周瑜", "age": 30}
# dict1["sex"] = "男"
# dict1["age"] = 25
# for a,b in dict1.items():
#     print("%s:%s" % (a,b))

# int1 = input("输入一串字符:")
# if int1.isdigit():
#     print("输入的全是数字")
# else:
#     print("不全是数字")

# str1 = "gongfuxong@itcast.cn"
# if "@" in str1:
#     print("包含@符号")
# else:
#     print("不包含@符号")


# str1 = "刘备与曹操是哥们"
# str1 = str1.replace("曹操","关羽")
# print(str1)

#
# str1 = "abEsaAuY"
# str1 = str1.swapcase()
# print(str1)


# str1 = "9*7+12-5"
# list1 = []
# for i in str1:
#     if i.isdigit():
#         list1.append(int(i))

str1 = "9*7+12-5"
str1 = str1.replace("*",' ').replace("+",' ').replace("-",' ')
list1 = str1.split(' ')
# i = 1
# while i <= len(list1):
#     list1[i-1] = int(list1[i-1])
#     i+=1
print(int(list1[0])*int(list1[1])+int(list1[2])-int(list1[3]))






# str1 = str1.replace("*",' ')
# str1 = str1.replace("+",' ')
# str1 = str1.replace("-",' ')
# list1 = str1.split(" ")
# print(int(list1[0])*int(list1[1])+int(list1[2])-int(list1[3]))
# list2 = []
# for i in list1:
#     i = int(i)
#     list2.append(i)















# str1 = "9*7+12-5"
print(eval("9*99"))

































