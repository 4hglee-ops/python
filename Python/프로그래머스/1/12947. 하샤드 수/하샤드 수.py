def solution(x):
    x_str = str(x)
    x_sum = 0
    
    for num in x_str:
        x_sum += int(num)
    if x%x_sum==0:
        return True
    return False