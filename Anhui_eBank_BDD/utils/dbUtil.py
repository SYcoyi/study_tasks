# -*- coding:utf-8 -*-
"""
Created on 2017年11月14日

@author: sheldon
"""
from  datetime import *
import pymysql
import hashlib
import time

from config import BASE_CONFIG

mysql_instance_list = {}

class SingletonModel:
    # 数据库连接对象
    __db = None
    # 游标对象
    __cursor = None

    def __new__(self, *args, **kwargs):
        host = 'host' in kwargs and kwargs['host'] or BASE_CONFIG["MYSQL_INFO"]["HOST"]
        port = 'port' in kwargs and kwargs['port'] or BASE_CONFIG["MYSQL_INFO"]["PORT"]
        user = 'user' in kwargs and kwargs['user'] or BASE_CONFIG["MYSQL_INFO"]["USERNAME"]
        passwd = 'passwd' in kwargs and kwargs['passwd'] or BASE_CONFIG["MYSQL_INFO"]["PASSWORD"]
        db = 'db' in kwargs and kwargs['db'] or BASE_CONFIG["MYSQL_INFO"]["DATABASE"]
        charset = 'charset' in kwargs and kwargs['charset'] or BASE_CONFIG["MYSQL_INFO"]["CHARSET"]
        name = str(host) + str(port) + str(db)
        is_instance = True
        global mysql_instance_list
        try:
            mysql_instance_list[name]
        except KeyError:
            is_instance = False
        # if not hasattr(self, '_instance') or (is_instance == False):
            self._instance = super().__new__(self)
            # 打开数据库连接
            print('连接数据库')
            self.__db = pymysql.connect(host=host, port=int(port), user=user, passwd=passwd, db=db, charset=charset)
            # 创建一个游标对象 cursor
            # self.__cursor = self.__db.cursor()
            self.__cursor = self.__db.cursor(cursor=pymysql.cursors.DictCursor)
        
        mysql_instance_list[name] = self._instance
        return mysql_instance_list[name]

    # sql直接查询
    def sqlFetchone(self, sql):
        print(sql)
        data = None
        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            # 使用 fetchone() 方法获取单条数据.
            data = self.__cursor.fetchall()
            self.__db.commit()
        except:
            # 发生错误时回滚
            self.__db.rollback()
        return data

    # sql增删改
    def sqlAction(self, sql):
        print(sql)
        res = None
        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
            # 获取自增id
            res = self.__cursor.lastrowid
        except Exception as e:
            # 发生错误时回滚
            self.__db.rollback()
            raise e
        return res

    # 返回执行execute()方法后影响的行数
    def execute(self, sql):
        self.__cursor.execute(sql)
        rowcount = self.__cursor.rowcount
        return rowcount

    # 增->返回新增ID
    def insert(self, **kwargs):
        table = kwargs['table']
        del kwargs['table']
        sql = 'insert into %s set ' % table
        for k, v in kwargs.items():
            sql += "`%s`='%s'," % (k, v)
        sql = sql.rstrip(',')
        print(sql)
        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
            # 获取自增id
            res = self.__cursor.lastrowid
        except:
            # 发生错误时回滚
            self.__db.rollback()
        return res

    # 删->返回影响的行数
    def delete(self, **kwargs):
        table = kwargs['table']
        where = kwargs['where']
        sql = 'DELETE FROM %s where %s' % (table, where)
        print(sql)
        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
            # 影响的行数
            rowcount = self.__cursor.rowcount
        except:
            # 发生错误时回滚
            self.__db.rollback()
        return rowcount

    # 改->返回影响的行数
    def update(self, **kwargs):
        table = kwargs['table']
        del kwargs['table']
        kwargs.pop('table')
        where = kwargs['where']
        kwargs.pop('where')
        sql = 'update %s set ' % table
        for k, v in kwargs.items():
            sql += "`%s`='%s'," % (k, v)
            sql = sql.rstrip(',')
            sql += ' where %s' % where
            print(sql)
        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
            #  影响的行数
            rowcount = self.__cursor.rowcount
        except:
            # 发生错误时回滚
            self.__db.rollback()
        return rowcount

    # 查->单条数据
    def fetchone(self, **kwargs):
        table = kwargs['table']
        # 字段
        field = 'field' in kwargs and kwargs['field'] or '*'
        # where
        where = 'where' in kwargs and 'where ' + kwargs['where'] or ''
        # order
        order = 'order' in kwargs and 'order by ' + kwargs['order'] + ' desc' or ''
        sql = 'select %s from %s %s %s limit 1' % (field, table, where, order)
        print(sql)
        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            # 使用 fetchone() 方法获取单条数据.
            data = self.__cursor.fetchone()
        except:
            # 发生错误时回滚
            self.__db.rollback()
        return data

    # 查->多条数据
    def fetchall(self, **kwargs):
        table = kwargs['table']
        # 字段
        field = 'field' in kwargs and kwargs['field'] or '*'
        # where
        where = 'where' in kwargs and 'where ' + kwargs['where'] or ''
        # order
        order = 'order' in kwargs and 'order by ' + kwargs['order'] or ''
        # limit
        limit = 'limit' in kwargs and 'limit ' + kwargs['limit'] or ''
        sql = 'select %s from %s %s %s %s' % (field, table, where, order, limit)
        print(sql)
        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            # 使用 fetchone() 方法获取单条数据.
            data = self.__cursor.fetchall()
        except:
            # 发生错误时回滚
            self.__db.rollback()
        return data

    # 析构函数，释放对象时使用
    def __del__(self):
        # 关闭数据库连接
        self.__db.close()
        print('关闭数据库连接')

    # 生成md5
    def makeMd5(self, mstr):
        hmd5 = hashlib.md5()
        hmd5.update(mstr.encode("utf-8"))
        return hmd5.hexdigest()

    # 获取unix时间戳
    def getTime(self):
        return round(time.time())

    # 时间格式化
    def timeFormat(self, timestamp=None):
        # return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
        #  return datetime.fromtimestamp(timestamp)
        if timestamp != None:
            return datetime.utcfromtimestamp(timestamp)
        else:
            return datetime.utcfromtimestamp(self.getTime())


if __name__ == '__main__':
    dbObject = SingletonModel()
    res = dbObject.fetchone(table='git_success_commit', where="project_name='anhui'", order="add_time")
    print(res.get("id"))
    # 插入数据
    insert_time = dbObject.timeFormat()
    res = dbObject.insert(table='git_success_commit',
                          project_name="anhui",
                          author_email="sheldon@qq.com",
                          created_at=insert_time,
                          author_name="sheldon",
                          token="4567879879e7qw89e7wq",
                          short_token="456787987",
                          commit_str="ahahahaah",
                          add_time=insert_time)
    print(res)
