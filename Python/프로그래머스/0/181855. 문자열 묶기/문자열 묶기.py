def solution(strArr):
    answer = 0
    str_dict = {}
    for arr in strArr:
        if len(arr) not in str_dict:
            str_dict[len(arr)] = 1
        else:
            str_dict[len(arr)] += 1
    return max(str_dict.values())