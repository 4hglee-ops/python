def solution(myString):
    answer = []
    for myS in myString:
        if ord(myS) <= ord('l'):
            answer.append('l')
        else:
            answer.append(myS)
    
    return ''.join(answer)