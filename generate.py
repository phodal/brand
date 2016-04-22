import random

import svgwrite


def generate_idea():
    dwg = svgwrite.Drawing('shields/idea.svg', profile='full', size=(u'1006', u'150'))
    y_text_split = 641
    height = 150
    rect_length = 10
    width = 1206
    max_rect_length = 40

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (640, 150), fill='#5E6772'))
    shapes.add(dwg.rect((640, 0), (366, 150), fill='#2196F3'))
    shapes.add(dwg.text('PHODAL', insert=(83, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

    for x in range(y_text_split + rect_length, width, rect_length):
        shapes.add(dwg.line((x, 0), (x, height), stroke='#EEEEEE', stroke_opacity=0.3))

    for y in range(rect_length, height, rect_length):
        shapes.add(dwg.line((y_text_split, y), (width, y), stroke='#EEEEEE', stroke_opacity=0.3))

    for x in range(y_text_split + max_rect_length, width, max_rect_length):
        for y in range(0, height, max_rect_length):
            shapes.add(dwg.line((x, y - 4), (x, y + 4), stroke='#EEEEEE', stroke_width='2', stroke_opacity=0.4))

    for y in range(0, height, max_rect_length):
        for x in range(y_text_split + max_rect_length, width, max_rect_length):
            shapes.add(dwg.line((x - 4, y), (x + 4, y), stroke='#EEEEEE', stroke_width='2', stroke_opacity=0.4))

    shapes.add(dwg.text('idea', insert=(704, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))
    dwg.save()


def generate_article():
    dwg = svgwrite.Drawing('shields/article.svg', size=(u'1086', u'150'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (640, 150), fill='#5E6772'))
    shapes.add(dwg.rect((640, 0), (446, 150), fill='#2196F3'))
    shapes.add(dwg.text('PHODAL', insert=(83, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))
    shapes.add(dwg.text('article', insert=(704, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

    dwg.save()


def get_some_random10(num):
    results = ''
    for x in range(1, num):
        results += str(random.getrandbits(1))
    return results


def generate_works():
    dwg = svgwrite.Drawing('shields/works.svg', size=(u'1066', u'150'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))

    shapes.add(dwg.rect((640, 0), (426, 150), fill='#2c3e50'))
    for x in range(0, 300, 10):
        text = get_some_random10(100)
        shapes.add(
            dwg.text(text, insert=(641, x), fill='#27ae60', font_size=12, font_family='Inconsolata for Powerline',
                     opacity=0.3, transform="rotate(15 1200, 0)"))

    shapes.add(dwg.rect((0, 0), (640, 150), fill='#5E6772'))
    shapes.add(dwg.text('PHODAL', insert=(83, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))
    shapes.add(dwg.text('works', insert=(704, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

    dwg.save()


def generate_design():
    dwg = svgwrite.Drawing('shields/design.svg', size=(u'1126', u'150'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (640, 150), fill='#5E6772'))

    shapes.add(dwg.rect((640, 90), (486, 60), fill='#03a9f4'))
    shapes.add(dwg.text('design', insert=(706, 120), fill='#000', stroke_width=4, font_size=120, font_family='Helvetica'))
    shapes.add(dwg.rect((640, 0), (486, 90), fill='#00bcd4'))
    #shapes.add(dwg.rect((640, 88), (486, 3), fill='#e91e63'))
    shapes.add(dwg.rect((640, 90), (486, 0.5), fill='#000'))
    shapes.add(dwg.text('design', insert=(704, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

    #for D Rect
    shapes.add(dwg.line((700, 25), (700, 130), stroke='#EEEEEE', stroke_width='1', stroke_opacity=0.3, stroke_dasharray="3,3"))
    shapes.add(dwg.line((770, 25), (770, 130), stroke='#EEEEEE', stroke_width='1', stroke_opacity=0.3, stroke_dasharray="3,3"))
    shapes.add(dwg.line((700, 25), (770, 25), stroke='#EEEEEE', stroke_width='1', stroke_opacity=0.3, stroke_dasharray="3,3"))
    shapes.add(dwg.line((700, 130), (770, 130), stroke='#EEEEEE', stroke_width='1', stroke_opacity=0.3, stroke_dasharray="3,3"))

    shapes.add(dwg.text('PHODAL', insert=(83, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

    dwg.save()


def generate_cool_deisgn():
    y_text_split = 841
    height = 150
    rect_length = 10
    width = 1206
    max_rect_length = 40

    dwg = svgwrite.Drawing('shields/cool-idea.svg', profile='full', size=(u'1206', u'150'))
    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (y_text_split, height), fill='#5E6772'))
    shapes.add(dwg.rect((y_text_split, 0), (366, height), fill='#2196F3'))
    shapes.add(dwg.text('PHODAL', insert=(-18, height), fill='#FFFFFF', font_size=210, font_family='Helvetica'))

    for x in range(y_text_split + rect_length, width, rect_length):
        shapes.add(dwg.line((x, 0), (x, height), stroke='#EEEEEE', stroke_opacity=0.3))

    for y in range(rect_length, height, rect_length):
        shapes.add(dwg.line((y_text_split, y), (width, y), stroke='#EEEEEE', stroke_opacity=0.3))

    for x in range(y_text_split + max_rect_length, width, max_rect_length):
        for y in range(0, height, max_rect_length):
            shapes.add(dwg.line((x, y - 4), (x, y + 4), stroke='#EEEEEE', stroke_width='2', stroke_opacity=0.4))

    for y in range(0, height, max_rect_length):
        for x in range(y_text_split + max_rect_length, width, max_rect_length):
            shapes.add(dwg.line((x - 4, y), (x + 4, y), stroke='#EEEEEE', stroke_width='2', stroke_opacity=0.4))

    shapes.add(dwg.text('idea', insert=(920, 119), fill='#fff', font_size=120, font_family='Helvetica'))
    dwg.save()


generate_idea()
generate_article()
#generate_works()
generate_design()
generate_cool_deisgn()
