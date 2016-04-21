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
  dwg = svgwrite.Drawing('shields/article.svg', size=(u'1286', u'150'))

  shapes = dwg.add(dwg.g(id='shapes', fill='none'))
  shapes.add(dwg.rect((0, 0), (640, 150), fill='#5E6772'))
  shapes.add(dwg.rect((640, 0), (446, 150), fill='#2196F3'))
  shapes.add(dwg.text('PHODAL', insert=(83, 119), fill='#FFFFFF', font_size=120, font_family='Helvetica'))
  shapes.add(dwg.text('article', insert=(704, 122), fill='#FFFFFF', font_size=120, font_family='Helvetica'))

  dwg.save()

generate_idea()
generate_article()