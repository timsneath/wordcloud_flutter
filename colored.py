# Example tweaked from:
#  https://amueller.github.io/word_cloud/auto_examples/colored.html

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'survey.txt')).read()

# read the mask / color image
logo_coloring = np.array(Image.open(path.join(d, "logo_color_large.png")))


wc = WordCloud(font_path="/Library/Fonts/GoogleSans-Regular-v1.27.ttf",
               background_color="white", max_words=1000, mask=logo_coloring,
               relative_scaling=0, random_state=42)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(logo_coloring)

# show
fig, axes = plt.subplots(1, 2)
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
axes[0].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
axes[1].imshow(logo_coloring, cmap=plt.cm.gray, interpolation="bilinear")
for ax in axes:
    ax.set_axis_off()
plt.show()
