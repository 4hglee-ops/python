def solution(balls, share):
    answer = 0
    n_fac = 1
    m_fac = 1
    n_m_fac = 1
    
    for i in range(balls):
        n_fac *= i+1
    for i in range(share):
        m_fac *= i+1
    for i in range(balls-share):
        n_m_fac *= i+1
    
    return n_fac/(m_fac*n_m_fac)