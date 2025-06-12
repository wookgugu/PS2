N,M = map(int, input().split())
dud = []
all = []
for _ in range(N) :
    dud.append(input())
    
for _ in range(M) :
    bo = input()
    if bo in dud :
        all.append(bo)

all = sorted(all)

print(len(all))
for i in all :
    print(i)


# 딕셔너리로 풀기
N,M = map(int, input().split())
dct = {}
all = []
for _ in range(N) :
    dct[input()] = False
    
for _ in range(M) :
    bo = input()
    if bo in dct :
        all.append(bo)

all = sorted(all)

print(len(all))
for i in all :
    print(i)    