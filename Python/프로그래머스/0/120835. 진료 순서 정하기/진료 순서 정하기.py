def solution(emergency):
    answer = []
    
    sort_emer = sorted(emergency,reverse = True)
    
    for emer_num in emergency:
        for idx, num in enumerate(sort_emer):
            if emer_num == num:
                answer.append(idx+1)
    
    
    return answer