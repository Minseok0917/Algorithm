import re

while True:
    try:
        chars = input()
        a0 = len(re.findall("[a-z]",chars))
        a1 = len(re.findall("[A-Z]",chars))
        a2 = len(re.findall("[0-9]",chars))
        a3 = len(re.findall(" ",chars))
        print(a0,a1,a2,a3)
    except EOFError:
        break