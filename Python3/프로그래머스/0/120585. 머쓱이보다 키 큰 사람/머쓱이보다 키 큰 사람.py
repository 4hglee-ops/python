def solution(array, height):
    answer = 0
    for num in range(len(array)):
        if array[num]> height:
            answer += 1
    return answer