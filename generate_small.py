import random

import svgwrite

phodal_width = 176
secondary_text_x = 200
basic_text_y = 35


def generate_idea():
    y_text_split = phodal_width + 1
    height = 50
    rect_length = 2
    width = 290
    max_rect_length = 10

    dwg = svgwrite.Drawing('shields/idea-small.svg', profile='full', size=(u'290', u'50'))

    a_mask = dwg.mask((0, 0), (width, height), id='a')
    a_mask.add(dwg.rect((0, 0), (width, height), fill='#eee', rx=3))
    dwg.add(a_mask)

    g = dwg.add(dwg.g(id='g', fill='none', mask='url(#a)'))
    g.add(dwg.rect((0, 0), (phodal_width, height), fill='#5E6772'))
    g.add(dwg.rect((phodal_width, 0), (width - phodal_width, height), fill='#2196F3'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))

    shapes.add(dwg.text('phodal', insert=(28, basic_text_y + 1), fill='#000', fill_opacity=0.3, font_size=40,
                        font_family='Helvetica'))
    shapes.add(dwg.text('phodal', insert=(27, basic_text_y), fill='#FFFFFF', font_size=40, font_family='Helvetica'))

    def draw_for_bg_plus():
        for x in range(y_text_split + rect_length, width, rect_length):
            shapes.add(dwg.line((x, 0), (x, height), stroke='#EEEEEE', stroke_width='0.5', stroke_opacity=0.1))

        for y in range(rect_length, height, rect_length):
            shapes.add(
                dwg.line((y_text_split, y), (width, y), stroke='#EEEEEE', stroke_width='0.5', stroke_opacity=0.1))

        for x in range(y_text_split + max_rect_length, width, max_rect_length):
            for y in range(0, height, max_rect_length):
                shapes.add(dwg.line((x, y - 2), (x, y + 2), stroke='#EEEEEE', stroke_width='0.8', stroke_opacity=0.15))

        for y in range(0, height, max_rect_length):
            for x in range(y_text_split + max_rect_length, width, max_rect_length):
                shapes.add(dwg.line((x - 2, y), (x + 2, y), stroke='#EEEEEE', stroke_width='0.8', stroke_opacity=0.15))

    draw_for_bg_plus()

    shapes.add(
        dwg.text('idea', insert=(secondary_text_x + 1, basic_text_y + 1), fill='#000', font_size=40, fill_opacity=0.3,
                 font_family='Helvetica'))
    shapes.add(dwg.text('idea', insert=(secondary_text_x, basic_text_y), fill='#FFFFFF', font_size=40,
                        font_family='Helvetica'))
    dwg.save()


def generate_article():
    dwg = svgwrite.Drawing('shields/article-small.svg', size=(u'323', u'50'))

    height = 50
    width = 323

    a_mask = dwg.mask((0, 0), (width, height), id='a')
    a_mask.add(dwg.rect((0, 0), (width, height), fill='#eee', rx=3))
    dwg.add(a_mask)

    g = dwg.add(dwg.g(id='g', fill='none', mask='url(#a)'))
    g.add(dwg.rect((0, 0), (phodal_width, height), fill='#5E6772'))
    g.add(dwg.rect((phodal_width, 0), (width - phodal_width, height), fill='#ffeb3b'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.text('phodal', insert=(28, basic_text_y + 1), fill='#000', fill_opacity=0.3, font_size=40,
                        font_family='Helvetica'))
    shapes.add(dwg.text('phodal', insert=(27, basic_text_y), fill='#FFFFFF', font_size=40, font_family='Helvetica'))

    shapes.add(dwg.text(insert=(phodal_width, 6), fill='#34495e', opacity=0.2, font_size=4,
                        text='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, fe-'))
    shapes.add(dwg.text(insert=(phodal_width, 12), fill='#34495e', opacity=0.2, font_size=4,
                        text='ugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi'))
    shapes.add(dwg.text(insert=(phodal_width, 18), fill='#34495e', opacity=0.2, font_size=4,
                        text='vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, '))
    shapes.add(dwg.text(insert=(phodal_width, 24), fill='#34495e', opacity=0.2, font_size=4,
                        text='condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum '))
    shapes.add(dwg.text(insert=(phodal_width, 30), fill='#34495e', opacity=0.2, font_size=4,
                        text='rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus,'))
    shapes.add(dwg.text(insert=(phodal_width, 36), fill='#34495e', opacity=0.2, font_size=4,
                        text=' neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi,'))
    shapes.add(dwg.text(insert=(phodal_width, 42), fill='#34495e', opacity=0.2, font_size=4,
                        text=' tincidunt quis, accumsan porttitor, facilisis luctus, metus'))
    shapes.add(dwg.text(insert=(phodal_width, 48), fill='#34495e', opacity=0.2, font_size=4,
                        text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus magna. Cras in mi at felis aliquet congue. Ut a est eget '))
    shapes.add(dwg.text(insert=(phodal_width, 54), fill='#34495e', opacity=0.2, font_size=4,
                        text='ligula molestie gravida. Curabitur massa. Donec eleifend, libero at sagittis mollis, tellus est malesuada tellus, at luctus '))
    shapes.add(dwg.text(insert=(phodal_width, 60), fill='#34495e', opacity=0.2, font_size=4,
                        text='turpis elit sit amet quam. Vivamus pretium ornare est.'))

    shapes.add(dwg.text('article', insert=(secondary_text_x + 1, basic_text_y + 1), fill='#000', fill_opacity=0.3,
                        font_size=40, font_family='Helvetica'))
    shapes.add(dwg.text('article', insert=(secondary_text_x, basic_text_y), fill='#34495e', font_size=40,
                        font_family='Helvetica'))

    dwg.save()


def get_some_random10(num):
    results = ''
    for x in range(1, num):
        results += str(random.getrandbits(1))
    return results


def generate_works():
    dwg = svgwrite.Drawing('shields/works-small.svg', size=(u'316', u'50'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))

    shapes.add(dwg.rect((phodal_width, 0), (142, 50), fill='#2c3e50'))
    for x in range(0, 100, 5):
        text = get_some_random10(100)
        shapes.add(
            dwg.text(text, insert=(phodal_width + 1, x), fill='#27ae60', font_size=4,
                     font_family='Inconsolata for Powerline',
                     opacity=0.3, transform="rotate(15 300, 0)"))

    shapes.add(dwg.rect((0, 0), (phodal_width, 50), fill='#5E6772'))
    shapes.add(dwg.text('phodal', insert=(28, basic_text_y + 1), fill='#000', fill_opacity=0.3, font_size=40,
                        font_family='Helvetica'))
    shapes.add(dwg.text('phodal', insert=(27, basic_text_y), fill='#FFFFFF', font_size=40, font_family='Helvetica'))
    shapes.add(
        dwg.text('works', insert=(secondary_text_x + 1, basic_text_y + 1), fill='#000', fill_opacity=0.3, font_size=40,
                 font_family='Helvetica'))
    shapes.add(dwg.text('works', insert=(secondary_text_x, basic_text_y), fill='#FFFFFF', font_size=40,
                        font_family='Helvetica'))

    dwg.save()


def generate_design():
    dwg = svgwrite.Drawing('shields/design-small.svg', size=(u'338', u'50'))

    # for D Rect
    red_point = 272
    design_width = 162

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (phodal_width, 50), fill='#5E6772'))

    def draw_design_word():
        shapes.add(dwg.rect((phodal_width, 25.6), (design_width, 30), fill='#2196f3'))
        shapes.add(dwg.text('design', insert=(secondary_text_x + 5, 36), fill='#000', stroke_width=4, font_size=40,
                            font_family='Helvetica'))
        shapes.add(dwg.rect((phodal_width, 0), (design_width, 26), fill='#03a9f4'))
        # shapes.add(dwg.rect((phodal_width, 88), (486, 3), fill='#e91e63'))
        shapes.add(dwg.rect((phodal_width, 25.6), (design_width, 0.6), fill='#000'))
        shapes.add(dwg.text('design', insert=(secondary_text_x + 4, basic_text_y), fill='#FFFFFF', font_size=40,
                            font_family='Helvetica'))

    def draw_red_point():
        shapes.add(dwg.ellipse((red_point, 8), (3, 3), fill='#000'))
        shapes.add(dwg.ellipse((red_point + 1, 8), (3, 3), fill='#f44336'))

    draw_design_word()
    draw_red_point()

    shapes.add(dwg.text('phodal', insert=(28, basic_text_y + 1), fill='#000', fill_opacity=0.3, font_size=40,
                        font_family='Helvetica'))
    shapes.add(dwg.text('phodal', insert=(27, basic_text_y), fill='#FFFFFF', font_size=40, font_family='Helvetica'))

    dwg.save()


generate_idea()
generate_article()
# generate_works()
generate_design()
