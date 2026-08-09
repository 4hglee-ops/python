#공통된 숫자 구하기 how?
#시작인자로 x,  x y 겹치면 y 그부분 제거
#int로 변환하는 작업은 아주 무거움
def solution(X, Y):
    answer = ''
    com = []
    comstr = ""
    comint = 0
    dicX = {"0" : 0,"1" : 0,"2" : 0,"3" : 0,"4" : 0,"5" : 0,"6" : 0,"7" : 0,"8" : 0,"9" : 0}
    dicY = {"0" : 0,"1" : 0,"2" : 0,"3" : 0,"4" : 0,"5" : 0,"6" : 0,"7" : 0,"8" : 0,"9" : 0}
     
    for x in X:
        dicX[x] += 1
    for y in Y:
        dicY[y] += 1    

    for i in range(9,-1,-1):
        i = str(i)
        while dicX[i] > 0 and dicY[i] > 0:
            com.append(i)
            dicX[i] -= 1
            dicY[i] -= 1
            
    #com.sort(reverse=True)
    if com == []:
        return "-1"    
    else:
        comstr = "".join(com)
    if comstr[0] == "0" :
        return "0"
    else :
        answer = comstr
    return answer