def solution(x, n):
    answer = []
    x_sum = x
    for i in range(n):
        answer.append(x_sum)
        x_sum+=x
    return answer