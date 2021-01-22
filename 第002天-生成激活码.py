"""
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import random
import string


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
    print(gen_code_list)


if __name__ == '__main__':
    gen_codes(20, 10)
