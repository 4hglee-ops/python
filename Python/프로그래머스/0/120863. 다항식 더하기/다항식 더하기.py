def solution(polynomial):
    answer = ''
    stack = ''
    x_sum = 0
    num_sum = 0
    poly_list = polynomial.split()
    print(poly_list)    
    for poly in poly_list:
        print(poly,type(poly))
        if "x" in poly:
            if len(poly) != 1:
                x_sum += int(poly[:-1])
            else:
                x_sum += 1
        elif poly.isdigit():
            num_sum += int(poly)
    if num_sum != 0 and x_sum > 1:     
        answer = str(x_sum)+'x + '+str(num_sum)
    elif num_sum == 0 and x_sum > 1:
        answer = str(x_sum)+'x'
    elif x_sum == 1 and num_sum != 0:
        answer = 'x + '+str(num_sum)
    elif x_sum == 1 and num_sum == 0:
        answer = 'x'
    else:
        answer = str(num_sum)
        
    return answer