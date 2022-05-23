"""
练习--战船
print(["O"] * 5)  # 用*可以复制

letters = ['a', 'b', 'c', 'd']
print('---'.join(letters))   # a---b---c---d   join的用法

from random import randint
coin = randint(0, 1)  # 结果有 0 和 1
dice = randint(1, 6)

if x not in range(8) or y not in range(3):  #超出范围
    print("超出了范围")

"""
from random import randint

board = []
for i in range(5):
    board.append(["O"] * 5)
# print("原始地图board为：{}".format(board))


def print_board(board_in):
    """
    打印成所需要的地图样子
    :param board_in: 原始地图列表的列表
    :return: 地图的样子
    """
    for row in board_in:
        print("   ".join(row))


print_board(board)


def random_row(board_in):
    """
    返回一个坐标-行/列
    :param board_in: type为list
    :return: 0到n的随机数
    """
    return randint(0, len(board_in) - 1)


def random_col(board_in):
    """
    返回一个坐标-行/列
    :param board_in: type为list
    :return: 0到n的随机数
    """
    return randint(0, len(board_in) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print("Turn", turn + 1)
    guess_row = int(input("猜一下船在第几行："))
    guess_col = int(input("猜一下船在第几列："))

    if guess_row == ship_row and guess_col == ship_col:
        print("恭喜你，击沉了战船！")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("输入的行/列超出范围")
        elif board[guess_row][guess_col] == 'X':
            print("您已经猜过这个{}行{}列了".format(guess_row, guess_col))
        else:
            print("很遗憾，战船未击沉")

    if guess_row in range(5) and guess_col in range(5):
        board[guess_row][guess_col] = 'X'
        print_board(board)

    if turn == 3:
        print("Game Over")
