def solution(num_list):
    a = 1
    b = 0
    for num in num_list:
        a *= num
        b += num
    if a>b**2:
        return 0
    else:
        return 1