def solution(arr, queries):
    save = 0
    for querie in queries:
        i, j = querie
        save = arr[i]
        arr[i] = arr[j]
        arr[j] = save
    return arr