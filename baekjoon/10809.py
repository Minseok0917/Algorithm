s = input()
print(
   " ".join(
       list(map(lambda v: str(s.find(v)), 'abcdefghijklmnopqrstuvwxyz'))
   )
)