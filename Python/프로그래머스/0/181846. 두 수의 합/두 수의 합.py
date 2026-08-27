def solution(a, b):
    answer = []
    answer_str = ''
    plus_num = 0
    save_num = ''
    if len(b)>len(a):
        save_num = a
        a = b
        b = save_num
    elif len(b) == len(a):
        #print(a,b)
        for idx in range(len(a)-1,-1,-1):
            #print("idx",idx)
            if b[idx] > a[idx]:
                save_num = a
                a = b
                b = save_num
                print(a,b)
                break
    a = a[::-1]
    b = b[::-1]
    #if len(a)>=len(b):
    for i in range(len(a)):
        if i <=len(b)-1:
            if int(a[i])+int(b[i])+plus_num > 9:
                answer.append(int(a[i])+int(b[i])+plus_num-10)
                plus_num = 1
            else:
                answer.append(int(a[i])+int(b[i])+plus_num)
                plus_num = 0
        else:
            num = int(a[i]) + plus_num
            if num > 9:
                answer.append(num - 10)
                plus_num = 1
            else:
                answer.append(num)
                plus_num = 0
    if plus_num:
        answer.append(plus_num)
    if not answer:
        return "0"
    for i in range(len(answer)-1,-1,-1):
        answer_str += str(answer[i])
    return answer_str
        
    