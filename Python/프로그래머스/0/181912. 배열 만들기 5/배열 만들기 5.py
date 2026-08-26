def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        a = int(intStr[s:s+l])
        if k<a:
            answer.append(a)
    return answer