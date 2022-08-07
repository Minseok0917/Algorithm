while True:
    values = list(map(int,input().split()))
    big = max(values)
    if big == 0: break
    values.remove(big)
    print( 'right' if values[0]**2 + values[1]**2 == big**2 else 'wrong'   )




