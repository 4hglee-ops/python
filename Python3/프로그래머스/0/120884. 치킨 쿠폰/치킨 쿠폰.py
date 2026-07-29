def solution(chicken):
    answer = 0
    coupon = 0
    while chicken > 0 :
        coupon += chicken
        answer += coupon // 10
        chicken = coupon // 10
        coupon = coupon % 10
        
    return answer