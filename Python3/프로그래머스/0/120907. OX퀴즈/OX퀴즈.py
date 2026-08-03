def solution(quiz):
    answer = []
    sp_list = []
    num1 = ""
    num2 = ""
    sum_num = ""
    state = ""
    for qu in quiz:
        num1, state , num2 , _, sum_num = qu.split()
        num1 = int(num1)
        num2 = int(num2)
        sum_num = int(sum_num)
        
        if state == "+":
            if num1+num2 == sum_num:
                answer.append("O")
            else:
                answer.append("X")
        else:
            if num1-num2 == sum_num:
                answer.append("O")
            else:
                answer.append("X")
    return answer