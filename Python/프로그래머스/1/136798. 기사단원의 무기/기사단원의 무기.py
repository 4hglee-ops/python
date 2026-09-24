# 약수 개수 먼저 구하고
# limit 넘는지 검사 후 power 입력

def solution(number, limit, power):
    answer = 0
    for yaksu in range(1,number+1):
        y = 0
        for i in range(1,int((yaksu**0.5)+1)):
            if yaksu % i == 0:
                if i * i == yaksu:
                    y += 1
                else:
                    y += 2
        if y > limit:
            answer += power
        else:
            answer += y
    return answer