def solution(numbers, k):
    answer = 0
    idx = 0+((k-1)*2)
    if idx > len(numbers)-1:
        idx = idx%len(numbers)
    answer = numbers[idx]
    print(len(numbers),idx,answer)
    
    return answer

# 0 2 4 %len()-1
# 0 2 4 6 8 10
# 0 2 4 0 2 4
# 1 3 5 1 3 5

# 0 2 4 6
# 0 2 1 0
# 1 3 2 1
