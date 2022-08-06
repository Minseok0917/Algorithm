import sys

input = sys.stdin.readline

def list_input(): return list(map(int,input().split()))

N, M = list_input()
N_Store = []
M_Store = []
M_Dict = {}


for _ in range(N):
    N_Store.append(list_input())
for idx in range(M):
    value = int(input())
    M_Dict[value] = idx
    M_Store.append([value,idx])

M_Sort = list( zip(M_Dict.keys(),M_Dict.values()) )
M_Sort.sort( key=lambda value: value[0])

def upper_bound(arrays,min,max):
    left, right = 0, len(arrays)-1
    while left < right:
        mid = (left + right)//2
        value = arrays[mid][0]
        if min <= value and value < max:
            right = mid-1
        else:
            left = mid+1
    return right
def lower_bound(arrays,min,max):
    left, right = 0, len(arrays)-1
    while left < right:
        mid = (left + right)//2
        value = arrays[mid][0]
        if min <= value and value < max:
            left = mid+1
        else:
            right = mid-1
    return right

def findK(min,max):
    start = upper_bound(M_Sort,min,max)
    end = upper_bound(M_Sort, min, max)
    print(start,end)
    clone = M_Sort[start:end]
    clone.sort(key=lambda value: value[1])
    print(clone,'123312312',M_Sort)

for n in N_Store:
    min, max = n
    if max < min:
        max, min = n
    print(min,max)
    findK(min,max)