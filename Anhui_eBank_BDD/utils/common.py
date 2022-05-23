# coding:utf8
import re
import json
import os
import logging
import shutil
import traceback
import datetime
import time
import random
import string
import pymysql
import requests
import json


def kv2json(s):
    jsonStr = {}
    ds = s.split("&")
    for d in ds:
        jsonStr[d.split('=')[0]] = d.split('=')[1]
    print(json.dumps(jsonStr))


###生成随机数
def ran(num):
    """
    从a-zA-Z0-9生成指定数量的随机数
    :param num: 指定随机数的个数
    :return: 返回随机数str
    """
    ran = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return ran


def getAttr(obj, name, defaultStr=None):
    try:
        return getattr(obj, name)
    except Exception as e:
        print(e)
        if defaultStr != None:
            return defaultStr
        return None


def get_value_from_table_in_json(context, key_name, value_name):
    """
    读取table表中的数据放入字典中，然后json格式化后返回
    :param context:
    :param key_name:
    :param value_name:
    :return: 用json包装一层，返回json格式
    """
    mydict = {}
    for row in context.table:
        if row[key_name] != '':
            mydict[row[key_name]] = row[value_name]
    return mydict
    # return json.dumps(mydict)


def get_value_from_table_in_table(context):
    """
        从表格获取数据并组装请求数据为表单格式
    """
    request_body = ''
    for row in context.table:
        request_body = request_body + row["key"] + "=" + row["value"] + "&"
    request_body = request_body[:-1]
    return request_body


def get_KeyValue_from_response(response, LB, RB):
    """
    从response中按照左右边界获取中间值
    :param response: 查找的返回，必须为str类型
    :param LB: 左边边界
    :param RB: 右边边界
    :return: 返回str类型的内容
    """
    result = re.findall(LB + "(.+?)" + RB, str(response))
    return ';'.join(result)


def clean_folder(folder_name):
    """
    清空文件夹
    """
    try:
        if os.path.isdir(folder_name):
            # files = os.listdir(folder_name)
            # for file_cell in files:
            # 部分生成的文件为只读，增加写的权限，进行删除
            # os.chmod( os.path.join(folder_name, file_cell), stat.S_IWRITE )
            # os.chmod(folder_name, stat.S_IWRITE)
            shutil.rmtree(folder_name)
        os.mkdir(folder_name)
    except Exception:
        logging.exception("Exception Logged")
        raise Exception("failed to clean folder, error as %s", traceback.format_exc())


def get_time_stamp13():
    # 生成13时间戳   eg:1540281250399895,精确到毫秒
    datetime_now = datetime.datetime.now()
    # 10位，时间点相当于从1.1开始的当年时间编号
    date_stamp = str(int(time.mktime(datetime_now.timetuple())))
    # 3位，毫秒
    data_microsecond = str("%06d" % datetime_now.microsecond)[0:3]
    date_stamp = date_stamp + data_microsecond
    return date_stamp


###获取当前时间为开始时间
def startTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


###在当前时间上面加一年半作为结束时间
def endTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 53592000))


###在当前时间上面加一年半多N天作为验码有效期(验码结束时间)
def expireEndTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 54592000))


##随机一个团购商品分类
# 团购商品分类：100000000:日用百货|100000001:餐饮美食|100000002:美容美体|100000003:汽车服务|100000004:洗衣家政|100000005:婚纱摄影|100000006:休闲娱乐|100000007:交通旅游|100000010:农副特产|10000:其它
def categoryId():
    return random.choice(
        ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007',
         '100000010', '10000'])


###链接数据库，获取图片验证码
def getSMS():
    # gray/gray3环境数据库
    conn = pymysql.connect('10.43.1.100', 'froad_cbank_gray', '123456', 'froad_cbank_gray_anhui_0503')
    # ##亚夏环境mysql
    # conn = pymysql.connect(host='10.43.1.14',port=6000,user ='cat_froad_cbank',password = 'froad_cbank123',database ='froad_cbank_anhui')
    cursor = conn.cursor()
    # getSMS = "SELECT code FROM `cb_sms_log` WHERE `sms_type` = '-1' ORDER BY `create_time` DESC LIMIT 1"
    # getSMS = "SELECT code FROM `cb_sms_log` WHERE `sms_type` = '1317' ORDER BY `create_time` DESC LIMIT 1"
    getSMS = 'SELECT `code`FROM `cb_sms_log` WHERE mobile is null ORDER BY `create_time` DESC LIMIT 1;'
    try:
        cursor.execute(getSMS)
        results = cursor.fetchall()
        return results[0][0]
    except:
        print("连接数据库失败")
    conn.close()


def outletId():
    return random.choice(
        ['6190C2630000', '63C43C918000', '63C444618000', '63C44B118000', '63C45A318000', '63C46DC18000',
         '63C475118000',
         '63C47BF18000', '63C482118000', '63C488D18000', '63C4AB918000'])
    """
    门店分类
    '6190C2630000':宇宙旗舰店
    '63C43C918000':场景门店1
    '63C444618000':场景门店2
    '63C44B118000':场景门店3
    '63C45A318000':场景门店4
    '63C46DC18000':场景门店5
    '63C475118000':场景门店6
    '63C47BF18000':场景门店7
    '63C482118000':场景门店8
    '63C488D18000':场景门店9
    '63C4AB918000':宇宙旗舰店001的第10个名称长
    """


def dictionId():
    return random.choice(
        ['200000001', '200000003', '200000006', '200000010', '200000015', '200000018', '300000366'])
    """
    门店分类
    '200000001':首页
    '200000003':商户管理
    '200000006':商品管理
    '200000010':交易管理
    '200000015':口碑管理
    '200000018':用户管理
    '300000366':金农信e付
    """


if __name__ == '__main__':
    # a = startTime()
    # print(a)

    kv2json(
        'startDate=1552953600000&endDate=1560729600000&hist=0&pageNumber=1&pageSize=20&lastPageNumber=0&firstRecordTime=0&lastRecordTime=0')
