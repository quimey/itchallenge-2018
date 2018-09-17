x = 171024
y = 12825
z = 14359
for d in range(1, 10):
    w = z - y - 2 * d - 1
    p = (x + w - 1)// w
    print d, p, w
