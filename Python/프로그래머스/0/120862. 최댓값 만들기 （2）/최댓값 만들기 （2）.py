def solution(numbers):
    answer = 0
    sort_numbers = sorted(numbers)
    low_num = sort_numbers[0]*sort_numbers[1]
    high_num = sort_numbers[-1]*sort_numbers[-2]
    
    if low_num > high_num:
        answer = low_num
    else:
        answer = high_num
    
    return answer

