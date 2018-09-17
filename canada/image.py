from PIL import Image
from collections import defaultdict, deque

f = Image.open('ImagenIndescifrable.png')
print(f.size)

p = f.load()

a = defaultdict(list)
b = defaultdict(list)
c = defaultdict(list)
d = defaultdict(list)

vertex = []
up = defaultdict(list)
down = defaultdict(list)
left = defaultdict(list)
right = defaultdict(list)

for i in range(20):
    for j in range(20):
        data = {}
        for k in range(49):
            for l in range(49):
                data[(k, l)] = p[50 * i + 1 + k, 50 * j + 1 + l]
        index = i * 20 + j
        data['left'] = (data[(0, 0)], data[(48, 0)])
        data['up'] = (data[(0, 0)], data[(0, 48)])
        data['right'] = (data[(0, 48)], data[(48, 48)])
        data['down'] = (data[(48, 0)], data[(48, 48)])
        vertex.append(data)

        a[data['left']].append(index)
        b[data['up']].append(index)
        c[data['right']].append(index)
        d[data['down']].append(index)

for index, data in enumerate(vertex):
    up[index].extend(d[data['up']])
    down[index].extend(b[data['down']])
    left[index].extend(c[data['left']])
    right[index].extend(a[data['right']])

t = [[defaultdict(int) for i in range(20)] for j in range(20)]

for index in [108, 384]: #range(400):
    vis = set()
    mapa = {}
    q = deque()
    if index == 108:
        q.append((index, 0, 1))
    else:
        q.append((index, 17, 3))
    while q:
        index, x, y = q.pop()
        mapa[x, y] = index
        if len(up[index]) == 1:
            nxt = up[index][0]
            if nxt not in vis:
                vis.add(nxt)
                q.append((nxt, x - 1, y))
        if len(down[index]) == 1:
            nxt = down[index][0]
            if nxt not in vis:
                vis.add(nxt)
                q.append((nxt, x + 1, y))
        if len(left[index]) == 1:
            nxt = left[index][0]
            if nxt not in vis:
                vis.add(nxt)
                q.append((nxt, x, y - 1))
        if len(right[index]) == 1:
            nxt = right[index][0]
            if nxt not in vis:
                vis.add(nxt)
                q.append((nxt, x, y + 1))

    mx = my = 0
    for x, y in mapa:
        if mapa[x, y] == 108 and mapa[x, y + 1] == 346:
            mx = x
            my = y - 1
            break

    for x, y in mapa:
        try:
            t[x - mx][y - my][mapa[x, y]] += 1
        except:
            pass

tt = [[-1 for j in range(20)] for i in range(20)]
used = set()
for i in range(20):
    for j in range(20):
        ma = 0
        for key, value in t[i][j].items():
            if value > ma and key not in used:
                ma = value
                used.add(key)
                tt[i][j] = key

for k in range(5):
    for i in range(20):
        for j in range(20):
            if tt[i][j] < 0:
                candidates = set(range(400))
                if i > 0 and tt[i - 1][j] >= 0:
                    candidates &= set(down[tt[i - 1][j]])
                if i < 19 and tt[i + 1][j] >= 0:
                    candidates &= set(up[tt[i + 1][j]])
                if j > 0 and tt[i][j - 1] >= 0:
                    candidates &= set(right[tt[i][j - 1]])
                if j < 19 and tt[i][j + 1] >= 0:
                    candidates &= set(left[tt[i][j + 1]])
                # print(i, j, len(candidates))
                if len(candidates) == 1:
                    tt[i][j] = candidates.pop()

print([i for i in range(400) if i not in used])

for r in tt:
    print(r)

im = Image.new(f.mode, f.size)
pix = im.load()

for i in range(20):
    for j in range(20):
        if tt[i][j] >= 0:
            index = tt[i][j]
            bw = [(255,255,255), (0,0,0)]
            bl = 0
            wh = 0
            for a in range(49):
                for b in range(49):
                    if vertex[index][a, b] == (255,255,255):
                        wh += 1
                    if vertex[index][a, b] == (0,0,0):
                        bl += 1
            for a in range(49):
                for b in range(49):
                    pix[i * 49 + a, j * 49 + b] = vertex[index][a, b]
                    # if pix[i * 49 + a, j * 49 + b] not in bw:
                    #     pix[i * 49 + a, j * 49 + b] = (0,0,0) if bl > wh else (255,255,255)
im.show()
im.save('image.png')
