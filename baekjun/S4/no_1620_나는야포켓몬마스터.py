n, m = map(int, input().split())
name_dic = {}
num_dic = {}
ans = []
for i in range(n) :
    name = input()
    name_dic[f'{i+1}'] = name
    num_dic[name] = f'{i+1}'
for i in range(m) :
    q = input()
    if q in num_dic.keys() :
        ans.append(num_dic[q])
    else:
        ans.append(name_dic[q])

for a in ans :
    print(a)