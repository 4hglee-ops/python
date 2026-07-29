def solution(n):
    answer = 0
    n_range = len(str(n))-1

    for i in range(n_range,-1,-1):
        answer += n // (10 ** i)
        n = n % (10**i)
        print(i,10**i,answer,n)
    
    return answer
