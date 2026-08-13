def solution(myString):
    answer = []
    answer = sorted(myString.split("x"))
    while answer[0] == "":
        del answer[0]
    return answer