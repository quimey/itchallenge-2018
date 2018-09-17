nn = 27
kk = 42
#nn = 3
#kk = 6

d = {}
def calc(n, k):
    if k == 0:
        return 0
    if (n, k) not in d:
        res = 0
        for i in range(1, k + 1):
            # elijo > i en 1 ... i y < i en 1 ... (i - 1)
            for a in range(i + 1, n + 1):
                for b in range(i):
                    x = binomial(n, b) * ((i - 1) ** b - calc(b, i - 1)) * binomial(n - b, a - b) * (k - i) ** (n - a)
                    #print i, a, b, x
                    res += x
        d[(n, k)] = res
    return d[(n, k)]
print calc(nn, kk) / kk ** nn
