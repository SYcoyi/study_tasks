from datetime import datetime

# print("单双引号混用')
# #SyntaxError: unterminated string literal
# EOL  end of line
# ^  符号提示错误位置
# 中文尚无通用名称，可以是乘方、插入符号、插入符、脱字符号等；英文称为caret (英语发音：/ˈkærət/)，是个倒 V 形的字素。
#
#
# print(未用引号)
# # NameError: name '未用引号' is not defined
# 遇到没有引号的东西时，就会理解为是类似于print一样的功能或者方法，所以就回去查找这个函数的定义，但发现没有所以就会报错未定义
#
# print 无括号
# print"无括号"
# # SyntaxError: Missing parentheses in call to 'print'

# 1.100作业
# book1 = 30 * 0.8
# book2 = 45 * 0.6
# fee = 10
# bookTotalPrice = book1 + book2 + fee
# print(bookTotalPrice)

# 1.120作业
# pen = int(1)
# print(pen)
# price = float(4.25)
# total_cost = pen * price
# print(total_cost)
# print(type(total_cost))

# haiku = """The old pond
# A frog jumps in:
# Plop!
# """
# print(haiku)

##结果均为True
# print(1 == True)
# print(0 == False)


# star = True
# moon = False
# print(1 == star)
# print(0 == moon)
# print(2 == True)
# print(3 == False)

# number_7 = 7
# print(number_7)
# str_8 = str(number_7+1)
# print(str_8)
# print(type(str_8))
# number_8 = int(str_8)
# print(number_8)


# 1.150作业
# float_1 = 0.25
# float_2 = 40.0
# product = 1
# print(type(product))
# product = float_1 * float_2
# print(product)
# print(type(product))
#
# big_string = "The product was "
# big_string += str(product)
# print(big_string)


# # 复习
# skill_completed = "Python Syntax"
# case_study = 13
# points_per_case = 5
# """
# points_per_case: 每个小节的分值
# """
# point_total = 100
#
# point_total += case_study*points_per_case
#
# print("I got " + str(point_total) + " points!")


# 任务7、8、9
# startTime_hour = 6
# startTime_minutes = 32
# run_slow_time = 6/1
# run_fast_time = 0.5/3
# run_totalTime = run_slow_time + run_fast_time
# endTime = startTime_minutes + run_totalTime
# print(endTime)
# print("跑完时是早上" + str(startTime_hour) + ":" + str(int(endTime)))
#

# 2.010作业
# str_1 = "This isn't flying,this is falling with style!"
# str_2 = 'This isn\'t flying,this is falling with style!'
# print(str_1 + "\n" + str_2)


# # 2.020作业
# c = "cats"[0]
# n = "Ryan"[3]
#
# monty = "MONTY"
# fifth_letter_1 = monty[4]
# fifth_letter_2 = monty[-1]
# print(fifth_letter_1 + "\n" + fifth_letter_2)


# 字符串的四个方法：str(a) len(a)  a.lower() a.upper()
# 调用方式有的是括号，有的是点号。点号的只能用于字符串
# game = "I like WangZhe!"
# print(game)
# print(len(game))
# print(game.lower())
# print(game.upper())

# pi = 3.14
# print(str(pi))


# 2.040 字符串拼接
# 大括号{}为占位符
# python3推荐第二种
# print("Good " + "good " + "study!")
# print("{} {} {}!".format("Good", "good", "study"))
# print("{2} {1} {0}!".format("Good", "good", "study"))

# print("煎饼" + "果子")
# print("{}{}".format("煎饼", "果子"))
# print("我每顿吃" + str(2) + "个包子")
# 下面这里的2没有加引号，因为format格式会自动将int转为str
# print("{}{}{}".format("我每顿吃", 2, "个包子"))

# {:.4}保留4个字符
# {:.4f}保留4位小数
# print("{:.4}".format("1234.567"))

# print("{:.4f}".format(1234.567899))
# print("{}{:.3f}{}".format("我每顿吃", 2.25678, "个包子"))

# name = input("你叫什么名字？")
# height = input("身高多少？")
# food = input("喜欢吃什么？")
# print(type(height))
# print("你叫{}，身高{}，喜欢吃{}。".format(name, height, food))

# 2.050 复习作业
# my_word = "Coyi"
# print(len(my_word))
# print(my_word.upper())

# str_1 = "+++Hello,I am back.+++"
# print(str_1.center(50, "*"))  # 指定宽度并将指定字符作为占位居中
# print(str_1.strip("+"))   # 去掉前后的指定字符
# print(str_1.find("ello"))  # 打印出第一次出现的下标

# 2.060 时间日期
# from datetime import datetime
now = datetime.now()
# year = now.year
# month = now.month
# day = now.day
# print("现在是{}年{}月{}日".format(year, month, day))

# {:04d}保留两位整数不够则补0
# print("{:4d}-{:02d}-{:02d}".format(now.year, now.month, now.day))
# print("{:02d}/{:02d}/{:4d}".format(now.month, now.day, now.year))

# hour = now.hour
# minute = now.minute
# second = now.second
# print(type(second))
# print("{}:{}:{}".format(hour, minute, second))
# print("{:02d}/{:02d}/{:4d} {}:{}:{}".format(now.month, now.day, now.year, hour, minute, second))
