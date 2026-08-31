def solution(left, right):
    answer = 0
    a_dict = {}
    for ran in range(left,right+1):
        a_list = []
        for i in range(1,ran+1):
            if ran%i==0:
                a_list.append(i)
        a_dict[i] = len(a_list)
    for k,v in a_dict.items():
        if not v%2:
            answer += k
        else:
            answer -= k
    return answer