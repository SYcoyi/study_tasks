# -*- coding:utf-8 -*-
"""
Created on 2017年11月14日

@author: sheldon
"""

import random
import time


def regiun():
    '''生成身份证前六位'''
    # 列表里面的都是一些地区的前六位号码
    first_list = ['610101', '610102', '610103', '610104', '610111', '610112', '610113', '610114', '610115', '610116',
                  '610122', '610124', '610125', '610126', '610201', '610202', '610203', '610204', '610222', '610301',
                  '610302', '610303', '610304', '610322', '610323', '610324', '610326', '610327', '610328', '610329', ]
    first = random.choice(first_list)
    return first


def year():
    '''生成年份'''
    now = time.strftime('%Y')
    # 1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
    second = random.randint(1948, int(now) - 18)
    age = int(now) - second
    # print('随机生成的身份证人员年龄为：' + str(age))
    return second


def month():
    '''生成月份'''
    three = random.randint(1, 12)
    # 月份小于10以下，前面加上0填充
    if three < 10:
        three = '0' + str(three)
        return three
    else:
        return three


def day():
    '''生成日期'''
    four = random.randint(1, 31)
    # 日期小于10以下，前面加上0填充
    if four < 10:
        four = '0' + str(four)
        return four
    else:
        return four


def randoms():
    '''生成身份证后四位'''
    # 后面序号低于相应位数，前面加上0填充
    five = random.randint(0, 300)
    if five < 10:
        five = '00' + str(five)
        return five
    elif 10 < five < 100:
        five = '0' + str(five)
        return five
    else:
        return five


def weight(id):
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3',
                 '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
    return checkcode[str(count % 11)]


def IDcard():
    first = regiun()
    second = year()
    three = month()
    four = day()
    five = randoms()
    IDcard = str(first) + str(second) + str(three) + str(four) + str(five)
    IDcard = IDcard + weight(IDcard)
    return IDcard

if __name__ == '__main__':
    now = time.time()
    print(IDcard())
    print(time.time() - now)
