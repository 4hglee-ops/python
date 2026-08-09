def solution(n):
    answer = 0
    num_list = []
    for i in range(n+1):
        if i%2==0:
            num_list.append(i)
    for j in num_list:
        answer += j
    
    return answer