strs = input()
print(
    ' '.join(
        list(map(lambda v: str(strs.count(v)),'abcdefghijklmnopqrstuvwxyz'))
    )
)

