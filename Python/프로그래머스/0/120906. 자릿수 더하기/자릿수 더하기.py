def solution(n):
    answer = 0
    nstr = str(n)
    for i in range(len(nstr)):
        answer += int(nstr[i])
    return answer
