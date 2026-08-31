def solution(arr1, arr2):
    max_y = len(arr1)
    max_x = len(arr1[0])
    
    for y in range(max_y):
        for x in range(max_x):
            arr1[y][x] += arr2[y][x]
    
    return arr1