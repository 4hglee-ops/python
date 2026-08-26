def solution(str1, str2):
    answer = ''
    for s,t in zip(str1,str2):
        answer += s+t
    return answer