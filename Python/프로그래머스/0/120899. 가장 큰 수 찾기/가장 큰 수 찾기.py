# 정렬해서 마지막숫자가 가장 큰숫자
# 마지막 숫자랑 같은 숫자인 위치찾기

def solution(array):
    answer = []
    array1 = sorted(array)
    answer.append(array1[-1])
    for i in range(len(array)):
        if array1[-1]==array[i]:
            answer.append(i)
    return answer