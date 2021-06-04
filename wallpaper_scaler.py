# /usr/bin/env python3
from PIL import Image, ImageFilter
import sys

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print(f'usage: {sys.argv[0]} <image to make into wallpaper> [output file]')
    exit()

output = 'output.png'

if len(sys.argv) > 2:
    output = sys.argv[2]

base = Image.open(sys.argv[1])
blurimage = base.filter(ImageFilter.GaussianBlur(50))

# Change this to the Resolution of your monitor!
width = 3840
height = 2160

h_factor = (height // base.size[1])
w_factor = (width // base.size[0])

if h_factor == 0:
    num = (base.size[1] // height) + 1
    if num % 2 != 0:
        num += 1
    h_factor = 1/num

if (base.size[0] * w_factor) < width or w_factor == 0:
    w_factor += 1

blurimage = blurimage.resize(
    (base.size[0] * w_factor, base.size[1] * w_factor), Image.NEAREST)
vertical = (blurimage.size[1] - height) // 2
blurimage = blurimage.crop((0, vertical, width, height + vertical))

if h_factor >= 1:
    base = base.resize((int(base.size[0] * h_factor),
                        int(base.size[1] * h_factor)), Image.NEAREST)
else:
    base = base.resize(
        (int(base.size[0] * h_factor), int(base.size[1] * h_factor)), Image.NEAREST)


pos = ((width // 2) - (base.size[0] // 2), (height // 2) - (base.size[1] // 2))
blurimage.paste(base, pos)

blurimage.save(output)
