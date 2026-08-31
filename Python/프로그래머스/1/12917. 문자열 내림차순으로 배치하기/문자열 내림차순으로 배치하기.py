def solution(s):
    s_list = list(s)
    s_list = sorted(s_list,reverse=True)
    return ''.join(s_list)