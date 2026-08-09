def solution(hp):
    answer = 0
    div5 = hp//5
    div3 = hp%5//3
    div1 = hp%5%3//1
    
    answer = div5+div3+div1
    
    return answer