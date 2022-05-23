# -*- coding:utf-8 -*-
"""
Created on 2017年11月14日

@author: sheldon
"""


class switch(object):
    def __init__(self, value):
        self.value = value.strip().lower()
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, args):
        if self.fall or not args.strip().lower():
            return True
        elif self.value.strip().lower() in args.strip().lower():
            self.fall = True
            return True
        else:
            return False
