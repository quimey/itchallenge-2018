import base64

r = open('roulette.txt', 'r').read()
print(len(r))
m = "z"
mp = -1
l = 100
for p in range(len(r) - l):
    x = r[p: p + l]
    if x < m:
        m = x
for p in range(len(r) - l):
    x = r[p: p + l]
    if x == m:
        mp = p
        print(p)

d = r[mp + 500000: mp + 502976]
u = base64.b64decode(d)
f = open('roulette.html', 'wb')
f.write(u)
