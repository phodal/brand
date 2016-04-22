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


def generate_works():
  dwg = svgwrite.Drawing('shields/design.svg', size=(u'1126', u'150'))

  shapes = dwg.add(dwg.g(id='shapes', fill='none'))
  shapes.add(dwg.rect((0, 0), (640, 150), fill='#5E6772'))
  shapes.add(dwg.rect((640, 0), (486, 150), fill='#2196F3'))
  shapes.add(dwg.text('PHODAL', insert=(83, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))
  shapes.add(dwg.text('design', insert=(704, 122), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

  dwg.save()

generate_idea()
generate_article()
generate_works()
generate_works()
