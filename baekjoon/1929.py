min, max = map(int,input().split())
dummy = {}

for i in range(2,max+1):
    if not i in dummy:
        if i >= min:
            print(i)
        for j in range(i*2,max+1,i):
            dummy[j] = True
