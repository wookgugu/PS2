import re

rule = re.compile('^[A-F]?A+F+C+[A-F]?$')
n = int(input())
for _ in range(n):
    q = input()
    if rule.match(q) == None:
        print('Good')
    else :
        print('Infected!')