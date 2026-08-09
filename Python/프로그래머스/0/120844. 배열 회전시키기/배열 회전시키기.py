def solution(numbers, direction):
    answer = []

    if direction == 'left':
        for i in range(len(numbers)):
            if i == len(numbers)-1:
                answer.append(numbers[0])
            else :
                answer.append(numbers[i+1])
    elif direction == 'right':
        for i in range(len(numbers)):
            if i == 0:
                answer.append(numbers[-1])
            else :
                answer.append(numbers[i-1])

                
        
    return answer