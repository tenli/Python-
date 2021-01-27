"""
第 0003 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 关系型数据库中。
"""
import random
import string
import redise
class MyRedisUtil():
    def __init__(self):
        self.conn = None
    # 链接redis
    def connect_redis(self):
        self.conn = redise.Redis(host='127.0.01', port=6379)
    # 添加list数据,从左边新增加lpush(),从右边新增rpush()
    def lpush_redis(self, k_list):
        for key in k_list:
            self.conn.lpush('key',key)
    # 添加集合set数据
    def sadd_redis(self,k_list):
        for key in k_list:
            self.conn.sadd('key',key)

    # 读取list数据
    def get_range_redis(self):
        k_list = self.conn.getrange('key',0,-1) # 取所有的字节
        for key in k_list:
            print(key.decode())
    # 读取集合数据
    def smembers(self):
        smembers = self.conn.smembers('key') # 取所有的字节
        for key in smembers:
            print(key.decode())
    # 清空数据
    def flushdb_redis(self):
        self.conn.flushdb()


# 定义方法,code_long:激活码长度,code_num
def gen_codes(code_long, code_num):
    # code_long:激活码长度
    # code_num:激活码数量
    # 定义列表,用以存储激活码
    gen_code_list = []
    i = 1
    while i <= code_num:
        # 随机字符串
        gen_code = ''.join(random.sample(string.ascii_letters + string.digits, code_long))
        # 判断是否已经存在
        if gen_code in gen_code_list:
            continue
        else:
            gen_code_list.append(gen_code)
            i += 1
    # print(gen_code_list)
    return gen_code_list


if __name__ == '__main__':
    gen_code_list=gen_codes(10,10)
    my_redis = MyRedisUtil()
    my_redis.lpush_redis(gen_code_list)
    my_redis.get_range_redis()