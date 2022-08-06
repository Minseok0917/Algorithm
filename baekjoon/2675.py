n = int(input())
for i in range(n):
    cnt, s= input().split()
    text = ''.join(list(map(lambda v : v * int(cnt),s)))
    print(text)