# 条件分支 3.010
# def choice():
#     print("请选择，左还是右？")
#     answer = input("请输入‘左’ 或者 ‘右’：")
#     if answer == "左" or answer == "左边":
#         print("你选择了左")
#     elif answer == "右" or answer == "右边":
#         print("你选择了右")
#     else:
#         print("你没有做出选择,是否再试一次？")
#
#
# choice()
# choice()


# print(17 < 328)
# bool_two = ((20 - 10)>15)
# bool_three = ((10 + 17) == 3**16)
# bool_four = (1**2 <= -1)
# bool_five = (100 != 10**2)
# print(type(bool_five))
#
# print("\n", bool_two, "\n", bool_three, "\n", bool_four, "\n", bool_five)


# 3.030 布尔表达式：not or and
# bool_one = -(-(-(-2))) == -2 and 4 >= 16**0.5
# print(16**0.5)
# print(bool_one)
# bool_two = 19 % 4 != 300 / 10 / 10 and False  # 两个false为false
# print(bool_two)
# bool_three = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2
# print(2**0)
# print(bool_three)
# bool_five = True and True
# print(bool_five)
#
# bool_1 = 2 ** 3 == 108 % 100 or 'Cleese' == 'King'
# print(bool_1)
# print(True or False)
# print(100 ** 0.5 >= 50 or False)
# print(True or True)
# bool_2 = 1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1
# print(bool_2)
#
# print(not True)
# print(not 3 ** 4 < 4 ** 3)
# print(not 10 % 3 <= 10 % 2)
# print(not 3 ** 2 + 4 ** 2 != 5 ** 2)
# print(not not False)
# print(True or not False and False)  # True


# print(False or not True and True)
# print(False and not True or True)
# print(True and not (False or False))
# print(not not True or False and not True)
# print(False or not (True and True))
#
# bool_1 = not((2 <= 2) and "QQ" == "NN")
# bool_2 = not(22 != 2*11) or len("aa") == 2 and 100 % 5 <= -1
# print(bool_2)

# # 3.040 条件分支
# if 8 < 9:
#     print('right!')
#
# answer = 'left'
# if answer == 'left':
#     print("This is the Verbal Abuse Room!")


# def using_control_once():
#     if 1 > 0:
#         return "Success #1"
#
#
# def using_control_again():
#     if 1 ** 4 != 2:
#         return "Success #2"
#
#
# print(using_control_once())
# print(using_control_again())


# if 8 > 9:
#     print("不会被执行")
# elif 8 < 9:
#     print("执行这里")
# else:
#     print("我也不会被执行")


# def greater_less_equal_5(answer):
#     if answer > 5:
#         return 1
#     elif answer < 5:
#         return -1
#     else:
#         return 0
#
#
# print(greater_less_equal_5(4))
# print(greater_less_equal_5(5))
# print(greater_less_equal_5(6))

# # 3.050复习
# def grade_converter(grade):
#     if grade >= 90:
#         return "优秀"
#     elif 80 <= grade < 90:
#         return "良好"
#     elif 70 <= grade < 79:
#         return "尚可"
#     elif 60 <= grade < 69:
#         return "待改进"
#     else:
#         return "不及格"
#
#
# print(grade_converter(94))
# print(grade_converter(86))
# print(grade_converter(76))
# print(grade_converter(66))
# print(grade_converter(56))

# 3.060 Pig Latin

# def piglatin(word):
#     word_count = len(word) - 1
#     word_new = word[1:word_count] + word[0].lower() + "ay"
#     print(word_new)
#
#
# piglatin('Python')
# check_word(word_start)


# pyg = 'ay'
# original = input("请输入一个英文单词：")
# if len(original) > 0 and original.isalpha():
#     print(original)
#     word = original.lower()
#     first = word[0]
#     new_word = word + first + pyg
#     new_word = new_word[1:len(new_word)]
#     print(new_word)
# else:
#     print("您输入的单词不正确")


