def solution(name, yearning, photo):
    answer = []
    for p in photo:
        sum_score = 0
        for p_name in p:
            if p_name in name:
                sum_score += yearning[name.index(p_name)]
        answer.append(sum_score)
    return answer