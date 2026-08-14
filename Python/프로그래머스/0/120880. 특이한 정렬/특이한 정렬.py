def solution(numlist, n):
    answer = []
    cal_save = {}
    for num in numlist:
        cal_save[num]=[max(n-num,num-n),num]
    cal_save = sorted(cal_save.values(),key=lambda x: x[1],reverse=True)
    cal_save = sorted(cal_save,key=lambda x: x[0],reverse=False)
    for num in cal_save:
        answer.append(num[1])    
    
    return answer