def solution(arr):
    answer = [[]]
    x = len(arr)
    y = len(arr[0])
    if x > y:
        for i in range(x):
            arr[i].extend([0]*(x-y))
    elif x < y:
        for i in range(x+1,y+1):
            arr.append([0]*y)
    return arr