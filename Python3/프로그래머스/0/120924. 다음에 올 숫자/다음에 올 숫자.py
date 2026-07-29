def solution(common):
    answer = 0
    a = common[1]-common[0]
    b = common[2]-common[1]
       
    if a != b :
        ratio = common[1]//common[0]
        answer = common[len(common)-1] * ratio
        
    elif a == b :
        answer = common[len(common)-1] + a
    

    return answer