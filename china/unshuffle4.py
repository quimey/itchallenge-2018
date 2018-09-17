from PIL import Image
import os
import random

images = []
img = []
N = 200
for filename in os.listdir('sarasas'):
    if len(images) >= N:
        break
    if filename[-3:] == 'pgm':
        continue
    try:
        im = Image.open(os.path.join('sarasas', filename))
        img.append(im)
        images.append(im.load())
    except OSError:
        pass

def calc(b, d, i):
    s = 0
    for v in range(64):
        s += abs(images[i][4 * b, v] - images[i][4 * d, v])
    return s

vecs = {}
for b in range(16):
    res = []
    for d in range(16):
        s = 0
        for i in range(N):
            s += calc(b, d, i)
        res.append((s, d))
    res.sort()
    print(b)
    for s, d in res[1: 3]:
        print(d, s)
    print("--")
