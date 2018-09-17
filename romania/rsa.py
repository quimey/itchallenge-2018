from Crypto.PublicKey import RSA
key_encoded='''-----BEGIN RSA PUBLIC KEY-----
MCgCIQCKkJ7C1rP6I1dyoIO/Hm3Tob+rgB6oMVMGVsRpFmQ7lQIDAQAB
-----END RSA PUBLIC KEY-----'''


def powmod(r, e, n):
    if e == 0:
        return r % n
    a = powmod(r, e//2, n)
    if e % 2:
        return (a * a * r) % n
    return (a * a) % n

pubkey = RSA.importKey(key_encoded)
n = pubkey.n
e = pubkey.e

q = 1094782941871623486260250734009229761
p = pubkey.n // q
d = 58363580108870086903455850238621164852907433225466704443201501230569963020033

print(pubkey.n % q, p, q)

data = open('data', 'rb').read()
print(len(data))
print(data)

x = RSA.construct((n, e, d, p, q))
print(x)
z = x.decrypt(data)
print(z)
with open('sarasa', 'wb') as f:
    f.write(z)
print(x.decrypt(z))
