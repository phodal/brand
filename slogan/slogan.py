# coding=utf-8
import svgwrite
from svgwrite.container import Hyperlink


def generate_slogan():
    width = 600
    height = 50

    dwg = svgwrite.Drawing('slogan.svg', profile='full', size=(u'540', u'50'))

    mask = dwg.mask((0, 0), (540, height), id='a')
    mask.add(dwg.rect((0, 0), (540, height), fill='#eee', rx=5))

    dwg.add(mask)

    g = dwg.add(dwg.g(id='g', fill='none', mask='url(#a)'))
    g.add(dwg.rect((0, 0), (width / 3, height), fill='#03a9f4'))
    g.add(dwg.rect((width / 3, 0), (width / 3, height), fill='#e91e63'))
    g.add(dwg.rect((width * 2 / 3, 0), (width * 2 / 3, height), fill='#ecf0f1'))

    slogan_link = Hyperlink('http://www.xuntayizhan.com/person/ji-ke-ai-qing-zhi-er-shi-dai-wo-dai-ma-bian-cheng-qu-ni-wei-qi-ke-hao-wan/', target='_blank')
    slogan_link.add(dwg.text('待我代码编成', insert=(10, 35), fill='#fff', font_size=30, font_family='STFangSong'))
    slogan_link.add(dwg.text('娶你为妻可好', insert=(210, 35), fill='#fff', font_size=30, font_family='STFangSong'))
    dwg.add(slogan_link)

    link = Hyperlink('http://www.hug8217.com/', target='_blank')
    link.add(dwg.text('@花仲马', insert=(410, 35), fill='#34495e', font_size=30, font_family='STFangSong'))

    dwg.add(link)

    dwg.save()


if __name__ == '__main__':
    generate_slogan()
