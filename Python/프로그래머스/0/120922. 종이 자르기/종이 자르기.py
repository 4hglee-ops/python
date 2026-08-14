def solution(M, N):
    n = max(M,N)
    m = min(M,N)
    if M * N == 1:
        return 0
    return ((n-1) * m) + (m-1)