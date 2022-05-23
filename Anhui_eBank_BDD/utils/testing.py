# -*- coding:utf-8 -*-
"""
Created on 2017年11月14日

@author: sheldon
"""
import json

import requests

class DictToStruct:
    def __init__(self, **entries):
        self.__dict__.update(entries)




def send_get():
    params = {
        'abc': '123'
    }
    result = requests.get('https://www.sheldoncoco.com/home/login', params=params)
    result = requests.get('https://www.sheldoncoco.com/home/login/?abc=123')
    print(result.url)
    print(result.text)
    print(result.headers)


if __name__ == '__main__':
    file = open("../http_result/scenario4379216472.json")
    for line in file:
        http_result = eval(line)
        http_result = DictToStruct(**http_result)
        print(http_result.__dict__)
    file.close()
    # class ClsTest1(object):
    #     pass
    #
    #     def hello(self):
    #         print('ClsTest1 hello')
    #
    #
    # class ClsTest2(ClsTest1):
    #     def __init__(self):
    #         print("init")
    #
    #     def __new__(cls, *args, **kwargs):
    #         print("new %s" % cls)
    #         print(id(cls))
    #         print(id(ClsTest2))
    #         return object.__new__(cls, *args, **kwargs)
    #
    #     def hello(self):
    #         print('ClsTest2 hello')
    #
    # b = ClsTest2()
    # print(type(b))
    # b.hello()
