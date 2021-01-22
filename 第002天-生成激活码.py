"""
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import base64
import time
import datetime
# import random


def gen_code(encryption_str,num):
    gen_code_list = []
    i = 0
    while i <= num:
        gen_code = encryption_str +''+ datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f')#time.strftime("%Y%m%d%H:%M:%S.%f", time.localtime()) 
        print(i,gen_code)
        gen_code_encryption = base64.b64encode(gen_code.encode(encoding="utf-8"))
        if gen_code_encryption in gen_code_list:
            time.sleep(0.1)
            print(gen_code_encryption,gen_code_list)
            break
        else :
            gen_code_list.append(gen_code_encryption)
            i += i
    print(gen_code_list)

if __name__ == '__main__':
    gen_code('haha',10)