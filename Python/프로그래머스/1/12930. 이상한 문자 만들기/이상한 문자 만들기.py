def solution(s):
    split_s = s.split(' ')
    a_list=[]
    for text in split_s:
        answer = ''
        for idx,t in enumerate(text):
            if idx%2:
                answer += t.lower()
            else:
                answer += t.upper()
        a_list.append(answer)
    return ' '.join(a_list)