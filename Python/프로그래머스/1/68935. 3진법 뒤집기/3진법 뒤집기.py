# 124816
# 1 3 9 27 81 243 729 

def solution(n):
    answer = 0
    save_list = []
    save_n = n
    save_3 = ''
    save_3_r = 0
    for i in range(17):
        if i == 0:
            save_list.append(1)
        else:
            save_list.append(save_list[i-1] * 3)
    save_list.sort(reverse=True)
    for num in save_list:
        if save_n >= num * 2:
            save_3 += "2"
            save_n-=num*2
        elif save_n >= num:
            save_3 += "1"
            save_n-=num
        else:
            save_3 += "0"
        #print(save_3, save_n,num)
    #print(save_3)
    save_3_r = str(int(save_3))[::-1]
    #print(save_3_r)
    for idx,text in enumerate(save_3_r[::-1]):
        if text == '2':
            answer += 3**idx * 2
        elif text == '1':
            answer += 3**idx * 1
        elif text == '0':
            pass
        #print(idx,text,answer)
    return answer