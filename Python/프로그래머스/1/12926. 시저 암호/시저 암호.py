# 'A' = 65
# 'Z' = 90
# 'a' = 97
# 'z' = 122

def pusher_text(text,n):
    ord_type = ''
    ord_text = ord(text)
    if 65<=ord_text<=90:
        ord_type = 'upper'
    elif 97<=ord_text<=122:
        ord_type = 'lower'
    p_text = ord_text + n    
    if ord_type == "upper":
        if p_text > 90:
            p_text -= 26
        return chr(p_text)
    elif ord_type == "lower":
        if p_text > 122:
            p_text -= 26
        return chr(p_text)
    else:
        return text    
        

def solution(s, n):
    answer = ''
    for text in s:
        answer+=pusher_text(text,n)
    return answer