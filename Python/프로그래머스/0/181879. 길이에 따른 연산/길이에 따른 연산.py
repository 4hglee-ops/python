def solution(num_list):
    a = 1
    if len(num_list)>=11:
        return sum(num_list)
    else:
        for num in num_list:
            a *= num
        return a