def solution(participant, completion):
    par = sorted(participant)
    com = sorted(completion)
    for i in range(0,len(par)-1):
        if par[i] != com[i] :
            return par[i]
    return par[-1]