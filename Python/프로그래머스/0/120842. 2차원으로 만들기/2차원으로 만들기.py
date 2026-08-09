def solution(num_list, n):
    answer = [[0]*n for _ in range(len(num_list)//n)]
    row = 0
    col = 0
    for idx,num in enumerate(num_list):
        row = idx // n
        col = idx % n
        answer[row][col]=num
    
    
    return answer