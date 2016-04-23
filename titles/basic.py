# coding=utf-8
import svgwrite


def generate_works():
    dwg = svgwrite.Drawing('generate/basic.svg', size=(u'1200', u'600'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))

    for x in range(1, 150):
        shapes.add(dwg.line((250, 60 + x), (380, 0 + x), stroke='#59B840', stroke_width=1))

    for x in range(1, 150):
        shapes.add(dwg.line((380, 0 + x), (420, 60 + x), stroke='#1A7906', stroke_width=1))

    # color bg: #1A7906

    shapes.add(dwg.rect((420, 60), (950, 250), fill='#59B840'))

    shapes.add(dwg.text('标题', insert=(450, 240), fill='#fff', font_size=160,
                        font_family='Helvetica'))
    shapes.add(dwg.line((440, 280), (1180, 280), stroke='#fff', stroke_width=4))

    dwg.save()


if __name__ == '__main__':
    generate_works()
