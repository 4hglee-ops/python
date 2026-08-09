def solution(my_string):
    answer = 0
    num_sum = ""
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    for idx,text in enumerate(my_string):
        if text in num_list:
            num_sum += text
            print("if",text,type(text),num_sum,answer)
        else:
            if num_sum != "":
                answer += int(num_sum)
                num_sum = ""
                print("elif",text,type(text),num_sum,answer)
        if my_string[-1] in num_list and idx == len(my_string)-1:
            answer += int(num_sum)
            print("2if",text,type(text),num_sum,answer)
            
    return answer