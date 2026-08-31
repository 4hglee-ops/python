def solution(price, money, count):
    answer = 0
    sum_price = 0
    c_price = price
    for c in range(count):
        answer += c_price
        c_price += price
    return answer-money if answer-money > 0 else 0 