#!/usr/bin/env python2
from os import path

import numpy as np
from PIL import Image
from wordcloud import WordCloud
import ConfigParser

ConfigColor = ConfigParser.ConfigParser()
ConfigColor.read("./color.ini")

d = path.dirname(__file__)

text = open(path.join(d, 'lang.txt')).read()

origin_image = Image.open(path.join(d, "map.png"))
img = origin_image.convert("RGBA")
datas = img.getdata()

newData = []
bg_color = datas[0]
for item in datas:
    if item[0] == bg_color[0] and item[1] == bg_color[1] and item[2] == bg_color[2]:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)

alice_mask = np.array(img)

wc = WordCloud(background_color=None, max_words=2000, mask=alice_mask, max_font_size=6,
               width=1423, height=601, mode="RGBA")
# generate word cloud
wc.generate(text)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def get_font_color(bg):
    color = bg[0], bg[1], bg[2]
    bg_hex = rgb_to_hex(color)
    for color_name, color in ConfigColor.items('Color'):
        color_bg = color.split(',')[0]
        if color_bg == bg_hex:
            return color.split(',')[1]

font_color = hex_to_rgb(get_font_color(bg_color))

text_cloud_image = wc.to_image()

text_cloud_image.show()
text_cloud_image.save('out.png')
