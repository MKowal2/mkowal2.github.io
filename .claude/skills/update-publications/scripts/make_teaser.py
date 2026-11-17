"""Crop a figure to a website teaser image.

Usage: python3 make_teaser.py <input image> <x0> <y0> <x1> <y1> <output path>
  - x0,y0,x1,y1 are FRACTIONS (0-1) of the input width/height, so you can pick them by
    eyeballing a downscaled preview.
  - Output is padded with the corner background color to the 14:9 card aspect
    (cards render at 280x180 with object-fit: cover), and resized to <=1400px wide.
  - Output format follows the extension: use .jpg for photo-heavy figures (PNG > ~600KB).
Also: python3 make_teaser.py --preview <input> <out.png>   (writes a <=1400px preview)
      python3 make_teaser.py --sheet <out.png> <img1> <img2> ...   (contact sheet at card size)
"""
import sys
from PIL import Image, ImageDraw
A = 14 / 9
args = sys.argv[1:]
if args[0] == '--preview':
    im = Image.open(args[1]).convert('RGB'); im.thumbnail((1400, 1400)); im.save(args[2]); sys.exit()
if args[0] == '--sheet':
    out, fs = args[1], args[2:]
    rows = (len(fs) + 1) // 2
    sheet = Image.new('RGB', (1190, rows * 415 + 10), 'white'); d = ImageDraw.Draw(sheet)
    for i, f in enumerate(fs):
        x, y = 10 + (i % 2) * 590, 10 + (i // 2) * 415
        sheet.paste(Image.open(f).convert('RGB').resize((560, 360)), (x, y)); d.text((x, y + 365), f.split('/')[-1], fill='black')
    sheet.save(out); sys.exit()
src, x0, y0, x1, y1, out = args[0], *map(float, args[1:5]), args[5]
im = Image.open(src).convert('RGB')
c = im.crop((int(x0 * im.width), int(y0 * im.height), int(x1 * im.width), int(y1 * im.height)))
w, h = c.size
W, H = (w, round(w / A)) if w / h > A else (round(h * A), h)
canvas = Image.new('RGB', (W, H), c.getpixel((2, 2))); canvas.paste(c, ((W - w) // 2, (H - h) // 2))
if canvas.width > 1400: canvas = canvas.resize((1400, round(1400 / A)), Image.LANCZOS)
kw = {'quality': 86} if out.lower().endswith(('.jpg', '.jpeg')) else {}
canvas.save(out, optimize=True, **kw)
print(out, canvas.size)
