# @Time:2021/9/15 19:32
# @Author:王袁垒
# @file:王袁垒0916.py
# for i in range(1,5):#等腰三角形
#     for j in range(1,5-i):
#         print(' ',end=' ')
#     for k in range(2*i-1):
#         print('*',end=' ')
#     print()
# 1.
# a = 0
# while a<10:
#     print("我爱python",end="")
#     a+=1
# 2.
# a = 0
# while a<10:
#     print("我爱python")
#     a+=1
# 3.
# a = 0
# while a < 101:
#     print(a)
#     a+=1
# 4.
# a = 10
# while a < 21:
#     print(a)
#     a+=1
# # 5.
# while True:
#     a = int(input("请输入一个数字:"))
#     if a == 0:
#         print("你输入的是0,程序结束!")
#         break
#6.
# for a in range(20,9,-1):
#     print(a)
# a = "abc123"
# for i in a:
#     print(i)




# zifu = "a-bc-12----3"
# sum = 0
# for a in zifu:
#     if a == "-":
#         sum += 1
# print(sum)



# 定义一个列表变量，名字叫list1，有三个元素
# list1 = ["刘备","关羽","张飞"]
# # 通过dir 函数显示列表所有的方法
# print(dir(list1))
# 向列表中添加字符用inster(索引,数据)
# list1 = []
# list2 = ["刘","关","张","赵"]
# list1.insert(0,3)
# list1.insert(1,9)
# list1.insert(2,13)
# list2.extend(list1) # 追加另一个列表中的数据在这个列表后面
# list2.append("赵")# append(数据) 末尾添加数据
# 修改列表的值 list[索引] = 值   list2[2]= "赵"
# 删除指定索引的值   del(list2[2])
# 删除第一次出现的数据
# list2.remove("刘")

# list1 = ["郑爽","张哲瀚","吴亦凡","吴亦凡","吴亦凡"]
# list2 = ["张大大"]
# list1 = [1,5,9,2,6,5,8,7]
'''list1.insert(0,"赵薇")    #指定索引添加数据'''
'''list1.append("赵薇")      #在指定的列表末尾追加数据'''
'''list1.extend(list2)       #在一个列表中追加另一个列表的数据'''
'''list1[2]='吴签'           #修改,指定列表的索引为什么'''
'''del(list1[2])            #删除列表指定索引的值'''
'''list1.remove("吴亦凡")    #删除第一次出现的指定数据  '''
'''list1.pop()              #删除列表末尾的数据'''
'''list1.clear()            #清空列表'''
'''a= list1.count("吴亦凡") print(a)  #统计指定数据在列表中出现的次数'''
'''a= list1.index("吴亦凡")  #返回指定数据在列表中的索引值,有多个的时候只返回第一个的索引值'''
'''list1.sort()             #升序排列,按照从小到大的方式'''
'''list1.sort(reverse=True) #降序排列,按照从大到小的方式'''
'''list1.reverse()          #逆转反转,头变尾,尾变头'''
# print(list1)

# # 定义一个空列表变量 向列表内添加 5, 9, 13 这三个数字
# list1 = []
# for a in (5,9,13):
#     list1.append(a)
# print(list1)
# # 定义一个列表变量，内容如下 ["张飞", "刘备", "关羽", "刘邦", "刘老二" ,"曹操" ] 把”刘老二”修改为”周瑜”
# list2 = ["张飞", "刘备", "关羽", "诸葛亮", "刘老二" ,"曹操" ]
# list2[list2.index("刘老二")]='周瑜'
# print(list2)


'''
list1 = ["王昭君","西施","杨玉环","貂蝉"]
for a in list1:
    print(a)
'''
'''
定义一个列表变量，内容如下
使用 for 循环遍历计算列表中一共有多少数字
'''
# list1 = [0, 3, 3, 9, 10, 3, 5]
# num = 0
# for i in list1:
#     num += 1
# print(num)
'''
定义一个列表变量，内容如下 [0, 3, 3, 9, 10 ,3 ,5] 
计算列表中所有数字相加的总和
'''
# list2 = [0, 3, 3, 9, 10, 3, 5]
# num = 0
# for i in list2:
#     num += i
# print(num)

# #拆包
# # 定义一个列表
# list1 = ["王天明", "20岁", 185,"8块腹肌","古力娜扎的男朋友"]
# # 通过对列表进行拆包方式获取列表中每个元素的值
# a, b, c,d ,e= list1
# print(a, b, c,d,e)

# # a 的内容为[0, 1, 2, 3]
# a = [x for x in range(4)]
#
# # a 的内容为[2, 3]
# a = [x for x in range(2, 4)]
#
# # a 的内容为[3, 5, 7, 9]
# a = [x for x in range(3, 10, 2)]
# print(a)

# a = [x for x in range(0, 101) if x % 10 == 0]
# print(a)

# 公共方法
# list1 = ["王天明", "20岁", 185,"8块腹肌","古力娜扎的男朋友"]
# print(len(list1))
# list2 = [1,3,5,9,8,6,7,3,5]
# print(max(list2))
# print(min(list2))
#
# if 3 in list2:
#     print("我在")
# if 2 not in list2:
#     print("我不在")
# else:
#     print("我在")

# 定义一个列表变量，内容如下 ["张飞", "刘备", "关羽", "刘邦", "刘老二" ,"曹操" ]
# 查找列表中是否有刘备，如果有将其删除
# list1 = ["张飞", "刘备", "关羽", "刘邦", "刘老二" ,"曹操" ]
# if "刘备" in list1:
#     list1.remove("刘备")
#     print(list1)
# else:
#     print(list1)
# # 定义一个列表变量，内容如下 [3, 5, 67, 2, 34, 12, 5, 11] 显示列表中最大值
# list2 = [3, 5, 67, 2, 34, 12, 5, 11]
# print(max(list2))

# 元组
# tuple1 = 165,34,25,36
# tuple2 = "a",
# for a in tuple1:
#     print(a)

# tuple3 = "字符串"
# print(type(tuple3))
# tuple4 = "字符串",
# print(type(tuple4))

# # 公共方法
# tuple5 = 5,8,9,10,58,36,10
# #len()
# n1 = len(tuple5)
# print(n1)
# #max()
# n2 = max(tuple5)
# print(n2)
# #min()
# n3 = min(tuple5)
# print(n3)
# # 值 in , 值 not in

# list 和 tuple 类型的转换
# list 转换为tuple
# list1 = [1,2,3,4]
# print(type(tuple(list1)))
# print(tuple(list1))
# # tuple转换为list
# tuple1 = (1,2,3,4,5)
# print(type(list(tuple1)))
# print(list(tuple1))

# 将元组 tuple1 的元素追加到 list1 元素后面
# list1 = ["刘备","关羽","张飞"]
# tuple1 = ("曹操", "周瑜")
# list1.extend(list(tuple1))
# print(list1)



# list1 = ["刘备","男",30]
# list1.append("玄德")
# list1.insert(4,100)
# list1.remove("男")
# list1.reverse()
# for a  in list1:
#     print(a)

# list2 = [x for x in range(30,100)]
# print(list2)
# tuple1 = ("张飞",12,15)
# list1  = list(tuple1)
# list1[list1.index("张飞")] = "关羽"
# print(list1)

# list1 = []
# list1.append("孙尚香")
# list1.append(169)
# list1.append(29.5)
# for a in list1:
#     print(a)

# tuple1 = ()
# list1 = list(tuple1)
# list1.append("大乔")
# list1.append(170)
# list1.append(36)
# tuple1 = tuple(list1)
# for a  in tuple1:
#     print(a)


# list1 = ["蜀","刘备字玄德","张飞字翼德","关羽字云长"]
# list2 = ["黄忠字汉升"]
# # 增
# list1.insert(4,"赵云字子龙") #插入数据
# list1.append("诸葛亮字孔明") #追加数据
# list1.extend(list2) #追加列表
# #修改
# list1[2] = "莽撞人" #根据索引修改数据
# # 删除
# '''
# list1.remove("莽撞人") #指定数据删除
# del(list1[1])#指定索引删除
# list1.pop()#删除最后一个
# list1.clear()#全表删除
# '''
# # 统计
# '''
# a = list1.count("蜀")
# b = list1.index("蜀")
# '''
# # 排序
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)
# list1.reverse()
# print(list1)
#公共方法
# len()
# list1 = ["貂蝉","西施","杨玉环","王昭君"]
# a = len(list1)
# print(a)
# # max()
# list1 = [1,2,33,55,6,8,8,88,44]
# a = max(list1)
# print(a)
# # min()
# list1 = [1,2,33,55,6,8,8,88,44]
# a = min(list1)
# print(a)
# # in
# list1 = ["貂蝉","西施","杨玉环","王昭君"]
# if "杨玉环" in list1:
#     print("我是四大美女")
# # not in
# if "东施" not in list1:
#     print("我不是四大美女")
# else:
#     print("我是四大美女")
# # tuple
# tuple1 = ("貂蝉","西施","杨玉环","王昭君")
# tuple2 = 10,20,50,100,200,500
# # len()
# a = len(tuple1)
# print(a)
# #max()
# print(max(tuple2))
# #min()
# print(min(tuple2))

# in
# if "貂蝉" in tuple1:
#     print("我是貂蝉")
# else:
#     print("我不是貂蝉")
# # not in
# if "貂蝉" not in tuple1:
#     print("我不是貂蝉")
# else:
#     print("我是貂蝉")

























