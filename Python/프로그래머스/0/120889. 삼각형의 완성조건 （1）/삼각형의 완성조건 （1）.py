# 배열 정렬하기
# 배열 비교하기
# 판단하기

def solution(sides):
    answer = 0
    sides.sort()
    if sides[2] < sides[0] + sides[1] :
        answer = 1
    else : 
        answer = 2
    return answer