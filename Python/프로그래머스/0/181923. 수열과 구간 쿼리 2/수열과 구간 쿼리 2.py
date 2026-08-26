def solution(arr, queries):
    answer = []
    for query in queries:
        min_num = 1000000
        s,e,k = query
        for i,a in enumerate(arr):
            if s<= i <= e and arr[i]>k:
                if min_num > arr[i]:
                    min_num = arr[i]
        if min_num == 1000000:
            answer.append(-1)
        else:
            answer.append(min_num)
            
    return answer