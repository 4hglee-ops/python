# 10진수 -> 2진수 변환
# 2진수 & 연산으로 새로운 배열에 입력

def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    num = 0    
    
    for a1 in arr1:
        a1_bin = bin(a1)[2:]
        if len(a1_bin) < n:
            a1_bin = ('0'* (n-len(a1_bin))) + a1_bin
        arr1_bin.append(a1_bin)
    for a2 in arr2:
        a2_bin = bin(a2)[2:]
        if len(a2_bin) < n:
            a2_bin = ('0'* (n-len(a2_bin))) + a2_bin
        arr2_bin.append(a2_bin)    
        
    for y in range(n):
        answer_x = ''
        for x in range(n):
            num = int(arr1_bin[y][x]) + int(arr2_bin[y][x]) 
            if num >= 1:
                answer_x = answer_x + '#' 
            else:
                answer_x = answer_x + ' '
        answer.append(answer_x)              
                
    return answer