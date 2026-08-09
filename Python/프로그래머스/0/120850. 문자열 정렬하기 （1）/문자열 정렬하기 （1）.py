def solution(my_string):
    answer = []
    num_list = ["0","1","2","3","4","5","6","7","8","9"]
    
    for text in my_string:
        if text in num_list:
            answer.append(int(text))
    answer.sort()
    return answer