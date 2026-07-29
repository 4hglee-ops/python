def solution(ingredient):
    answer = 0
    stack = []
    target = [1,2,3,1]
    
    for num in ingredient :
        stack.append(num)
        
        if stack[-4:] == target:
            answer += 1
            del stack[-4:]
            
    return answer