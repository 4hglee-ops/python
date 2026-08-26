def solution(arr, queries):
    for querie in queries:
        s,e,k = querie
        if k == 0:
            return arr
        for idx,a in enumerate(arr):
            if idx == 0 and s == 0: 
                arr[idx] += 1
            elif s <= idx <= e and idx % k == 0:
                arr[idx] +=1
    return arr