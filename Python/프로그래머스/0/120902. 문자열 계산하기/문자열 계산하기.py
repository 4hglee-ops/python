def solution(my_string):
    answer = 0
    state = 'plus'
    num = ''
    space_count = 0
    for idx,text in enumerate(my_string):
        if text.isdigit():
            num += text
        if text == " " or idx == len(my_string)-1:
            if space_count == 0:
                space_count += 1
                if state == 'plus':
                    answer += int(num)
                    num = ''
                else:
                    answer -= int(num)
                    num = ''
            else :
                space_count = 0 
        elif text == '+':
            state = 'plus'
        elif text == '-':
            state = 'minus'
        print(idx,text,num,space_count,state,answer)
    return answer