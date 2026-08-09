def solution(array, n):
    answer = 0
    array.append(n)
    array.sort()
    for idx, num in enumerate(array):
        if num == n:
            if idx == 0:
                answer = array[1]
            elif num == array[-1]:
                answer = array[-2]
            else:
                snum = num-array[idx-1]
                lnum = array[idx+1]-num
                if lnum > snum or lnum == snum:
                    answer = array[idx-1]
                    print("lnum > ",array,idx,num,n,lnum,snum)
                else:
                    answer = array[idx+1]
                    print("snum > ",array,idx,num,n,lnum,snum)
            break
    return answer