def tri_selection(T):
    for i in range(len(T)):
        min = T[i]
        for j in range(len(T)-i):
            if min > T[j+i]:
                min = T[j+i]
                min_id = j+i
            elif j == 0 :
                min_id = j+i
        if T[i] == T[min_id]:
            pass
        else :   
            temp = T[min_id]
            T[min_id] = T[i]
            T[i] = temp 
            
    return T
