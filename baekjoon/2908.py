a,b = map(lambda i: int(i[::-1]) ,input().split())
print( a if a > b else b )