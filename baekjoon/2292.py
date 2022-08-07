find = int(input())
total, idx = 1, 1
while True:
    if total >= find: break
    total += 6*idx
    idx+=1
print(idx)