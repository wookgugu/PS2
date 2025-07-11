import re

n = int(input())
patt = input()
patt = patt.replace('*','.*')
p = re.compile(patt)
for _ in range(n):
    q = input()
    if re.fullmatch(p, q) :
        print('DA')
    else :
        print('NE')