def solution(dots):
    dots = sorted(dots,key=lambda x:x[1])
    dots = sorted(dots,key=lambda x:x[0])
    print(dots)
    return abs((dots[1][1]-dots[0][1]))*abs((dots[2][0]-dots[0][0]))