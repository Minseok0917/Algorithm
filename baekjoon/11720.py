import sys

input = sys.stdin.readline

n = input()
numbers = str(input()).replace('\n','')
result = 0
for number in numbers:
    result += int(number)

print(result)

