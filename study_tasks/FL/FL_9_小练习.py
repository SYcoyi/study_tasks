# 9.050 小练习
# def is_even(x):
#     """
#     判断是否是偶数
#     :param x:
#     :return: True 、False
#     """
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(is_even(0))
#
#
# def is_int(x):
#     """
#     判断是否为整数
#     :param x:
#     :return:
#     """
#     if type(x) == int:
#         return True
#     elif type(x) == float and x - int(x) == 0:
#         return True
#     else:
#         return False
#
#
# print(is_int(7.0))
#
#
# def digit_sum(n):
#     """
#     正整数的各个位数上求和
#     :param n:
#     :return:
#     """
#     list_n = []
#     if type(n) == int and n > 0:
#         for item in str(n):
#             list_n.append(int(item))
#         return sum(list_n)
#     else:
#         return "输入数据不正确，只可以为正整数"
#
#
# def digit_sum_2(n):
#     """
#     正整数的各个位数上求和
#     :param n:
#     :return:
#     """
#     list_n = []
#     sum_n = 0
#     if type(n) == int and n > 0:
#         for item in str(n):
#             list_n.append(int(item))
#         for i in range(len(list_n)):
#             sum_n = int(list_n[i]) + sum_n
#         return sum_n
#     else:
#         return "输入数据不正确，只可以为正整数"
#
#
# print(digit_sum(12345888))
# print(digit_sum_2(12345888))
#
#
# def factorial(x):
#     """
#     返回该数字的阶乘
#     :param x: 理论上只能为正整数
#     :return: 该数字阶乘即 4！= 4 * 3 *2 *1
#     """
#     total = 1
#     if type(x) == int and x > 0:
#         for i in range(1, x+1):
#             total = total * i
#         return total
#     elif x == 0:
#         return 1
#     else:
#         return "输入数据不正确，只可以为0或正整数"
#
#
# print(factorial(6))


# def is_prime(x):
#     """
#     判断是否为质数。质数：大于1的自然数，除了1和它自身外，不能整除其他自然数。
#     :param x:
#     :return:是否为质数
#     """
#     if type(x) == int and x > 1:
#         if x == 2:
#             return True
#         else:
#             i = 2
#             while i in range(2, x):
#                 if x % i == 0:
#                     return False
#                     break
#                 else:
#                     i += 1
#             return True
#     else:
#         return "您输入的数字不合法，需为大于1的自然数(正整数)"
#
#
# print(is_prime(101))


# def reverse(text):
#     """
#     倒序字符串，含有特殊字符
#     :param text: str
#     :return: 倒序的字符串
#     """
#     text_list = []
#     new_text_list = []
#     for letter in text:
#         text_list.append(letter)
#     for i in range(len(text)):
#         new_text_list.append(text_list[len(text) - 1 - i])
#     return "".join(new_text_list)
#
#
# print(reverse("He is on the tree! \n while she is looking at him."))

# 小练习2
# text = 'Apple'
# print(type(text))
# print(type(1))
# test_list = ['A', 'p', 'p', 'l', 'e']
# vowel = 'aeiou'
# vowel_all = vowel + vowel.upper()
# print(vowel_all[0])
# vowel_all = ['a', 'e', 'i', 'o', 'u']
# # 加for循环
# if 'A' in test_list:
#     test_list.remove('A')
# print(test_list)
# new_str = "".join(test_list)
# print(new_str)


# 任务1
# def anti_vowel(text):
#     vowel = 'aeiou'
#     vowel_all = vowel + vowel.upper()
#     test_list = []
#     if type(text) == str:
#         for letter in text:
#             test_list.append(letter)
#         for vowel_letter in vowel_all:
#             if vowel_letter in test_list:
#                 test_list.remove(vowel_letter)
#         return "".join(test_list)
#     else:
#         return "输入不合法，请输入字符串"
#
#
# print(anti_vowel('Hey You!'))
# print(anti_vowel(222))

# 任务2 Scrabble积分
# score = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1,
#          'd': 2, 'g': 2,
#          'b': 3, 'c': 3, 'm': 3, 'p': 3,
#          'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
#          'k': 5,
#          'j': 8, 'x': 8,
#          'q': 10, 'z': 10}
#
#
# def scrabble_score(word):
#     """
#     英文字母计算分数
#     :param word: 字符串，不考虑特殊字符等
#     :return:得分
#     """
#     score_final = 0
#     for word_letter in word.lower():
#         for key, value in score.items():
#             if key == word_letter:
#                 score_final = score_final + value
#     return score_final
#
#
# print(scrabble_score('Helix'))


# 任务3 屏蔽
# def censor(text, word):
#     """
#     隐藏text内的word
#     :param text:
#     :param word:
#     :return: word长度的隐藏后的text
#     """
#     text_list = text.split(' ')
#     for i in range(len(text_list)):
#         if word == text_list[i]:
#             text_list[i] = "*" * len(word)
#     return " ".join(text_list)
#
#
# word = 'hack'
# text = 'this hack is wack hack'
# print(censor(text, word))


# 任务4
# item_int = 1
# item_float = 1.1
# item_str = 'str'
# item_list = [list]
# sequence = [[1], 1.1, "str", 1, 1, 1]
# print(item_list == sequence[0])
#
#
# def count(sequence, item):
#     """
#     计算item在列表sequence中出现的次数
#     :param sequence: list
#     :param item: 被计算次数的数据，可为int str float list
#     :return: 出现的次数
#     """
#     total = 0
#     for i in range(len(sequence)):
#         if item == sequence[i]:
#             total += 1
#     return total
#
#
# sequence = [[1], 1.1, "str", 1, 1, 1]
# print(count(sequence, 's'))

# 任务5
# def purify(numbers):
#     """
#     删除其中的所有奇数
#     :param numbers:只有整数的list
#     :return: 删除后的新列表
#     """
#     purified_nums = []
#     for num in numbers:
#         if num % 2 == 0:
#             purified_nums.append(num)
#     return purified_nums
#
#
# numbers = [-1, -4, 1, 2, 3, 4]
# print(purify(numbers))

# 任务6
# def product(numbers):
#     """
#     返回传入列表中所有元素的乘积 即[1, 2, 3] 返回1 * 2 * 3的结果6
#     :param numbers: 整数list
#     :return: 所有元素的乘积
#     """
#     result = 1
#     if len(numbers) != 0:
#         for num in numbers:
#             result = result * num
#         return result
#     else:
#         return "列表不能为空！"
#
#
# numbers = [-1, -4, 1, 2, 3, 4]
# print(product(numbers))

# 任务7
# def remove_duplicates(s):
#     """
#     删除列表中重复的元素
#     :param s: 列表
#     :return: 重复元素去除后的新列表
#     """
#     new_s = []
#     for s_letter in s:
#         if s_letter not in new_s:
#             new_s.append(s_letter)
#     return new_s
#
#
# numbers = [-1, '-4', '-4', 2, 3, -4]
# print(remove_duplicates(numbers))

# 任务8
# num_list = [1, 1, 2, 5, 4]
# num_sorted = sorted(num_list)
# print(num_sorted)
# mid_index = len(num_list) // 2
# print(num_sorted[mid_index])
#
#
# def median(x):
#     """
#     取列表中的中间数，若列表长为偶数，则取中间两数的平均值
#     :param x:列表
#     :return: 中间数/中间两数平均值
#     """
#     x_sorted = sorted(x)
#     mid_index = len(x) // 2  # 取出中间数的下标
#     result_even = 0
#     if len(x) % 2 != 0:
#         return x_sorted[mid_index]
#     else:
#         result_even = (x_sorted[mid_index - 1] + x_sorted[mid_index]) / 2
#         return result_even
#
#
# print(median(num_list))
