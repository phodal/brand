# coding=utf-8
import ConfigParser
import svgwrite

ConfigColor = ConfigParser.ConfigParser()
ConfigColor.read("./color.ini")

bg_colors = []
font_colors = []


def generate_title_by_colors(color_name, bg_color, font_color):
    dwg = svgwrite.Drawing('generate/cover/' + color_name + '.svg', size=(u'950', u'500'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))

    shapes.add(dwg.rect((0, 0), (950, 500), fill='#' + bg_color))
    shapes.add(dwg.text('JavaScript', insert=(475, 190), fill='#' + font_color, font_size=120,
                        style="text-anchor: middle; dominant-baseline: hanging;",
                        font_family='Helvetica'))

    dwg.save()


def generate_cover_titles():
    for color_name, color in ConfigColor.items('Color'):
        bg_color = color.replace('#', '').split(',')[0]
        font_color = color.replace('#', '').split(',')[1]

        generate_title_by_colors(color_name, bg_color, font_color)


def generate_article_title(color_name, bg_color, font_color):
    bg_color = '#' + bg_color
    font_color = '#' + font_color

    dwg = svgwrite.Drawing('generate/titles/' + color_name + '.svg', size=(u'950', u'300'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))

    shapes.add(dwg.rect((0, 0), (950, 500), fill=bg_color))
    shapes.add(dwg.text('PHODAL', insert=(475, 50), fill=font_color, font_size=22,
                        style="text-anchor: middle; dominant-baseline: hanging;",
                        font_family='Helvetica'))
    shapes.add(dwg.rect((220, 54), (200, 10), fill=font_color))
    shapes.add(dwg.rect((530, 54), (200, 10), fill=font_color))

    shapes.add(dwg.text('这是一个标题', insert=(475, 100), fill=font_color, font_size=120,
                        style="text-anchor: middle; dominant-baseline: hanging;",
                        font_family='Helvetica'))

    shapes.add(dwg.text('CREATE & SHARE', insert=(475, 220), fill=font_color, font_size=22,
                        style="text-anchor: middle; dominant-baseline: hanging;",
                        font_family='Helvetica'))

    shapes.add(dwg.rect((50, 225), (320, 5), fill=font_color))
    shapes.add(dwg.rect((580, 225), (320, 5), fill=font_color))

    dwg.save()


def generate_article_titles():
    for color_name, color in ConfigColor.items('Color'):
        bg_color = color.replace('#', '').split(',')[0]
        font_color = color.replace('#', '').split(',')[1]

        generate_article_title(color_name, bg_color, font_color)


if __name__ == '__main__':
    generate_cover_titles()
    generate_article_titles()
