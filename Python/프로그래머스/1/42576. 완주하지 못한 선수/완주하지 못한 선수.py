def solution(participant, completion):
    answer = ''
    dict_part = {}
    dict_com = {}
    
    for name in participant:
        if name not in dict_part:
            dict_part[name] = 1
        else:
            dict_part[name] += 1
    for name in completion:
        if name not in dict_com:
            dict_com[name] = 1
        else:
            dict_com[name] += 1
    for name in participant:
        if dict_part[name] != dict_com.get(name,0):
            answer = str(name)
        
    return answer