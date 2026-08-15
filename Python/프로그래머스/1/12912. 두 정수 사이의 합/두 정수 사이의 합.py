def solution(a, b):
    answer = 0
    min_num = min(a,b)
    max_num = max(a,b)+1
    for i in range(min_num,max_num):
        answer += i
    return answer