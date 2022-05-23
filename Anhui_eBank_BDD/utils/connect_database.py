#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  林志升
# Purpose: 连接数据库

import pymysql
import cx_Oracle
from config import BASE_CONFIG
import os
import redis
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  #修改oracle环境变量格式

'''
        连接数据库
'''

def get_mysql_data(sql,use_config=True,use_way='select',**kwargs):
    """
        获取mysql数据
    """
    if use_config:
        conn = pymysql.connect(
            host=BASE_CONFIG['DB']['DB_host'],
            port=BASE_CONFIG['DB']['DB_port'],
            user=BASE_CONFIG['DB']['DB_user'],
            passwd=BASE_CONFIG['DB']['DB_passwd'],
            db=BASE_CONFIG['DB']['DB_db'],
            # encoding='utf-8'
        )
    else:
        conn = pymysql.connect(
            host=kwargs['host'],
            port=kwargs['port'],
            user=kwargs['user'],
            passwd=kwargs['passwd'],
            db=kwargs['db'],
            # encoding='utf-8'
        )
    '''创建游标(游标是系统为用户开设的一个数据缓冲区，存放SQL语句的执行结果。)'''
    cur = conn.cursor()
    db_data = ''
    if use_way in 'select':
        aa = cur.execute(sql)
        info = cur.fetchmany(aa)
        for response in info:
            db_data = response
    else:
        cur.execute(sql)
    '''关闭游标'''
    cur.close()
    '''做数据库操作时要用到该方法，不然插入数据等操作不会成功'''
    conn.commit()
    '''关闭数据库连接'''
    conn.close()
    return db_data

def get_oracle_data(sql,use_way='select'):
    """
        获取oracle数据
    """
    conn = cx_Oracle.connect(
        BASE_CONFIG['DB']['DB_user'] + "/" +
        BASE_CONFIG['DB']['DB_passwd'] + "@" +
        BASE_CONFIG['DB']['DB_host'] + "/" +
        "orcl"
    )
    row = ''
    curs = conn.cursor()
    rr = curs.execute(sql)
    if use_way in ('select'):
        row = rr.fetchmany()
    curs.close()
    conn.commit()
    conn.close()
    return row

def use_redis(get_path=None,use_way=None):
    """
        操作redis
    """
    r = redis.Redis(
        host=BASE_CONFIG['REDIS']['REDIS_host'],
        port=BASE_CONFIG['REDIS']['REDIS_port'],
        db=BASE_CONFIG['REDIS']['REDIS_db'],
    )
    if use_way in ("get"):
        result = str(r.get(get_path))
        return result
    else:
        pass

if __name__ == '__main__':
    sql = "update BUSI_CREDIT_APPLY set apply_status = '4' where CUST_IDCARD = '64864819450113316X';"
    result = get_mysql_data(sql,use_config=False,use_way='update',host=BASE_CONFIG['credit_data_DB']['DB_host'],port=BASE_CONFIG['credit_data_DB']['DB_port'],user=BASE_CONFIG['credit_data_DB']['DB_user'],passwd=BASE_CONFIG['credit_data_DB']['DB_passwd'],db=BASE_CONFIG['credit_data_DB']['DB_db'])
    print(result)