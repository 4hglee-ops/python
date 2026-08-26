def solution(my_string, overwrite_string, s):
    answer = ''
    for idx,mys in enumerate(my_string):
        if s<=idx<=len(overwrite_string)+s-1:
            answer+=overwrite_string[idx-s]
        else:
            answer+=mys
    return answer