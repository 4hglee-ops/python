def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        num_str = str(num)
        for text in num_str:
            if int(text) == k:
                answer += 1
    return answer