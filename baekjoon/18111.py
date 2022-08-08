import sys
n, m, b = map(int,input().split())
blocks = []
time = 0

for _ in range(n):
    blocks += sys.stdin.readline().split(" ")

blocks = list(map(int,blocks))

while True:
    minFloor, maxFloor = min(blocks), max(blocks)
    minCount, maxCount = blocks.count(minFloor), blocks.count(maxFloor)
    minTime, maxTime = minCount * 2, maxCount * 1
    if minTime < maxTime and minCount <= b:
        for idx in range(n*m):
            if blocks[idx] == minFloor:
                blocks[idx] +=1
                b -=1
                time +=1
        if blocks.count(minFloor+1) == n*m:
            print(time,minFloor+1)
            break
    else:
        for idx in range(n*m):
            if blocks[idx] == maxFloor:
                blocks[idx] -=1
                b +=1
                time +=2
        if blocks.count(maxFloor-1) == n*m:
            print(time,maxFloor-1)
            break
