def solution(n):
    answer = 0
    n_range = len(str(n))-1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(n_range)
    for i in range(n_range,-1,-1):
        answer += n // (10 ** i)
        n = n % (10**i)
        print(i,10**i,answer,n)
    
    
    return answer