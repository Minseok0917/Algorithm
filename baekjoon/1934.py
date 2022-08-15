import math
n = int(input())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
for _ in range(n):
    a,b = map(int,input().split())
    g = gcd(a,b)
    print(
        math.trunc(g*(a/g)*(b/g))
    )
