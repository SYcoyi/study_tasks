# 10.010 操作符in
# my_dict = {'Python': 1, 'English': 2, 'ChildCare': 3}
# print(my_dict.items())
# print(my_dict.keys())
# print(my_dict.values())
#
# # for num in range(5):
# #     print(num)
# #
# # d = {'name': 'Eric', 'age': 27}
# # for key in d:
# #     print(key, d[key])
# #
# # for letter in 'Eric':
# #     print(letter)
#
# for key in my_dict:
#     print(key, my_dict[key], end=' ')

# 10.020 构建列表
# my_list = range(50)
# evens_to_50 = [i for i in range(51) if i % 2 == 0]
# print(evens_to_50)
# new_list = [x for x in range(1, 6)]
# print(new_list)
# new_list = [x * 2 for x in range(1, 6)]
# print(new_list)
# new_list = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# print(new_list)

# 任务1
# even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]
# print(even_squares)
# c = ['Copy' for x in range(5) if x < 3]
# print(c)   # ['Copy', 'Copy', 'Copy']
#
# # 任务2
# cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
# print(cubes_by_four)

# 10.030 带步长的切片
# 步长为正数，表示从start开始向后计算步长
# 步长为负数，从end-1开始向前计算步长
# list_a = [i ** 2 for i in range(1, 11)]
# print(list_a)
# print(list_a[2:9:2])   # [start:end:stride]  前含后不含，步长  等差数列：第二个元素的下标= 第一个元素的下标+步长
# print(list_a[2:9:4])
#
# to_five = ['A', 'B', 'C', 'D', 'E']
# print(to_five[3:])  # ['D', 'E']
# print(to_five[:2])  # ['A', 'B']
# print(to_five[::2])  # ['A', 'C', 'E']
#
# # 倒序输出的方法1
# print("to_five[::-1]: ", to_five[::-1])   # ['E', 'D', 'C', 'B', 'A']    倒序输出了
#
# # 倒序输出的方法2
# to_five = ['A', 'B', 'C', 'D', 'E']
# to_five.reverse()
# print("to_five.reverse(): ", to_five)
#
# # 倒序输出的方法3
# to_five = ['A', 'B', 'C', 'D', 'E']
# print("list((reversed(to_five))): ", list((reversed(to_five))))
#
# # 任务3
# my_list = [x for x in range(1, 11)]
# print(my_list[::2])    # [1, 3, 5, 7, 9]
# print(my_list[::-2])   # [10, 8, 6, 4, 2]
# print(my_list[::-1])
#
# # 任务4
# to_one_hundred = range(101)
# hundred_list = [i for i in range(101)]
# print(hundred_list[::-10])
#
# # 任务5
# to_21 = [x for x in range(1, 22)]
# print(to_21)
# odds = to_21[::2]
# print(odds)
# to_21_3pics = int(len(to_21) / 3)
# print(to_21_3pics)
# middle_third = to_21[to_21_3pics - 1:to_21_3pics + 7:]
# print(middle_third)

# # 匿名函数 lambda
# my_list = range(16)
# print(list(filter(lambda x: x % 3 == 0, my_list)))  # filter 返回的是迭代器，所以需要加list来转换类型
#
# languages = ['HTML', 'JavaScript', 'Python', 'Ruby']
# print(list(filter(lambda x: x == 'Python', languages)))
#
# squares = [i ** 2 for i in range(1, 11)]
# print(list(filter(lambda x: 30 <= x <= 70, squares)))


# 11.010 类
# class Square(object):
#     def __init__(self):
#         self.sides = 4
#
#
# my_shape = Square()  # 创建了一个Square类的对象，并将其存放在变量my_shape中。这个对象也叫做Square的一个实例
# print(my_shape.sides)


# class Animal(object):  # class NewClass(object): 类名一般以大写字母开始，括号内的object代表NewClass类继承自这个父类
#     def __init__(self, name, age, is_hungry):  # 初始化方法__init__，该方法带的第一个参数必须是self。因为self以后会用来代表这个类创建出来的对象
#         self.name = name  # 第二个参数为name，然后给创建的对象添加一个name。name的值取自参数传递过来的name值
#         self.age = age
#         self.is_hungry = is_hungry
#
#
# zebra = Animal('Jeffrey', 2, True)
# giraffe = Animal('Bruce', 1, False)
# panda = Animal('Chad', 7, True)     # 三个对象里都有name，age，is_hungry这三个类的属性。但是不同对象之间不会共享对象里属性的值
# print(zebra.name, zebra.age, zebra.is_hungry)
# print(giraffe.name, giraffe.age, giraffe.is_hungry)
# print(panda.name, panda.age, panda.is_hungry)

# 11.030 类的变量类型
# class Animal(object):
#     is_alive = True  # 这是一个类变量
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# print(Animal.is_alive)
# zebra = Animal('Jeffrey', 2)
# giraffe = Animal('Bruce', 1)
# panda = Animal('Chad', 7)
# print(zebra.is_alive)
# print(giraffe.is_alive)
# print(panda.is_alive)
#
# zebra.is_alive = False   # 修改其中一个对象名.类变量名时，不会影响其他对象里的这个变量的值
# print(zebra.is_alive)
# print(giraffe.is_alive)
# print(panda.is_alive)
#
# Animal.is_alive = False  # 一旦修改 类名.类变量名 的值，则所有对象的这个变量的值都被改变了
# print(zebra.is_alive)
# print(giraffe.is_alive)
# print(panda.is_alive)

# 类的方法
# class Animal(object):
#     is_alive = True  # 这是一个类变量
#     health = 'Good'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         print(self.name, end=' ')
#         print(self.age)
#
#
# hippo = Animal('Jack', 3)
# sloth = Animal('Coco', 1)
# ocelot = Animal('Tiger', 2.5)
# hippo.description()
# print(hippo.health)
# print(sloth.health)
# print(ocelot.health)


# class ShoppingCart(object):
#     def __init__(self, customer_name):
#         self.customer_name = customer_name
#         self.items_in_cart = {}
#
#     def add_item(self, product, price):
#         if product not in self.items_in_cart:
#             self.items_in_cart[product] = price
#             print("{}加入了购物车".format(product))
#         else:
#             print("{}本来就在购物车里".format(product))
#
#     def remove_item(self, product):
#         if product in self.items_in_cart:
#             del self.items_in_cart[product]
#             print("{}被移出了购物车".format(product))
#         else:
#             print("{}不在购物车里".format(product))
#
#
# my_cart = ShoppingCart('Coyi')
# my_cart.add_item('Pen', 22)
# my_cart.add_item('Pencil', 3)
# print(my_cart.items_in_cart)
# my_cart.remove_item('pen')
# my_cart.remove_item("Pen")
# print(my_cart.items_in_cart)

# 类的继承
# class Customer(object):
#     def __init__(self, customer_id):
#         self.customer_id = customer_id
#
#     def display_cart(self):
#         print("购物车中有以下商品：XXXX，XXXX")
#
#
# class ReturningCustomer(Customer):
#     def display_order_history(self):
#         print("历史订单有：1.XXX 2.XXX")
#
#
# monty_python = ReturningCustomer('ID: 123456')
# monty_python.display_cart()
# monty_python.display_order_history()

# class Shape(object):
#     def __init__(self, number_of_sides):
#         self.number_of_sides = number_of_sides
#
#
# class Triangle(Shape):
#     def __init__(self, side1, side2, side3, number_of_sides):
#         super().__init__(number_of_sides)    # 父类调用，PEP8规范中
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3

# 方法重写
# class Employee(object):
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self, other):
#         print("Hello，%s" % other.name)
#
#
# class BOSS(Employee):
#     def greet(self, other):    # 子类里重新改写了父类的greet方法，调用时直接用子类的方法
#         print("去干活儿！，%s" % other.name)
#
#
#
# boss_name = BOSS('比尔')
# emp = Employee('小明')
# emp.greet(boss_name)
# boss_name.greet(boss_name)

# 任务3  方法重写override
# class Employee(object):
#     def __init__(self, employee_name):
#         self.hours = None
#         self.employee_name = employee_name
#
#     def calculate_wage(self, hours):
#         self.hours = hours
#         return hours * 100.00
#
#
# class PartTimeEmployee(Employee):
#     def calculate_wage(self, hours):
#         self.hours = hours
#         return hours * 40.00
#
#
# name = Employee('Bill')   # 创建这个类的实例时，就默认把init里面的变量值给附上去了
# print(name.employee_name, name.hours)
# print(name.calculate_wage(2))     # 调用时只需要传入该方法需要的变量值即可
# part_time_name = PartTimeEmployee('Json')
# print(part_time_name.calculate_wage(2))

# 方法重写后想要访问父类的方法
# class Base(object):
#     def m(self):
#         return "父类的方法调用结果"
#
#
# class Derived(Base):
#     def m(self):
#         return super(Derived, self).m() + " 子类的计算结果"  # 写法如此
#
#
# d = Derived()
# print(d.m())  # 父类的方法调用结果 子类的计算结果

# 任务4
class Employee(object):
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)


#
#
# milton = PartTimeEmployee('milton')
# print(milton.full_time_wage(10))

# 类的复习---重难点！
# class Triangle(object):
#     number_of_sides = 3
#
#     def __init__(self, angle1, angle2, angle3):
#         self.angle1 = angle1
#         self.angle2 = angle2
#         self.angle3 = angle3
#
#     def check_angles(self):
#         if self.angle1 + self.angle2 + self.angle3 == 180:
#             return True
#         else:
#             return False
#
#
# class Equilateral(Triangle):
#     angle = 60
#
#     def __init__(self):
#         self.angle1 = self.angle   # 将子类中的angle值赋给父类中的angle1
#         self.angle2 = self.angle
#         self.angle3 = self.angle
#
#
# my_triangle = Triangle(90, 30, 60)
# print(my_triangle.number_of_sides)
# print(my_triangle.check_angles())
# my_equilateral = Equilateral(90, 60, 30)
# print(my_equilateral.angle1)

