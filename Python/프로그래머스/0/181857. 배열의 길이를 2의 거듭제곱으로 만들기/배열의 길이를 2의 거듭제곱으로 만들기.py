def solution(arr):
    arr_list = [1,2,4,8,16,32,64,128,256,512,1024] 
    save_num = 0
    for idx,num in enumerate(arr_list):
        if num > len(arr):
            save_num = num
            break
        print(save_num)
    if len(arr) not in arr_list:
        arr.extend([0]*(save_num-len(arr)))
    return arr