def solution(l, r):
    answer = []
    answer_set = ['0','5']
    for i in range(l,r+1):
        set_i = set(str(i))
        list_i = list(set_i)
        if len(set_i) > 2:
            continue
        elif len(list_i) == 1 and list_i[0] in answer_set:    
            answer.append(i)
        elif len(list_i) == 2 and list_i[0] in answer_set and list_i[1] in answer_set:    
            answer.append(i)
    if not answer:
        return [-1]
    return answer