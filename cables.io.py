# -*- coding=utf-8 -*-
'''
读取cables_io.xls中的信息进行布线
'''
import svgwrite
import xlrd

def read_xls(file):
    xls= xlrd.open_workbook(file)
    table = xls.sheet_by_index(0)
    data = {}
    for i in range(table.nrows):
        data[table.row_values(i)[0]] = table.row_values(i)[1:]
    return data

print read_xls('cable_io.xls')

def station_draw(dwg,x,y):
    dwg.add(dwg.rect((x, y),(130,130), 0, 0))



def cable_draw(dwg,x,y,cables):
    direction = {u"南":(x+65,y+130,10,0),
                 u"北":(x+65,y,-10,0),
                 u"西":(x,y+65,0,-10),
                 u"东":(x+130,y+65,0,10)}
    for i in range(len(cables)-1):
        cable = []
        print cables[i+1][0],i
        dir = cables[i+1][0]
        num = cables[i+1][1]
        vol = cables[i+1][2]
        name = cables[i+1][3]
        s_x,s_y,move_x,move_y = direction[dir]
        print dir,x,y,direction
        for j in range(int(num)):
            start_x = s_x+j*move_x
            start_y = s_y+j*move_y
            start_point = (start_x,start_y)
            end_x = start_x + 10*move_y
            end_y = start_y + 10*move_x
            end_point = (end_x,end_y)
            dwg.add(dwg.line(start_point, end_point, stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.add(dwg.text(dir, end_point, fill='red'))
        print start_point,end_point

dwg1 = svgwrite.Drawing('test.svg', profile='tiny')
station_draw(dwg1,400,400)
cables_xls = read_xls('cable_io.xls')
cable_draw(dwg1,400,400,cables_xls)
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