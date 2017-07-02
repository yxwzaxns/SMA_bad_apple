#!/usr/bin/env python3

import os, sys
import base64

indir = sys.argv[1]
outdir = sys.argv[2]

for root, dirs, filenames in os.walk(indir):
    for infile in filenames:
        print('start {} '.format(f))
        with open(os.path.join(indir, infile), 'rb') as f:
            name = f[:-3]+'txt'
            baseed = base64.b64encode(f.read() )
            with open(os.path.join(outdir, name), 'w') as f1:
                f1.write(baseed)
