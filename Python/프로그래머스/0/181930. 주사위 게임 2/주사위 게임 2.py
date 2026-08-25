def solution(a, b, c):
    count = 0
    if a==b:
        count += 1
    if a==c:
        count += 1
    if b==c:
        count += 1
    match count:
        case 3:
            return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
        case 1:
            return (a+b+c)*(a**2+b**2+c**2)
        case 0:
            return (a+b+c)
