# # 复习列表
# n = [1, 3, 5]
# print(n[1])
# n[1] = n[1] * 5
# print(n)
# n.append(4)
# print(n)
# n.remove(n[0])
# print(n)
# del n[0]  # 按照值来删除
# print(n)
# print(n.pop(0))  # 按照index位置来删除
# print(n)

# 复习方法
# number = 5
#
#
# def my_function(x):
#     return x * 3
#
#
# print(my_function(number))
#
# m = 5
# n = 3
#
#
# def add_function(m, n):
#     return sum((m, n))
#
#
# print(add_function(m, n))
#
# n = "hello"
#
#
# def string_function(s):
#     return s + "word"
#
#
# print(string_function(n))
#
#
# def list_function(x):
#     x[1] += 3
#     return x
#
#
# n = [3, 5, 7]
# print(list_function(n))
#
#
# # 列表+方法
# def first_item(items):
#     print(items[0])
#
#
# numbers = [2, 7, 9]
# first_item(numbers)

#
# def double_first(n):
#     n[0] = n[0] * 2
#     # return n[0]
#
#
# numbers = [1, 2, 3, 4]
# double_first(numbers)
# print(numbers)


# def list_extender(lst):
#     lst.append(9)
#     return lst
#
#
# n = [3, 5, 7]
# print(list_extender(n))


# def print_list(x):
#     for i in x:
#         print(i)
#
#
# n = [3, 5, 7]
# print_list(n)


# def double_list(x):
#     new_x = []
#     for i in x:
#         new_x.append(i * 2)
#     return new_x
#
#
# n = [3, 5, 7]
# print(double_list(n))

# 列表+方法练习2
# print(list(range(6)))   # range(stop)
# print(list(range(1, 6)))  # range(start, stop)
# print(list(range(1, 6, 3)))  # range(start, stop, step)  step即步长，默认为1/增量值/每个元素间的间隔
# print(list(range(10, 1, -3)))  # range(start, stop, step)  即步长/减量值
#
#
# def my_function(x):
#     y = []
#     for i in range(1, len(x)):
#         y.append(x[i])
#     return y
#
#
# print(my_function(range(5)))
# print(my_function(range(1, 10, 2)))

# 遍历列表的两种方法
# for item in list:    # 通过in遍历 可直接简单的遍历这个列表，但是不能遍历时修改这个列表
#     print(item)
#
# for i in range(len(list)):  # 通过下标来遍历  可遍历的同时对列表内元素进行修改
#     print(list[i])


# def total(numbers):
#     """
#     两种方法求列表内各元素的和
#     :param numbers:
#     :return: 返回和
#     """
#     result = 0
#     # for num in numbers:
#     #     result = result + num
#     # return result
#     for i in range(len(numbers)):
#         result = result + numbers[i]
#     return result
#
#
# n = [3, 5, 7]
# print(total(n))
# print(sum(n))

# def join_strings(words):
#     """
#     将列表内的字符串拼接
#     :param words:  list
#     :return:
#     """
#     result = ''
#     # for letter in words:
#     #     result = result + letter
#     # return result
#     for i in range(len(words)):
#         result = result + words[i]
#     return result
#
#
# n = ['Michael', 'Lieberman']
# print(join_strings(n))

# 列表+方法练习3
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)
#
#
# def join_lists(x, y):
#     """
#     用于连接列表
#     :param x:  list
#     :param y:  list
#     :return: 连接后的列表
#     """
#     return x + y
#
#
# print(join_lists(a, b))

# list_of_lists = [[1, 2, 3], [4, 5, 6]]
# for lst in list_of_lists:
#     for item in lst:
#         print(item)

def flatten(lists):
    """
    连接列表内所有子列表
    :param lists: 列表
    :return: 连接子列表后的列表
    """
    results = []
    # for numbers in lists:
    #     for num in numbers:
    #         results.append(num)
    # return results


list_of_lists = [[1, 2, 3], [4, 5, 6, 7, 8]]
print(flatten(list_of_lists))
print(list_of_lists[0] + list_of_lists[1])



