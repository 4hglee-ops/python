def solution(n):
    answer = 0
    fact_list = []
    for i in range(1,11):
        fact_list.append(1)
        for j in range(1,i+1):
            fact_list[i-1] *= j
    for idx,fact_num in enumerate(fact_list):
        if n < fact_num:
            break
        answer = idx + 1
    return answer