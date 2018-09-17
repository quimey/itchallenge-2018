import json

vecs = {}

with open('shuffled_data_200.txt', 'r') as f:
    for j in range(64 * 16):
        a, b = eval(f.readline())
        vecs[a, b] = []
        for i in range(2):
            c, d = eval(f.readline())
            vecs[a, b].append((c, d))

rvecs = {}
for a in range(64):
    for b in range(16):
        rvecs[a, b] = []
        for c, d in vecs[a, b]:
            if (a, b) in vecs[c, d]:
                rvecs[a, b].append((c, d))

tiras = []
used = set()
for a in range(64):
    for b in range(16):
        if len(rvecs[a, b]) == 1 and (a, b) not in used:
            c, d = rvecs[a, b][0]
            tira = [(a, b), (c, d)]
            used.add((a, b))
            used.add((c, d))
            p = a
            q = b
            entro = True
            while len(rvecs[c, d]) > 1 and len(tira) < 64 and entro:
                entro = False
                for x, y in rvecs[c, d]:
                    if x != p or y != q:
                        if (x, y) in used:
                            break
                        tira.append((x, y))
                        used.add((x, y))
                        entro = True
                        p = c
                        q = d
                        c = x
                        d = y
            tiras.append(tira)

print(len(tiras), len(used))
tiras.sort(key=len, reverse=True)
#for t in tiras:
#    print(len(t))


from PIL import Image
import os
import random

images = []
img = []
N = 200
#for filename in sorted(os.listdir('shuffled')):
for i in range(N):
    filename = '{}.png'.format(i + 1)
    if len(images) >= N:
        break
    if filename[-3:] == 'pgm':
        continue
    try:
        im = Image.open(os.path.join('shuffled', filename))
        img.append(im)
        images.append(im.load())
        print(filename)
    except OSError:
        pass

rev = [6, 9, 13, 15] # manually inspected images
# generated with unsorted4.py and manuall inspection
order = [1, 11, 14, 2, 10, 12, 3, 8, 7, 15, 0, 9, 6, 13,4, 5]

for idx in range(N):
    new_image = Image.new(img[idx].mode, img[idx].size)
    pix = new_image.load()
    for i in range(16):
        for j, (a, b) in enumerate(tiras[i]):
            for v in range(4):
                s = 3 + j if i in rev else 63 - j
                if s < 64:
                    pix[4 * order.index(i) + v, s] = images[idx][4 * b + v, a]
    new_image.save('sarasas/sarasa{}'.format(os.path.basename(img[idx].filename)))
