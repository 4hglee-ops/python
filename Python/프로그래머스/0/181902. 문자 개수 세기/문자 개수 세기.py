def solution(my_string):
    answer_dict = {}
    for i in range(ord('A'),ord('Z')+1):
        answer_dict[chr(i)] = 0
    for i in range(ord('a'),ord('z')+1):
        answer_dict[chr(i)] = 0
    for string in my_string:
        answer_dict[string]+=1
    return list(answer_dict.values())