def solution(picture, k):
    answer = []
    for idx,pic in enumerate(picture):
        stack = ''
        for p in pic:
            for i in range(k):
                stack += p
        for i in range(k):
            answer.append(stack)        
    return answer