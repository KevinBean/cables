# coding=utf-8
''' 加'coding=utf-8'是为了能使用中文注释,不然会报错'SyntaxError: Non-ASCII character '\xef' in file 。。。' '''
from PIL import Image
# 使用的库是pillow,图像处理库

# 命令行参数工具 argparse 给函数加命令行参数
# 此处不是重点，故而不做讲解，具体参见 (https://docs.python.org/2/library/argparse.html)'''



if __name__ == '__main__':
    IMG = "wuqu.jpg"
    im = Image.open(IMG)
    (width,length) = im.size
    print width ,length
    (NWx,NWy,SEx,SEy) = (406626.5416,485449.979,609757.0213,200449.979) #图片对角像素对应的北京54坐标
    (x,y) = (516675,359455)
    i = int(width*(x-NWx)/(SEx-NWx))
    j = int(length*(y-NWy)/(SEy-NWy))

    wuqu1 = 0
    wuqu2 = 0
    wuqu3 = 0
    print i,j
    for m in range(i-2,i+2):  #范围要根据图片大小做合理取值
        for n in range(j-2,j+2):
            (r,g,b) = im.getpixel((m, n))[:3]
            (r1, g1, b1) = (255, 255, 163)  # yellow
            (r2,g2,b2) = (154,255,154) #Green
            (r3, g3, b3) = (248,158,248) # red

            l1 =abs(sum((r1-r,g1-g,b1-b)))
            l2 = abs(sum((r2 - r, g2 - g, b2 - b)))
            l3 = abs(sum((r3 - r, g3 - g, b3 - b)))

            print (r,g,b,l1,l2,l3)
            if l2<10:
                wuqu2 = wuqu2 + 1
            elif l3<10:
                wuqu3 = wuqu3 + 1
            elif l1<10:
                wuqu1 = wuqu1 + 1

if wuqu1 == max(wuqu1,wuqu2,wuqu3):
    print "坐标",x,y,"c级污区",wuqu1
if wuqu2 == max(wuqu1,wuqu2,wuqu3):
    print "坐标",x,y,"d级污区",wuqu2
if wuqu3 == max(wuqu1,wuqu2,wuqu3):
    print "坐标",x,y,"e级污区",wuqu3