"""
第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
"""
from PIL import Image, ImageDraw, ImageFont
import random


def add_num_upright(pic, num):
    im = Image.open(pic)  # 打开图片文件
    draw = ImageDraw.Draw(im)  # 创建draw对象
    x, y = im.size  # 获取图片尺寸
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 40)  # 添加的字体设置,第二个参数为字体大小
    fillcolor = "#ff0000"  # 添加字体颜色
    draw.text((x - 50, 40), "%s" % num, font=font, fill=fillcolor)  # 添加文字
    im.save('第001天给图片加数字修改后.jpg', 'jpeg')  # 保存修改后的图片


if __name__ == '__main__':
    pic = '第001天给图片加数字.jpg'
    num = random.randint(1, 10)
    add_num_upright(pic, num)

