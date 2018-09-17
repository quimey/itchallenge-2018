x=map(lambda a: a.split(),"""9106 137
5339 852
3726 3952
994 210
5304 1471
5990 3581
3266 4392
5290 439
9299 296
9437 479""".split('\n'))
y = "7 6 8 1 6 7 7 3 7 6".split()
res = []
for a in y:
    a = int(a) -1
    u = int(x[a][0])
    v = int(x[a][1])
    s = -1
    for b, c in x:
        b = int(b)
        c = int(c)
        if abs(b + c - u) <= v and abs(b - c - u) <= v:
            s += 1
    print s
    res.append(str(s))
print ''.join(res)
