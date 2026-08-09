def solution(my_str, n):
    answer = []
    word = ''
    
    for idx,text in enumerate(my_str):
        word+=text
        if len(word) == n:
            answer.append(word)
            word = ''
        elif idx == len(my_str)-1:
            answer.append(word)
            
        
    return answer