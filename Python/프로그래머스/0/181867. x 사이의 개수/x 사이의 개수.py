def solution(myString):
    answer = []
    myString_list = myString.split("x")
    for text in myString_list:
        answer.append(len(text))
    return answer