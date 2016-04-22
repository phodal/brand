#!/usr/bin/env python2
"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path

import numpy as np
from PIL import Image
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'article.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
origin_image = Image.open(path.join(d, "map.png"))
alice_mask = np.array(origin_image)

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               width=1423, height=601, mode="RGBA")
# generate word cloud
wc.generate(text)

text_cloud_image = wc.to_image()

text_cloud_image.save('out.png')

img = text_cloud_image.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.show()

origin_image.paste(img, (0, 0), img)
origin_image.show()
origin_image.save("bg.png", "PNG")

