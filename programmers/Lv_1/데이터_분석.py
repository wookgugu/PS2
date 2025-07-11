def solution(data, ext, val_ext, sort_by):

    if ext == 'code' :   
        d_data = list(filter(lambda x : int(x[0]) < val_ext, data))
    elif ext == 'date' :   
        d_data = list(filter(lambda x : int(x[1]) < val_ext, data))
    elif ext == 'maximum' :   
        d_data = list(filter(lambda x : int(x[2]) < val_ext, data))
    elif ext == 'remain' :   
        d_data = list(filter(lambda x : int(x[3]) < val_ext, data))  
    
    if sort_by == 'code' :    
        answer = sorted(d_data, key = lambda x : x[0])
    elif sort_by == 'date' :
        answer = sorted(d_data, key = lambda x : x[1])
    elif sort_by == 'maximum' :
        answer = sorted(d_data, key = lambda x : x[2])
    elif sort_by == 'remain' :
        answer = sorted(d_data, key = lambda x : x[3])
    
    return answer