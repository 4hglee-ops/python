def solution(strArr):
    answer = []
    for arr in strArr:
        if "ad" not in arr:
            answer.append(arr)
    return answer