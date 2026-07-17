def solution(arr):
    answer = []

    for idx,num in enumerate(arr):
        if idx == 0:
            answer.append(num)
        else :
            if num != arr[idx-1]:
                answer.append(num)
    return answer