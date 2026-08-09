def solution(num, k):
    answer = 0
    num_str = ''
    num_str = str(num)
    for i in range(len(num_str)):
        if int(num_str[i]) == k :
            answer = i+1
            break
        else :
            answer = -1
    return answer