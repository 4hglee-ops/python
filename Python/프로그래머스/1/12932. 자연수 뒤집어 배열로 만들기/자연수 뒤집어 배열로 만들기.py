def solution(n):
    str_n = str(n)[::-1]
    answer = []
    for s in str_n:
        answer.append(int(s))
    return answer