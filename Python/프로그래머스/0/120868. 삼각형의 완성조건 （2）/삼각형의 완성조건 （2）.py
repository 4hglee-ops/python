def solution(sides):
    answer = 0
    a = min(sides[0],sides[1])
    b = max(sides[1],sides[0])
    for i in range(b-a+1,a+b):
        answer += 1
    return answer

# 1 2 : 2
# 3 6 : 45678
# 11 7 : 56789 10 11 12 13 14 15 16 17 