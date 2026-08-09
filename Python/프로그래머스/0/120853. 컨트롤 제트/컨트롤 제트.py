def solution(s):
    answer = 0
    s_list = s.split()
    for idx,n in enumerate(s_list):
        if n != 'Z':
            answer += int(n)
        else:
            answer -= int(s_list[idx-1])
            
    print(s_list)
    return answer