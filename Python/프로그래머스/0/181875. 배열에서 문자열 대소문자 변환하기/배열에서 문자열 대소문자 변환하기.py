def solution(strArr):
    answer = []
    for idx,arr in enumerate(strArr):
        if idx%2==0:
            answer.append(arr.lower())
        else:
            answer.append(arr.upper())
    return answer