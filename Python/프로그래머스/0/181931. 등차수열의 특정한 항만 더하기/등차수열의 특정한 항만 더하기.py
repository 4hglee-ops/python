def solution(a, d, included):
    answer = 0
    in_list = []
    in_num = a
    for i in range(len(included)):
        in_list.append(in_num)
        in_num+=d
    for include,num in zip(included,in_list):
        if include:
            answer += num
    return answer