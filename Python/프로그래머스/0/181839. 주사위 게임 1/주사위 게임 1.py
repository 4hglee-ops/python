def solution(a, b):
    answer = 0
    ab_list = [0,0]
    
    if a % 2 == 1:
        ab_list[0] += 1
    if b % 2 == 1:
        ab_list[1] += 1
    match sum(ab_list):
        case 0:
            return abs(a-b)
        case 1:
            return 2 * (a + b)
        case 2:
            return a**2 + b**2
    return answer