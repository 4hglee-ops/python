def solution(s):
    answer = ''
    s_dict = {}
    for text in s:
        s_dict[text]=s_dict.get(text,0)
        if s_dict[text]==0:
            s_dict[text] = 1
        else:
            s_dict[text]+=1
    for key in s_dict.keys():
        if s_dict[key] == 1:
            answer += key
        answer = "".join(sorted(answer))
    return answer