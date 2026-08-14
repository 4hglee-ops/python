def solution(num_list):
    odd_sum = 0
    even_sum = 0
    for idx,num in enumerate(num_list):
        if idx % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    if odd_sum > even_sum:
        return odd_sum
    return even_sum