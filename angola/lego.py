M = 10 ** 9 + 7

s = {0: 1}
def calc(i):
    if i < 0:
        return 0
    if i not in s:
        s[i] = (calc(i - 1) + calc(i - 2) + calc(i -3) + calc(i - 4)) % M
    return s[i]

def powmod(x, e):
    if e == 0:
        return 1
    y = powmod(x, e // 2)
    if e % 2:
        return (y * y * x) % M
    return (y * y) % M

cr = {}
def calc_roto(n, m):
    if (n, m) not in cr:
        cr[(n, m)] = powmod(calc(m), n)
    return cr[(n, m)]

cs = {}
def calc_sano(n, m):
    if (n, m) not in cs:
        cs[(n, m)] = calc_roto(n, m)
        for i in range(1, m):
            cs[(n, m)] = (cs[(n, m)] - calc_sano(n, i) * calc_roto(n, m - i)) % M
    return cs[(n, m)]

t = int(input())
results = []
for i in range(t):
    n, m = map(int, input().split())
    results.append(str(calc_sano(n, m)))
print(''.join(results))
