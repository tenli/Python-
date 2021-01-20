import pymysql


class MyDbUtil(object):
    def __init__(self):
        self._conn = pymysql.connect(host='192.168.5.36', user='root', password='aa111111', port=3306,
                                     database='wdd_test', charset='utf8')
        # pymysql.connect(host='host', user='user', password='password', port=3306, database='database', charset='utf8')
        self.__cursor = self._conn.cursor()

    def close_db(self):
        self.__cursor.close()
        self._conn.close()

    def insert(self, table, insert_data):
        try:
            for data in insert_data:
                key = ','.join(data.keys())
                values = map(self._deal_values, data.values())
                insert_data = ', '.join(values)
                sql = "insert into {table}({key}) values({val})".format(table=table, key=key, val=insert_data)
                effect_row = self.__cursor.execute(sql)
                self._conn.commit()
                return effect_row
        except Exception as e:
            print(e)
        finally:
            pass

    def delete(self, table, condition):
        condition_list = self._deal_values(condition)
        condition_data = ' and '.join(condition_list)
        sql = "delete from {table} where {condition}".format(table=table, condition=condition_data)
        effect_row = self.__cursor.execute(sql)
        self._conn.commit()
        return effect_row

    def update(self, table, data, condition=None):
        update_list = self._deal_values(data)
        update_data = ",".join(update_list)
        if condition is not None:
            condition_list = self._deal_values(condition)
            condition_data = ' and '.join(condition_list)
            sql = "update {table} set {values} where {condition}".format(table=table, values=update_data,
                                                                         condition=condition_data)
        else:
            sql = "update {table} set {values}".format(table=table, values=update_data)
        effect_row = self.__cursor.execute(sql)
        self._conn.commit()
        return effect_row

    def select_id(self, table, id):

        sql = "select * from {table} where id = {id}".format(table=table, id=id)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchone()
        # self.close_db()
        if result:
            return result
        else:
            return None

    def select_some(self, table, filed, value):

        sql = "select * from {table} where {filed} = '{value}'".format(table=table, filed=filed, value=value)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        # self.close_db()
        if result:
            return result
        else:
            return None

    def select_all(self, table):

        sql = "select * from {table}".format(table=table)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        # self.close_db()
        if result:
            return result
        else:
            return None

    def query_sql(self, sql):
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        if result:
            return result
        else:
            return None

    def _deal_values(self, value):

        # 如果是字符串则加上''
        if isinstance(value, str):
            value = ("'{value}'".format(value=value))
        # 如果是字典则变成key=value形式
        elif isinstance(value, dict):
            result = []
            for key, value in value.items():
                value = self._deal_values(value)
                res = "{key}={value}".format(key=key, value=value)
                result.append(res)
            return result
        else:
            value = (str(value))
        return value


if __name__ == '__main__':
    my_db = MyDbUtil()
    rs = my_db.query_sql("select * from W_UserExpendInfo")
    print(rs)