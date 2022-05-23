# -*- coding:utf-8 -*-
"""
Created on 2019年04月09日

@author: sheldon
"""
import random
import math
import uuid

from utils.basicSwitch import switch
from utils.generatorId import IDcard


class RandomBar(object):
    """
    随机数生成器工具类
    """

    """
        ---------------随机数---------------
        gb = RandomBar()
        gb.getRandomFloat() 随机产生一个[0,1)的浮点数
        gb.getRandomBetweenFloat(start, stop) 随机产生一个a、b区间的浮点数
        gb.getRandomBetweenInt(start, stop=None, step=1) 随机产生一个a、b-1区间的整数:[a,b)
        gb.getRandomObject(self, population, k=1) 从population数组中随机挑选k个值（重复挑选）
        gb.getRandomObjectSimple(population, k=1) 从population数组中随机挑选k个值（不会重复挑选）
        gb.makeRandomShuffle(deck) 将数组中的对象打乱顺序
        ---------------随机对象---------------
        RandomBar.getRandomId() 获取一个随机身份证号
        ---------------UUID---------------
        RandomBar.getUUID(type=1, namespace=uuid.NAMESPACE_URL, name="defauleUUID") 获取一个1类、3类、4类、5类的UUID
    """

    def __randomSeed(self, a, version):
        """
        随机种子
        :param seedNumInt:
        :return: 当前GeneratorBar
        """
        random.seed(a=a, version=version)
        return self

    def __getRandomState(self):
        """
        返回当前随机状态，可用于恢复状态
        :return:
        """
        return random.getstate()

    def __setRandomState(self, state):
        """
        恢复随机状态
        :return:
        """
        random.setstate(state)

    def getRandomFloat(self, seedNumInt=None):
        """
        随机产生一个[0,1)的浮点数
        :param seedNumInt:传入的seedNumInt为随机种子，该值可以保证使用相同的种子碰撞出最终值，使最终值相同
        :return:
        """
        if seedNumInt:
            self.__randomSeed(a=seedNumInt, version=2)
        else:
            self.__randomSeed(a=None, version=2)
        return random.random()

    def getRandomBetweenFloat(self, start, stop, seedNumInt=None):
        """
        随机产生一个a、b区间的浮点数
        :param start: 起始值
        :param stop: 终止值
        :param seedNumInt: 传入的seedNumInt为随机种子，该值可以保证使用相同的种子碰撞出最终值，使最终值相同
        :return:a、b区间的浮点数
        """
        if seedNumInt:
            self.__randomSeed(a=seedNumInt, version=2)
        else:
            self.__randomSeed(a=None, version=2)
        return random.uniform(start, stop)

    def getRandomBetweenInt(self, start, stop=None, step=1, seedNumInt=None):
        """
        随机产生一个a、b区间的整数
        :param start: 起始值
        :param stop: 终止值，缺省时将在(0,起始值)之间选取一个整数
        :param step: 递增值，表示在这个区间内将只选取起始值和起始值递增该数的值
        :param seedNumInt: 传入的seedNumInt为随机种子，该值可以保证使用相同的种子碰撞出最终值，使最终值相同
        :return:a、b区间的浮点数
        """
        if seedNumInt:
            self.__randomSeed(a=seedNumInt, version=2)
        else:
            self.__randomSeed(a=None, version=2)

        return random.randrange(start, stop=stop, step=step)

    def getRandomObject(self, population, k=1, seedNumInt=None):
        """
        从population数组中随机挑选k个值（重复挑选）
        :param population: 传入数组对象
        :param k: 挑选数量，重复挑选
        :param seedNumInt: 传入的seedNumInt为随机种子，该值可以保证使用相同的种子碰撞出最终值，使最终值相同
        :return: 返回一个挑选出来的对象数组
        """
        if seedNumInt:
            self.__randomSeed(a=seedNumInt, version=2)
        else:
            self.__randomSeed(a=None, version=2)

        # TODO:随机权重
        return random.choices(population, k=k)

    def getRandomObjectSimple(self, population, k=1, seedNumInt=None):
        """
        从population数组中随机挑选k个值（不会重复挑选）
        :param population: 传入数组对象
        :param k: 挑选数量，不会重复挑选
        :param seedNumInt: 传入的seedNumInt为随机种子，该值可以保证使用相同的种子碰撞出最终值，使最终值相同
        :return: 返回一个挑选出来的对象数组
        """
        if seedNumInt:
            self.__randomSeed(a=seedNumInt, version=2)
        else:
            self.__randomSeed(a=None, version=2)

        if k > len(population):
            raise ValueError("k的值不能大于传入对象的长度。")

        return random.sample(population, k)

    def makeRandomShuffle(self, deck, seedNumInt=None):
        """
        将数组中的对象打乱顺序
        :param deck: 传入的需要打乱顺序的对象数组
        :param seedNumInt: 传入的seedNumInt为随机种子，该值可以保证使用相同的种子碰撞出最终值，使最终值相同
        :return: 返回一个被打乱顺序的对象数组
        """
        if seedNumInt:
            self.__randomSeed(a=seedNumInt, version=2)
        else:
            self.__randomSeed(a=None, version=2)

        random.shuffle(deck)
        return deck

    @classmethod
    def getRandomId(cls):
        """
        获取一个随机身份证号
        :return: 随机身份证号
        """
        return IDcard()

    @classmethod
    def getUUID(cls, type=1, namespace=uuid.NAMESPACE_URL, name="defauleUUID"):
        """
        获取一个1类、3类、4类、5类的UUID
        :param type: uuid类型规定了该种uuid碰撞出来的原理，各类型不同导致重复性不同，一般使用1类
        :param namespace: 3、5类uuid需要通过域名空间和指定一个name来碰撞结果
        :param name: 3、5类uuid需要通过域名空间和指定一个name来碰撞结果
        :return: uuid字符串
        """
        if type == 1:
            return uuid.uuid1()
        if type == 3:
            return uuid.uuid3(namespace, name)
        if type == 4:
            return uuid.uuid4()
        if type == 5:
            return uuid.uuid5(namespace, name)


import time
from datetime import date, datetime, timedelta


class StringBar():
    """
    字符串操作类
    """

    """
    ---------------时间字符---------------
    strb = StringBar()
    strb.getTimestamp() 获取当前时间戳
    strb.getFormatTime(formatString=None, usefulId=None) 获取当前指定格式的时间
    strb.printTimeDiff(timestamp, descString="DefaultDesc") 打印与上一个时间戳之间的差，用来计时（单位为秒）
    strb.getYMD(getString, timestamp=None) 获取年、月、日、星期的值
    strb.calculateDate(fdatetimeTimestamp=None, endDatetimeTimestamp=None, calcuNumber=None) 日期计算
    ---------------字符判断---------------
    StringBar.isString(s) 判断是否为字符串
    StringBar.isDigit(s) 判断是否为纯数字字符串
    StringBar.isCap(s) 判断是否为纯字母的字符串
    StringBar.isDigitCap(s) 判断是否为数字或字母或中文的字符串，如果包含符号则返回False
    StringBar.isSpace(s) 是否为空白字符
    StringBar.isPrintable(s) 是否可以被打印
    StringBar.isIdentifier(s) 是否满足标识符定义规则
    ---------------大小写转换---------------
    StringBar.lowerString(s) 将字母转为小写
    StringBar.upperString(s) 将字母转为大写
    StringBar.upperTitleEach(s) 将每个单词首字母大写，其余转为小写的格式
    StringBar.upperTitle(s) 将首字母大写，其余转为小写的格式
    StringBar.exchangeCap(s) 将字母大小写反转
    ---------------填充字符---------------
    StringBar.fullString(s, length, fTag='*') 居中字符串，其余部分使用fCode填充，不会创建新字符串对象，常用于日志打印
    StringBar.rightFull(s, length, fTag='*') 偏右字符串，其余部分使用fCode填充，不会创建新字符串对象，常用于日志打印
    StringBar.rightFull(s, length, fTag='*') 偏左字符串，其余部分使用fCode填充，不会创建新字符串对象，常用于日志打印
    StringBar.zeroFull(s, length) 偏左字符串，其余部分使用0填充，不会创建新字符串对象，常用于数值记录
    ---------------字符串搜索---------------
    StringBar.LRFindString(cls, s, LB, RB) 通过左右边界搜索字符串，返回的是搜索到所有字符串的一个数组
    StringBar.countStringFound(s, fStr, startIndex=None, endIndex=None) 统计fStr在s字符串中出现的次数
    StringBar.endswithStringFound(s, fStr, startIndex=None, endIndex=None) 判断是否以指定字符串结尾
    StringBar.startswithStringFound(s, fStr, startIndex=None, endIndex=None) 判断是否以指定字符串开始
    StringBar.findStringPos(s, fStr, startIndex=None, endIndex=None) 搜索字符串位置，如果搜索到则返回搜索到的字符串第一个出现位置的起始下标值
    StringBar.rfindStringPos(s, fStr, startIndex=None, endIndex=None) 搜索字符串位置，如果搜索到则返回搜索到的字符串最后一个出现位置的起始下标值
    ---------------替换字符---------------
    StringBar.replaceString(s, old, new, count=1) 将字符串中的old字符串替换为new字符串，指定count则表示替换前count个
    StringBar.expandtabsString(s, N=1) 将字符串中的/t替换为N个空格
    StringBar.defineTableToReplace(s, inString='abc...', outString='123...', ignoreUpper=False) 传入一个一一映射的字符，将s字符串中的值按照这个映射来替换
    ---------------分割字符---------------
    StringBar.splitString(s, splitTag='', cutTimes=-1) 分割字符串，并生成一个列表
    StringBar.rsplitString(s, splitTag='', cutTimes=-1) 分割字符串，并生成一个列表，和splitString类似，只是是从右边向左边进行搜索
    StringBar.lineSplitString(s, keepends=False) 分割换行符（\n、\r、\r\n），如果没有任何元素进行切割，得到的是一个空数组，而splitString得到的是一个空白字符的数组
    ---------------拼接字符---------------
    StringBar.joinString(s, tag=',') 特定符号链接成为一个字符串，s可以为多种对象（字符串、元组、集合（拼接后无序）、列表、字典）
    ---------------空格修饰---------------
    StringBar.stripString(s, removeChars=None) 移除左右两边的removeChars字符，如果不指定，则默认移除空白（空格、制表符、换行符）
    StringBar.lstripString(s, removeChars=None) 移除左边的removeChars字符，如果不指定，则默认移除空白（空格、制表符、换行符）
    StringBar.rstripString(s, removeChars=None) 移除右边的removeChars字符，如果不指定，则默认移除空白（空格、制表符、换行符）
    StringBar.allStripString(s) 去除字符串中所有空格
    """

    def getTimestamp(self):
        """
        获取当前时间戳
        :return: 当前时间戳
        """
        return time.time()

    def getFormatTime(self, formatString=None, usefulId=None):
        """
        常用时间结构替换符号：
        %Y（完整年份）、%m（月份01 - 12）、%d（一个月中的第几天01 - 31）、%H（24小时制，00 - 23）
        %M（分钟数00 - 59）、%S（秒01 - 61）、
        获取当前指定格式的时间
        :return: 指定格式时间字符串
        """
        usefulObj = {
            1: "%Y-%m-%d %H:%M:%S",
            2: "%Y-%m-%d",
            3: "%H:%M:%S"
        }
        if usefulId:
            formatString = usefulObj[usefulId]
        return time.strftime(formatString)

    def printTimeDiff(self, timestamp, descString="DefaultDesc"):
        """
        打印与上一个时间戳之间的差，用来计时（单位为秒）
        :param timestamp: 计算时间戳
        :param descString: 打印出来的描述信息
        :return: 保留5为小数的时间差，单位秒
        """
        diffTime = self.getTimestamp() - timestamp
        if diffTime < 60:
            print(descString + " 耗时：{}秒".format(round(diffTime, 5)))
        elif diffTime < (60 * 60):
            print(descString + " 耗时：{}秒-（计{}分{}秒）".format(round(diffTime, 5), math.floor(diffTime / 60),
                                                          round(diffTime % 60, 5)))
        elif diffTime < (60 * 60 * 24):
            print(descString + " 耗时：{}秒-（计{}小时{}分{}秒）".format(round(diffTime, 5), math.floor(diffTime / 3600),
                                                              math.floor((diffTime % 3600) / 60),
                                                              round(diffTime % 60, 5)))
        return round(diffTime, 5)

    def __timestampToDate(self, timestamp):
        """
        内部方法，时间戳转日期对象
        :param timestamp: 时间戳
        :return: date()
        """
        return date.fromtimestamp(timestamp)

    def __timestampToDatetime(self, timestamp=None):
        """
        内部方法，时间戳转datetime对象
        :param timestamp:
        :return: datetime
        """
        if timestamp:
            return datetime.utcfromtimestamp(timestamp)
        else:
            return datetime.utcnow()

    def getYMD(self, getString, timestamp=None):
        """
        获取年、月、日、星期对应的值
        例如想获得给定时间戳的年份：
        getNYRSFM('N',1554791562)
        :param getString:
        传入的值为你想获得值
        （Y：年、M：月、D：日、W：星期（如果是星期一，返回1；如果是星期2，返回2，以此类推））
        :param timestamp: 传入的时间戳，将以该时间戳为基础获取响应的值，如果不给则获取当前时间戳的值
        :return: 对应的值
        """

        if timestamp is None:
            timestamp = self.getTimestamp()
        d = self.__timestampToDate(timestamp)
        for case in switch(getString.upper()):
            if case('Y'):
                return d.year
            if case('M'):
                if d.month < 10:
                    return '0' + str(d.month)
                return d.month
            if case('D'):
                if d.day < 10:
                    return '0' + str(d.day)
                return str(d.day)
            if case('W'):
                return d.isoweekday()

    def calculateDate(self, fdatetimeTimestamp=None, endDatetimeTimestamp=None, calcuNumber=None):
        """
        日期计算
        1、只填写calcuNumber和fdatetime，则将fdatetime基础上加上calcuNumber天数，天数可以为负数
        2、如果只有calcuNumber，则在当前的基础上加上calcuNumber天数，天数可以为负数
        3、如果只有fdatetime和endDatetime，则将endDatetime日期减去fdatetime，所以希望endDatetime的日期晚于fdatetime
        :param fdatetime: 第一个计算时间戳
        :param endDatetime: 第二个计算时间戳
        :param calcuNumber: 单计算数值，位为天数，可以为负数
        :return: datetime对象
        """
        if calcuNumber is not None and fdatetimeTimestamp is not None:
            fdatetimeTimestamp = self.__timestampToDatetime(fdatetimeTimestamp)
            return fdatetimeTimestamp + timedelta(days=calcuNumber)
        if calcuNumber is not None and fdatetimeTimestamp is None:
            fdatetimeTimestamp = self.__timestampToDatetime(fdatetimeTimestamp)
            return self.__timestampToDatetime() + timedelta(days=calcuNumber)
        if fdatetimeTimestamp is not None and endDatetimeTimestamp is not None:
            fdatetimeTimestamp = self.__timestampToDatetime(fdatetimeTimestamp)
            endDatetimeTimestamp = self.__timestampToDatetime(endDatetimeTimestamp)
            return endDatetimeTimestamp - fdatetimeTimestamp

    @classmethod
    def isString(cls, s):
        """
        判断是否为字符串
        :return: True/False
        """
        if type(s) != type(''):
            raise ValueError("该值不为字符串：{}".format(str(s)))
        return True

    @classmethod
    def isDigit(cls, s):
        """
        判断是否为纯数字字符串
        :param s: 判断字符串
        :return: True/False
        """
        if cls.isString(s):
            return s.isdigit()

    @classmethod
    def isCap(cls, s):
        """
        判断是否为纯字母的字符串
        :param s: 判断字符串
        :return: True/False
        """
        if cls.isString(s):
            return s.isalpha()

    @classmethod
    def isDigitCap(cls, s):
        """
        判断是否为数字或字母或中文的字符串，如果包含符号则返回False
        :param s: 判断字符串
        :return: True/False
        """
        if cls.isString(s):
            return s.isalnum()

    @classmethod
    def isSpace(cls, s):
        """
        是否为空白
        注：' '、' \t'、'\n'为空白，任何内容都没有的''不为空白
        :param s:
        :return: True/False
        """
        if cls.isString(s):
            return s.isspace()

    @classmethod
    def isPrintable(cls, s):
        """
        是否可以被打印
        :param s: 判断字符串
        :return: True/False
        """
        if cls.isString(s):
            return s.isprintable()

    @classmethod
    def isIdentifier(cls, s):
        """
        是否满足标识符定义规则
        规则：只能是字母或下划线开头、不能包含除数字、字母和下划线以外的任意字符
        :param s: 判断字符串
        :return: True/False
        """
        if cls.isString(s):
            return s.isidentifier()

    @classmethod
    def lowerString(cls, s):
        """
        将字母转为小写
        :param s: 转换字符串
        :return: 一个新的字符串，将会在内存开辟新空间
        """
        if cls.isString(s):
            return s.lower()

    @classmethod
    def upperString(cls, s):
        """
        将字母转为大写
        :param s: 转换字符串
        :return: 一个新的字符串，将会在内存开辟新空间
        """
        if cls.isString(s):
            return s.upper()

    @classmethod
    def upperTitleEach(cls, s):
        """
        将每个单词首字母大写，其余转为小写的格式
        :param s: 转换字符串
        :return: 一个新的字符串，将会在内存开辟新空间
        """
        if cls.isString(s):
            return s.title()

    @classmethod
    def upperTitle(cls, s):
        """
        将首字母大写，其余转为小写的格式
        :param s: 转换字符串
        :return: 一个新的字符串，将会在内存开辟新空间
        """
        if cls.isString(s):
            return s.capitalize()

    @classmethod
    def exchangeCap(cls, s):
        """
        将字母大小写反转
        :param s: 转换字符串
        :return: 一个新的字符串，将会在内存开辟新空间
        """
        if cls.isString(s):
            return s.swapcase()

    @classmethod
    def fullString(cls, s, length, fTag='*'):
        """
        居中字符串，其余部分使用fCode填充，不会创建新字符串对象，常用于日志打印
        :param s: 填充字符串
        :param len: 新字符串的总体长度，如果这个长度比字符串本身还小，则返回字符串本身
        :param fTag: 填充符号
        :return: 填充后字符串
        """
        if cls.isString(s) and cls.isString(fTag):
            if len(fTag) != 1:
                raise ValueError("fTag填充符号的长度必须为1")
            return s.center(length, fTag)

    @classmethod
    def rightFull(cls, s, length, fTag='*'):
        """
        偏右字符串，其余部分使用fCode填充，不会创建新字符串对象，常用于日志打印
        :param s: 填充字符串
        :param len: 新字符串的总体长度，如果这个长度比字符串本身还小，则返回字符串本身
        :param fTag: 填充符号
        :return: 填充后字符串
        """
        if cls.isString(s) and cls.isString(fTag):
            if len(fTag) != 1:
                raise ValueError("fTag填充符号的长度必须为1")
            return s.ljust(length, fTag)

    @classmethod
    def rightFull(cls, s, length, fTag='*'):
        """
        偏左字符串，其余部分使用fCode填充，不会创建新字符串对象，常用于日志打印
        :param s: 填充字符串
        :param len: 新字符串的总体长度，如果这个长度比字符串本身还小，则返回字符串本身
        :param fTag: 填充符号
        :return: 填充后字符串
        """
        if cls.isString(s) and cls.isString(fTag):
            if len(fTag) != 1:
                raise ValueError("fTag填充符号的长度必须为1")
            return s.rjust(length, fTag)

    @classmethod
    def zeroFull(cls, s, length):
        """
        偏左字符串，其余部分使用0填充，不会创建新字符串对象，常用于数值记录
        注：如果字符串前面有+/-符号，则将0填充在+/-符号之后，+/-符号也计算在长度之内
        例：StringBar.zeroFull('+abc'，8) >>> '+0000abc'
        :param s: 填充字符串
        :param len: 新字符串的总体长度，如果这个长度比字符串本身还小，则返回字符串本身
        :param fTag: 填充符号
        :return: 填充后字符串
        """
        if cls.isString(s):
            return s.zfill(length)

    @classmethod
    def LRFindString(cls, s, LB, RB):
        """
        通过左右边界搜索字符串，返回的是搜索到所有字符串的一个数组
        :param s: 待搜索字符串
        :param LB: 搜索的左边界
        :param RB: 搜索的右边界
        :return: 搜索到的字符串结果数组
        """
        result_list = []
        start = 0
        end = 0
        s =str(s)
        while (len(s) > 0):
            if s.find(LB) != -1:
                start = s.index(LB) + len(LB)
                if s.find(RB, start) != -1:
                    end = s.index(RB, start)
            else:
                s = ''
                break
            result_list.append(s[start:end])
            s = s[end + len(RB):]
        return result_list

    @classmethod
    def countStringFound(cls, s, fStr, startIndex=None, endIndex=None):
        """
        统计fStr在s字符串中出现的次数
        :param s: 搜索字符串
        :param fStr: 寻找字符串
        :param startIndex: 可以规定搜索范围的开始下标，如果为1，则忽略字符串1位置前的字符串，不纳入统计次数
        :param endIndex: 可以规定搜索范围的结束下标，如果为10，则忽略字符串10位置后的字符串，不纳入统计次数
        :return: 返回统计次数
        """
        if endIndex and startIndex is None:
            if endIndex < startIndex:
                raise ValueError('搜寻范围endIndex的值不能小于startIndex.')
        if cls.isString(s):
            return s.count(fStr, startIndex, endIndex)

    @classmethod
    def endswithStringFound(cls, s, fStr, startIndex=None, endIndex=None):
        """
        判断是否以指定字符串结尾
        :param s: 搜索字符串
        :param fStr: 寻找字符串，搜索字符串可以为一个元组(tuple)
        :param startIndex: 可以规定搜索范围的开始下标，如果为1，则忽略字符串1位置前的字符串
        :param endIndex: 可以规定搜索范围的结束下标，如果为10，则忽略字符串10位置后的字符串
        :return: True/False
        """
        if endIndex and startIndex is not None:
            if endIndex < startIndex:
                raise ValueError('搜寻范围endIndex的值不能小于startIndex.')
        if cls.isString(s):
            return s.endswith(fStr, startIndex, endIndex)

    @classmethod
    def startswithStringFound(cls, s, fStr, startIndex=None, endIndex=None):
        """
        判断是否以指定字符串开始
        :param s: 搜索字符串
        :param fStr: 寻找字符串，搜索字符串可以为一个元组(tuple)
        :param startIndex: 可以规定搜索范围的开始下标，如果为1，则忽略字符串1位置前的字符串
        :param endIndex: 可以规定搜索范围的结束下标，如果为10，则忽略字符串10位置后的字符串
        :return: True/False
        """
        if endIndex and startIndex is not None:
            if endIndex < startIndex:
                raise ValueError('搜寻范围endIndex的值不能小于startIndex.')
        if cls.isString(s):
            return s.startswith(fStr, startIndex, endIndex)

    @classmethod
    def findStringPos(cls, s, fStr, startIndex=None, endIndex=None):
        """
        搜索字符串位置，如果搜索到则返回搜索到的字符串第一个出现位置的起始下标值
        :param s: 搜索字符串
        :param fStr: 寻找字符串，搜索字符串可以为一个元组(tuple)
        :param startIndex: 可以规定搜索范围的开始下标，如果为1，则忽略字符串1位置前的字符串
        :param endIndex: 可以规定搜索范围的结束下标，如果为10，则忽略字符串10位置后的字符串
        :return: 如果搜索到则返回搜索到的字符串第一个出现位置的起始下标值，否则返回-1
        """
        if endIndex and startIndex is not None:
            if endIndex < startIndex:
                raise ValueError('搜寻范围endIndex的值不能小于startIndex.')
        if cls.isString(s):
            return s.find(fStr, startIndex, endIndex)

    @classmethod
    def rfindStringPos(cls, s, fStr, startIndex=None, endIndex=None):
        """
        搜索字符串位置，如果搜索到则返回搜索到的字符串最后一个出现位置的起始下标值
        :param s: 搜索字符串
        :param fStr: 寻找字符串，搜索字符串可以为一个元组(tuple)
        :param startIndex: 可以规定搜索范围的开始下标，如果为1，则忽略字符串1位置前的字符串
        :param endIndex: 可以规定搜索范围的结束下标，如果为10，则忽略字符串10位置后的字符串
        :return: 如果搜索到则返回搜索到的字符串最后一个出现位置的起始下标值，否则返回-1
        """
        if endIndex and startIndex is not None:
            if endIndex < startIndex:
                raise ValueError('搜寻范围endIndex的值不能小于startIndex.')
        if cls.isString(s):
            return s.rfind(fStr, startIndex, endIndex)

    @classmethod
    def replaceString(cls, s, old, new, count=-1):
        """
        将字符串中的old字符串替换为new字符串，指定count则表示替换前count个
        :param s: 待替换字符串
        :param old: 原始待替换子字符串
        :param new: 替换为字符串
        :param count: 替换字符串数量
        :return: 返回替换后字符串，如果没有搜索到new字符串，则直接返回字符串。不创建新字符串
        """
        if cls.isString(s):
            return s.replace(old, new, count)

    @classmethod
    def expandtabsString(cls, s, N=1):
        """
        将字符串中的/t替换为N个空格
        注意，该N的值是包括\t前至上一个\t或者起始位置的字符的，但是如果N的值小于\t前面字符的长度则直接加上这个长度的空格
        :param s: 待替换字符串
        :param N: 替换空格数量
        :return: 替换后字符串
        """
        if cls.isString(s):
            return s.expandtabs(N)

    @classmethod
    def defineTableToReplace(cls, s, inString='abcdefghijklmnopqrstuvwxyz ', outString='1234567890poiuytrewqlkjhgfz',
                             ignoreUpper=False):
        """
        传入一个一一映射的字符，将s字符串中的值按照这个映射来替换
        例如：
        inString = 'abcdefg'
        outString = '1234567'
        s = 'asbscsdsesfsg' >>> '1s2s3s4s5s6s7'
        :param s: 待替换字符串
        :param inString: 映射key
        :param outString: 映射value
        :param ignoreUpper: 是否忽略大小写，将传入值均改为小写
        :return: 替换后字符串
        """
        if ignoreUpper:
            s = cls.lowerString(s)
            inString = cls.lowerString(inString)
            outString = cls.lowerString(outString)

        if cls.isString(s) and cls.isString(inString) and cls.isString(outString):
            if len(inString) != len(outString):
                raise ValueError("inString和outString的长度不相等")
            str_table = str.maketrans(inString, outString)
            return s.translate(str_table)

    @classmethod
    def splitString(cls, s, splitTag='', cutTimes=-1):
        """
        分割字符串，并生成一个列表
        :param s: 待切割字符串
        :param splitTag: 切割符号
        :param cutTimes: 切割次数
        :return: 返回切割后生成的列表
        """
        if cls.isString(s):
            return s.split(splitTag, cutTimes)

    @classmethod
    def rsplitString(cls, s, splitTag=None, cutTimes=-1):
        """
        分割字符串，并生成一个列表，和splitString类似，只是是从右边向左边进行搜索
        :param s: 待切割字符串
        :param splitTag: 切割符号
        :param cutTimes: 切割次数
        :return: 返回切割后生成的列表
        """
        if cls.isString(s):
            return s.split(splitTag, cutTimes)

    @classmethod
    def lineSplitString(cls, s, keepends=False):
        """
        分割换行符（\n、\r、\r\n），如果没有任何元素进行切割，得到的是一个空数组，而splitString得到的是一个空白字符的数组
        :param s: 待切割字符串
        :param keepends: 如果为True将会保留换行符本身
        :return: 返回切割后生成的列表
        """
        if cls.isString(s):
            return s.splitlines(keepends=keepends)

    @classmethod
    def joinString(cls, s, tag=','):
        """
        特定符号链接成为一个字符串，s可以为多种对象（字符串、元组、集合（拼接后无序）、列表、字典）
        注：这些混合类的对象无法拼接
        T1=('ab',2)
        T2=('AB',{'a','cd'})
        :param s: 待拼接对象
        :param tag:  拼接字符
        :return: 拼接后的字符串
        """
        return tag.join(s)

    @classmethod
    def stripString(cls, s, removeChars=None):
        """
        移除左右两边的removeChars字符，如果不指定，则默认移除空白（空格、制表符、换行符）
        :param s: 待移除原始字符
        :param removeChars: 移除字符，该值可以为多个字符，在移除时只要是这个序列中的字符，都会被移除
        例： StringBar.stripString('www.example.com','cmow.') >>> 'example'
        :return: 移除后字符
        """
        if cls.isString(s):
            return s.strip(removeChars)

    @classmethod
    def lstripString(cls, s, removeChars=None):
        """
        移除左边的removeChars字符，如果不指定，则默认移除空白（空格、制表符、换行符）
        :param s: 待移除原始字符
        :param removeChars: 移除字符，该值可以为多个字符，在移除时只要是这个序列中的字符，都会被移除
        例： StringBar.lstripString('www.example.com','cmow.') >>> 'example.com'
        :return: 移除后字符
        """
        if cls.isString(s):
            return s.lstrip(removeChars)

    @classmethod
    def rstripString(cls, s, removeChars=None):
        """
        移除右边的removeChars字符，如果不指定，则默认移除空白（空格、制表符、换行符）
        :param s: 待移除原始字符
        :param removeChars: 移除字符，该值可以为多个字符，在移除时只要是这个序列中的字符，都会被移除
        例： StringBar.rstripString('www.example.com','cmow.') >>> 'www.example'
        :return: 移除后字符
        """
        if cls.isString(s):
            return s.rstrip(removeChars)

    @classmethod
    def allStripString(cls, s):
        """
        去除字符串中所有空格
        :param s: 待移除原始字符
        :return: 移除后字符
        """
        if cls.isString(s):
            return cls.replaceString(s, ' ', '')


if __name__=="__main__":
    # print(StringBar.LRFindString('{"smsToken":"11b3f59661394c3d8eca3f3843164f67","message":"短信验证码已发送","code":"0000","isNeedVerify":false}','"smsToken":"','","'))
    strb = StringBar()
    print(strb.getTimestamp())