def solution(num, total):
    answer = []
    if num % 2 == 0:
        middle_idx = num // 2 - 2
    else:
        middle_idx = num // 2 - 1
    print(middle_idx)
    for i in range(num):
        answer.append(total//num-(middle_idx-i)-1)
    return answer