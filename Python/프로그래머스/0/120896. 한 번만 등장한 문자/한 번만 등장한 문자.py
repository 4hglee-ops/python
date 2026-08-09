def solution(s):
    answer = ''
    s_dict = {}
    for text in s:
        s_dict[text]=s_dict.get(text,0)+1
    for key in s_dict.keys():
        if s_dict[key] == 1:
            answer += key
    answer = "".join(sorted(answer))
    return answer

# def solution(s):
#     answer = []
#     set_s = set(s)
#     for text in set_s:
#         if s.count(text)==1:
#             answer.append(text)
#     answer = "".join(sorted(answer))
#     return answer