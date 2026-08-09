# sorted(원본) 은 원본을 안건드리고 정렬해서 새로 리스트 만듬

def solution(array):
    answer = 0
    sort_array = sorted(array)
    answer = sort_array[len(array)//2]
    return answer