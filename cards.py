import PIL
from PIL import Image
import os

#5:7 Aspect ratio that is larger than cardface pngs
CARD_SIZE = (260, 364)

#adds background to transparent card faces found in /card_faces
def add_background(path):

   img = Image.open(path)
   
   dimensions = img.size
   background = Image.open('card_background.png')
   bg_w, bg_h = background.size
   #centers cardface on card
   offset = ((bg_w - dimensions[0]) // 2, (bg_h - dimensions[1]) // 2)
   background.paste(img, offset, img)
   img = background
   dimensions = img.size
   img.save(f'cards/{path.split("/")[-1]}')

l = os.listdir('card_faces')
for card in l:
   add_background(f'card_faces/{card}')
