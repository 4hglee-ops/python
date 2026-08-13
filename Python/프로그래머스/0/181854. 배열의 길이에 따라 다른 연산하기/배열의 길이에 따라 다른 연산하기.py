def solution(arr, n):
    answer = []
    state = 'odd'
    if len(arr)%2 == 0:
        state = 'even'
    for idx, a in enumerate(arr):
        if state == 'even':
            if idx%2==1:
                answer.append(a+n)
            else:
                answer.append(a)
        else:
            if idx%2==0:
                answer.append(a+n)
            else:
                answer.append(a)
    return answer