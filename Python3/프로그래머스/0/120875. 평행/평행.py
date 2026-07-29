def solution(dots):
    answer = 0
    dots.sort(key=lambda x: x[0])
    
    m1 = (dots[1][1]-dots[0][1]) / (dots[1][0]-dots[0][0])
    m2 = (dots[3][1]-dots[2][1]) / (dots[3][0]-dots[2][0])
    m3 = (dots[2][1]-dots[0][1]) / (dots[2][0]-dots[0][0])
    m4 = (dots[3][1]-dots[1][1]) / (dots[3][0]-dots[1][0])
    m5 = (dots[3][1]-dots[0][1]) / (dots[3][0]-dots[0][0])
    m6 = (dots[2][1]-dots[1][1]) / (dots[2][0]-dots[1][0])
    
    if m1 == m2 or m3 == m4 or m5 == m6 :
        answer = 1
    
    
    return answer