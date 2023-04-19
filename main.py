import os
import glob
from PIL import ImageFilter, Image
os.chdir("9.1")
a=os.getcwd()
if not os.path.isdir("new"):
     os.mkdir("new")
for img in glob.glob('*.jpg'):
    imgs=os.listdir()
    with Image.open(img) as im:
        im.load()
        nim = im.filter(ImageFilter.CONTOUR)
        os.chdir("new")
        nim.save("new_" + img)
        os.chdir(a)
