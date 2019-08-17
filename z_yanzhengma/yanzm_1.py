from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from code_1 import code

img = Image.new("RGB", (150,50), (255,255,255))

draw = ImageDraw.Draw(img)
for _ in range(10):
    draw.point(
        ( random.randint(0,150), random.randint(0,50)),   #坐标
        fill = (0,0,0))   #颜色
for _ in range(10):
    draw.line([(random.randint(0,150),random.randint(0,50)),
           (random.randint(0,150),random.randint(0,50))],
          fill=(150,150,2))

font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf", 24)
draw.text((20,10), code, font=font, fill="green")
img.show()
img.save('code.jpg')