# 列表和字典
# 5.010 初识列表
# empty_list = []
# print(breakfast[1])

# numbers = [5, 6, 1, 2]
# numbers_sum1 = numbers[1] + numbers[3]
# numbers_sum2 = sum((numbers[1], numbers[3]))
# print(numbers_sum1)
# print(numbers_sum2)
#
# breakfast = ["鸡蛋", "面包", "牛奶"]
# breakfast[1] = "三明治"
# print(breakfast)

# letters = ['a', 'b', 'c']
# print("{}的长度为{}".format(letters, len(letters)))
# letters.append('d')
# print("{}的长度为{}".format(letters, len(letters)))

# suitcase = []
# suitcase.append("眼镜")  # 每次只能加一个
# suitcase.append("化妆盒")
# list_length = len(suitcase)
# print("手提箱里有{}件东西,分别是：".format(list_length))
# print(suitcase)

# letters = ['a', 'b', 'c', 'd', 'e']
# slice = letters[1:3]   # 前取后不取
# print(slice)
# print(letters)

# 列表和字符串的切片
# suitcase = ['1_glasses', '2_cloths', '3_markup', '4_money', '5_keys', '6_shoes']
# first = suitcase[0:2]
# print(first)
# middle = suitcase[2:4]
# print(middle)
# last = suitcase[4:6]
# print(last)
#
# print(suitcase[2:])
# print(suitcase[:4])
# first_half = suitcase[:3]
# second_half = suitcase[3:]
# print(first_half)
# print(second_half)
# print(suitcase[:-3])
# print(suitcase[-3:])
#
# letter = "123456"
# print(letter[:3])
# print(letter[3:])
# print(letter[:-3])
# print(letter[-3:])

# # 5.040 插入元素
# animals = ["猫", "狗", "兔", 1, ("a", "b")]
# print(animals.index("狗"))
# animals.insert(1, "鸟")  # 将插入的元素放在这个index位置上
# print(animals)
#
# for variable in animals:
#     print(variable)
#     print(type(variable))

# my_list = [1, 2, 3, 4, 5]
# for num in my_list:
#     print(num * 2)

# 排序
# animals = ['dog', 'cat', 'pig']
# animals.sort()   # 会改变原值  .号调用，为列表专属方法
# for animal in animals:
#     print(animal)
# print(animals)
#
# animals = ['dog', 'cat', 'pig']
# print(sorted(animals))  # 不会改变原值 直接调用说明①sorted是一个内建方法，②sorted能接受的数据类型不止列表
# print(animals)

# start_list = [5, 3, 4, 1, 2]
# square_list = []
# for num in start_list:
#     square_list.append(num ** 2)
#
#
# print(sorted(square_list))  # 此处排序不可以用.sort()  因为.sort是用的英文字母开头来排序的
#


# 5.070 字典
# d = {'key1': 1, 'key2': 2, 'key3': 3}
# print(d['key2'])

# phone_numbers = {"小红": 13788889999, "小红": 15488883333, "小韩": 18900001111}
# print(phone_numbers['小红'])  # key不可以相同，若相同则有一个取不到
# print(phone_numbers['小韩'])
# phone_numbers["小元"] = 15788883333
# print(phone_numbers)

# d = {}
# d['cat'] = '老虎'
# d['pig'] = '猪猪'
# d['dog'] = '狗狗'
# print(d)

# menu = {}
# menu['蟹粉小笼'] = 49.5
# print(menu)
# menu['糖醋里脊'] = 30.3
# menu['锅包肉'] = 35.5
# print("菜单一共有{}道菜".format(len(menu)))
# menu['糖醋里脊'] = 20
# print(menu)
# del menu['蟹粉小笼']
# print(menu)

# colors = ['a', 'b', 'c', 'c', 'd']
# del colors[1]  # 列表用del是下标名
# print(colors)
# colors.remove('c')  # 删除的第一个指定的重复的元素
# print(colors)

# d = {"foo": "bar", "foo2": "bar2"}
# for key in d:  # 用字典d的key组成了一个列表["foo", "foo2"]
#     print(d[key])   # 打印出的value
# for key, value in d.items():  # 可直接打印出键值对
#     print(key)
#     print(value)

# webster = {
#     "Aardvark": "A star of a popular children's show",
#     "Baa": "The sound a goat makes",
#     "Carpet": "Goes on the floor",
#     "Dab": "A small I amount."
#            }
# for key in webster:
#     print(webster[key])

# 5.100 练习
# inventory = {
#     '零钱': 500,
#     '小口袋': ['小刀', '绳子', '手套'],
#     '大口袋': ['帐篷', '水杯', '睡袋', '毛巾']
# }
# inventory['零食'] = ['苹果', '面包', '牛奶']
# print(inventory)
# inventory['大口袋'].sort()
# print(inventory)
# inventory['零钱'] += 50
# print(inventory)

# names = ["Adam", "Alex", "Mariah", "Martine", "Columbus"]
# for name in names:
#     print(name)

# import keyword
# print("Python中的保留字共有{}个，他们是：{}".format(len(keyword.kwlist), keyword.kwlist))

# a = [1, 3, 4, 8, 7]
# for number in a:
#     if number % 2 == 0:
#         print(number)

# numbers = range(1, 101)  # 打印出的是str
# for num in numbers:
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# 5.110 列表加方法
# def count_small(numbers):
#     total = 0
#     for n in numbers:
#         if n < 10:
#             print(n)
#             total = total + 1
#     return total
#
#
# numbers_list = [4, 5, 12, 44, 45]
# small = count_small(numbers_list)
# print(small)

# # 任务5
# numbers1 = range(1, 101)  # 打印出的是列表
# numbers_list = []
# for number in numbers1:
#     if number % 3 == 0 and number % 5 == 0:
#         numbers_list.append("FizzBuzz")
#     elif number % 3 == 0:
#         numbers_list.append("Fizz")
#     elif number % 5 == 0:
#         numbers_list.append("Buzz")
#     else:
#         numbers_list.append(number)
# print(numbers_list)
#
#
# def fizz_count(x):
#     count = 0
#     for n in x:
#         if n == "Fizz":
#             count += 1
#     return count
#
#
# r = fizz_count(numbers_list)
# print(r)

# 任务6
# for letter in "testup测试进阶":
#     print(letter)
#     print()
#
# word = "Programming is fun!"
# for letter in word:
#     if letter == "i":
#         print(letter)
#