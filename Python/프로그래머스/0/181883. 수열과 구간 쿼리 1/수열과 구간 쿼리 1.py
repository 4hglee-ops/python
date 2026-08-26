def solution(arr, queries):
    for idx_q,querie in enumerate(queries):
        s, e = querie
        for idx,a in enumerate(arr):
            if s<=idx<=e:
                arr[idx] = a+1
    return arr