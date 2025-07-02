def solution(new_id):
    new_id = new_id.lower()
    n_id = []
    for n in new_id :
        if n.isalpha() or n.isdigit() or n in ['-','_']:
            n_id.append(n)
        elif n == '.' :
            if len(n_id) != 0:
                if n_id[-1] == '.' :
                    continue
                else :
                    n_id.append(n)
            else :
                n_id.append(n)     
                
    if n_id[0]=='.':
        if len(n_id)>=2 :
            n_id = n_id[1:]
        else :
            n_id = ['a']
    if n_id[-1]=='.':
        if len(n_id)>=2 :
            n_id = n_id[:-1]
        else :
            n_id = ['a']
            
    if len(n_id)>15 :
        n_id = n_id[:15]
        if n_id[-1] == '.' :
            n_id = n_id[:14]
    if n_id == [''] :
        n_id = ['a']
        
    while len(n_id) < 3:
        n_id.append(n_id[-1])


    return ''.join(n_id)