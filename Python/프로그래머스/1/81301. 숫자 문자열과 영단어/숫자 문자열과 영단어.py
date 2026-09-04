def solution(s):
    answer = ''
    num_dict = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    stack = ''
    for text in s:
        if text.isalpha():
            stack+=text
            if stack in num_dict:
                answer += num_dict[stack]
                stack = ''
        else:
            if stack:
                answer+=num_dict[stack]
                stack=''
            answer+=text
            
    return int(answer)