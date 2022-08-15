import math
a, b = map(int,input().split())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)


g = gcd(a,b)
l = math.trunc(g * (a/g) * (b/g))
print(g)
print(l)