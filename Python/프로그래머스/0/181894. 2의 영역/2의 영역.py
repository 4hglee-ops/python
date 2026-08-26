def solution(arr):
    str_arr = ''.join(map(str,arr))
    str_arr = str_arr.replace('10','1')
    arr_find = str_arr.find('2')
    arr_rfind = str_arr.rfind('2')
    if '2' not in str_arr:
        return [-1]
    elif arr_find == arr_rfind:
        return [arr[arr_find]]
    else:
        return arr[arr_find:arr_rfind+1]
