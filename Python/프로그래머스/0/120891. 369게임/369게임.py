def solution(order):
    answer = 0
    order_str = str(order)
    game_369 = ['3','6','9']
    for text in order_str:
        if text in game_369:
            answer += 1
    return answer