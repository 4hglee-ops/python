# 현재 상태 : up, down, left, right
# 규칙 : 처음만 max 한번 찍으면 -11, 그 이후 max가 2번 반복되면 -1 됨

def solution(n):
    answer = [[]]
    answer = [[None] * n for _ in range(n)]
    max_move = n
    move_cnt = 1
    max_num = n-1
    min_num = 0
    max_count = 1
    num=1
    row = 0
    col = 0
    
    current_state = 'Right'

    while num <= n*n :
        if current_state == 'Right':
            answer[row][col] = num
            num += 1
            col += 1
            move_cnt += 1
            if move_cnt > max_move:
                current_state = 'Down'
                move_cnt = 1
                row += 1
                col = max_num
                max_count -= 1
                if max_count == 0:
                    max_move -= 1
                    max_count = 2            
        elif current_state == 'Down':
            answer[row][col] = num
            num += 1
            row += 1
            move_cnt += 1
            if move_cnt > max_move:
                current_state = 'Left'
                move_cnt = 1
                col -= 1
                row = max_num
                max_count -= 1
                if max_count == 0:
                    max_move -= 1
                    max_count = 2
        elif current_state == 'Left':
            answer[row][col] = num
            num += 1
            col -= 1
            move_cnt += 1
            if move_cnt > max_move :
                current_state = 'Up'
                move_cnt = 1
                row -= 1
                col = min_num
                max_count -= 1
                min_num += 1
                max_num -= 1
                if max_count == 0:
                    max_move -= 1
                    max_count = 2
        elif current_state == 'Up':
            answer[row][col] = num
            num += 1
            row -= 1
            move_cnt += 1
            if move_cnt > max_move:
                current_state = 'Right'
                move_cnt = 1
                col += 1
                row = min_num
                max_count -= 1
                if max_count == 0:
                    max_move -= 1
                    max_count = 2

    return answer