def solution(arr):
    while_count = 0
    save_arr = []
    while True:
        if save_arr == arr:
            return while_count-1
        save_arr = list(arr)
        for idx,a in enumerate(arr):
            if a >= 50 and a % 2 == 0:
                arr[idx] //= 2
            elif a < 50 and a % 2 == 1:
                arr[idx] = arr[idx]*2 +1
        while_count+=1