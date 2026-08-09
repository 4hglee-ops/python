def solution(age):
    answer = ''
    age_dict = {
        0:'a',1:'b',2:'c',3:'d',4:'e',
        5:'f',6:'g',7:'h',8:'i',9:'j'
    }
    age_str = str(age)
    
    for text in age_str:
        answer+=age_dict[int(text)]
    
    
    return answer