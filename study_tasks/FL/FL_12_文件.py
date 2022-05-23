# 12.010 写文件
"""
文件操作模式：
‘r’: 读
‘w’：写
‘a’：追加  不可读
‘r+’== r + w 可读可写，文件若不存在则报错IOError
‘w+’== w+r 可读可写，文件若不存在就创建
‘a+’ == a + r  可追加可读 文件若不存在就创建
"""
# my_list = [i ** 2 for i in range(1, 11)]
# print(my_list)
# f = open('output.txt', 'w')  # 只有文件名则默认是在脚本所在的当前目录下。w只能写不能读  把打开的文件存放在变量f中
# print(type(f))
# for item in my_list:
#     f.write(str(item) + '\n')
# f.close()
#
# my_file = open('output.txt', 'r+')   # r+ 既可以读又可以写
# print(my_file)
# my_file.write('我是写入文件的字符串')
# my_file.close()

# 任务2
# my_list = [i ** 2 for i in range(1, 11)]
# my_file = open('output.txt', 'w')
# for item in my_list:
#     my_file.write(str(item) + '\n')    # 数字须转换成str后才可以写入文件
# my_file.close()

# my_list = [i ** 2 for i in range(1, 11)]
# my_file = open('output.txt', 'a')    # 为追加
# for item in my_list:
#     my_file.write(str(item) + '\n')
# my_file.close()

# my_list = [i ** 2 for i in range(1, 11)]
# my_file = open('output.txt', 'r')    # 为追加
# print(my_file.read())   # 一次性读取整个文件
# my_file.close()

# my_file = open('text.txt', 'r', encoding='utf-8')
# print(my_file.readline())   # 一次只能读取一行
# print(my_file.readline())
# print(my_file.readline())
# my_file.close()

# write_file = open('text.txt', 'w')
# read_file = open('text.txt', 'r')
# write_file.write('文件不关闭会有问题')
# # write_file.close()
# print(read_file.read())

# 用with读写文件
# 该方式打开文件后，在with内语句执行完毕后，会自动执行文件对象的__exit__方法，也就是说会自动关闭打开的文件
# 语法：with open('文件路径', '模式') as 变量:
# with open('text.txt', 'w') as my_file:  # ‘r’操作是对as后的变量做的
#     my_file.write("Success!")
#     # if not my_file.closed:
#     #     my_file.close()
#
# f = open('text.txt')
# print(f.closed)  # 查看文件是否关闭，关闭返回True，未关闭返回False
# f.close()
# print(f.closed)
