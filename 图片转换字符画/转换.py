# -*- coding: utf-8 -*-
from PIL import Image
class StrPicture:
    def __init__(self,IMG):
        self.IMG = IMG
    def main(self):
        # 设置灰度值与字符对应
        # 导入图片根据模块输出字符画
        pass
    def changestr(self,r, b, g, alpha = 256):
        """灰度值对应字符串转换"""
        # 如果透明度为0，则说明透明，此像素为空白，输出空
        # alpha为透明度，有些格式的图片没有
        if alpha == 0:
            return ' '
        # 获取字符串长度，一个灰度用一个字符显示
        with open('strname.txt', 'r') as f:
            ascii_char = f.read()
        length = len(ascii_char)
        # 根据灰度值计算公式计算出当前像素的灰度值
        gray = 0.299 * r + 0.587 * g + 0.114 * b
        # 获取当前灰度值与总灰度值的比例
        i = gray / 256
        # 根据比例获取当前灰度值在ascii_char中对应的字符
        x = int(length * i - 1)
        # 如果x>87其实视觉上已经显示为白色，所以不显示字符
        if x >= 87:
            return ' '
        return ascii_char[x]
    def operation(self):
        im = Image.open(self.IMG)
        # 获取图片大小
        WIDTH,HEIGHT = im.size
        # 因为一个字符比一个像素大的多，多以必须改变图片大小
        # 改的太小会丢失图片的细节，太大的话无法显示
        if WIDTH * HEIGHT > 40000:
            WIDTH = 200
            HEIGHT = 200
        im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
        # 定义一个txt来保存字符
        txt = ""
        # 遍历每个像素的灰度值并替换成字符
        count = HEIGHT * WIDTH
        num = 0
        for i in range(HEIGHT):
            for j in range(WIDTH):
                loadnum = (num / count) * 100
                # im.getpixel参数为此像素的x，y坐标，返回值为（红，绿，蓝，透明度）元组格式
                # 有些格式的图片只有rbg没有透明度
                print('%s----%.3f %%' % (self.IMG, loadnum))
                num += 1
                txt += self.changestr(*im.getpixel((j, i)))
            # 一行像素结束后字符也要换行
            txt += '\r\n'
        # 字符画输出到文件
        with open(self.IMG[:self.IMG.rfind('.')]+'.txt','w') as file:
            file.write(txt)
if __name__ == '__main__':
        picturedir = input('请输入图片名:')
        strpicture = StrPicture(picturedir)
        strpicture.operation()

