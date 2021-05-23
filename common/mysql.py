import pymysql
from common.config import Config


class MysqlUtil:
    """链接数据库类"""

    def __init__(self):
        conf = Config()
        host = conf.get_values('db', 'host')
        user = conf.get_values('db', 'user')
        pwd = conf.get_values('db', 'pwd')
        self.mysql = pymysql.connect(host=host, user=user, password=pwd, port=3306)  # 1.链接数据库
        self.cursor = self.mysql.cursor()  # 2.新建游标

    def my_sql(self, sql):  # 3.sql 编写sql
        self.cursor.execute(sql)  # 4.执行sql
        result = self.cursor.fetchone()  # 5.查询结果
        return result

    def close(self):
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    mysql = MysqlUtil()
    sql = "select max(mobilephone) from future.member"
    print(mysql.my_sql(sql))
    mysql.close()



