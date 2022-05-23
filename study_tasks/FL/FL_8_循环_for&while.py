# # 循环---while循环
# count = 0
# if count < 5:   # 无循环，执行一次即停止
#     print("现在执行的是if语句，现在count=", count)
# while count < 5:
#     print("现在执行的是while语句，现在count=", count)
#     count += 1

# loop_condition = True
# while loop_condition:
#     print("我是循环体的语句")
#     loop_condition = False
#
# i = 1
# while i in range(1, 11):
#     print(i * i)
#     i += 1

# choice = input("Do you like this programming? ")
# while choice != "y" and choice != "n":
#     choice = input("对不起，无法识别输入值，清重新输入(y/n):")

# 8.040 死循环
# count = 0
# while count < 10:
#     print(count)
#     count += 1

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 10:
#         break      # 用break结束整个循环

# count = 0
# while True:
#     count += 1
#     if count == 6:
#         continue     # 用continue结束当前循环，下面的语句不再执行，提前进入下一个循环
#     print(count)
#     if count >= 10:
#         break

# for循环 ---适合知道要循环几次
# for i in range(20):
#     print(i)

# hobbies = []
# for hobby in range(3):
#     hobby = input("请输入一项您的爱好：")
#     hobbies.append(hobby)
# print(hobbies)

# thing = 'spam!'
# for c in thing:
#     print(c)
#
# word = "eggs!"
# for c in word:
#     print(c, end='')  # end = ''让print不自动换行

# phrase = "A bird in the hand..."
# for char in phrase:
#     if char == "A" or char == "a":
#         print("X", end='')
#     else:
#         print(char, end='')

# 带下标的for循环
# help(enumerate)
# help(zip)
# choices = ['披萨', '沙拉', '可乐', '薯条']
# print("菜单：")
# for index, item in enumerate(choices):  # 内置函数，列举的意思，可直接打印下标
#     print(index, item)  # 0 披萨
#     print(type(index), type(item))   # <class 'int'> <class 'str'>
#
# for item in enumerate(choices, start=1):
#     print(item)   # (1, '披萨')
#     print(type(item))  # <class 'tuple'>

# 同时对多个列表for循环
# 使用内置函数zip实现，zip会把两个列表里相同下标的元素组成一组，然后遍历会再较短的列表结束时结束
# list_a = [3, 9, 17, 15, 19]
# list_b = [2, 4, 8, 10, 30, 40, 50, 60, 80, 90]
# list_c = [1, 5, 9, 22]
# for a, b, c in zip(list_a, list_b, list_c):
#     print(min(a, b, c))


