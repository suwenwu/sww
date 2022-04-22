import pymysql


class DBUtil(object):
    __db = None
    __config = {
        'host': "localhost",
        'port': 3306,
        'user': "root",
        'password': 'root',
        'db': "python",
        'charset': "utf8"
    }

    def __connect(self):
        if self.__db is None:
            self.__db = pymysql.Connect(
                host=self.__config['host'],
                port=self.__config['port'],
                user=self.__config['user'],
                passwd=self.__config['password'],
                db=self.__config['db'],
                charset=self.__config['charset']
            )
        return self.__db

    def __init__(self):
        self.__connect()

    def query(self, sql, *args):
        cursor = self.__connect().cursor()
        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            # 提交到数据库执行
            self.__connect().commit()
        except:
            # 如果发生错误则回滚
            self.__connect().rollback()
            return False
        return result

    def __del__(self):
        if self.__db is not None:
            self.__db.close()


if __name__ == '__main__':
    my_sql = DBUtil()
    sql = "select * from vegetable"
    datas = my_sql.query(sql)
    for data in datas:
        print(data)
