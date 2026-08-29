def solution(n):
    sqrt_n = int(n**0.5)
    
    if sqrt_n**2 == n:
        return (sqrt_n+1)**2
    return -1


# def solution(n):
#     n_dict = {}
#     for i in range(1,n+1):
#         n_dict[i**2] = i
#     return (n_dict[n]+1)**2 if n in n_dict.keys() else -1