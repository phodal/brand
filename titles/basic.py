# coding=utf-8
import svgwrite

def generate_works():
    dwg = svgwrite.Drawing('basic.svg', size=(u'950', u'600'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))

    shapes.add(dwg.line((150, 250), (380, 250), stroke='#1A7906', stroke_width=140, transform="rotate(-15 0, 0)"))

    shapes.add(dwg.rect((240, 20), (200, 150), fill='#59B840', transform="rotate(15 0, 0)"))
    shapes.add(dwg.text('01', insert=(220, 230), fill='#fff', font_size=120, font_family='Helvetica', transform="rotate(-5 0, 0)"))

    shapes.add(dwg.rect((413, 76), (600, 250), fill='#59B840'))

    shapes.add(dwg.text('标题', insert=(450, 160), fill='#fff', font_size=70,
                        font_family='Helvetica'))
    shapes.add(dwg.line((440, 180), (930, 180), stroke='#5E6772', stroke_width=2))

    dwg.save()


if __name__ == '__main__':
    generate_works()