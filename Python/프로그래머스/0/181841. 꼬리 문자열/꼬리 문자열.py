def solution(str_list, ex):
    answer = str_list.copy()
    del_cnt = 0
    for idx,s_l in enumerate(str_list):
        if ex in s_l:
            del answer[idx-del_cnt]
            del_cnt += 1
    return "".join(answer)
