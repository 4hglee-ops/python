# 3141592
# 0123456
# -len(p)   

def solution(t, p):
    answer = 0
    t_list = []
    if len(p) == 1:
        t_list = list(map(int,t))
    else:
        for idx,num in enumerate(t[:-len(p)+1]):
            t_list.append(int(t[idx:idx+len(p)]))
    int_p = int(p)  
    for num in t_list:
        if int_p >= num:
            answer += 1
    
    return answer