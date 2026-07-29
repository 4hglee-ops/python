def solution(mats, park):
    answer = 0
    mats.sort(reverse=True) #돗자리 크기 내림차순 정렬
    H = len(park) # 공원 행 크기 정의
    W = len(park[0]) # 공원 열 크기 정의
    
    def can_park(r,c,s) :
        if r+s > H or c+s > W :
            return False 
        for i in range(r,r+s):
            for j in range(c,c+s):
                if park[i][j]!="-1" :
                    return False
        return True

    for size in mats :
        for i in range(H-size+1) :
            for j in range(W-size+1) :
                if can_park(i,j,size) == True :
                    answer = size
                    return answer                  
            
    return -1

