def solution(n):
    answer = 0
    for i in range(1,n+1):
        answer += 1
        while answer % 3 == 0 or answer%100 % 10 == 3 or answer%100 // 10 == 3 or answer // 100 == 3:
            answer += 1
        print(i,answer)
    return answer