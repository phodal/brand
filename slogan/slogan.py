# coding=utf-8
import svgwrite


def generate_slogan():
    width = 600
    height = 50

    dwg = svgwrite.Drawing('slogan.svg', profile='full', size=(u'600', u'50'))

    mask = dwg.mask((0, 0), (600, height), id='a')
    mask.add(dwg.rect((0, 0), (600, height), fill='#eee', rx=5))

    dwg.add(mask)

    g = dwg.add(dwg.g(id='g', fill='none', mask='url(#a)'))
    g.add(dwg.rect((0, 0), (width / 3, height), fill='#03a9f4'))
    g.add(dwg.rect((width / 3, 0), (width / 3, height), fill='#f44336'))
    g.add(dwg.rect((width * 2 / 3, 0), (width * 2 / 3, height), fill='#ecf0f1'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.text('待我代码编成', insert=(10, 35), fill='#ecf0f1', font_size=30, font_family='Helvetica'))
    shapes.add(dwg.text('娶你为妻可好', insert=(210, 35), fill='#fff', font_size=30, font_family='Helvetica'))
    shapes.add(dwg.text('@hug8217', insert=(420, 35), fill='#34495e', font_size=30, font_family='Helvetica'))

    dwg.save()


if __name__ == '__main__':
    generate_slogan()
