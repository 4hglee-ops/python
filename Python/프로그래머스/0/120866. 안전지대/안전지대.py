def solution(board):
    answer = 0
    num_min = 0
    num_max = len(board)-1
    
    for i in range(len(board)):
        for j in range(len(board)):
            left = max(num_min,j-1)
            right = min(num_max,j+1)
            up = min(num_max,i+1)
            down = max(num_min,i-1)
            
            if board[i][left] + board[i][right] + board[up][j] + board[down][j] + board[down][left] + board[down][right] + board[up][left] + board[up][right] + board[i][j]== 0:
                answer +=1
                print(board[i][j],i,j,answer)
            
        
    
    return answer