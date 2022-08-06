print(
    sum(list(
        map(lambda i: int(i)*int(i),input().split(' '))
    ))%10
)
