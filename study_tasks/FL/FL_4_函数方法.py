# # 4.010 函数
# def coupon(original_price):
#     """
#     满80减20    ----简单描述
#     :param original_price: 原价  ----参数名及含义
#     :return: 折后价  ---返回值描述
#     """
#     new_price = original_price - int(original_price / 80) * 20
#     print("您选择的满减，折后价为：{}".format(new_price))
#     return new_price
#
#
# def discount(original_price):
#     """
#     打85折
#     :param original_price: 原价
#     :return: 折后价
#     """
#     new_price = original_price * 0.85
#     print("您选择的直接打折，折后价为：{}".format(new_price))
#     return new_price
#
#
# original_price = 159
# price_coupon = coupon(original_price)  # 变量名 = 方法名（参数表）
# price_discount = discount(original_price)

# def cook():
#     """
#     just for demo
#     :return: none
#     """
#     print("🍅+🥚")
#
#
# cook()


# def square(n):
#     """
#     计算一个数的平方
#     :param n: 用来计算的数字
#     :return: 返回该数字的平方值。注：print不是return,不会给出返回值
#     """
#     squared = n ** 2
#     # print("{}的平方是{}".format(n, squared))
#     return squared
#
#
# my_number_squared = square(3.333)   # 将返回值保存在了变量里
# print(my_number_squared)
# print(square(30))    # 直接使用了返回值，未保存在变量里


# # 4.040 参数表和传入值
# def power(base, exponent):
#     result = base ** exponent
#     print("{}的{}次方等于{}".format(base, exponent, result))
#
#
# power(35, 3)


# # 方法调用方法
# def fun_one(n):
#     return n + 1
#
#
# def fun_two(n):
#     return fun_one(n) + 1


# def fun(n):
#     if n % 3 == 0:
#         return n ** 3
#     else:
#         return False
#
#
# print(fun(3))
# print(fun(4))


# def cube(n):
#     """
#     计算立方
#     :param n:
#     :return: 返回立方
#     """
#     return n ** 3
#
#
# def test_three(n):
#     """
#     调用并返回n的立方
#     :param n:
#     :return:
#     """
#     if n % 3 == 0:
#         return cube(n)
#     else:
#         return False
#
#
# print(test_three(5))
# print(test_three(3))
# print(test_three(3.3))

# 4.070 模块的导入
# import math  # 导入整个库，调用时需引用
# print(math.sqrt(25))

# from math import sqrt  #导入单独某个函数，调用时可不用再引用
# print(sqrt(25))

# from math import *   # 导入所有方法，不建议使用。可能引起模块内方法重名
# print(sqrt(25))

# import math
# everything = dir(math)  # 列出该库中所有函数
# print(everything)

# 内建函数
# def biggest_number(*args):  # 一个* 代表类型为元祖，**为字典
#     print(max(args))
#     print(type(args))
#     return max(args)
#
#
# def smallest_number(*args):
#     print(min(args))
#     return min(args)
#
#
# def distance_from_zero(arg):  # 绝对值
#     print(abs(arg))
#     return abs(arg)
#
#
# biggest_number(-10, -6, 5, 55, 555)
# smallest_number(-10, -6, 5, 55)
# distance_from_zero(-10)

# help(abs(1))  # 获取该方法的介绍

# import random
#
# num = random.choice(range(10))  # 从0-9中随机挑选一个数
# print(num)

# 4.090 练习
# def shut_down(s):
#     """
#     练习题
#     :param s:
#     :return:
#     """
#     if s == "yes":
#         return "关闭执行中"
#     elif s == "no":
#         return "已取消关闭操作"
#     else:
#         return "对不起，无法执行"
#
#
# print(shut_down('yes'))
# print(shut_down("no"))
# print(shut_down("yes?"))

# from math import sqrt
# r = sqrt(13689)
# print(r)


# def distance_from_zero(m):
#     if type(m) == int or type(m) == float:
#         return abs(m)
#     else:
#         return "算了"
#
#
#
#
# r1 = distance_from_zero(-22)
# r2 = distance_from_zero(23.333)
# r3 = distance_from_zero("4.444")
# print("{}  {}  {}".format(r1, r2, r3))


# # 4.100 更多的练习---计算旅行费用
# def hotel_cost(nights):
#     """
#     计算住宿费
#     :param nights: 住几晚
#     :return: 住宿所花费费用
#     """
#     return 488 * nights
#
#
# def train_cost(city):
#     """
#     计算高铁费用
#     :param city:城市名字
#     :return: 到达输入的城市所花费的费用
#     """
#     if city == "上海":
#         return 92.5
#     elif city == "南京":
#         return 117.5
#     elif city == "苏州":
#         return 111.5
#     elif city == "西安":
#         return 653.5
#     else:
#         return "无法得知该城市高铁费用"
#
#
# def rent_car_cost(days):
#     """
#     计算租车费用
#     :param days: 租用天数
#     :return: 租车的费用
#     """
#     if days >= 7:
#         return 78 * days - 67
#     elif 3 <= days < 7:
#         return 78 * days - 20
#     else:
#         return 78 * days
#
#
# def trip_cost(city, days, spending_money):
#     """
#     计算旅行总花费
#     :param city: 城市
#     :param days: 旅行天数(注意非住宿天数)
#     :param spending_money: 零花钱
#     :return:
#     """
#     return hotel_cost(days-1) + rent_car_cost(days) + train_cost(city) * 2 + spending_money
#
#
# cost_xian = trip_cost("西安", 5, 3000)
# cost_shanghai = trip_cost("上海", 2, 4000)
# print(cost_xian)
# print(cost_shanghai)
