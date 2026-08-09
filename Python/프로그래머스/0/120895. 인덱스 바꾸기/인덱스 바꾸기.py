def solution(my_string, num1, num2):
    answer = ''
    num1_save = num1
    num2_save = num2
    
    if num1 > num2 :
        num1 = num2_save
        num2 = num1_save
    
    for i in range(len(my_string)):
        if i == num1:
            answer += my_string[num2]
        elif i == num2:
            answer += my_string[num1]
        else :
            answer += my_string[i]            
    
    return answer