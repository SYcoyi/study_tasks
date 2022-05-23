# # 6.010 水果店
# prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
# stocks = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
#
#
# def list_fruit(price, stock):
#     """
#     列出所有水果的价格及库存
#     :param price:
#     :param stock:
#     :return:
#     """
#     for key in price:
#         if key in stock:
#             return print("{}\n售价{}\n现有数量{}\n".format(key, price[key], stock[key]))
#
#
# list_fruit(prices, stocks)
#
#
# def total_money(price, stock):
#     """
#     计算所有水果销售后的总价
#     :param price:
#     :param stock:
#     :return:
#     """
#     sum_price = []
#     sum_per_fruit = 0
#     for key in price:
#         if key in stock:
#             sum_per_fruit = price[key] * stock[key]
#             sum_price.append(sum_per_fruit)
#     return sum(sum_price)
#
#
# print(total_money(prices, stocks))
#
# foods = {'banana': 1, 'orange': 1, 'apple': 1}
#
#
# def compute_bill(food, price, stock):
#     """
#     计算购买的水果总价
#     :param food:
#     :param price:
#     :param stock:
#     :return:
#     """
#     price_food = 0
#     sum_price_food = []
#     for key, value in food.items():
#         if value <= stock[key]:
#             price_food = price[key] * value
#             stock[key] -= value
#             sum_price_food.append(price_food)
#         else:
#             price_food = price[key] * stock[key]
#             stock[key] = 0
#             sum_price_food.append(price_food)
#     return sum(sum_price_food)
#
#
# print(compute_bill(foods, prices, stocks))
#

# 算分数
lilei = {"name": "Lilei", "homework": [], "quizzes": [], "tests": []}
hanmeimei = {"name": "Hanmeimei", "homework": [], "quizzes": [], "tests": []}
jim = {"name": "Jim", "homework": [], "quizzes": [], "tests": []}

lilei_homework = [90, 97, 75, 92]
lilei_quizzes = [88, 40, 94]
lilei_testScores = [75, 90]

hanmeimei_homework = [100, 92, 98, 100]
hanmeimei_quizzes = [82, 83, 91]
hanmeimei_testScores = [89, 97]

jim_homework = [0, 87, 75, 22]
jim_quizzes = [0, 75, 78]
jim_testScores = [100, 100]


def list_append(num_list, name_dic, key):
    """
    将列表里的数据添加进字典对应的key中
    :param num_list: 原始数据
    :param name_dic: 学生字典
    :param key: 数据对应字典内的key值
    :return:
    """
    for num in num_list:
        name_dic[key].append(num)


list_append(lilei_homework, lilei, "homework")
list_append(lilei_quizzes, lilei, "quizzes")
list_append(lilei_testScores, lilei, 'tests')
list_append(hanmeimei_homework, hanmeimei, 'homework')
list_append(hanmeimei_quizzes, hanmeimei, 'quizzes')
list_append(hanmeimei_testScores, hanmeimei, 'tests')
list_append(jim_homework, jim, 'homework')
list_append(jim_quizzes, jim, "quizzes")
list_append(jim_testScores, jim, 'tests')

students = [lilei, hanmeimei, jim]
for student in students:
    print("********")
    for key, value in student.items():
        print("{}:{}\n".format(key, value))


def average(numbers):
    """
    计算每一个列表/科目中的平均值
    :param numbers: 类型为列表
    :return:
    """
    total = sum(numbers)
    return total / len(numbers)


def get_average(student):
    """
    学生加上科目权重后的整体的平均值
    :param student: 类型为字典
    :return:个人最终平均分
    """
    score_list = []
    homework = average(student['homework']) * 0.1
    quizzes = average(student['quizzes']) * 0.3
    tests = average(student['tests']) * 0.6
    score_list.append(homework)
    score_list.append(quizzes)
    score_list.append(tests)
    return sum(score_list)


print("Lilei的最终平均分为：{:.2f}".format(get_average(lilei)))
print("Hanmeimei的最终平均分为：{:.2f}".format(get_average(hanmeimei)))
print("Jim的最终平均分为：{:.2f}\n".format(get_average(jim)))


def get_letter_grade(score):
    """
    跟进平均分来划分等级
    :param score: 平均分
    :return: 等级
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print("Lilei的成绩等级为：{}".format(get_letter_grade(get_average(lilei))))
print("Hanmeimei的成绩等级为：{}".format(get_letter_grade(get_average(hanmeimei))))
print("Jim的成绩等级为：{}\n".format(get_letter_grade(get_average(jim))))


def get_class_average(class_list):
    """
    班级平均分
    :param class_list: 列表，含有三个学生成绩的字典
    :return:
    """
    results = []
    for class_list_student in class_list:
        results.append(get_average(class_list_student))
    return average(results)


print("班级的最终平均分为：{:.2f}".format(get_class_average(students)))
