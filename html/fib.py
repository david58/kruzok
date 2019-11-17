import sys

sys.setrecursionlimit(1000000000)

def fib1(n):
    if n < 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

memo={}
def fib2(n):
    if not n in memo:
        if n < 2:
            memo[n] = 1
        else:
            memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]

def fib3(n):
    fibs=[1,1]
    while len(fibs)<n+1:
        fibs.append(fibs[-1]+fibs[-2])
    return fibs[-1]

def fib4(n):
    a,b=1,1
    for i in range(n-1):
        a,b = b, a+b
    return b

def fib_magic(n):
    def _fib(n):
        if n == 0:
            return (0, 1)
        else:
            a, b = _fib(n // 2)
            c = a * (b * 2 - a)
            d = a * a + b * b
            if n % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)
    return _fib(n)[0]

print('čísla sú veľké, preto iba modulo 10')
print(f'fib1 pre 30: {fib1(30)%10}')
print(f'fib2 aj pre 15 000 (viac často spadne na obmädzenej veľkosti stacku): {fib2(15000)%10}')
print(f'fib3 pre 100 000 vyžerie veľa pamäte: {fib3(100000)%10}')
print(f'fib4 aj pre 200 000: {fib4(200000)%10}')
print(f'fib_magic aj pre 2 000 000: {fib_magic(2000000)%10}')
