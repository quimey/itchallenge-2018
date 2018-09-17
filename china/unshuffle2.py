from PIL import Image
import os
import random

images = []
img = []
N = 200
for filename in os.listdir('shuffled'):
    if len(images) >= N:
        break
    if filename[-3:] == 'pgm':
        continue
    try:
        im = Image.open(os.path.join('shuffled', filename))
        img.append(im)
        images.append(im.load())
    except OSError:
        pass

def calc(a, b, c, d, i):
    s = 0
    for v in range(4):
        s += abs(images[i][b + v, a] - images[i][d + v, c])
    return s


def swap(a, b, c, d):
    for j in range(N):
        for k in range(4):
            tmp = images[j][4 * c + k, a]
            images[j][4 * c + k, a] = images[j][4 * d + k, b]
            images[j][4 * d + k, b] = tmp

vecs = {}
for a in range(64):
    for b in range(16):
        res = []
        for c in range(64):
            for d in range(16):
                s = 0
                for i in range(N):
                    s += calc(a, 4 * b, c, 4 * d, i)
                res.append((s, c, d))
        res.sort()
        print((a, b))
        for s, c, d in res[1: 3]:
            print((c, d))
