import sys
ns = []

def prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i+=1
    return True
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
       ns.append(n)

mi = max(ns)
ss = [True]*mi
r = []
for i in range(2,mi):
    if ss[i] == True:
        if i%2 == 1:
            r.append(i)
        for j in range(i*2,mi,i):
            ss[j] = False



for n in ns:
    for j in r:
        if prime(n-j):
            print(n,'=',j,'+',n-j)
            break