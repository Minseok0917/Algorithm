from sys import stdin

n = int(stdin.readline())
array = list(map(int,stdin.readline().split()))
mx = max(array)+1

count = 0
mm = {}
for i in range(2,mx):
    if not i in mm:
        if i in array:
            count+=1
        for j in range(i*2,mx,i):
            mm[j] = 0

print(count)