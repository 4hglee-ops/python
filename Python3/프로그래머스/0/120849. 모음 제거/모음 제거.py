def solution(my_string):
    answer = ''
    for idx,text in enumerate(my_string):
        if text not in "aeiou":
            answer += text
    return answer