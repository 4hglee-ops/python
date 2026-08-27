def solution(arr, k):
    list_arr = []
    for num in arr:
        if num not in list_arr:
            list_arr.append(num)
    if len(list_arr) >= k:
        return list_arr[:k]
    else:
        list_arr.extend([-1]*(k-len(list_arr)))
        return list_arr
