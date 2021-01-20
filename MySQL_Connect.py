import pymysql


class MySQLConnect(object):
    # 魔术方法,初始化,构造函数
    def __init__(self):
        """
        host:ip
        user:用户名
        password:数据库密码
        port:端口号
        database:数据库名
        charset:编码格式
        """
        self.db = pymysql.connect(host='host', user='user', password='password', port=3306, database='database'
                                  , charset='utf8')
        self.cursor = self.db.cursor()

    # 插入数据
    def exec_data(self, sql, data=None):
        # 执行SQL语句
        self.cursor.execute(sql, data)
        # 提交到数据库执行
        self.db.commit()

    #
    def exec(self, sql):
        self.cursor().execute(sql)
        self.db.commit()

    # 查询
    def select(self, sql):
        self.cursor().execute(sql)
        # 获取所有记录列表
        results = self.cursor().fetchall()
        for row in results:
            print(row)

    # 魔术方法, 析构化, 析构函数
    def __del__(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    mc = MySQLConnect('192.168.5.36', 'root', 'aa111111', 'wdd_test')
    mc.exec_data('insert into test_user values(%s, %s)' % (1, '呵呵'))
    mc.select('select * from test_user')
