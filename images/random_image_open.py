import glob
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

images = glob.glob("*.jpg")


def front_view(TEXTINPUT):
    img = random.sample(images,1)
    font = ImageFont.truetype("msjhbd.ttc", 60)
    for image in img:
        with open(image, 'rb') as file:
            img = Image.open(file)
            draw1 = ImageDraw.Draw(img)
            draw1.text((0, 0),TEXTINPUT,(255,255,255),font=font)
            img.show()

def right_view(TEXTINPUT):
    img = random.sample(images,1)
    font = ImageFont.truetype("msjhbd.ttc", 60)
    for image in img:
        with open(image, 'rb') as file:
            img = Image.open(file)
            draw2 = ImageDraw.Draw(img)
            draw2.text((0, 0),TEXTINPUT,(255,255,255),font=font)
            img.show()

front_view("前視圖")
right_view("右視圖")