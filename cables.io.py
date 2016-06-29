# -*- coding=utf-8 -*-
'''
读取cables_io.xls中的信息进行布线;
xls文件中表头格式"序号	出线方向	回路数	电压等级	名称"

'''
import svgwrite
import xlrd

#读取xls中数据
def read_xls(file):
    xls= xlrd.open_workbook(file)
    table = xls.sheet_by_index(0)
    data = {}
    for i in range(table.nrows):
        data[table.row_values(i)[0]] = table.row_values(i)[1:]
    return data

#绘制变电站
def station_draw(dwg,x,y):
    dwg.add(dwg.rect((x, y),(130,130), 0, 0))

#绘制出线
def cable_draw(dwg,x,y,cables):
    #方向与坐标对应表
    direction = {u"南":(x+65,y+130,10,0),
                 u"北":(x+65,y,-10,0),
                 u"西":(x,y+65,0,-10),
                 u"东":(x+130,y+65,0,10)}
    #分条目绘制进出线
    for i in range(len(cables)-1):

        print cables[i+1][0],i
        dir = cables[i+1][0] #方向
        num = cables[i+1][1] #回路数
        vol = cables[i+1][2] #电压等级
        name = cables[i+1][3] #路名
        s_x,s_y,move_x,move_y = direction[dir] #根据方向读取坐标

        print dir,x,y,direction
        for j in range(int(num)):

            start_x = s_x+j*move_x
            start_y = s_y+j*move_y
            start_point = (start_x,start_y) #起始点坐标

            end_x = start_x + 10*move_y
            end_y = start_y + 10*move_x
            end_point = (end_x,end_y) #终点坐标

            dwg.add(dwg.line(start_point, end_point, stroke=svgwrite.rgb(10, 10, 16, '%')))

        dwg.add(dwg.text(name+'('+str(int(vol))+')', end_point, fill='red'))

        print start_point,end_point

dwg1 = svgwrite.Drawing('test.svg', profile='tiny')
#变电站起始坐标
station_x = 400
station_y = 400
#绘制变电站
station_draw(dwg1,station_x,station_y)
#读取进出线数据
cables_xls = read_xls('cable_io.xls')
#绘制进出线
cable_draw(dwg1,station_x,station_y,cables_xls)
#保存矢量图
dwg1.save()

'''
    for
    if
    dwg.add(dwg.line)

dwg1 = svgwrite.Drawing('test.svg', profile='tiny')
station_draw(dwg1,500,500)

dwg.add(dwg.line((0, 0), (100, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
m = (100,100)
dwg.add(dwg.rect((200,200),m,0,0))
dwg.add(dwg.text('Test', insert=(0, 65), fill='red'))
dwg.save()
'''
'''
import svgwrite
from svgwrite import cm, mm

def basic_shapes(name):
    dwg = svgwrite.Drawing(filename=name, debug=True)
    hlines = dwg.add(dwg.g(id='hlines', stroke='green'))
    for y in range(20):
        hlines.add(dwg.line(start=(2*cm, (2+y)*cm), end=(18*cm, (2+y)*cm)))
    vlines = dwg.add(dwg.g(id='vline', stroke='blue'))
    for x in range(17):
        vlines.add(dwg.line(start=((2+x)*cm, 2*cm), end=((2+x)*cm, 21*cm)))
    shapes = dwg.add(dwg.g(id='shapes', fill='red'))

    # set presentation attributes at object creation as SVG-Attributes
    shapes.add(dwg.circle(center=(15*cm, 8*cm), r='2.5cm', stroke='blue',
                          stroke_width=3))

    # override the 'fill' attribute of the parent group 'shapes'
    shapes.add(dwg.rect(insert=(5*cm, 5*cm), size=(45*mm, 45*mm),
                        fill='blue', stroke='red', stroke_width=3))

    # or set presentation attributes by helper functions of the Presentation-Mixin
    ellipse = shapes.add(dwg.ellipse(center=(10*cm, 15*cm), r=('5cm', '10mm')))
    ellipse.fill('green', opacity=0.5).stroke('black', width=5).dasharray([20, 20])
    dwg.save()

if __name__ == '__main__':
    basic_shapes('basic_shapes.svg')
'''