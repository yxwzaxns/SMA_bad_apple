#!/usr/bin/env python3

from PIL import Image
import os, sys

indir = sys.argv[1]
outdir = sys.argv[2]

for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        print('start {} '.format(f))
        name = f[:-3]+'txt'
        im = Image.open(os.path.join(root, f))
        rgb_im = im.convert('RGB')
        with open(os.path.join(outdir, name), 'w') as f:
            for y in [y for y in range(240)]:
                cow = ''
                for x in [x for x in range(320)]:
                    r, g, b = rgb_im.getpixel((x, y))
                    if r <= 200 or g <= 200 or b <= 200:
                        cow += '1'
                    else:
                        cow += '0'
                cow += '\n'
                f.write(cow)
        im.close()
