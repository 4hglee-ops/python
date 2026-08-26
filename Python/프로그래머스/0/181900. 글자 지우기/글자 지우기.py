def solution(my_string, indices):
    answer = ''
    for idx,text in enumerate(my_string):
        if idx not in indices:
            answer += text
    return answer