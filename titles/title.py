# coding=utf-8
import ConfigParser
import svgwrite

ConfigColor = ConfigParser.ConfigParser()
ConfigColor.read("./color.ini")

bg_colors = []
font_colors = []


def generate_works(color_name, bg_color, font_color):
    dwg = svgwrite.Drawing('generate/titles/' + color_name + '.svg', size=(u'950', u'500'))

    shapes = dwg.add(dwg.g(id='shapes', fill='none'))

    shapes.add(dwg.rect((0, 0), (950, 500), fill='#' + bg_color))
    shapes.add(dwg.text('JavaScript', insert=(475, 190), fill='#' + font_color, font_size=120, style="text-anchor: middle; dominant-baseline: hanging;",
                        font_family='Helvetica'))

    dwg.save()


if __name__ == '__main__':
    for color_name, color in ConfigColor.items('Color'):
        bg_color = color.replace('#', '').split(',')[0]
        font_color = color.replace('#', '').split(',')[1]

        generate_works(color_name, bg_color, font_color)
