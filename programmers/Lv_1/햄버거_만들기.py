def solution(ingredient):
    answer = 0
    bur = []
    for i in ingredient :
        bur.append(i)
        if bur[-4:] == [1,2,3,1] :
            answer += 1
            bur.pop()
            bur.pop()
            bur.pop()
            bur.pop()
            
    
    return answer