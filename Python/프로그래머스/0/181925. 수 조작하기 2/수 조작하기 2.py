def solution(numLog):
    answer = []
    num_dict = {
        1 : "w",
        -1 : "s",
        10 : "d",
        -10 : "a"
    }
    
    for idx,num in enumerate(numLog):
        if idx != 0:
            answer.append(num_dict[num-numLog[idx-1]])
        
    return ''.join(answer)