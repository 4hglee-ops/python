from math import gcd 

def solution(a, b):
    
    common = 0
    cal_b = b
    common = gcd(a,b)
    cal_b //= common
    
    while cal_b % 2 == 0:
        cal_b = cal_b // 2
    while cal_b % 5 == 0:
        cal_b = cal_b // 5
    if cal_b == 1:
        return 1
    else:
        return 2
# def solution(a, b):
#     a_list = []
#     b_list = []
#     cal_b = b
    
#     for i in range(2,a+1):
#         while a%i==0:
#             a_list.append(i)      
#     for al in a_list:
#         if cal_b % al == 0:
#             cal_b = cal_b//al
#     while cal_b % 2 == 0:
#         cal_b = cal_b // 2
#     while cal_b % 5 == 0:
#         cal_b = cal_b // 5
#     if cal_b == 1:
#         return 1
#     else:
#         return 2
