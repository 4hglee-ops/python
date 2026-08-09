def solution(array):
    count = {}
    for num in array:
        if num in count:
            count[num]+=1
        else :
            count[num]=1
    
    max_count = max(count.values())
    
    mode = []
    for key, value in count.items():
        if value == max_count:
            mode.append(key)
    if len(mode) > 1:
        return -1
    else :
        return mode[0]
