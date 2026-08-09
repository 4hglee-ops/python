def solution(rsp):
    answer = ''
    for text in rsp:
        if text == "0":
            answer += "5"
        elif text == "2":
            answer += "0"
        elif text == "5":
            answer += "2"
    return answer