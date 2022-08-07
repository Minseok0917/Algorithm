import math
array = []
for _ in range(int(input())):
   array.append(map(int,input().split()))
for i in array:
    h, w, n = i
    row = math.ceil(n/h)
    column = h if n%h == 0 else n%h
    print(column*100+row)