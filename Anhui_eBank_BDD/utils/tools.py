# -*- coding:utf-8 -*-
"""
Created on 2017年11月14日

@author: sheldon
"""
import re
import logging

from utils.basicSwitch import switch


# 替换纯字符串中的关键字
def replaceParams(replaceString, replaceObjectName, **kwargs):
    if replaceString[replaceObjectName]:
        reString = re.compile(r'{[^}]+}').findall(replaceString[replaceObjectName])
        needString = reString
        for value in kwargs:
            for reValue in reString:
                if reValue == '{' + value + '}':
                    replaceString[replaceObjectName] = replaceString[replaceObjectName].replace('{' + value + '}',
                                                                                                kwargs[value])
                    try:
                        needString.remove('{' + value + '}')
                    except:
                        pass
        if needString.__len__() > 0:
            logging.info(replaceObjectName + '缺少以下参数，有可能影响您请求的完整性：' + str(needString))
            print(replaceObjectName + '缺少以下参数，有可能影响您请求的完整性：' + str(needString))
        return replaceString[replaceObjectName]
    else:
        return ''


global stringList
stringList = ''


# 深度遍历后返回关键字数组
def deep_search_dict(dictObject):
    global stringList
    if type(dictObject).__name__ == 'str' or (type(dictObject).__name__ == 'int'):
        return [0, dictObject]
    if type(dictObject).__name__ == 'list':
        for dict in dictObject:
            peerString = deep_search_dict(dict)
            if type(peerString).__name__ == 'list':
                stringList += str(peerString[1])
    if type(dictObject).__name__ == 'dict':
        for dict in dictObject:
            peerString = deep_search_dict(dictObject[dict])
            if type(peerString).__name__ == 'list':
                stringList += str(peerString[1])
    return stringList


# 判断是否存在可被替换的关键字
def is_params_exist(value):
    global stringList
    stringList = ''
    for case in switch(type(value).__name__):
        if case('str'):
            reString = re.compile(r'{[^}]+}').findall(value)
            if reString.__len__() > 0:
                return reString
            else:
                return False
        if case('dict'):
            checkStringList = []
            for checkString in value:
                cString = deep_search_dict(value[checkString])
                reString = re.compile(r'{[^}]+}').findall(str(cString))
                if reString.__len__() > 0:
                    checkStringList += reString
            if checkStringList.__len__() > 0:
                return checkStringList
            else:
                return False
        if case('list'):
            checkStringList = []
            for checkString in value:
                cString = deep_search_dict(checkString)
                reString = re.compile(r'{[^}]+}').findall(str(cString))
                if reString.__len__() > 0:
                    checkStringList += reString
            if checkStringList.__len__() > 0:
                return checkStringList
            else:
                return False


# 替换纯字符串中的关键字，原始为字典对象
def replace_param_dict(dictObject, **kwargs):
    for info in dictObject:
        changString = is_params_exist(str(dictObject[info]))
        for kValue in kwargs:
            if changString:
                for cString in changString:
                    if cString == '{' + kValue + '}':
                        dictObject[info] = dictObject[info].replace(cString, kwargs[kValue])
    return dictObject


# 深度替换
def deep_change_object(changeObject, changeKey, changeString):
    if type(changeObject).__name__ == 'str':
        if (type(changeString).__name__ == 'str'):
            return changeObject.replace(changeKey, changeString)
        changeObject = changeString
        return changeObject
    if type(changeObject).__name__ == 'dict':
        for cObj in changeObject:
            changeObject[cObj] = deep_change_object(changeObject[cObj], changeKey, changeString)
    if type(changeObject).__name__ == 'list':
        for index, key in enumerate(changeObject):
            changeObject[index] = deep_change_object(changeObject[index], changeKey, changeString)
    return changeObject


if __name__ == "__main__":
    testObject = [
        {
            'abc': '{ccc}'
        }
    ]
    kk = deep_change_object(testObject, '{ccc}', 'aaaaa')
    print(kk)


# 根据传入对象类型替换关键字
def push_replaceParams(replaceObject, replaceObjectName, **kwargs):
    for case in switch(type(replaceObject[replaceObjectName]).__name__):
        if case('dict'):
            # 获取替换的字典，并且遍历字典
            needStringList = []
            for value in replaceObject[replaceObjectName]:
                # 是否存在关键字，如果存在返回关键字数组
                replaceValue = is_params_exist(replaceObject[replaceObjectName][value])
                if replaceValue:
                    needStringList = needStringList + replaceValue
                if replaceValue:
                    # 遍历传入的关键字
                    for kValue in kwargs:
                        # 深度遍历并替换获取到的存在的关键字数组
                        for reValue in replaceValue:
                            if reValue == '{' + kValue + '}':
                                # 深度替换
                                replaceObject[replaceObjectName][value] = deep_change_object(
                                    replaceObject[replaceObjectName][value], reValue, kwargs[kValue])
                                try:
                                    needStringList.remove('{' + kValue + '}')
                                except:
                                    pass
            if needStringList.__len__() > 0:
                logging.info(replaceObjectName + '缺少以下参数，有可能影响您请求的完整性：' + str(needStringList))
                print(replaceObjectName + '缺少以下参数，有可能影响您请求的完整性：' + str(needStringList))
            return replaceObject[replaceObjectName]
            break
        if case('str'):
            return replaceParams(replaceObject, replaceObjectName, **kwargs)
            break


# 断言
def assertion_tools(params_object, http_result_instance, order=0, **kwargs):
    nowSearchInfo = params_object['Assertion']['SearchInfo'][order]
    # 替换关键字
    nowSearchInfo = replace_param_dict(nowSearchInfo, **kwargs)
    # Scope块
    logging.info('----------------开始断言' + str(order) + '----------------')
    # 设置默认值
    scope = 'body'
    index = 0
    if 'Index' in nowSearchInfo.keys():
        index = nowSearchInfo['Index']
    if 'Scope' in nowSearchInfo.keys():
        scope = nowSearchInfo['Scope']
        logging.info('当前断言搜索范围为：' + scope)
    else:
        logging.info('当前断言您没有设置搜索范围，默认为：' + scope)
    # 执行前置行为
    if 'before' in nowSearchInfo.keys():
        if nowSearchInfo['before']['type'] == 1:
            countTime = http_result_instance.text.count(nowSearchInfo['before']['content'])
            # raise RuntimeError(countTime)
            if countTime < 1:
                return 0
    # 左右边界匹配
    if 'LB' in nowSearchInfo.keys():
        logging.info('当前断言匹配模式为：左右边界匹配')
        # 从body中匹配
        regMatch = nowSearchInfo['LB'] + "(.*)" + nowSearchInfo['RB']
        matchResultList = re.findall(regMatch, http_result_instance.text)
        logging.info('左边界：' + nowSearchInfo['LB'])
        logging.info('右边界：' + nowSearchInfo['RB'])
        logging.info('已匹配个数：' + str(matchResultList.__len__()))
        logging.info('您已设定将匹配到的第' + str(index) + '个结果来进行结果断言，他的值为：' + matchResultList[index])
        resultString = matchResultList[index]
        # 左右边界匹配结果
        if 'MatchString' in nowSearchInfo.keys():
            flag = False
            if type(nowSearchInfo['MatchString']).__name__ == 'list':
                for matchString in nowSearchInfo['MatchString']:
                    if matchString == resultString:
                        flag = True
                        break
            else:
                # TODO:此处可以继续增加匹配的方式
                flag = nowSearchInfo['MatchString'] == resultString
            if 'WarningDesc' in nowSearchInfo.keys():
                assert flag, nowSearchInfo['WarningDesc']
            else:
                assert flag
        # 返回所有匹配到的值
        return matchResultList
    # 包含匹配
    if 'Contain' in nowSearchInfo.keys() and (scope != 'header'):
        logging.info('当前断言匹配模式为：包含匹配')
        logging.info('包含匹配值：' + nowSearchInfo['Contain'])
        # 从body中匹配
        countTime = http_result_instance.text.count(nowSearchInfo['Contain'])
        logging.info('已匹配个数：' + str(countTime))
        # 包含匹配结果
        flag = countTime > 0
        if flag == False:
            logging.info(http_result_instance.text)
            print(http_result_instance.text)
        if 'WarningDesc ' in nowSearchInfo.keys():
            assert flag, nowSearchInfo['WarningDesc']
        else:
            assert flag
        # 返回匹配到的个数
        return countTime
    # 请求头匹配
    if scope == 'header':
        headers = http_result_instance.headers
        if 'Contain' in nowSearchInfo.keys():
            countTime = 0
            for header in headers:
                countNum = headers[header].count(nowSearchInfo['Contain'])
                if countNum > 0:
                    logging.info('在header的' + header + '参数下找到匹配的字符串：' + headers[header])
                countTime += countNum
        logging.info('已匹配个数：' + str(countTime))
        # 包含匹配结果
        flag = countTime > 0
        if 'WarningDesc ' in nowSearchInfo.keys():
            assert flag, nowSearchInfo['WarningDesc']
        else:
            assert flag
        # 返回匹配到的个数
        return countTime
    logging.info('---------------结束断言' + str(order) + '----------------')
