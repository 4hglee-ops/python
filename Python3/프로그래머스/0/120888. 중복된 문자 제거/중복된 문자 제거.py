def solution(my_string):
    answer = ''
    for text in my_string:
        if text not in answer:
            answer+=text
    return answer