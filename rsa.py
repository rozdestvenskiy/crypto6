n = 5000
primes = [x for x in range(2, n + 1) if x not in [i for sub in [list(range(2 * j, n + 1, j)) for j in range(2, n // 2)] for i in sub]]
import random
random.seed()
print(primes[10])
p = primes[random.randint(0, len(primes) - 1)]
q = primes[random.randint(0, len(primes) - 1)]

print('p = ', p)
print('q = ', q)

n = p * q
phi = (p - 1) * (q - 1)


def evklid(x, y):
    while (x != 0) and (y != 0):
        if x >= y:
            x %= y
        else:
            y %= x
    return x or y

i = 0
e_candidates = []
while i < len(primes) and primes[i] < phi:
    if evklid(phi, primes[i]) == 1:
        e_candidates.append(primes[i])
    i += 1

if len(e_candidates) == 0:
    print('err')
    exit(123123)

e = sorted(e_candidates, key = lambda x: bin(x).count('1'), reverse=True)[0]

d = 0
i = 2
while i < n:
    if (i * e) % phi == 1:
        d = i
    i += 1
print('------------')
print('phi = ', phi)
print('n = ', n)
print('e = ', e)
print('d = ', d)
print('------------')
print('open key: ', e, n)
print('private key: ', d, n)


# here should be fast umnozhenie po modulu lol kek cheburek


def rsa_scf(base, degree, module):
    degree = bin(degree)[2:]
    r = 1

    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module

    return r

Message = 1020304050
scf = rsa_scf(Message, e, n)
print(scf)
unscf = rsa_scf(scf, d, n)
print(unscf)
