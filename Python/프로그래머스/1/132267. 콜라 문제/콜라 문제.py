'''
a = 가져가는 콜라병
b = 반환되는 콜라
n = 빈병 수
20 
10 잔여 병 0
5 잔여 병 0
2 잔여 병 1
1 잔여 병 1
1 잔여병 0

20
6 잔여 병 2
2 잔여병 2
1 잔여병 1

'''

def solution(a, b, n):
    answer = 0
    coke_bottle = n
    empty_bottle = 0
    while coke_bottle+empty_bottle >= a:
        coke_bottle += empty_bottle
        empty_bottle = 0
        empty_bottle = coke_bottle % a
        coke_bottle = (coke_bottle // a) * b

        answer += coke_bottle
        
    return answer