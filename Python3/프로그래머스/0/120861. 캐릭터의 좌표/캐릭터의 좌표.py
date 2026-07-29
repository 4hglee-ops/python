def solution(keyinput, board):
    answer = [0,0]
    move = {
        'up' : [0,1],
        'down' : [0,-1],
        'left' : [-1,0],
        'right' : [1,0]
    }
    
    max_x = board[0]//2
    max_y = board[1]//2
    
    for key in keyinput:
        dx, dy = move[key]
        next_x = answer[0] + dx
        next_y = answer[1] + dy
        answer[0] = min(max_x,max(-max_x,next_x))
        answer[1] = min(max_y,max(-max_y,next_y))
    
    return answer
