import svgwrite


def generate_idea():
    dwg = svgwrite.Drawing('shields/idea.svg', profile='full', size=(u'1006', u'150'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (640, 150), fill='#5E6772'))
    shapes.add(dwg.rect((640, 0), (366, 150), fill='#2196F3'))
    shapes.add(dwg.text('PHODAL', insert=(83, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))
    shapes.add(dwg.text('idea', insert=(704, 122), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

    dwg.save()


def generate_article():
    dwg = svgwrite.Drawing('shields/article.svg', size=(u'1086', u'150'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (640, 150), fill='#5E6772'))
    shapes.add(dwg.rect((640, 0), (446, 150), fill='#2196F3'))
    shapes.add(dwg.text('PHODAL', insert=(83, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))
    shapes.add(dwg.text('article', insert=(704, 122), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

    dwg.save()


def generate_works():
    dwg = svgwrite.Drawing('shields/works.svg', size=(u'1066', u'150'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (640, 150), fill='#5E6772'))
    shapes.add(dwg.rect((640, 0), (426, 150), fill='#2196F3'))
    shapes.add(dwg.text('PHODAL', insert=(83, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))
    shapes.add(dwg.text('works', insert=(704, 122), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

    dwg.save()


def generate_design():
    dwg = svgwrite.Drawing('shields/design.svg', size=(u'1126', u'150'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (640, 150), fill='#5E6772'))
    shapes.add(dwg.rect((640, 0), (486, 150), fill='#2196F3'))
    shapes.add(dwg.text('PHODAL', insert=(83, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))
    shapes.add(dwg.text('design', insert=(704, 122), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

    dwg.save()


def generate_cool_deisgn():
    dwg = svgwrite.Drawing('shields/cool-idea.svg', profile='full', size=(u'1206', u'150'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))
    shapes.add(dwg.rect((0, 0), (841, 150), fill='#5E6772'))
    shapes.add(dwg.rect((841, 0), (366, 150), fill='#2196F3'))
    shapes.add(dwg.text('PHODAL', insert=(-18, 150), fill='#FFFFFF', font_size=210, font_family='Helvetica'))

    for x in range(861, 1206, 20):
        shapes.add(dwg.line((x, 0), (x, 150), stroke='#EEEEEE'))

    for y in range(20, 150, 20):
        shapes.add(dwg.line((841, y), (1206, y), stroke='#EEEEEE'))

    shapes.add(dwg.text('idea', insert=(920, 122), fill='#fff', font_size=120, font_family='Helvetica'))
    dwg.save()


generate_idea()
generate_article()
generate_works()
generate_design()
generate_cool_deisgn()
